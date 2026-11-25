"""Runs every Python example in README.md and docs/**/*Api.md against the local stand-in API.

README blocks run in order in one namespace (later blocks use the `client` of the first), except a
block after a `<!-- standalone -->` line, which runs on its own so a missing import shows. Each
docs/ example runs on its own. Nothing calls Astrada: "sandbox" and "production" point at the
stand-in (conftest.py).
"""

import base64
import hashlib
import hmac
import json
import re
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(r"(<!-- standalone -->\n)?```python\n(.*?)\n```", re.S)


def blocks(path):
    return [(bool(m.group(1)), m.group(2)) for m in BLOCK.finditer(path.read_text(encoding="utf-8"))]


DOC_PAGES = [
    page
    for folder in ("docs", "docs/banking", "docs/sandbox")
    for page in sorted((ROOT / folder).glob("*Api.md"))
]
DOC_EXAMPLES = [
    pytest.param(code, id="%s#%d" % (page.relative_to(ROOT), index))
    for page in DOC_PAGES
    for index, (_, code) in enumerate(blocks(page))
]


def run(code, namespace, name):
    exec(compile(code, name, "exec"), namespace)


def sign(secret, body, msg_id="msg_1", timestamp=None):
    timestamp = str(int(time.time()) if timestamp is None else timestamp)
    key = base64.b64decode(secret[len("whsec_"):])
    digest = hmac.new(key, f"{msg_id}.{timestamp}.{body}".encode(), hashlib.sha256).digest()
    return {
        "webhook-id": msg_id,
        "webhook-timestamp": timestamp,
        "webhook-signature": "v1," + base64.b64encode(digest).decode(),
        "webhook-event-type": "transaction.created",
        "Content-Type": "application/json",
    }


def check_webhook_app(app, secret, standin):
    """The README's Flask handler answers 204 to a good delivery and 400 to a bad one."""
    main = standin.state.specs[1]
    body = json.dumps(main.sample({"$ref": "#/components/schemas/transaction"}))
    web = app.test_client()
    good = web.post("/astrada/webhooks", data=body, headers=sign(secret, body))
    assert good.status_code == 204, good.data
    bad_headers = sign(secret, body)
    bad_headers["webhook-signature"] = "v1," + base64.b64encode(b"x" * 32).decode()
    bad = web.post("/astrada/webhooks", data=body, headers=bad_headers)
    assert bad.status_code == 400
    # A signed body the SDK cannot read: never a 2xx until it is stored. The sample's store is a
    # stub that raises, so it answers 500; with a working store it answers 500, then 204 at the limit.
    unreadable = json.dumps({"id": "not-a-transaction"})
    for _ in range(4):
        assert web.post("/astrada/webhooks", data=unreadable, headers=sign(secret, unreadable, "msg_u")).status_code == 500
    stored = []
    namespace = app.view_functions["astrada_webhook"].__globals__
    namespace["store_unreadable"] = lambda event, raw: stored.append((event.id, raw)) or len(stored)
    codes = [web.post("/astrada/webhooks", data=unreadable, headers=sign(secret, unreadable, "msg_u")).status_code
             for _ in range(3)]
    assert codes == [500, 500, 204] and stored[-1] == ("msg_u", unreadable.encode())
    # Only some messages unreadable: the transaction is handled, the delivery stored, and 204 at once.
    partial = json.loads(body)
    partial["_embedded"] = {"messages": [{"id": "not-a-uuid"}]}
    partial = json.dumps(partial)
    stored.clear()
    assert web.post("/astrada/webhooks", data=partial, headers=sign(secret, partial, "msg_p")).status_code == 204
    assert stored == [("msg_p", partial.encode())]


def test_readme_examples(standin_env, capsys):
    examples = blocks(ROOT / "README.md")
    assert len(examples) >= 10
    shared = {"__name__": "readme"}
    for index, (standalone, code) in enumerate(examples):
        namespace = {"__name__": "readme_standalone"} if standalone else shared
        run(code, namespace, "README.md#%d" % index)
        if "app" in namespace and standalone:
            import os

            check_webhook_app(namespace["app"], os.environ["ASTRADA_WEBHOOK_SECRET"], standin_env)
    out = capsys.readouterr().out
    assert "Send this link:" in out
    assert "Not found:" in out
    assert "sync_bank_link needs banking:admin" in out


@pytest.mark.parametrize("code", DOC_EXAMPLES)
def test_doc_example(standin_env, code):
    """Each example runs; one that needs banking:admin, with a stand-in client without it, raises
    ScopeRequiredError naming its scope (and runs with the staff client)."""
    import astrada
    from astrada.banking import _staff_only

    staff = [op for op in _staff_only.OPERATIONS if ".%s(" % op["operation"] in code]
    if not staff:
        run(code, {"__name__": "doc_example"}, "docs example")
        return
    with pytest.raises(astrada.ScopeRequiredError) as raised:
        run(code, {"__name__": "doc_example"}, "docs example")
    assert raised.value.required_scope == staff[0]["scope"]
    assert "The likely cause is that your API client does not have it" in str(raised.value)
    assert "A 403 can also mean the resource is not this account's." in str(raised.value)
    standin_env_staff(standin_env)
    run(code, {"__name__": "doc_example"}, "docs example")


def standin_env_staff(standin):
    import os

    from standin.server import STAFF_CLIENT_ID

    os.environ["ASTRADA_CLIENT_ID"] = STAFF_CLIENT_ID  # monkeypatch restores it after the test


@pytest.mark.parametrize("code", DOC_EXAMPLES)
def test_doc_example_against_the_mock(code, monkeypatch):
    """The same examples on astrada.testing: every operation's canned answer parses."""
    import astrada
    from astrada.testing import MockAstrada

    mock = MockAstrada()
    monkeypatch.setattr(astrada, "Astrada", lambda *args, **kwargs: mock.client)
    monkeypatch.setenv("ASTRADA_ACCOUNT_ID", "a")
    monkeypatch.setenv("ASTRADA_CLIENT_ID", "b")
    monkeypatch.setenv("ASTRADA_CLIENT_SECRET", "c")
    run(code, {"__name__": "doc_example"}, "docs example")
    assert mock.calls and mock.calls[-1].operation is not None
