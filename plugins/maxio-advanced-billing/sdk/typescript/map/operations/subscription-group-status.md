<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionGroupStatus — operations

Accessor: `client.subscriptionGroupStatus` · Source: `src/resources/subscription-group-status.ts` · 4 operations · Request and error types: namespace `SubscriptionGroupStatus`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### cancelDelayedCancellationForGroup

- **Signature**: `cancelDelayedCancellationForGroup(request: SubscriptionGroupStatus.CancelDelayedCancellationForGroupRequest, options?: RequestOptions): ApiPromise<undefined, SubscriptionGroupStatus.CancelDelayedCancellationForGroupError>`
- **Wire**: `DELETE /subscription_groups/{uid}/delayed_cancel.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroupStatus.CancelDelayedCancellationForGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroupStatus.CancelDelayedCancellationForGroupRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### cancelSubscriptionsInGroup

- **Signature**: `cancelSubscriptionsInGroup(request: SubscriptionGroupStatus.CancelSubscriptionsInGroupRequest, options?: RequestOptions): ApiPromise<undefined, SubscriptionGroupStatus.CancelSubscriptionsInGroupError>`
- **Wire**: `POST /subscription_groups/{uid}/cancel.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroupStatus.CancelSubscriptionsInGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroupStatus.CancelSubscriptionsInGroupRequest` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |
| `body` | `body` | `CancelGroupedSubscriptionsRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CancelGroupedSubscriptionsRequest` | `cancelGroupedSubscriptionsRequestSchema` | `src/models/cancel-grouped-subscriptions-request.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### initiateDelayedCancellationForGroup

- **Signature**: `initiateDelayedCancellationForGroup(request: SubscriptionGroupStatus.InitiateDelayedCancellationForGroupRequest, options?: RequestOptions): ApiPromise<undefined, SubscriptionGroupStatus.InitiateDelayedCancellationForGroupError>`
- **Wire**: `POST /subscription_groups/{uid}/delayed_cancel.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroupStatus.InitiateDelayedCancellationForGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroupStatus.InitiateDelayedCancellationForGroupRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### reactivateSubscriptionGroup

- **Signature**: `reactivateSubscriptionGroup(request: SubscriptionGroupStatus.ReactivateSubscriptionGroupRequestParams, options?: RequestOptions): ApiPromise<ReactivateSubscriptionGroupResponse, SubscriptionGroupStatus.ReactivateSubscriptionGroupError>`
- **Wire**: `POST /subscription_groups/{uid}/reactivate.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ReactivateSubscriptionGroupResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroupStatus.ReactivateSubscriptionGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroupStatus.ReactivateSubscriptionGroupRequestParams` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |
| `body` | `body` | `ReactivateSubscriptionGroupRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ReactivateSubscriptionGroupRequest` | `reactivateSubscriptionGroupRequestSchema` | `src/models/reactivate-subscription-group-request.ts` |
| `ReactivateSubscriptionGroupResponse` | `reactivateSubscriptionGroupResponseSchema` | `src/models/reactivate-subscription-group-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

