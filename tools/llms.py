"""Writes the files for developers' AI agents next to the pdoc reference site.

    python tools/llms.py SITE_DIR [README.md]

SITE_DIR is the pdoc output (the public repository's docs.yml builds it, then runs this, so this file
is part of the public export). It writes:
    SITE_DIR/llms.txt          the llmstxt.org index: what the SDK is, then links to markdown pages
    SITE_DIR/md/guide/*.md     an Overview page (the README's introduction) and one page per README
                               section; links between sections point at the matching page
    SITE_DIR/md/reference/*.md one page per documented module and per public class, from pdoc's own
                               model of the package (the docstrings and signatures the HTML shows),
                               inherited members of the SDK's own base classes included
    SITE_DIR/llms-full.txt     every linked page in one file
It exits 1 when a link in llms.txt or between guide pages points at a page that was not written, or
when the guides, modules or classes come out empty (a changed pdoc or README layout).
    LLMS_BASE_URL   where the site is served (default https://fidellimited.github.io/astrada-python/)
"""

import os
import re
import shutil
import sys
from pathlib import Path

# The package from this checkout, as the pdoc command sees it (run from the repository root).
sys.path.insert(0, os.getcwd())

import pdoc.doc  # noqa: E402

MODULES = ["astrada", "astrada.banking", "astrada.sandbox", "astrada.testing", "astrada.pagination",
           "astrada.webhooks", "astrada.environments"]
"""The modules the reference site documents: the same list as the pdoc command in docs.yml and
python.yml (scripts/test/test_llms.py checks that they agree)."""
SKIP = {"support", "license", "versions"}


def slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def readme_parts(path: Path):
    """The introduction (text before the first "## ") and the sections, split outside code fences."""
    intro, sections, current, fenced = [], [], None, False
    for line in path.read_text(encoding="utf-8").split("\n"):
        if line.startswith("```"):
            fenced = not fenced
        heading = None if fenced else re.match(r"^## (.+)$", line)
        if heading:
            current = {"title": heading.group(1).strip(), "lines": []}
            sections.append(current)
        elif current is not None:
            current["lines"].append(line)
        elif not line.startswith("# "):
            intro.append(line)
    return "\n".join(intro).strip(), sections


def signature(obj) -> str:
    try:
        return str(obj.signature)
    except Exception as error:  # a pdoc regression should be visible, not silent
        print(f"llms: no signature for {obj.fullname}: {type(error).__name__}", file=sys.stderr)
        return "(...)"


def own_api(member) -> bool:
    """A member defined by the SDK (on this class or one of its astrada.* bases), not by pydantic,
    urllib3 or the standard library."""
    module = (member.taken_from or ("",))[0] or ""
    return module == "astrada" or module.startswith("astrada.")


def class_page(cls, include_note: str) -> str:
    lines = [f"# class {cls.fullname}", "", (cls.docstring.strip() or "(no description)"), ""]
    for member in cls.members.values():
        if (member.name.startswith("_") and member.name != "__init__") or not own_api(member):
            continue
        if isinstance(member, pdoc.doc.Function):
            name = cls.name if member.name == "__init__" else member.name
            lines += [f"## {name}{signature(member)}", "", member.docstring.strip(), ""]
        elif isinstance(member, pdoc.doc.Variable):
            lines += [f"## {member.name}{member.annotation_str or ''}", "", member.docstring.strip(), ""]
    return expand_includes("\n".join(lines), include_note).rstrip() + "\n"


def expand_includes(text: str, note: str) -> str:
    """pdoc expands ".. include::" only when rendering HTML; the markdown pages point at the guides."""
    return re.sub(r"^\.\. include:: .*$", note, text, flags=re.M)


