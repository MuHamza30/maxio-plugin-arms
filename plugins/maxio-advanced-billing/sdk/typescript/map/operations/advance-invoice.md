<!-- Generated file — do not edit; regenerated with the SDK. -->

# AdvanceInvoice — operations

Accessor: `client.advanceInvoice` · Source: `src/resources/advance-invoice.ts` · 3 operations · Request and error types: namespace `AdvanceInvoice`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### issueAdvanceInvoice

- **Signature**: `issueAdvanceInvoice(request: AdvanceInvoice.IssueAdvanceInvoiceRequestParams, options?: RequestOptions): ApiPromise<Invoice, AdvanceInvoice.IssueAdvanceInvoiceError>`
- **Wire**: `POST /subscriptions/{subscription_id}/advance_invoice/issue.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `Invoice`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `AdvanceInvoice.IssueAdvanceInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `AdvanceInvoice.IssueAdvanceInvoiceRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `IssueAdvanceInvoiceRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `IssueAdvanceInvoiceRequest` | `issueAdvanceInvoiceRequestSchema` | `src/models/issue-advance-invoice-request.ts` |
| `Invoice` | `invoiceSchema` | `src/models/invoice.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readAdvanceInvoice

- **Signature**: `readAdvanceInvoice(request: AdvanceInvoice.ReadAdvanceInvoiceRequest, options?: RequestOptions): ApiPromise<Invoice, AdvanceInvoice.ReadAdvanceInvoiceError>`
- **Wire**: `GET /subscriptions/{subscription_id}/advance_invoice.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `Invoice`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `AdvanceInvoice.ReadAdvanceInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `AdvanceInvoice.ReadAdvanceInvoiceRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `Invoice` | `invoiceSchema` | `src/models/invoice.ts` |

### voidAdvanceInvoice

- **Signature**: `voidAdvanceInvoice(request: AdvanceInvoice.VoidAdvanceInvoiceRequest, options?: RequestOptions): ApiPromise<Invoice, AdvanceInvoice.VoidAdvanceInvoiceError>`
- **Wire**: `POST /subscriptions/{subscription_id}/advance_invoice/void.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `Invoice`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `AdvanceInvoice.VoidAdvanceInvoiceError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `AdvanceInvoice.VoidAdvanceInvoiceRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `VoidInvoiceRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `VoidInvoiceRequest` | `voidInvoiceRequestSchema` | `src/models/void-invoice-request.ts` |
| `Invoice` | `invoiceSchema` | `src/models/invoice.ts` |

