<!-- Generated file — do not edit; regenerated with the SDK. -->

# Webhooks — operations

Accessor: `client.webhooks` · Source: `src/resources/webhooks.ts` · 6 operations · Request and error types: namespace `Webhooks`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createEndpoint

- **Provider notes (Maxio)**: `knowledge/operations/webhooks.md#createendpoint`
- **Signature**: `createEndpoint(request: Webhooks.CreateEndpointRequest, options?: RequestOptions): ApiPromise<EndpointResponse, Webhooks.CreateEndpointError>`
- **Wire**: `POST /endpoints.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `EndpointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Webhooks.CreateEndpointError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Webhooks.CreateEndpointRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateOrUpdateEndpointRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateOrUpdateEndpointRequest` | `createOrUpdateEndpointRequestSchema` | `src/models/create-or-update-endpoint-request.ts` |
| `EndpointResponse` | `endpointResponseSchema` | `src/models/endpoint-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### enableWebhooks

- **Provider notes (Maxio)**: `knowledge/operations/webhooks.md#enablewebhooks`
- **Signature**: `enableWebhooks(request: Webhooks.EnableWebhooksRequestParams, options?: RequestOptions): ApiPromise<EnableWebhooksResponse, ApiError>`
- **Wire**: `PUT /webhooks/settings.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `EnableWebhooksResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Webhooks.EnableWebhooksRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `EnableWebhooksRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `EnableWebhooksRequest` | `enableWebhooksRequestSchema` | `src/models/enable-webhooks-request.ts` |
| `EnableWebhooksResponse` | `enableWebhooksResponseSchema` | `src/models/enable-webhooks-response.ts` |

### listEndpoints

- **Signature**: `listEndpoints(options?: RequestOptions): ApiPromise<Endpoint[], ApiError>`
- **Wire**: `GET /endpoints.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `Endpoint[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

| Type | Schema value | Source |
| --- | --- | --- |
| `Endpoint` | `endpointSchema` | `src/models/endpoint.ts` |

### listWebhooks

- **Provider notes (Maxio)**: `knowledge/operations/webhooks.md#listwebhooks`
- **Signature**: `listWebhooks(request: Webhooks.ListWebhooksRequest, options?: RequestOptions): ApiPromise<WebhookResponse[], ApiError>`
- **Wire**: `GET /webhooks.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `WebhookResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Webhooks.ListWebhooksRequest` (7):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `status` | `query` | — | `WebhookStatus` | no | — |
| `sinceDate` | `query` | `since_date` | `string` | no | — |
| `untilDate` | `query` | `until_date` | `string` | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `order` | `query` | — | `WebhookOrder` | no | — |
| `subscription` | `query` | — | `number` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `WebhookStatus` | `webhookStatusSchema` | `src/models/webhook-status.ts` |
| `WebhookOrder` | `webhookOrderSchema` | `src/models/webhook-order.ts` |
| `WebhookResponse` | `webhookResponseSchema` | `src/models/webhook-response.ts` |

### replayWebhooks

- **Provider rules (Maxio)**: Send at most 1000 ids per call. Replay only after `last_sent_at` is well outside the automatic retry intervals. Notes: `knowledge/operations/webhooks.md#replaywebhooks`
- **Signature**: `replayWebhooks(request: Webhooks.ReplayWebhooksRequestParams, options?: RequestOptions): ApiPromise<ReplayWebhooksResponse, ApiError>`
- **Wire**: `POST /webhooks/replay.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ReplayWebhooksResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Webhooks.ReplayWebhooksRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `ReplayWebhooksRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ReplayWebhooksRequest` | `replayWebhooksRequestSchema` | `src/models/replay-webhooks-request.ts` |
| `ReplayWebhooksResponse` | `replayWebhooksResponseSchema` | `src/models/replay-webhooks-response.ts` |

### updateEndpoint

- **Provider rules (Maxio)**: Send the complete `webhook_subscriptions` list: read the current one with `listEndpoints`, then send every event to keep plus the new ones. An event left out is unsubscribed, and an empty list unsubscribes all. Notes: `knowledge/operations/webhooks.md#updateendpoint`
- **Signature**: `updateEndpoint(request: Webhooks.UpdateEndpointRequest, options?: RequestOptions): ApiPromise<EndpointResponse, Webhooks.UpdateEndpointError>`
- **Wire**: `PUT /endpoints/{endpoint_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `EndpointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Webhooks.UpdateEndpointError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Webhooks.UpdateEndpointRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `endpointId` | `path` | `endpoint_id` | `number` | yes |
| `body` | `body` | — | `CreateOrUpdateEndpointRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateOrUpdateEndpointRequest` | `createOrUpdateEndpointRequestSchema` | `src/models/create-or-update-endpoint-request.ts` |
| `EndpointResponse` | `endpointResponseSchema` | `src/models/endpoint-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

