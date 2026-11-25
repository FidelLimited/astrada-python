# coding: utf-8
"""Iterate over every item of a list call, page after page. Hand-written; not generated.

    for subaccount in astrada.paginate(client.subaccounts.list_subaccounts, limit=100):
        print(subaccount.id)

Works with every ``list_*`` method: the card APIs page with ``cursor`` or ``offset`` and say where
the next page starts in ``_links.next``; the Banking API pages with ``cursor`` and says it in
``pagination.cursor`` and ``pagination.hasMore``. The next page is requested only when the loop
reaches it.
"""

from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple
from urllib.parse import parse_qs, urlsplit

from pydantic import BaseModel


def _items(page: Any) -> List[Any]:
    items = getattr(page, "items", None)
    if isinstance(items, list):
        return items
    embedded = getattr(page, "embedded", None)
    if isinstance(embedded, BaseModel):
        for name in type(embedded).model_fields:
            value = getattr(embedded, name)
            if isinstance(value, list):
                return value
    return []


def _next_params(page: Any) -> Optional[Dict[str, Any]]:
    """The query parameters of the next page, or None on the last page."""
    pagination = getattr(page, "pagination", None)
    if pagination is not None and hasattr(pagination, "has_more"):
        if pagination.has_more and pagination.cursor:
            return {"cursor": pagination.cursor}
        return None
    links = getattr(page, "links", None)
    next_link = getattr(links, "next", None) if links is not None else None
    href = getattr(next_link, "href", None)
    if not href:
        return None
    query = parse_qs(urlsplit(href).query)
    if "cursor" in query:
        return {"cursor": query["cursor"][0]}
    if "offset" in query:
        return {"offset": int(float(query["offset"][0]))}
    return None


def pages(list_method: Callable[..., Any], *args: Any, **params: Any) -> Iterator[Any]:
    """Each page a ``list_*`` method returns, following the next-page cursor or offset."""
    seen: List[Tuple[Tuple[str, Any], ...]] = []
    while True:
        page = list_method(*args, **params)
        yield page
        following = _next_params(page)
        if not following:
            return
        key = tuple(sorted(following.items()))
        if key in seen:  # the API pointed back at a page already read
            return
        seen.append(key)
        params = {**params, **following}


def paginate(list_method: Callable[..., Any], *args: Any, **params: Any) -> Iterator[Any]:
    """Every item a ``list_*`` method returns across all pages.

    :param list_method: a list method, for example ``client.subaccounts.list_subaccounts``
    :param args: its positional arguments (for example the subaccount id of a banking list)
    :param params: its keyword arguments (filters and ``limit``, the page size)
    """
    for page in pages(list_method, *args, **params):
        yield from _items(page)
