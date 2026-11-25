# Astrada Python SDK

The Python client for the [Astrada API](https://docs.astrada.co): subaccounts, enrollment links,
card subscriptions, transactions, webhooks, the Banking API and the sandbox simulations, from one
client object. The SDKs have no card-enrollment methods. Card enrollment happens in the browser with the Unified Enrollment SDK v2 or an enrollment link. If you are an approved direct-API partner and send card data through the generic request method, it passes through your server and your PCI scope applies.
Python 3.10+ (every Python version its maintainers still support is tested; one is dropped only
in a major release). API version 2024-02-28.

**Start here:** [sign up for a sandbox](https://astrada.co/sandbox) ·
[Getting Started](https://docs.astrada.co/docs/getting-started) ·
[Authentication](https://docs.astrada.co/docs/authentication) ·
[API reference](https://docs.astrada.co/reference)

Questions: developer@astrada.co. Bugs and feature requests: [GitHub issues](https://github.com/FidelLimited/astrada-python/issues).
Security problems: report them privately as [SECURITY.md](https://github.com/FidelLimited/astrada-python/blob/main/SECURITY.md) explains.

## Install

```sh
pip install astrada
```

## Upgrading from 1.x

- Install `astrada` from PyPI (`pip install astrada`) and `import astrada`: 1.x was the `astrada_api` package,
  which is gone. Python 3.10 or later is required (1.x allowed 3.9).
- Make one `astrada.Astrada(...)` client with `environment="sandbox"` or `"production"`; it logs in itself and
  covers the main API, `client.banking` and `client.sandbox`.
- Methods take the names in the API reference: `get_subaccounts` is `list_subaccounts`, `get_transactions` is
  `list_transactions`, `get_transaction_by_id` is `get_transaction`, `bin_lookup` is `lookup_bin` and
  `card_verification_list` is `list_card_verifications`. The `cardholder_api` module is gone: `get_cardholder` is
  on `client.card`.
- Models are named for what they hold, not for the status code: `GetSubaccounts200Response` is `SubaccountList`,
  `GetTransactions200Response` is `TransactionList`, `CreateSubaccountRequest` is `SubaccountCreateParams`,
  `CreateWebhookRequest` is `WebhookCreateParams` and `CreateWebhook201Response` is `WebhookCreateResult`.
- Errors are typed (`NotFoundException`, `RateLimitError`, `ApiConnectionError` and the rest; see "Errors"), and a
  Mastercard `TransactionMessage.date_time` is naive (see "Reading transaction times").

Every change is listed in the [releases](https://github.com/FidelLimited/astrada-python/releases) and
`CHANGELOG.md`.

## First call

With the sandbox credentials from your sign-up in `ASTRADA_ACCOUNT_ID`, `ASTRADA_CLIENT_ID` and
`ASTRADA_CLIENT_SECRET`, list your subaccounts:

```python
import astrada

client = astrada.Astrada(environment="sandbox")  # reads the three variables
for subaccount in client.subaccounts.list_subaccounts(limit=5).embedded.subaccounts:
    print(subaccount.name)
```

## Log in

Make API credentials in the Astrada dashboard first (see
[Authentication](https://docs.astrada.co/docs/authentication)). Sandbox and production are separate
environments with separate credentials, so the client asks which one you mean.

```python
import os

import astrada

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
```

The client logs in on its first call, keeps the token and gets a new one shortly before it expires.
The card APIs and the Banking API (`client.banking`) share that one login. If you leave out the
three credentials, the client reads the `ASTRADA_ACCOUNT_ID`, `ASTRADA_CLIENT_ID` and
`ASTRADA_CLIENT_SECRET` environment variables.

If the login is refused (`400` or `401`), the call raises `astrada.AuthenticationError` with the
reason the login service gave, for example
`Login failed (401): Invalid client or Invalid client credentials.`, and nothing is sent to the
API. A login that is rate limited or fails on Astrada's side is retried like other calls, then
raises `RateLimitError` (`429`) or `ServiceException` (`5xx`), not `AuthenticationError`; a wrong
`account_id` raises `NotFoundException` (`404`).

## Mint a token for the browser enrollment SDK

The Unified Enrollment SDK v2 in your page asks your backend for a token (its `getAccessToken` option). Mint it
with your **SDK client**: the separate client id and secret Astrada gives you for the browser. Never hand the
browser a token of your backend client: it would carry every scope the backend holds, writes and `banking:admin`
included, so `mint_sdk_access_token` refuses the backend client's own `client_id` unless that client calls the sandbox API.

The token carries every scope the SDK client holds; the login does not narrow a token on request. List in
`allowed_scopes` only the scopes the browser calls need, from the [SDK credentials
table](https://docs.astrada.co/docs/authentication#sdk-credentials): the eight in the sample, plus `cards:read`
if you want the card lookup and `network-bulk-enrollments:write` or `network-bulk-feeds:write` for bulk
enrollment requests on admin pages. Never list `banking:admin` or `webhooks:write`, and if your SDK client holds
any scope the browser does not need, ask Astrada to remove it. If you do not offer bank sign-in, leave out the
two banking scopes and have them removed too. With `allowed_scopes`, the call raises `UnexpectedScopesError`
instead of returning a token that carries any scope outside the list (the check covers the scopes the login
states in its answer); a token missing a listed scope is still returned.

The token is not tied to one subaccount: for its five minutes it works on every subaccount of your account, for
card enrollment and card lookups, with the banking scopes for bank links and bank data, and with the bulk
enrollment scopes for bulk enrollment requests. Your server decides who gets a token, not what the token reaches,
so check that the signed-in user may use the subaccount the page opens, and remember that a user who copies the
token can call the API with it until it expires.

Sandbox self sign-up only, never in production: that account has one client for both uses, so its token carries
every backend scope. There, leave `allowed_scopes` out (the default, None).

```python
import os

token = client.mint_sdk_access_token(
    os.environ["ASTRADA_SDK_CLIENT_ID"],
    os.environ["ASTRADA_SDK_CLIENT_SECRET"],
    allowed_scopes=["subaccounts:read", "card-subscriptions:read", "card-subscriptions:write",
                    "card-verifications:read", "card-verifications:write", "enrollment-methods:write",
                    "banking:read", "banking:write"],  # Example: replace with the scopes the browser calls need
)  # return this from your backend's token route, as plain text
```

## List subaccounts

```python
page = client.subaccounts.list_subaccounts(limit=2)
for subaccount in page.embedded.subaccounts:
    print(subaccount.id, subaccount.name)
```

Every API group is an attribute of the client (`client.subaccounts`, `client.enrollment_links`,
`client.card_subscription`, `client.transactions`, `client.webhooks` and so on; the full list is
under [Reference](#reference)). Each method returns a model with typed attributes.

To read every page, see [Pagination](#pagination).

## Enroll a card

An enrollment link is a hosted page where a cardholder enrolls their card. Create one for a
subaccount and send its `url` to the cardholder:

```python
subaccount_id = page.embedded.subaccounts[0].id

link = client.enrollment_links.create_enrollment_link(
    astrada.EnrollmentLinkCreateParams(
        subaccount_id=subaccount_id,
        kind="cardholder",  # a personal link; "team" makes one link for many people
    )
)
print("Send this link:", link.url)
```

When the cardholder finishes, a card subscription exists for their card (and a
`cardsubscription.created` webhook is sent, see [Webhooks](#verify-a-webhook)):

```python
subscriptions = client.card_subscription.list_card_subscriptions(subaccount_id=str(subaccount_id))
for subscription in subscriptions.embedded.card_subscriptions:
    print(subscription.card_id, subscription.state)
```

Other ways to enroll (the embedded enrollment SDK, network bulk feeds and bank linking) are
described in the [enrollment guides](https://docs.astrada.co/docs).

## Find out why a card failed

A card whose verification failed has a failed verification with a `failure_reason`: a stable
`category` to branch on, a `description` you can show the cardholder, and whether a retry can
work (`retryable`).

```python
card_id = subscriptions.embedded.card_subscriptions[0].card_id

verifications = client.card_verification.list_card_verifications(card_id, state="failed")
for verification in verifications.embedded.card_verifications:
    reason = verification.failure_reason
    if reason is not None:
        print(reason.category, reason.description, "retryable:", reason.retryable)
```

## Simulate activity in the sandbox

The sandbox can make test transactions on enrolled cards and simulate network bulk files (see
[Sandbox API](https://docs.astrada.co/docs/sandbox-api)). Those methods are on `client.sandbox`:

```python
from astrada.sandbox import SimulateTransactionRequest

accepted = client.sandbox.simulate_transaction(
    SimulateTransactionRequest(card_id=card_id, type="authorization", amount=4500)
)
print(accepted)
```

The simulation runs in the background; the transaction then shows up in
`client.transactions.list_transactions()` and in your webhooks.

`client.sandbox` only works on a sandbox client: on a client made with
`environment="production"` (or with a `base_url` that is not the sandbox API), every
`client.sandbox` method raises `astrada.SandboxOnlyError` before sending anything, not even the
login. To send sandbox calls through a proxy or a local mock, mark it:
`astrada.Astrada(environment="sandbox", base_url="http://localhost:4010", sandbox_base_url=True)`.

## Clear test data in the sandbox

`client.sandbox` also has the sandbox-only deletes, for clearing test data between runs:
`delete_subaccount` (the subaccount and everything under it: bank links, card subscriptions,
cards, transactions, bulk feeds and webhooks), `delete_card_subscription` and
`delete_network_bulk_feed`. They cannot be undone. Each returns when the delete has finished, or
raises `ServiceException` (`502`) when a step failed; calling it again after a failure is safe,
because finished steps are skipped. The SDK never retries them itself, since a second call while
the first is still running is not safe. The sandbox API's gateway answers `504` after 29 seconds
while a longer delete keeps running (the SDK's own 5-minute wait cannot extend that): after a
`504`, read the resource (`get_subaccount`, `get_card_subscription`, `get_network_bulk_feed`)
every few seconds: `404` (`NotFoundException`) means the delete finished. A delete runs for at most
about 5 minutes, so if the resource still answers after 6 minutes, the first delete has stopped part-way
and calling it again is safe (finished steps are skipped). A `401` is raised as `UnauthorizedException`: this client does not log in again on a
refused token, so it does not send the delete again either. Production has no delete calls, and
these raise `astrada.SandboxOnlyError` outside the sandbox.

```python
client.sandbox.delete_subaccount(subaccount_id)
```

## Test bulk enrollment in the sandbox

Bulk enrollment enrolls a company's cards from the card network's bulk feed. In the sandbox you
create the feed as in production, then make the network "deliver" a feed file with
`client.sandbox.simulate_bulk_feed_file`: `type` is `"vcf"` or `"vbds"` (Visa), `"smartdata"`
(Mastercard) or `"gl"` (American Express). The simulated cards come from a fixed sandbox test-card
pool, and each one becomes a card subscription on the feed (see
[Testing Bulk Enrollment](https://docs.astrada.co/docs/sandbox-bulk-enrollment)).

```python
feed = client.network_bulk_feeds.create_network_bulk_feed(
    astrada.NetworkBulkFeedCreateParams(
        network="VISA", network_reference="1_123_45_6789", subaccount_id=subaccount_id
    )
)

client.sandbox.simulate_bulk_feed_file(
    type="vcf", network_reference="1_123_45_6789", card_count=3, transactions_per_card=1
)

bulk_cards = client.card_subscription.list_card_subscriptions(network_bulk_feed_id=str(feed.id))
print(bulk_cards.total_items, "card(s) on the feed so far")
```

The file is processed in the background, so the cards appear a short while after the call. Each
of the four file kinds also has its own method (`simulate_bulk_feed_file_vcf` and so on), and the
same sandbox-only check applies to all of them.

## Verify a webhook

Pass the raw request body, the headers and the webhook's `secret` (returned once when you create
the webhook). `verify_webhook` raises `WebhookVerificationError` if the signature does not match,
the delivery is more than five minutes old or the body is not JSON. Otherwise it returns a
`WebhookEvent`: `event.type` is the event type, and `event.data` is a typed model for
transaction, transaction message, card subscription and cardholder events (a `dict` for the
others).

<!-- standalone -->
```python
import os

from flask import Flask, request

import astrada

app = Flask(__name__)
# After this many unreadable deliveries of one event, answer 2xx and rely on the stored copy.
MAX_UNREADABLE_DELIVERIES = 3


def store_unreadable(event: astrada.WebhookEvent, body: bytes) -> int:
    """Replace with your own store (a table keyed by event.id). Save event.id, event.type,
    event.timestamp, the raw body, the time of the check, event.unreadable and
    event.unreadable_messages (so a replay of a partial delivery knows which messages were
    missing), and return how many times this id has been saved, counting this one. Until you
    replace it, it raises, so the handler answers 500 and Astrada delivers the event again."""
    raise NotImplementedError("store_unreadable is not set up (delivery %s)" % event.id)


@app.post("/astrada/webhooks")
def astrada_webhook():
    body = request.get_data()
    try:
        event = astrada.verify_webhook(body, request.headers, os.environ["ASTRADA_WEBHOOK_SECRET"])
    except astrada.WebhookVerificationError:
        return "", 400  # not from Astrada, or too old: refuse it
    if event.unreadable or event.unreadable_messages:
        # Signed by Astrada (the check passed), but this SDK cannot read the body, or one of a
        # transaction's messages (event.messages has the others). Store it first; answer 2xx only
        # once it is stored.
        try:
            failures = store_unreadable(event, body)
        except Exception as error:
            # The type only: an error from a database driver can include the body it was given.
            print("Unreadable webhook not stored", event.id, type(error).__name__)
            return "", 500  # not stored: Astrada must deliver it again
        print("Unreadable webhook stored", event.id, failures, len(event.unreadable_messages))
        if event.unreadable:
            return "", 204 if failures >= MAX_UNREADABLE_DELIVERIES else 500
    if event.type == "transaction.created" and not event.unreadable:
        transaction = event.data  # an astrada.Transaction
        print("New transaction", transaction.id)
    # Record event.id as handled in your store here, so a replay or a repeated delivery can skip it.
    # Answer within 5 seconds; do slow work after answering.
    return "", 204
```

Answer `400` only for `WebhookVerificationError`. `event.unreadable` means the delivery is signed but this SDK
cannot read it: store it, then answer `500` so Astrada delivers it again, and answer `2xx` once it is stored and
has failed `MAX_UNREADABLE_DELIVERIES` times (3 here; choose your own). With only `event.unreadable_messages`, the
transaction itself was read and handled, so the sample stores the delivery and answers `204`; replay only its
missing messages later. The stored copy is how you recover the event: after updating the SDK, read each stored
delivery with `astrada.parse_stored_webhook(body, event_type, id, timestamp)`. It checks no signature (the
five-minute limit would refuse a stored delivery anyway), so give it only deliveries you stored after the check
passed, and keep the time of that check with them. Store whether a delivery was partial, so a replay knows which
part is missing.
Replay with care: skip a stored delivery whose id you already handled (except a partial delivery, whose
transaction you handled but whose missing messages you have not), because a retry can succeed once the SDK is
updated. The stored body is a snapshot: for a transaction, apply it only if its `data.updated_at` is newer than
your copy's; for other resources, fetch the current state first. (`event.timestamp` is when the delivery was
sent, so a late retry carries a newer one; do not compare it.) Mark the stored row as handled, or delete it, once
it is done.

Deliveries can repeat: `event.id` is the same on every retry of one event.

## Reading transaction times

A transaction message's `date_time` is a `datetime`, and what it holds depends on the card network:

- Visa and Amex send UTC (a `Z` in the API): `date_time` is timezone-aware, an exact moment.
- Mastercard sends the merchant's local date and time with no offset: `date_time` is naive. It is the
  wall-clock time where the card was used, and Astrada does not receive that merchant's time zone, so it is
  not an exact moment. Do not call `.timestamp()` or `.astimezone()` on it (Python would use your server's
  zone), and do not compare or sort it with an aware value (`TypeError`).
- Some messages carry an end-of-day value rather than the moment they happened: Visa clearings
  (`FINL_ADVC`, `FINL_REQU`) the settlement date at `23:59:59Z`, Visa reversals (`AUTH_ADVC` with a
  negative amount) `23:59:59Z` on the day Astrada received them, Amex clearings the business date at
  `23:59:59Z`. Use the transaction's `transaction_occurrence_date` for the purchase date.
- For other networks (such as `OPEN_BANKING`) the definition does not say which zone applies: an aware
  value is exact, a naive one is a wall time of unknown zone.

To order messages across networks, use `created_date_time`: when Astrada recorded the message, in UTC.
A `transaction.created` or `transaction.updated` webhook carries a short form of each message in
`_embedded.messages`; `verify_webhook` gives them as `event.messages`, with `date_time` read the same way.

```python
message = client.transaction_messages.get_transaction_message("3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b")
if message.date_time.tzinfo is None:
    print("local time, no zone (the merchant's for Mastercard):", message.date_time.isoformat())
else:
    print("UTC:", message.date_time.isoformat())
print("recorded:", message.created_date_time.isoformat())
```

## Pagination

List methods return one page. `astrada.paginate` walks every page for you and yields the items; it
asks for the next page only when the loop gets there:

```python
for subaccount in astrada.paginate(client.subaccounts.list_subaccounts, limit=100):
    print(subaccount.id)

for bank_link in astrada.paginate(client.banking.bank_links.list_bank_links):
    print(bank_link.id, bank_link.state)
```

It works for every `list_*` method, whether the endpoint pages with a cursor or an offset, and
passes your filters along. `astrada.pagination.pages` yields whole pages instead.

## Errors

Every failed call raises a subclass of `astrada.ApiException`. Each one has `status`, `title`,
`detail`, `code` (when the API sends one), `errors` (the list of problems in a `400`), `body` and
`headers`.

```python
try:
    client.subaccounts.get_subaccount("00000000-0000-0000-0000-000000000000")
except astrada.NotFoundException as e:
    print("Not found:", e.detail)
except astrada.ApiException as e:
    print("Failed:", e.status, e.title, e.detail)
```

| Exception | When |
|---|---|
| `AuthenticationError` | The login was refused with `400` or `401` (the token endpoint's message is in `detail`); its subclass `UnauthorizedException` is a `401` from the API |
| `BadRequestException` | `400`: `errors` lists each problem |
| `ForbiddenException` | `403`: often a scope your API client does not have |
| `NotFoundException` | `404` |
| `ConflictException` | `409` |
| `UnprocessableEntityException` | `422` |
| `RateLimitError` | `429` after the retries; `retry_after` is the wait the API asked for |
| `ServiceException` | `5xx` after the retries |
| `ApiConnectionError` | No answer, or not all of it: the host could not be reached, TLS failed, the call timed out, or the body stopped arriving or was cut off (`status` is 0) |
| `ScopeRequiredError` | `403` on a Banking API method that needs a scope, most likely one your API client does not have; `required_scope` names it |
| `SandboxOnlyError` | A `client.sandbox` method, or a sandbox-only path given to `client.request`, on a client that is not set up for the sandbox (nothing was sent) |
| `UnexpectedScopesError` | `mint_sdk_access_token` with `allowed_scopes`: the token carries other scopes (`extra_scopes`), or the login stated none; the token is not returned |

A response with a value this SDK version does not know yet (a new state or event type, say) does
not fail: the value is kept as a string. Unknown fields are ignored.

## Retries and timeouts

Each request waits up to 60 seconds. Calls that are safe to repeat (`GET`, `PUT`, `DELETE`) are
retried twice after a `429`, `500`, `502`, `503` or `504`, with waits that grow from half a second,
and the API's `Retry-After` is honoured when it is 60 seconds or less (a longer one ends the
retries, and the call raises at once); with this default policy a malformed `Retry-After` means
the usual wait. Connection failures are retried for every call except the sandbox deletes. A
`POST` or `PATCH` that got an answer is never sent again, and neither are the sandbox deletes (see
above). The login is retried the same way after a `429`,
a `5xx` or a timeout. Calls that need a token while one is being requested wait for it, so with
the defaults a login that keeps timing out can hold them for about three times the timeout; a
call's own `_request_timeout` does not shorten the login. A body that stops arriving or a
connection dropped mid-body raises `ApiConnectionError` and is not retried. With a urllib3 `Retry`
of your own (`retries=Retry(...)`), running out of retries still raises the matching exception
(such as `RateLimitError`), and the login adds `POST` to its allowed methods; its `Retry-After`
handling is urllib3's own (a malformed value raises `ApiConnectionError`, and there is no 60-second
cap).

```python
patient_client = astrada.Astrada(environment="sandbox", timeout=120, retries=5)
quiet_client = astrada.Astrada(environment="sandbox", retries=0)

# One call with its own timeout, in seconds:
client.subaccounts.list_subaccounts(_request_timeout=10)
```

## Operations that need banking:admin

A few Banking API methods (for example `client.banking.bank_links.sync_bank_link` and the bank
subscription reads) need the `banking:admin` scope. Their reference pages start with "Needs
banking:admin". If your API client does not have the scope, the API answers `403` and the method
raises `astrada.ScopeRequiredError`, a subclass of `ForbiddenException`, which names the scope in
`required_scope`. Ask Astrada to enable it if you need one of these operations. As with any `403`,
the resource may also not be your account's, so the message names the scope as the likely cause.

```python
try:
    client.banking.bank_links.sync_bank_link("enrollment_792dcb7d")
except astrada.ScopeRequiredError as e:
    print(e.operation, "needs", e.required_scope)
```

## Calling an endpoint the SDK doesn't wrap

If the API has an endpoint this version of the SDK has no method for, call it with `client.request`. It uses the
client's login, environment and timeouts, and raises the same exceptions (`NotFoundException`, `ApiException` and
the rest). It retries a GET, PUT or DELETE on the same rules as the rest of the SDK and never sends a POST or
PATCH twice. Every sandbox-only operation (listed from the sandbox API definition when the SDK is built, such as
`DELETE /subaccounts/{id}`) and any `/simulate` path get the same sandbox check as `client.sandbox`, and the
sandbox-only deletes are never retried. The path is normalised once (`.` and `..` resolved, repeated slashes
dropped; a raw `?`, `#`, `\`, space or control character, or an encoded `/`, `\`, `.`, `?`, `#` or control
character, refused), and the checks run on the path that is sent. It returns the parsed JSON body, or None for an
empty one.

```python
page = client.request("GET", "/cards", query={"limit": 5})
print(len(page["_embedded"]["cards"]))
```

## Testing your code

`astrada.testing.MockAstrada` gives you a client whose calls never leave your process. Every
method answers with the example from the API definition (regenerated with each SDK release, so it
follows the API), and you can set the answer of any method:

```python
from astrada.testing import MockAstrada

with MockAstrada() as mock:
    mock.respond(
        "get_subaccount", status=404, body={"title": "Not Found", "detail": "No such subaccount"}
    )
    try:
        mock.client.subaccounts.get_subaccount("3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b")
    except astrada.NotFoundException:
        print("handled the 404")

    page = mock.client.subaccounts.list_subaccounts()  # the definition's example
    print(len(page.embedded.subaccounts), "subaccount(s);", mock.calls[-1])
```

`mock.respond(name, handler=...)` takes a function of the recorded call for answers that depend
on the request, `mock.calls` lists what was sent, and `mock.refuse_login()` makes the next login
fail. Pass your own client (`MockAstrada(client)`) to answer for one your code already made.

To run a mock HTTP server instead (for a whole app, or to try requests by hand), serve the API
definition with [Prism](https://github.com/stoplightio/prism):

```sh
npx @stoplight/prism-cli mock https://raw.githubusercontent.com/FidelLimited/astrada-python/main/test/standin/openapi-main.json
```

and point a client at it (Prism has no login, so pass any token):

```python
prism_client = astrada.Astrada(
    environment="sandbox", base_url="http://127.0.0.1:4010", access_token="test"
)
```

The Banking API and the sandbox definitions are next to it (`openapi-banking.json`,
`openapi-sandbox.json`).

## Banking API

The Banking API (bank links, bank accounts, bank subscriptions, bank transactions and transaction
matches) is `client.banking`:

```python
bank_links = client.banking.bank_links.list_bank_links(limit=10)
for bank_link in bank_links.items:
    print(bank_link.id, bank_link.state)
```

## Reference

The full reference, built from the code, is at
[fidellimited.github.io/astrada-python](https://fidellimited.github.io/astrada-python/astrada.html).
Each method is also described on the API reference at
[docs.astrada.co/reference](https://docs.astrada.co/reference).

| Client attribute | Method | HTTP request |
|---|---|---|
| `client.bin_lookup` | [`lookup_bin`](https://github.com/FidelLimited/astrada-python/blob/main/docs/BinLookupApi.md#lookup_bin) | `GET /bin-lookup` |
| `client.card` | [`get_card`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardApi.md#get_card) | `GET /cards/{cardId}` |
| `client.card` | [`get_cardholder`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardApi.md#get_cardholder) | `GET /cards/{cardId}/cardholder` |
| `client.card` | [`list_cards`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardApi.md#list_cards) | `GET /cards` |
| `client.card` | [`update_cardholder`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardApi.md#update_cardholder) | `PATCH /cards/{cardId}/cardholder` |
| `client.card_subscription` | [`get_card_subscription`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardSubscriptionApi.md#get_card_subscription) | `GET /card-subscriptions/{subscriptionId}` |
| `client.card_subscription` | [`list_card_subscriptions`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardSubscriptionApi.md#list_card_subscriptions) | `GET /card-subscriptions` |
| `client.card_subscription` | [`update_card_subscription`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardSubscriptionApi.md#update_card_subscription) | `PATCH /card-subscriptions/{subscriptionId}` |
| `client.card_verification` | [`get_card_verification`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardVerificationApi.md#get_card_verification) | `GET /card-verifications/3ds/{verificationId}` |
| `client.card_verification` | [`list_card_verifications`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardVerificationApi.md#list_card_verifications) | `GET /card-verifications/3ds` |
| `client.card_verification` | [`unlock_card_verification_attempts`](https://github.com/FidelLimited/astrada-python/blob/main/docs/CardVerificationApi.md#unlock_card_verification_attempts) | `POST /card-verifications/unlock` |
| `client.enrollment_links` | [`create_enrollment_link`](https://github.com/FidelLimited/astrada-python/blob/main/docs/EnrollmentLinksApi.md#create_enrollment_link) | `POST /enrollment-links` |
| `client.enrollment_links` | [`create_team_link`](https://github.com/FidelLimited/astrada-python/blob/main/docs/EnrollmentLinksApi.md#create_team_link) | `POST /subaccounts/{subaccountId}/team-link` |
| `client.enrollment_links` | [`get_enrollment_link`](https://github.com/FidelLimited/astrada-python/blob/main/docs/EnrollmentLinksApi.md#get_enrollment_link) | `GET /enrollment-links/{linkId}` |
| `client.enrollment_links` | [`list_enrollment_links`](https://github.com/FidelLimited/astrada-python/blob/main/docs/EnrollmentLinksApi.md#list_enrollment_links) | `GET /enrollment-links` |
| `client.enrollment_links` | [`revoke_enrollment_link`](https://github.com/FidelLimited/astrada-python/blob/main/docs/EnrollmentLinksApi.md#revoke_enrollment_link) | `POST /enrollment-links/{linkId}/revoke` |
| `client.enrollment_methods` | [`get_enrollment_methods`](https://github.com/FidelLimited/astrada-python/blob/main/docs/EnrollmentMethodsApi.md#get_enrollment_methods) | `POST /enrollment-methods` |
| `client.network_bulk_enrollments` | [`create_network_bulk_confirmation`](https://github.com/FidelLimited/astrada-python/blob/main/docs/NetworkBulkEnrollmentsApi.md#create_network_bulk_confirmation) | `POST /network-bulk-confirmations` |
| `client.network_bulk_enrollments` | [`create_network_bulk_enrollment`](https://github.com/FidelLimited/astrada-python/blob/main/docs/NetworkBulkEnrollmentsApi.md#create_network_bulk_enrollment) | `POST /network-bulk-enrollments` |
| `client.network_bulk_enrollments` | [`get_network_bulk_enrollment`](https://github.com/FidelLimited/astrada-python/blob/main/docs/NetworkBulkEnrollmentsApi.md#get_network_bulk_enrollment) | `GET /network-bulk-enrollments/{networkBulkEnrollmentId}` |
| `client.network_bulk_enrollments` | [`get_open_network_bulk_enrollment`](https://github.com/FidelLimited/astrada-python/blob/main/docs/NetworkBulkEnrollmentsApi.md#get_open_network_bulk_enrollment) | `GET /network-bulk-enrollments/open` |
| `client.network_bulk_feeds` | [`create_network_bulk_feed`](https://github.com/FidelLimited/astrada-python/blob/main/docs/NetworkBulkFeedsApi.md#create_network_bulk_feed) | `POST /network-bulk-feeds` |
| `client.network_bulk_feeds` | [`get_network_bulk_feed`](https://github.com/FidelLimited/astrada-python/blob/main/docs/NetworkBulkFeedsApi.md#get_network_bulk_feed) | `GET /network-bulk-feeds/{networkBulkFeedId}` |
| `client.network_bulk_feeds` | [`list_network_bulk_feeds`](https://github.com/FidelLimited/astrada-python/blob/main/docs/NetworkBulkFeedsApi.md#list_network_bulk_feeds) | `GET /network-bulk-feeds` |
| `client.network_bulk_feeds` | [`update_network_bulk_feed`](https://github.com/FidelLimited/astrada-python/blob/main/docs/NetworkBulkFeedsApi.md#update_network_bulk_feed) | `PATCH /network-bulk-feeds/{networkBulkFeedId}` |
| `client.subaccounts` | [`create_subaccount`](https://github.com/FidelLimited/astrada-python/blob/main/docs/SubaccountsApi.md#create_subaccount) | `POST /subaccounts` |
| `client.subaccounts` | [`get_subaccount`](https://github.com/FidelLimited/astrada-python/blob/main/docs/SubaccountsApi.md#get_subaccount) | `GET /subaccounts/{subaccountId}` |
| `client.subaccounts` | [`list_subaccounts`](https://github.com/FidelLimited/astrada-python/blob/main/docs/SubaccountsApi.md#list_subaccounts) | `GET /subaccounts` |
| `client.subaccounts` | [`update_subaccount`](https://github.com/FidelLimited/astrada-python/blob/main/docs/SubaccountsApi.md#update_subaccount) | `PATCH /subaccounts/{subaccountId}` |
| `client.transaction_messages` | [`get_raw_transaction_message`](https://github.com/FidelLimited/astrada-python/blob/main/docs/TransactionMessagesApi.md#get_raw_transaction_message) | `GET /transaction-messages/{transactionMessageId}/raw` |
| `client.transaction_messages` | [`get_transaction_message`](https://github.com/FidelLimited/astrada-python/blob/main/docs/TransactionMessagesApi.md#get_transaction_message) | `GET /transaction-messages/{transactionMessageId}` |
| `client.transactions` | [`get_transaction`](https://github.com/FidelLimited/astrada-python/blob/main/docs/TransactionsApi.md#get_transaction) | `GET /transactions/{transactionId}` |
| `client.transactions` | [`list_transactions`](https://github.com/FidelLimited/astrada-python/blob/main/docs/TransactionsApi.md#list_transactions) | `GET /transactions` |
| `client.webhooks` | [`create_webhook`](https://github.com/FidelLimited/astrada-python/blob/main/docs/WebhooksApi.md#create_webhook) | `POST /webhooks` |
| `client.webhooks` | [`delete_webhook`](https://github.com/FidelLimited/astrada-python/blob/main/docs/WebhooksApi.md#delete_webhook) | `DELETE /webhooks/{webhookId}` |
| `client.webhooks` | [`get_webhook`](https://github.com/FidelLimited/astrada-python/blob/main/docs/WebhooksApi.md#get_webhook) | `GET /webhooks/{webhookId}` |
| `client.webhooks` | [`list_webhooks`](https://github.com/FidelLimited/astrada-python/blob/main/docs/WebhooksApi.md#list_webhooks) | `GET /webhooks` |
| `client.webhooks` | [`update_webhook`](https://github.com/FidelLimited/astrada-python/blob/main/docs/WebhooksApi.md#update_webhook) | `PATCH /webhooks/{webhookId}` |


Banking methods (`client.banking.<group>`) are listed in
[docs/banking/README.md](https://github.com/FidelLimited/astrada-python/blob/main/docs/banking/README.md), and the
sandbox methods (`client.sandbox`) in
[docs/sandbox/README.md](https://github.com/FidelLimited/astrada-python/blob/main/docs/sandbox/README.md).

## Versions

Releases follow semantic versioning; [CHANGELOG.md](https://github.com/FidelLimited/astrada-python/blob/main/CHANGELOG.md)
lists what each one changed. `astrada.__version__` is the installed version, and every request
sends it in the `User-Agent` header (`astrada-python/<version>`).
