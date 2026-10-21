# Webhooks: provider notes

Managing webhook endpoints. Receiving webhooks (signature, 200 OK, deduplication, ordering) is
`../rules.md` R19 and R20; the endpoint lifecycle is `../lifecycles.md` L7. An operation of this group
that has no section here has no provider notes (see `../index.json`).

### createEndpoint
`client.webhooks.create_endpoint` · `POST /endpoints.json` · contract: `map/operations/webhooks.md`

**Before you call**
- The receiving URL must be public, on port 80 or 443, accept `POST` with
  `application/x-www-form-urlencoded`, and use HTTPS for live sites (HTTP only in test mode) [docs].

**Rules**
- Subscribe only with event keys the contract lists for `webhook_subscriptions`. Maxio emits more
  event keys than that list holds, and a key outside it is rejected (second row below).
- On sites with the new Catalog experience, the webhooks reference lists renamed events:
  `subscription_plan_change`, `allocation_change` and `product_billing_date_change` [docs]. The
  announcement says no API names are being renamed, so which spelling arrives is not settled
  *(unconfirmed)*. Accept both spellings in the receiver (R20) and keep subscribing with the
  contract's keys.
- You may put `{signature_hmac_sha_256}` in the URL's query string as a replacement variable instead of
  reading the header [docs].

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "URL: invalid, only http and https supported" | The URL is not an http or https URL | Send a public http(s) URL on port 80 or 443 |
| 422 "Event key is not valid" | A key in `webhook_subscriptions` is not a known event (documented on `update_endpoint`; assumed here). The message ends with the key | Use only the keys the contract lists |

**Sources:** [spec] createEndpoint, updateEndpoint, Webhook-Subscription, Event-Key · [docs] webhooks
"Using Webhooks" and "Verifying Events", webhooks-reference · [announcement] 2026 "NEW Catalog
Experience and Terminology"

### updateEndpoint
`client.webhooks.update_endpoint` · `PUT /endpoints/{endpoint_id}.json` · contract: `map/operations/webhooks.md`
**Always:** Send the complete `webhook_subscriptions` list: read the current one with `list_endpoints`, then send every event to keep plus the new ones. An event left out is unsubscribed, and an empty list unsubscribes all.

**Rules**
- `webhook_subscriptions` **replaces the whole list**. To add one event, read the current list
  (`list_endpoints`) and send all of them; to drop one, send the list "without the specific event key";
  an empty list "will unsubscribe all events".

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Event key is not valid" | A key in `webhook_subscriptions` is not a known event. The message ends with the key | Use only the keys the contract lists |

**Sources:** [spec] updateEndpoint

### listWebhooks
`client.webhooks.list_webhooks` · `GET /webhooks.json` · contract: `map/operations/webhooks.md`

**Rules**
- `status` takes one value per call. To catch a failing receiver before it is disabled, ask once for
  `failed` and once for `paused` (lifecycles.md L7).
- Each record carries the exact `body` that was sent and its `signature_hmac_sha_256` [spec]. Together
  they make realistic fixtures for a receiver's signature test *(inferred)*.

**Sources:** [spec] listWebhooks, Webhook, Webhook-Status

### replayWebhooks
`client.webhooks.replay_webhooks` · `POST /webhooks/replay.json` · contract: `map/operations/webhooks.md`
**Always:** Send at most 1000 ids per call. Replay only after `last_sent_at` is well outside the automatic retry intervals.

**Rules**
- Up to 1000 ids, queued, not delivered inline. Replay only after `last_sent_at` is well outside the
  automatic retry intervals, or the same webhook arrives twice. The webhook `id` does not change on
  replay, so your deduplication still works.

**Sources:** [spec] replayWebhooks · [docs] webhooks "Responding to a Webhook"

### enableWebhooks
`client.webhooks.enable_webhooks` · `PUT /webhooks/settings.json` · contract: `map/operations/webhooks.md`

**Rules**
- Site-wide switch (`webhooks_enabled`). Whether endpoints deliver while it is off is not stated
  *(unconfirmed)*.

**Sources:** [spec] enableWebhooks
