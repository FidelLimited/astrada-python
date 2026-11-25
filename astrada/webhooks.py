# coding: utf-8
"""Checks that a webhook came from Astrada. Hand-written; not generated.

Astrada delivers webhooks through Svix. Each delivery carries ``webhook-id``, ``webhook-timestamp``
and ``webhook-signature`` headers (Svix also sends the same values as ``svix-id``, ``svix-timestamp``
and ``svix-signature``). The signature is ``v1,`` + base64(HMAC-SHA256(key, "{id}.{timestamp}.{body}")),
where the key is the base64-decoded webhook secret returned once by ``POST /webhooks``.
"""

import base64
import binascii
import hashlib
import hmac
import json
import math
import re
import time
from datetime import datetime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from astrada._lenient import lenient
from astrada.models.card_subscription import CardSubscription
from astrada.models.cardholder import Cardholder
from astrada.models.transaction import Transaction
from astrada.models.transaction_message import TransactionMessage


class WebhookVerificationError(Exception):
    """The delivery must be rejected: bad or missing signature, too old, or not JSON."""


EVENT_MODELS: Dict[str, Any] = {
    "transactionmessage.created": TransactionMessage,
    "transaction.created": Transaction,
    "transaction.updated": Transaction,
    "cardsubscription.created": CardSubscription,
    "cardsubscription.updated": CardSubscription,
    "cardholder.updated": Cardholder,
}
"""The event types whose body is an API resource the SDK has a model for. The bodies of the other
event types (bank linking, network bulk feeds, merchant enrichment) are described in the Event
Types reference and stay plain dicts in ``WebhookEvent.data``."""


