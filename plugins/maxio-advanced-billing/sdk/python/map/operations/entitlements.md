<!-- Generated file — do not edit; regenerated with the SDK. -->

# Entitlements — operations

Accessor: `client.entitlements` · Source: `maxio_advanced_billing/apis/entitlements.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.entitlements.read_subscription_entitlements

- **Provider rules (Maxio)**: Match on the prefixed key (`feature.<key>`, `usage.<key>`, `service.<key>`), key entries on `periodicity_key`, and grant access only when `enabled` is true. Notes: `knowledge/operations/entitlements.md#readsubscriptionentitlements`
- **Route**: `GET /subscriptions/{subscription_id}/entitlements.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_subscription_entitlements(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`
- **Params**: `subscription_id` — path
- **Returns (parsed)**: `AggregatedEntitlementsResponse`
- **Returns (raw)**: `ApiResult[AggregatedEntitlementsResponse, ReadSubscriptionEntitlementsErrorBody]`
- **Error**: `ReadSubscriptionEntitlementsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `AggregatedEntitlementsResponse` | `maxio_advanced_billing/models/aggregated_entitlements_response.py` |
| `ReadSubscriptionEntitlementsErrorBody` | `maxio_advanced_billing/errors/read_subscription_entitlements_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

