# coding: utf-8
"""Response parsing that tolerates values the SDK does not know yet. Hand-written; not generated.

Enum checks in the generated models stop a request with a value the API does not accept. When the
SDK parses a response (or a webhook) instead, a value added to the API after this SDK was released
must not fail the call: inside :func:`lenient` the enum checks keep the unknown value as a plain
string.
"""

import contextlib
import contextvars
from typing import Iterator

_LENIENT: contextvars.ContextVar[bool] = contextvars.ContextVar("astrada_lenient", default=False)


def active() -> bool:
    """True while a response or webhook is being parsed."""
    return _LENIENT.get()


@contextlib.contextmanager
def lenient() -> Iterator[None]:
    token = _LENIENT.set(True)
    try:
        yield
    finally:
        _LENIENT.reset(token)
