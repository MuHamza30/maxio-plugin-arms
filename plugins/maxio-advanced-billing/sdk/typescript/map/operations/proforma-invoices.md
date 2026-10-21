<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProformaInvoices — operations

Accessor: `client.proformaInvoices` · Source: `src/resources/proforma-invoices.ts` · 10 operations · Request and error types: namespace `ProformaInvoices`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createConsolidatedProformaInvoice

- **Signature**: `createConsolidatedProformaInvoice(request: ProformaInvoices.CreateConsolidatedProformaInvoiceRequest, options?: RequestOptions): ApiPromise<undefined, ProformaInvoices.CreateConsolidatedProformaInvoiceError>`
- **Wire**: `POST /subscription_groups/{uid}/proforma_invoices.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProformaInvoices.CreateConsolidatedProformaInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProformaInvoices.CreateConsolidatedProformaInvoiceRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createProformaInvoice

- **Signature**: `createProformaInvoice(request: ProformaInvoices.CreateProformaInvoiceRequest, options?: RequestOptions): ApiPromise<ProformaInvoice, ProformaInvoices.CreateProformaInvoiceError>`
- **Wire**: `POST /subscriptions/{subscription_id}/proforma_invoices.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProformaInvoice`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProformaInvoices.CreateProformaInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProformaInvoices.CreateProformaInvoiceRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProformaInvoice` | `proformaInvoiceSchema` | `src/models/proforma-invoice.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createSignupProformaInvoice

- **Signature**: `createSignupProformaInvoice(request?: ProformaInvoices.CreateSignupProformaInvoiceRequest, options?: RequestOptions): ApiPromise<ProformaInvoice, ProformaInvoices.CreateSignupProformaInvoiceError>`
- **Wire**: `POST /subscriptions/proforma_invoices.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProformaInvoice`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProformaInvoices.CreateSignupProformaInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"proformaBadRequestErrorResponse1"` [400] `ProformaBadRequestErrorResponse1` · `"errorArrayMapResponse1"` [422] `ErrorArrayMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProformaInvoices.CreateSignupProformaInvoiceRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateSubscriptionRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateSubscriptionRequest` | `createSubscriptionRequestSchema` | `src/models/create-subscription-request.ts` |
| `ProformaInvoice` | `proformaInvoiceSchema` | `src/models/proforma-invoice.ts` |
| `ProformaBadRequestErrorResponse1` | `proformaBadRequestErrorResponse1Schema` | `src/models/proforma-bad-request-error-response1.ts` |
| `ErrorArrayMapResponse1` | `errorArrayMapResponse1Schema` | `src/models/error-array-map-response1.ts` |

### deliverProformaInvoice

- **Signature**: `deliverProformaInvoice(request: ProformaInvoices.DeliverProformaInvoiceRequestParams, options?: RequestOptions): ApiPromise<ProformaInvoice, ProformaInvoices.DeliverProformaInvoiceError>`
- **Wire**: `POST /proforma_invoices/{proforma_invoice_uid}/deliveries.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProformaInvoice`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProformaInvoices.DeliverProformaInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProformaInvoices.DeliverProformaInvoiceRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `proformaInvoiceUid` | `path` | `proforma_invoice_uid` | `string` | yes |
| `body` | `body` | — | `DeliverProformaInvoiceRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `DeliverProformaInvoiceRequest` | `deliverProformaInvoiceRequestSchema` | `src/models/deliver-proforma-invoice-request.ts` |
| `ProformaInvoice` | `proformaInvoiceSchema` | `src/models/proforma-invoice.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listProformaInvoices

- **Signature**: `listProformaInvoices(request: ProformaInvoices.ListProformaInvoicesRequest, options?: RequestOptions): ApiPromise<ListProformaInvoicesResponse, ApiError>`
- **Wire**: `GET /subscriptions/{subscription_id}/proforma_invoices.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListProformaInvoicesResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ProformaInvoices.ListProformaInvoicesRequest` (13):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes | — |
| `startDate` | `query` | `start_date` | `string` | no | — |
| `endDate` | `query` | `end_date` | `string` | no | — |
| `status` | `query` | — | `ProformaInvoiceStatus` | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `direction` | `query` | — | `Direction` | no | `Direction.Desc` |
| `lineItems` | `query` | `line_items` | `boolean` | no | `false` |
| `discounts` | `query` | — | `boolean` | no | `false` |
| `taxes` | `query` | — | `boolean` | no | `false` |
| `credits` | `query` | — | `boolean` | no | `false` |
| `payments` | `query` | — | `boolean` | no | `false` |
| `customFields` | `query` | `custom_fields` | `boolean` | no | `false` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProformaInvoiceStatus` | `proformaInvoiceStatusSchema` | `src/models/proforma-invoice-status.ts` |
| `Direction` | `directionSchema` | `src/models/direction.ts` |
| `ListProformaInvoicesResponse` | `listProformaInvoicesResponseSchema` | `src/models/list-proforma-invoices-response.ts` |

### listSubscriptionGroupProformaInvoices

- **Signature**: `listSubscriptionGroupProformaInvoices(request: ProformaInvoices.ListSubscriptionGroupProformaInvoicesRequest, options?: RequestOptions): ApiPromise<ListProformaInvoicesResponse, ProformaInvoices.ListSubscriptionGroupProformaInvoicesError>`
- **Wire**: `GET /subscription_groups/{uid}/proforma_invoices.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListProformaInvoicesResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProformaInvoices.ListSubscriptionGroupProformaInvoicesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProformaInvoices.ListSubscriptionGroupProformaInvoicesRequest` (7):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `uid` | `path` | — | `string` | yes | — |
| `lineItems` | `query` | `line_items` | `boolean` | no | `false` |
| `discounts` | `query` | — | `boolean` | no | `false` |
| `taxes` | `query` | — | `boolean` | no | `false` |
| `credits` | `query` | — | `boolean` | no | `false` |
| `payments` | `query` | — | `boolean` | no | `false` |
| `customFields` | `query` | `custom_fields` | `boolean` | no | `false` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListProformaInvoicesResponse` | `listProformaInvoicesResponseSchema` | `src/models/list-proforma-invoices-response.ts` |

