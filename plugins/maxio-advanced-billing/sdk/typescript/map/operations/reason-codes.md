<!-- Generated file — do not edit; regenerated with the SDK. -->

# ReasonCodes — operations

Accessor: `client.reasonCodes` · Source: `src/resources/reason-codes.ts` · 5 operations · Request and error types: namespace `ReasonCodes`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createReasonCode

- **Signature**: `createReasonCode(request?: ReasonCodes.CreateReasonCodeRequestParams, options?: RequestOptions): ApiPromise<ReasonCodeResponse, ReasonCodes.CreateReasonCodeError>`
- **Wire**: `POST /reason_codes.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ReasonCodeResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ReasonCodes.CreateReasonCodeError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ReasonCodes.CreateReasonCodeRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateReasonCodeRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateReasonCodeRequest` | `createReasonCodeRequestSchema` | `src/models/create-reason-code-request.ts` |
| `ReasonCodeResponse` | `reasonCodeResponseSchema` | `src/models/reason-code-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### deleteReasonCode

- **Signature**: `deleteReasonCode(request: ReasonCodes.DeleteReasonCodeRequest, options?: RequestOptions): ApiPromise<OkResponse, ReasonCodes.DeleteReasonCodeError>`
- **Wire**: `DELETE /reason_codes/{reason_code_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `OkResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ReasonCodes.DeleteReasonCodeError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ReasonCodes.DeleteReasonCodeRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `reasonCodeId` | `path` | `reason_code_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `OkResponse` | `okResponseSchema` | `src/models/ok-response.ts` |

### listReasonCodes

- **Signature**: `listReasonCodes(request?: ReasonCodes.ListReasonCodesRequest, options?: RequestOptions): ApiPromise<ReasonCodeResponse[], ReasonCodes.ListReasonCodesError>`
- **Wire**: `GET /reason_codes.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ReasonCodeResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ReasonCodes.ListReasonCodesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ReasonCodes.ListReasonCodesRequest` (2):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ReasonCodeResponse` | `reasonCodeResponseSchema` | `src/models/reason-code-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readReasonCode

- **Signature**: `readReasonCode(request: ReasonCodes.ReadReasonCodeRequest, options?: RequestOptions): ApiPromise<ReasonCodeResponse, ReasonCodes.ReadReasonCodeError>`
- **Wire**: `GET /reason_codes/{reason_code_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ReasonCodeResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ReasonCodes.ReadReasonCodeError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ReasonCodes.ReadReasonCodeRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `reasonCodeId` | `path` | `reason_code_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ReasonCodeResponse` | `reasonCodeResponseSchema` | `src/models/reason-code-response.ts` |

### updateReasonCode

- **Signature**: `updateReasonCode(request: ReasonCodes.UpdateReasonCodeRequestParams, options?: RequestOptions): ApiPromise<ReasonCodeResponse, ReasonCodes.UpdateReasonCodeError>`
- **Wire**: `PUT /reason_codes/{reason_code_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ReasonCodeResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ReasonCodes.UpdateReasonCodeError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ReasonCodes.UpdateReasonCodeRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `reasonCodeId` | `path` | `reason_code_id` | `number` | yes |
| `body` | `body` | — | `UpdateReasonCodeRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateReasonCodeRequest` | `updateReasonCodeRequestSchema` | `src/models/update-reason-code-request.ts` |
| `ReasonCodeResponse` | `reasonCodeResponseSchema` | `src/models/reason-code-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