class TransactionWebhookMessage(BaseModel):
    """One of the transaction messages a transaction webhook carries in ``_embedded.messages``.

    This is a short form of a transaction message (``_links``, ``id``, ``messageType``,
    ``network``, ``result``, ``dateTime``, ``approvalCode``, ``transactionReference``), so every
    field may be missing. Any other key the webhook sends is kept as an extra attribute under its
    JSON name. ``date_time`` is naive for a Mastercard message (merchant's local time), in UTC for
    Visa and Amex, and in a zone the definition does not state for others such as ``OPEN_BANKING``; read the full message with ``get_transaction_message`` for the other fields.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    links: Optional[Dict[str, Any]] = Field(default=None, alias="_links")
    id: Optional[UUID] = None
    message_type: Optional[str] = Field(default=None, alias="messageType")
    network: Optional[str] = None
    result: Optional[str] = None
    date_time: Optional[datetime] = Field(default=None, alias="dateTime")
    approval_code: Optional[str] = Field(default=None, alias="approvalCode")
    transaction_reference: Optional[str] = Field(default=None, alias="transactionReference")


class WebhookEvent:
    """A verified webhook delivery.

    :ivar id: the delivery's ``webhook-id`` (the same on every retry of one event; use it to
        ignore repeats)
    :ivar type: the event type from the ``webhook-event-type`` header, for example
        ``"transaction.created"``; None if the header is missing
    :ivar timestamp: when the delivery was signed, Unix seconds
    :ivar data: the body as a model (``Transaction``, ``TransactionMessage``, ``CardSubscription``
        or ``Cardholder``) for those event types, else the parsed JSON
    :ivar raw: the parsed JSON body, always
    :ivar messages: for ``transaction.created`` and ``transaction.updated``, the body's
        ``_embedded.messages`` as ``TransactionWebhookMessage`` objects (``data`` keeps them as
        sent, in ``data.embedded.additional_properties["messages"]``); an empty list otherwise.
        A message this SDK cannot read is left out of it and listed in ``unreadable_messages``
    :ivar unreadable_messages: those messages as sent (dicts); usually empty
    :ivar unreadable: True when the event type has a model but this body does not fit it (often an
        SDK older than the event); ``data`` is then the parsed JSON. The signature was correct, so
        store the delivery first, then answer 5xx so Astrada delivers it again; answer 2xx only once
        it is stored. After updating the SDK, read the stored copy with
        :func:`parse_stored_webhook`. Answer 400 only for ``WebhookVerificationError``.
    """

    def __init__(
        self, id: str, type: Optional[str], timestamp: int, data: Any, raw: Any
    ) -> None:
        self.id = id
        self.type = type
        self.timestamp = timestamp
        self.data = data
        self.raw = raw
        self.messages, self.unreadable_messages = _split_messages(type, data)
        model = EVENT_MODELS.get(type or "")
        self.unreadable: bool = model is not None and not isinstance(data, model)

    def __repr__(self) -> str:
        return "WebhookEvent(id=%r, type=%r, data=%s)" % (
            self.id, self.type, type(self.data).__name__
        )


def _event_data(event_type: Optional[str], raw: Any) -> Any:
    model = EVENT_MODELS.get(event_type or "")
    if model is None or not isinstance(raw, dict):
        return raw
    try:
        with lenient():
            return model.from_dict(raw)
    except Exception:
        # A body this SDK cannot read as the model still reaches the handler, as a dict.
        return raw


def _split_messages(event_type: Optional[str], data: Any) -> Tuple[List[TransactionWebhookMessage], List[Any]]:
    """A transaction webhook's ``_embedded.messages``: those this SDK reads, typed, and the others
    as sent. One unreadable message does not hide the rest."""
    if event_type not in ("transaction.created", "transaction.updated"):
        return [], []
    embedded = data.get("_embedded") if isinstance(data, dict) else getattr(data, "embedded", None)
    extra = embedded if isinstance(embedded, dict) else getattr(embedded, "additional_properties", None)
    raw = extra.get("messages") if isinstance(extra, dict) else None
    if not isinstance(raw, list):
        return [], []
    good: List[TransactionWebhookMessage] = []
    bad: List[Any] = []
    for m in raw:
        try:
            good.append(TransactionWebhookMessage.model_validate(m))
        except Exception:
            bad.append(m)
    return good, bad


def _header(headers: Mapping[str, Any], name: str) -> Optional[str]:
    for key, value in headers.items():
        if key.lower() == name:
            if isinstance(value, (list, tuple)):
                return value[0] if value else None
            return value
    return None


def _secret_key(secret: str) -> bytes:
    encoded = secret[len("whsec_"):] if secret.startswith("whsec_") else secret
    try:
        key = base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError):
        raise WebhookVerificationError("The webhook secret is not base64")
    if not key:
        raise WebhookVerificationError("The webhook secret is empty")
    return key


def verify_webhook(
    payload: Union[bytes, str],
    headers: Mapping[str, Any],
    secret: str,
    tolerance_seconds: int = 300,
    now: Optional[float] = None,
) -> WebhookEvent:
    """Check the signature and age of a webhook delivery and return it as a :class:`WebhookEvent`.

    :param payload: the raw request body, exactly as received (do not parse and re-serialise it)
    :param headers: the request headers (any mapping; names are matched case-insensitively)
    :param secret: the webhook's ``secret``, as returned when the webhook was created
    :param tolerance_seconds: largest accepted difference between the delivery time and now
    :param now: the current Unix time; for tests
    :raises WebhookVerificationError: when the delivery must be rejected
    """
    msg_id = _header(headers, "webhook-id") or _header(headers, "svix-id")
    timestamp = _header(headers, "webhook-timestamp") or _header(headers, "svix-timestamp")
    signatures = _header(headers, "webhook-signature") or _header(headers, "svix-signature")
    if not msg_id or not timestamp or not signatures:
        raise WebhookVerificationError(
            "Missing webhook-id, webhook-timestamp or webhook-signature header"
        )

    try:
        sent_at = int(timestamp)
    except ValueError:
        raise WebhookVerificationError("Invalid webhook-timestamp header")
    current = int(time.time() if now is None else now)
    # A range check, the same as the other SDKs (no subtraction that could overflow there).
    if not current - tolerance_seconds <= sent_at <= current + tolerance_seconds:
        raise WebhookVerificationError("The webhook timestamp is outside the accepted window")

    body = payload if isinstance(payload, bytes) else payload.encode("utf-8")
    signed = msg_id.encode("utf-8") + b"." + timestamp.encode("utf-8") + b"." + body
    expected = hmac.new(_secret_key(secret), signed, hashlib.sha256).digest()

    # The header can hold several space-separated "v1,<signature>" entries (during secret rotation).
    for entry in signatures.split(" "):
        version, _, signature = entry.partition(",")
        if version != "v1" or not signature:
            continue
        try:
            received = base64.b64decode(signature)
        except (binascii.Error, ValueError):
            continue
        if hmac.compare_digest(received, expected):
            try:
                raw = json.loads(body)
            except ValueError:
                raise WebhookVerificationError("The webhook body is not JSON")
            event_type = _header(headers, "webhook-event-type")
            return WebhookEvent(msg_id, event_type, sent_at, _event_data(event_type, raw), raw)

    raise WebhookVerificationError("No matching webhook signature")


_MAX_UNIX_SECONDS = 10**11
"""Unix seconds up to this (year 5138) are read as seconds; a larger number is likely milliseconds."""

_ISO_WITH_OFFSET = re.compile(
    r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?)(?:\.(\d+))?(Z|[+-]\d{2}:?\d{2})$", re.IGNORECASE)


def _stored_seconds(timestamp: Any) -> int:
    """The shared rule for a stored webhook timestamp: Unix seconds as a number or an all-digit
    string (the ``webhook-timestamp`` header's own form), an aware ``datetime``, or an ISO 8601
    string with ``Z`` or an offset. A naive ``datetime`` or an offset-less string would be read in
    the host's time zone, and milliseconds would land thousands of years ahead, so they are
    refused."""
    refuse = ValueError(
        "parse_stored_webhook needs a valid timestamp: Unix seconds (a number or an all-digit "
        "string), an aware datetime, or an ISO 8601 string with Z or an offset; got %r" % (timestamp,))
    if isinstance(timestamp, datetime):
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise refuse
        return int(timestamp.timestamp())
    if isinstance(timestamp, str) and timestamp.isdigit():
        timestamp = int(timestamp)
    if isinstance(timestamp, (int, float)) and not isinstance(timestamp, bool):
        # The range first: math.isfinite raises OverflowError on an int too large for a float.
        if isinstance(timestamp, float) and not math.isfinite(timestamp):
            raise refuse
        if not 0 <= timestamp <= _MAX_UNIX_SECONDS:
            raise refuse
        return int(timestamp)
    if isinstance(timestamp, str):
        m = _ISO_WITH_OFFSET.match(timestamp)
        if not m:
            raise refuse
        # Python 3.10's fromisoformat takes only 3 or 6 fraction digits: normalise to 6.
        fraction = "." + (m.group(2) or "0").ljust(6, "0")[:6]
        offset = "+00:00" if m.group(3).upper() == "Z" else m.group(3)
        if ":" not in offset:
            offset = offset[:3] + ":" + offset[3:]
        # A time without seconds (16:00Z) gets ":00", so the fraction follows the seconds.
        clock = m.group(1) if len(m.group(1)) > 16 else m.group(1) + ":00"
        try:
            return int(datetime.fromisoformat(clock + fraction + offset).timestamp())
        except ValueError:
            raise refuse from None
    raise refuse


def parse_stored_webhook(
    body: Union[str, bytes, bytearray, memoryview, Dict[str, Any], List[Any]],
    event_type: Optional[str],
    id: str,
    timestamp: Union[int, float, str, datetime],
) -> WebhookEvent:
    """A delivery your server verified earlier and stored, read again: for replaying an event this
    SDK could not read when it arrived (``event.unreadable``, or the missing messages of a partial
    delivery), after you update the SDK.

    It checks no signature (and the age limit of :func:`verify_webhook` would refuse a stored
    delivery anyway), so pass only what you stored after a successful check, never a body from a
    request, and keep that record of the check with the body. Skip ids you already handled, except
    a partial delivery; for a transaction apply it only if its ``updated_at`` is newer than your
    copy's, and for other resources fetch the current state first.

    :param body: the raw body as received (``str``, ``bytes``, ``bytearray`` or ``memoryview``), or
        the parsed JSON (a ``dict`` or ``list``, as read from a JSON column)
    :param event_type: the delivery's ``webhook-event-type`` (``event.type``); None when the
        delivery had no such header, as :func:`verify_webhook` allows (``data`` is then the JSON)
    :param id: the delivery's ``webhook-id`` (``event.id``)
    :param timestamp: the delivery's ``webhook-timestamp``: Unix seconds (a number or an all-digit
        string), an aware ``datetime``, or an ISO 8601 string with ``Z`` or an offset
    :raises ValueError: a blank ``event_type`` or an empty ``id``, an invalid timestamp (a naive
        ``datetime``, an offset-less string, milliseconds, infinity), a body of another type, or a
        body that is not JSON
    """
    if event_type is not None and (not isinstance(event_type, str) or not event_type.strip()):
        raise ValueError("parse_stored_webhook needs the stored webhook-event-type, or None when the "
                         "delivery had none (event_type is blank)")
    if not isinstance(id, str) or not id.strip():
        raise ValueError("parse_stored_webhook needs the stored webhook-id (id is empty)")
    seconds = _stored_seconds(timestamp)
    if isinstance(body, (dict, list)):
        raw: Any = body
    elif isinstance(body, (str, bytes, bytearray, memoryview)):
        try:
            raw = json.loads(bytes(body) if isinstance(body, memoryview) else body)
        except ValueError:
            raise ValueError("The stored %s delivery %s is not JSON" % (event_type, id)) from None
    else:
        raise ValueError("parse_stored_webhook needs the body as str, bytes, memoryview, dict or list")
    return WebhookEvent(id, event_type, seconds, _event_data(event_type, raw), raw)
