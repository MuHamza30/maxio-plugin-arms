<!-- Generated file — do not edit; regenerated with the SDK. -->

# Entitlements — operations

Accessor: `client.entitlements` · Source: `src/resources/entitlements.ts` · 1 operation · Request and error types: namespace `Entitlements`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### readSubscriptionEntitlements

- **Provider rules (Maxio)**: Match on the prefixed key (`feature.<key>`, `usage.<key>`, `service.<key>`), key entries on `periodicity_key`, and grant access only when `enabled` is true. Notes: `knowledge/operations/entitlements.md#readsubscriptionentitlements`
- **Signature**: `readSubscriptionEntitlements(request: Entitlements.ReadSubscriptionEntitlementsRequest, options?: RequestOptions): ApiPromise<AggregatedEntitlementsResponse, Entitlements.ReadSubscriptionEntitlementsError>`
- **Wire**: `GET /subscriptions/{subscription_id}/entitlements.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `AggregatedEntitlementsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Entitlements.ReadSubscriptionEntitlementsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Entitlements.ReadSubscriptionEntitlementsRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `AggregatedEntitlementsResponse` | `aggregatedEntitlementsResponseSchema` | `src/models/aggregated-entitlements-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

