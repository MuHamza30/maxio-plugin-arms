<!-- Generated file — do not edit; regenerated with the SDK. -->

# ApiExports — operations

Accessor: `client.apiExports` · Source: `src/resources/api-exports.ts` · 9 operations · Request and error types: namespace `ApiExports`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### exportInvoices

- **Signature**: `exportInvoices(options?: RequestOptions): ApiPromise<BatchJobResponse, ApiExports.ExportInvoicesError>`
- **Wire**: `POST /api_exports/invoices.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `BatchJobResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ApiExports.ExportInvoicesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"singleErrorResponse1"` [409] `SingleErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

| Type | Schema value | Source |
| --- | --- | --- |
| `BatchJobResponse` | `batchJobResponseSchema` | `src/models/batch-job-response.ts` |
| `SingleErrorResponse1` | `singleErrorResponse1Schema` | `src/models/single-error-response1.ts` |

### exportProformaInvoices

- **Signature**: `exportProformaInvoices(options?: RequestOptions): ApiPromise<BatchJobResponse, ApiExports.ExportProformaInvoicesError>`
- **Wire**: `POST /api_exports/proforma_invoices.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `BatchJobResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ApiExports.ExportProformaInvoicesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"singleErrorResponse1"` [409] `SingleErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

| Type | Schema value | Source |
| --- | --- | --- |
| `BatchJobResponse` | `batchJobResponseSchema` | `src/models/batch-job-response.ts` |
| `SingleErrorResponse1` | `singleErrorResponse1Schema` | `src/models/single-error-response1.ts` |

### exportSubscriptions

- **Signature**: `exportSubscriptions(options?: RequestOptions): ApiPromise<BatchJobResponse, ApiExports.ExportSubscriptionsError>`
- **Wire**: `POST /api_exports/subscriptions.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `BatchJobResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ApiExports.ExportSubscriptionsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"singleErrorResponse1"` [409] `SingleErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

| Type | Schema value | Source |
| --- | --- | --- |
| `BatchJobResponse` | `batchJobResponseSchema` | `src/models/batch-job-response.ts` |
| `SingleErrorResponse1` | `singleErrorResponse1Schema` | `src/models/single-error-response1.ts` |

### listExportedInvoices

- **Signature**: `listExportedInvoices(request: ApiExports.ListExportedInvoicesRequest, options?: RequestOptions): ApiPromise<Invoice[], ApiExports.ListExportedInvoicesError>`
- **Wire**: `GET /api_exports/invoices/{batch_id}/rows.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `Invoice[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ApiExports.ListExportedInvoicesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ApiExports.ListExportedInvoicesRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `batchId` | `path` | `batch_id` | `string` | yes | — |
| `perPage` | `query` | `per_page` | `number` | no | `100` |
| `page` | `query` | — | `number` | no | `1` |

| Type | Schema value | Source |
| --- | --- | --- |
| `Invoice` | `invoiceSchema` | `src/models/invoice.ts` |

### listExportedProformaInvoices

- **Signature**: `listExportedProformaInvoices(request: ApiExports.ListExportedProformaInvoicesRequest, options?: RequestOptions): ApiPromise<ProformaInvoice[], ApiExports.ListExportedProformaInvoicesError>`
- **Wire**: `GET /api_exports/proforma_invoices/{batch_id}/rows.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ProformaInvoice[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ApiExports.ListExportedProformaInvoicesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ApiExports.ListExportedProformaInvoicesRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `batchId` | `path` | `batch_id` | `string` | yes | — |
| `perPage` | `query` | `per_page` | `number` | no | `100` |
| `page` | `query` | — | `number` | no | `1` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProformaInvoice` | `proformaInvoiceSchema` | `src/models/proforma-invoice.ts` |

### listExportedSubscriptions

- **Signature**: `listExportedSubscriptions(request: ApiExports.ListExportedSubscriptionsRequest, options?: RequestOptions): ApiPromise<Subscription[], ApiExports.ListExportedSubscriptionsError>`
- **Wire**: `GET /api_exports/subscriptions/{batch_id}/rows.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `Subscription[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ApiExports.ListExportedSubscriptionsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ApiExports.ListExportedSubscriptionsRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `batchId` | `path` | `batch_id` | `string` | yes | — |
| `perPage` | `query` | `per_page` | `number` | no | `100` |
| `page` | `query` | — | `number` | no | `1` |

| Type | Schema value | Source |
| --- | --- | --- |
| `Subscription` | `subscriptionSchema` | `src/models/subscription.ts` |

### readInvoicesExport

- **Signature**: `readInvoicesExport(request: ApiExports.ReadInvoicesExportRequest, options?: RequestOptions): ApiPromise<BatchJobResponse, ApiExports.ReadInvoicesExportError>`
- **Wire**: `GET /api_exports/invoices/{batch_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `BatchJobResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ApiExports.ReadInvoicesExportError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ApiExports.ReadInvoicesExportRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `batchId` | `path` | `batch_id` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `BatchJobResponse` | `batchJobResponseSchema` | `src/models/batch-job-response.ts` |

### readProformaInvoicesExport

- **Signature**: `readProformaInvoicesExport(request: ApiExports.ReadProformaInvoicesExportRequest, options?: RequestOptions): ApiPromise<BatchJobResponse, ApiExports.ReadProformaInvoicesExportError>`
- **Wire**: `GET /api_exports/proforma_invoices/{batch_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `BatchJobResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ApiExports.ReadProformaInvoicesExportError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ApiExports.ReadProformaInvoicesExportRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `batchId` | `path` | `batch_id` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `BatchJobResponse` | `batchJobResponseSchema` | `src/models/batch-job-response.ts` |

### readSubscriptionsExport

- **Signature**: `readSubscriptionsExport(request: ApiExports.ReadSubscriptionsExportRequest, options?: RequestOptions): ApiPromise<BatchJobResponse, ApiExports.ReadSubscriptionsExportError>`
- **Wire**: `GET /api_exports/subscriptions/{batch_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `BatchJobResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ApiExports.ReadSubscriptionsExportError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ApiExports.ReadSubscriptionsExportRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `batchId` | `path` | `batch_id` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `BatchJobResponse` | `batchJobResponseSchema` | `src/models/batch-job-response.ts` |

