# coding: utf-8
"""Tests for astrada.webhooks.verify_webhook against two known deliveries:

- SVIX: the test vector published with the Svix and Standard Webhooks libraries;
- ASTRADA: a delivery signed by the svix library 1.36.0 (the version service-webhooks-platform
  uses) with a secret made the way Astrada makes them, base64 of a UUID with no whsec_ prefix.
"""

import unittest

from astrada import WebhookVerificationError, verify_webhook

SVIX = dict(
    secret="whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw",  # gitleaks:allow (test vector)
    id="msg_p5jXN8AQM9LWM0D4loKWxJek",
    timestamp=1614265330,
    body='{"test": 2432232314}',
    signature="v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE=",
)
ASTRADA = dict(
    secret="OGYxNGU0NWYtY2VlYS00NjdhLTlkMmItMWEyYjNjNGQ1ZTZm",  # gitleaks:allow (test vector)
    id="msg_2Qh7Yx0Example",
    timestamp=1764000000,
    body='{"type":"transaction.created","data":{"id":"txn-1"}}',
    signature="v1,ugIbG2sIrsoxOkgpZ737QRM1NgtSDpGCDnpIVrDPAtE=",
)
EVENT = {"type": "transaction.created", "data": {"id": "txn-1"}}


def headers(v, prefix="webhook"):
    return {
        f"{prefix}-id": v["id"],
        f"{prefix}-timestamp": str(v["timestamp"]),
        f"{prefix}-signature": v["signature"],
    }


class TestVerifyWebhook(unittest.TestCase):
    def test_accepts_the_published_svix_vector(self):
        result = verify_webhook(SVIX["body"], headers(SVIX), SVIX["secret"], now=SVIX["timestamp"])
        self.assertEqual(result.raw, {"test": 2432232314})

    def test_accepts_an_astrada_secret_with_either_header_set(self):
        a = ASTRADA
        self.assertEqual(verify_webhook(a["body"], headers(a), a["secret"], now=a["timestamp"]).raw, EVENT)
        self.assertEqual(
            verify_webhook(a["body"].encode(), headers(a, "svix"), a["secret"], now=a["timestamp"]).raw,
            EVENT,
        )
        upper = {k.upper(): v for k, v in headers(a).items()}
        self.assertEqual(verify_webhook(a["body"], upper, a["secret"], now=a["timestamp"]).raw, EVENT)

    def test_accepts_any_matching_entry_in_a_multi_signature_header(self):
        a = ASTRADA
        h = headers(a)
        h["webhook-signature"] = "v1,bm90IHRoZSBzaWduYXR1cmU= " + a["signature"]
        self.assertEqual(verify_webhook(a["body"], h, a["secret"], now=a["timestamp"]).raw, EVENT)

    def test_rejects_a_changed_body_a_wrong_secret_and_a_missing_header(self):
        a = ASTRADA
        with self.assertRaises(WebhookVerificationError):
            verify_webhook(a["body"].replace("txn-1", "txn-2"), headers(a), a["secret"], now=a["timestamp"])
        with self.assertRaises(WebhookVerificationError):
            verify_webhook(a["body"], headers(a), SVIX["secret"], now=a["timestamp"])
        h = headers(a)
        del h["webhook-signature"]
        with self.assertRaises(WebhookVerificationError):
            verify_webhook(a["body"], h, a["secret"], now=a["timestamp"])

    def test_rejects_a_delivery_more_than_five_minutes_off(self):
        a = ASTRADA
        verify_webhook(a["body"], headers(a), a["secret"], now=a["timestamp"] + 300)
        for offset in (301, -301):
            with self.assertRaises(WebhookVerificationError):
                verify_webhook(a["body"], headers(a), a["secret"], now=a["timestamp"] + offset)