def module_page(module, class_links, include_note) -> str:
    lines = [f"# module {module.fullname}", "", module.docstring.strip(), ""]
    functions = [m for m in module.members.values() if isinstance(m, pdoc.doc.Function) and not m.name.startswith("_")]
    if class_links:
        lines += ["## Classes", ""] + [f"- [{name}]({link})" for name, link in class_links] + [""]
    if functions:
        lines += ["## Functions", ""]
        for fn in functions:
            lines += [f"### {fn.name}{signature(fn)}", "", fn.docstring.strip(), ""]
    return expand_includes("\n".join(lines), include_note).rstrip() + "\n"


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
    readme = Path(sys.argv[2] if len(sys.argv) > 2 else "README.md")
    base = os.environ.get("LLMS_BASE_URL", "https://fidellimited.github.io/astrada-python/").rstrip("/") + "/"
    version = re.search(r'^version = "(.*)"', Path("pyproject.toml").read_text(), re.M)
    version = version.group(1) if version else "unknown"

    guide_dir = site / "md" / "guide"
    ref_dir = site / "md" / "reference"
    for directory in (guide_dir, ref_dir):
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True)

    def url(path: str) -> str:
        return base + path

    # Guides: the introduction as Overview, then each section; "](#slug)" links point at the pages.
    intro, sections = readme_parts(readme)
    kept = [s for s in sections if slug(s["title"]) not in SKIP]
    pages = {slug(s["title"]): f"md/guide/{slug(s['title'])}.md" for s in kept}
    login = pages.get("log-in")
    problems = []

    def fix_anchors(text: str, page: str) -> str:
        def replace(m):
            target = pages.get(m.group(1))
            if target is None:
                problems.append(f"{page}: link to #{m.group(1)} matches no section")
                return m.group(0)
            return f"]({url(target)})"
        return re.sub(r"\]\(#([a-z0-9-]+)\)", replace, text)

    guides = [("Overview", "md/guide/overview.md")]
    (site / "md/guide/overview.md").write_text(f"# Overview\n\n{fix_anchors(intro, 'overview')}\n", encoding="utf-8")
    for section in kept:
        name = slug(section["title"])
        body = fix_anchors("\n".join(section["lines"]).strip(), name)
        # Pages whose examples use the client made in "Log in" say where it comes from.
        if login and name != "log-in" and re.search(r"\bclient\.", body):
            body = f"The examples use the `client` made in [Log in]({url(login)}).\n\n{body}"
        (site / pages[name]).write_text(f"# {section['title']}\n\n{body}\n", encoding="utf-8")
        guides.append((section["title"], pages[name]))

    include_note = f"The package overview and guides: [Overview]({url('md/guide/overview.md')})."
    modules, classes, written = [], [], {}
    for name in MODULES:
        module = pdoc.doc.Module.from_name(name)
        links = []
        for member in module.members.values():
            if isinstance(member, pdoc.doc.Class) and not member.name.startswith("_"):
                # One page per class object: a class re-exported by several modules is written once.
                key = id(member.obj)
                if key not in written:
                    path = f"md/reference/{member.fullname}.md"
                    written[key] = path
                    (site / path).write_text(class_page(member, include_note), encoding="utf-8")
                    origin = getattr(member.obj, "__module__", "") or ""
                    classes.append((member.fullname, path, ".models." in origin))
                links.append((member.name, url(written[key])))
        path = f"md/reference/{name}.md"
        (site / path).write_text(module_page(module, links, include_note), encoding="utf-8")
        modules.append((name, path))
    classes.sort()

    if not guides[1:] or not modules or not classes:
        print(f"llms: nothing to list (guides {len(guides) - 1}, modules {len(modules)}, classes {len(classes)}); "
              "has the README or pdoc layout changed?", file=sys.stderr)
        return 1

    def link(title: str, path: str, note: str = "") -> str:
        return f"- [{title}]({url(path)})" + (f": {note}" if note else "")

    llms = "\n".join([
        "# astrada",
        "",
        "> The Astrada Python SDK (`pip install astrada`, Python 3.10 or later) is the backend client for the "
        "Astrada API: one `astrada.Astrada` client for subaccounts, enrollment links, cards and card "
        "subscriptions, transactions and their messages, webhooks (verify, parse and replay), the Banking API "
        "(`client.banking`) and the sandbox simulations (`client.sandbox`), with typed errors, retries and a mock "
        "for tests. It has no card-enrollment methods: card enrollment happens in the browser with the Unified "
        "Enrollment SDK v2 or an enrollment link. An approved direct-API partner that sends card data through "
        "`client.request` has it pass through its own server, in its own PCI scope.",
        "",
        f"Every page below is markdown generated from the same sources as the HTML reference at {base}astrada.html, "
        f"for version {version} of the package.",
        "",
        "## Guides",
        "",
        *[link(t, p) for t, p in guides],
        "",
        "## API reference",
        "",
        *[link(t, p, "the module's docstring, its classes and functions") for t, p in modules],
        *[link(t, p) for t, p, model in classes if not model],
        "",
        "## Astrada documentation",
        "",
        "- [Astrada docs for AI agents](https://docs.astrada.co/llms.txt): the whole API documentation as an llms.txt index",
        "- [Backend SDKs](https://docs.astrada.co/docs/backend-sdks): how the TypeScript, Python and Java SDKs fit with the API",
        "",
        "## Optional",
        "",
        *[link(t, p) for t, p, model in classes if model],
        "",
    ])
    (site / "llms.txt").write_text(llms, encoding="utf-8")

    linked = []
    for target in re.findall(r"\]\((\S+?)\)", llms):
        if not target.startswith(base):
            continue
        path = target[len(base):]
        if (site / path).exists():
            linked.append(path)
        else:
            problems.append(f"llms.txt: {path} was not written")
    if problems:
        print("llms: broken links:\n  " + "\n  ".join(problems), file=sys.stderr)
        return 1
    full = [llms] + [f"\n\n---\n\nSource: {base}{p}\n\n" + (site / p).read_text(encoding="utf-8") for p in linked]
    (site / "llms-full.txt").write_text("".join(full), encoding="utf-8")
    models = sum(1 for c in classes if c[2])
    print(f"llms: {len(guides)} guide pages, {len(modules)} modules, {len(classes)} classes "
          f"({models} models under Optional); {len(linked)} links checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