### previewProformaInvoice

- **Signature**: `previewProformaInvoice(request: ProformaInvoices.PreviewProformaInvoiceRequest, options?: RequestOptions): ApiPromise<ProformaInvoice, ProformaInvoices.PreviewProformaInvoiceError>`
- **Wire**: `POST /subscriptions/{subscription_id}/proforma_invoices/preview.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProformaInvoice`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProformaInvoices.PreviewProformaInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProformaInvoices.PreviewProformaInvoiceRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProformaInvoice` | `proformaInvoiceSchema` | `src/models/proforma-invoice.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### previewSignupProformaInvoice

- **Signature**: `previewSignupProformaInvoice(request?: ProformaInvoices.PreviewSignupProformaInvoiceRequest, options?: RequestOptions): ApiPromise<SignupProformaPreviewResponse, ProformaInvoices.PreviewSignupProformaInvoiceError>`
- **Wire**: `POST /subscriptions/proforma_invoices/preview.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SignupProformaPreviewResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProformaInvoices.PreviewSignupProformaInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"proformaBadRequestErrorResponse1"` [400] `ProformaBadRequestErrorResponse1` · `"errorArrayMapResponse1"` [422] `ErrorArrayMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProformaInvoices.PreviewSignupProformaInvoiceRequest` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `include` | `query` | `CreateSignupProformaPreviewInclude` | no |
| `body` | `body` | `CreateSubscriptionRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateSignupProformaPreviewInclude` | `createSignupProformaPreviewIncludeSchema` | `src/models/create-signup-proforma-preview-include.ts` |
| `CreateSubscriptionRequest` | `createSubscriptionRequestSchema` | `src/models/create-subscription-request.ts` |
| `SignupProformaPreviewResponse` | `signupProformaPreviewResponseSchema` | `src/models/signup-proforma-preview-response.ts` |
| `ProformaBadRequestErrorResponse1` | `proformaBadRequestErrorResponse1Schema` | `src/models/proforma-bad-request-error-response1.ts` |
| `ErrorArrayMapResponse1` | `errorArrayMapResponse1Schema` | `src/models/error-array-map-response1.ts` |

### readProformaInvoice

- **Signature**: `readProformaInvoice(request: ProformaInvoices.ReadProformaInvoiceRequest, options?: RequestOptions): ApiPromise<ProformaInvoice, ProformaInvoices.ReadProformaInvoiceError>`
- **Wire**: `GET /proforma_invoices/{proforma_invoice_uid}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ProformaInvoice`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProformaInvoices.ReadProformaInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProformaInvoices.ReadProformaInvoiceRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `proformaInvoiceUid` | `path` | `proforma_invoice_uid` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProformaInvoice` | `proformaInvoiceSchema` | `src/models/proforma-invoice.ts` |

### voidProformaInvoice

- **Signature**: `voidProformaInvoice(request: ProformaInvoices.VoidProformaInvoiceRequest, options?: RequestOptions): ApiPromise<ProformaInvoice, ProformaInvoices.VoidProformaInvoiceError>`
- **Wire**: `POST /proforma_invoices/{proforma_invoice_uid}/void.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProformaInvoice`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProformaInvoices.VoidProformaInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProformaInvoices.VoidProformaInvoiceRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `proformaInvoiceUid` | `path` | `proforma_invoice_uid` | `string` | yes |
| `body` | `body` | — | `VoidInvoiceRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `VoidInvoiceRequest` | `voidInvoiceRequestSchema` | `src/models/void-invoice-request.ts` |
| `ProformaInvoice` | `proformaInvoiceSchema` | `src/models/proforma-invoice.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