class TestTransactionWebhookMessages(unittest.TestCase):
    """A transaction webhook keeps _embedded.messages, with each dateTime a datetime."""

    def test_embedded_messages_survive(self):
        import base64
        import datetime
        import hashlib
        import hmac
        import json

        from astrada import TransactionWebhookMessage
        from astrada.models.transaction import Transaction

        # The shape of the docs' "Transaction with Projected TransactionMessage Data" sample.
        body = json.dumps({
            "_links": {"self": {"href": "/transactions/0b4f3c5e-8a1d-4f2b-9c3e-6d7a8b9c0d1e"}, "subaccount": {"href": "/subaccounts/5a6b7c8d-9e0f-4a1b-8c2d-3e4f5a6b7c8d"},
                       "card": {"href": "/cards/1c2d3e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f"}, "messages": [{"href": "/transaction-messages/2d3e4f5a-6b7c-4d8e-9f0a-1b2c3d4e5f6a"}]},
            "acceptor": {"city": "LONDON", "country": "GBR", "mcc": "5734", "state": "LND"},
            "cardId": "1c2d3e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "cardholderBillingCurrency": "GBP", "cardholderBillingHoldAmount": 0,
            "cardholderBillingSettledAmount": 0.81, "createdAt": "2024-05-01T06:41:43.810Z",
            "descriptor": "Uber", "id": "0b4f3c5e-8a1d-4f2b-9c3e-6d7a8b9c0d1e", "network": "MASTERCARD", "status": "SETTLED",
            "subaccountId": "5a6b7c8d-9e0f-4a1b-8c2d-3e4f5a6b7c8d", "transactionCurrency": "USD", "transactionHoldAmount": 0,
            "transactionOccurrenceDate": "2024-05-01", "transactionSettledAmount": 1,
            "updatedAt": "2024-05-02T08:41:43.810Z",
            "_embedded": {"messages": [
                {"_links": {"self": {"href": "/transaction-messages/2d3e4f5a-6b7c-4d8e-9f0a-1b2c3d4e5f6a"}}, "approvalCode": "537254",
                 "transactionReference": "IWVQ22_2024-04-24", "dateTime": "2024-04-24T13:39:45",
                 "id": "2d3e4f5a-6b7c-4d8e-9f0a-1b2c3d4e5f6a", "messageType": "FINL_ADVC", "network": "MASTERCARD", "result": "APPROVED"},
                {"id": "3e4f5a6b-7c8d-4e9f-8a1b-2c3d4e5f6a7b", "messageType": "AUTH_REQU", "network": "VISA", "dateTime": "2024-04-24T13:39:45Z"},
            ]},
        })
        secret, ts, msg_id = ASTRADA["secret"], 1764000000, "msg_messages"
        mac = hmac.new(base64.b64decode(secret), f"{msg_id}.{ts}.{body}".encode(), hashlib.sha256)
        for event_type in ("transaction.created", "transaction.updated"):
            event = verify_webhook(body, {
                "webhook-id": msg_id, "webhook-timestamp": str(ts),
                "webhook-signature": "v1," + base64.b64encode(mac.digest()).decode(),
                "webhook-event-type": event_type,
            }, secret, now=ts)
            self.assertIsInstance(event.data, Transaction)
            messages = event.messages
            self.assertEqual(len(event.data.embedded.additional_properties["messages"]), 2)
            self.assertIn('"dateTime"', event.data.to_json())  # data still writes the JSON names
            self.assertEqual(len(messages), 2)
            self.assertEqual(messages[0].approval_code, "537254")
            self.assertIsNone(messages[0].date_time.tzinfo)  # Mastercard local time
            self.assertEqual(messages[1].date_time,
                             datetime.datetime(2024, 4, 24, 13, 39, 45, tzinfo=datetime.timezone.utc))
            self.assertIsInstance(messages[0], TransactionWebhookMessage)
            self.assertEqual(str(event.data.id), "0b4f3c5e-8a1d-4f2b-9c3e-6d7a8b9c0d1e")

    def test_one_unreadable_message_keeps_the_others(self):
        import base64
        import hashlib
        import hmac
        import json

        body = json.dumps({
            "id": "0b4f3c5e-8a1d-4f2b-9c3e-6d7a8b9c0d1e",
            "_embedded": {"messages": [
                {"id": "2d3e4f5a-6b7c-4d8e-9f0a-1b2c3d4e5f6a", "dateTime": "2024-04-24T13:39:45Z"},
                {"id": "not-a-uuid", "dateTime": "2024-04-24T13:39:45Z"},
                {"id": "3e4f5a6b-7c8d-4e9f-8a1b-2c3d4e5f6a7b", "dateTime": "yesterday"},
                {"id": "4f5a6b7c-8d9e-4f0a-9b1c-2d3e4f5a6b7c", "dateTime": "2024-04-24T13:39:45"},
            ]},
        })
        secret, ts, msg_id = ASTRADA["secret"], 1764000000, "msg_mixed"
        mac = hmac.new(base64.b64decode(secret), f"{msg_id}.{ts}.{body}".encode(), hashlib.sha256)
        event = verify_webhook(body, {
            "webhook-id": msg_id, "webhook-timestamp": str(ts),
            "webhook-signature": "v1," + base64.b64encode(mac.digest()).decode(),
            "webhook-event-type": "transaction.created",
        }, secret, now=ts)
        self.assertEqual([str(m.id) for m in event.messages],
                         ["2d3e4f5a-6b7c-4d8e-9f0a-1b2c3d4e5f6a", "4f5a6b7c-8d9e-4f0a-9b1c-2d3e4f5a6b7c"])
        self.assertEqual([m["id"] for m in event.unreadable_messages],
                         ["not-a-uuid", "3e4f5a6b-7c8d-4e9f-8a1b-2c3d4e5f6a7b"])


    def test_a_signed_body_that_does_not_fit_its_model_is_marked_unreadable(self):
        import base64
        import hashlib
        import hmac
        import json

        secret, ts, msg_id = ASTRADA["secret"], 1764000000, "msg_unreadable"
        for event_type, body, unreadable in (
            ("transaction.created", json.dumps({"id": "not-a-uuid"}), True),
            ("something.new", json.dumps({"id": "x"}), False),
            ("transaction.updated", json.dumps([1, 2]), True),
        ):
            mac = hmac.new(base64.b64decode(secret), f"{msg_id}.{ts}.{body}".encode(), hashlib.sha256)
            event = verify_webhook(body, {
                "webhook-id": msg_id, "webhook-timestamp": str(ts),
                "webhook-signature": "v1," + base64.b64encode(mac.digest()).decode(),
                "webhook-event-type": event_type,
            }, secret, now=ts)
            self.assertIs(event.unreadable, unreadable)
            self.assertEqual(event.data, json.loads(body))


    def test_a_stored_delivery_is_read_again_without_a_signature(self):
        import datetime
        import json

        from astrada import parse_stored_webhook
        from astrada.models.transaction import Transaction

        body = json.dumps({"id": "not-a-uuid"})
        event = parse_stored_webhook(body, "transaction.created", "msg_stored", 1764000000)
        self.assertTrue(event.unreadable)
        self.assertEqual((event.id, event.timestamp, event.raw), ("msg_stored", 1764000000, {"id": "not-a-uuid"}))
        self.assertFalse(parse_stored_webhook(body.encode(), "something.new", "msg_2", 1).unreadable)
        # A modelled event, replayed from each stored form of body and timestamp.
        transaction = {
            "_links": {"self": {"href": "/t"}, "subaccount": {"href": "/s"}, "card": {"href": "/c"},
                       "messages": [{"href": "/m"}]},
            "acceptor": {"city": "LONDON", "country": "GBR", "mcc": "5734", "state": "LND"},
            "cardId": "1c2d3e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f", "cardholderBillingCurrency": "GBP",
            "cardholderBillingHoldAmount": 0, "cardholderBillingSettledAmount": 0.81,
            "createdAt": "2024-05-01T06:41:43.810Z", "descriptor": "Uber",
            "id": "0b4f3c5e-8a1d-4f2b-9c3e-6d7a8b9c0d1e", "network": "MASTERCARD", "status": "SETTLED",
            "subaccountId": "5a6b7c8d-9e0f-4a1b-8c2d-3e4f5a6b7c8d", "transactionCurrency": "USD",
            "transactionHoldAmount": 0, "transactionOccurrenceDate": "2024-05-01", "transactionSettledAmount": 1,
            "updatedAt": "2024-05-02T08:41:43.810Z",
        }
        text = json.dumps(transaction)
        when = datetime.datetime(2025, 11, 24, 16, 0, tzinfo=datetime.timezone.utc)
        for stored_body in (text, text.encode(), memoryview(text.encode()), bytearray(text.encode()), transaction):
            for stored_time in (1764000000, "1764000000", when, "2025-11-24T16:00:00Z",
                                "2025-11-24T17:00:00+01:00", "2025-11-24T16:00:00.1Z", "2025-11-24T16:00:00+0000",
                                "2025-11-24T16:00Z", "2025-11-24T17:00+01:00"):
                event = parse_stored_webhook(stored_body, "transaction.updated", "msg_t", stored_time)
                self.assertIsInstance(event.data, Transaction)
                self.assertFalse(event.unreadable)
                self.assertEqual(event.timestamp, 1764000000)
        for bad in (dict(event_type=""), dict(event_type="  "), dict(id=""), dict(timestamp="yesterday"),
                    dict(timestamp=float("nan")), dict(timestamp=float("inf")), dict(timestamp=1764000000000),
                    dict(timestamp=10**400), dict(timestamp="9" * 400),
                    dict(timestamp="1764000000000"), dict(timestamp=-1), dict(timestamp=None),
                    dict(timestamp="2025-11-24T16:00:00"), dict(timestamp="2025-11-24 16:00:00"),
                    dict(timestamp=datetime.datetime(2025, 11, 24, 16, 0)), dict(body=42), dict(body="not json")):
            args = dict(body=text, event_type="transaction.updated", id="msg_t", timestamp=1)
            args.update(bad)
            with self.assertRaises(ValueError, msg=repr(bad)):
                parse_stored_webhook(**args)
        # A delivery without a type header replays as plain JSON, as verify_webhook gives it.
        untyped = parse_stored_webhook(text, None, "msg_n", 1764000000)
        self.assertIsNone(untyped.type)
        self.assertEqual(untyped.data["descriptor"], "Uber")


if __name__ == "__main__":
    unittest.main()
