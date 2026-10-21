<!-- Generated file — do not edit; regenerated with the SDK. -->

# Invoices — operations

Accessor: `client.invoices` · Source: `maxio_advanced_billing/apis/invoices.py` · 19 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.invoices.create_invoice

- **Provider rules (Maxio)**: Decide `status`: send `"draft"` for review; the default `open` issues the invoice now. Make each line item exactly one of `title` + `unit_price`, `product_id` or `component_id`. Keep `issue_date` at today or earlier. Notes: `knowledge/operations/invoices.md#createinvoice`
- **Route**: `POST /subscriptions/{subscription_id}/invoices.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_invoice(subscription_id: int, *, body: CreateInvoiceRequest | CreateInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `InvoiceResponse`
- **Returns (raw)**: `ApiResult[InvoiceResponse, CreateInvoiceErrorBody]`
- **Error**: `CreateInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorArrayMapResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateInvoiceRequest` | `maxio_advanced_billing/models/create_invoice_request.py` |
| `CreateInvoiceRequestDict` | `maxio_advanced_billing/models/create_invoice_request.py` |
| `InvoiceResponse` | `maxio_advanced_billing/models/invoice_response.py` |
| `CreateInvoiceErrorBody` | `maxio_advanced_billing/errors/create_invoice_error.py` |
| `ErrorArrayMapResponse1` | `maxio_advanced_billing/models/error_array_map_response1.py` |

### client.invoices.delete_invoice

- **Provider rules (Maxio)**: Delete only an ad hoc `draft` invoice, and only when it should be gone for good: the invoice "is permanently removed". Void an issued invoice with `void_invoice` instead. Notes: `knowledge/operations/invoices.md#deleteinvoice`
- **Route**: `DELETE /subscriptions/{subscription_id}/invoices/{uid}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def delete_invoice(subscription_id: int, uid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `uid`
- **Params**: `subscription_id` — path · `uid` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteInvoiceErrorBody]`
- **Error**: `DeleteInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteInvoiceErrorBody` | `maxio_advanced_billing/errors/delete_invoice_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.issue_invoice

- **Provider rules (Maxio)**: On automatic collection choose `on_failed_payment`. On remittance subscriptions never send `on_failed_payment`. Issue only `draft` or `pending` invoices (D16). Notes: `knowledge/operations/invoices.md#issueinvoice`
- **Route**: `POST /invoices/{uid}/issue.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def issue_invoice(uid: str, *, body: IssueInvoiceRequest | IssueInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path · `body` — JSON body
- **Returns (parsed)**: `Invoice`
- **Returns (raw)**: `ApiResult[Invoice, IssueInvoiceErrorBody]`
- **Error**: `IssueInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `IssueInvoiceRequest` | `maxio_advanced_billing/models/issue_invoice_request.py` |
| `IssueInvoiceRequestDict` | `maxio_advanced_billing/models/issue_invoice_request.py` |
| `Invoice` | `maxio_advanced_billing/models/invoice.py` |
| `IssueInvoiceErrorBody` | `maxio_advanced_billing/errors/issue_invoice_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.list_consolidated_invoice_segments

- **Route**: `GET /invoices/{invoice_uid}/segments.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_consolidated_invoice_segments(invoice_uid: str, *, page: int | None = 1, per_page: int | None = 20, direction: DirectionOrStr | None = Direction.ASC, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `invoice_uid`
- **Params**: `invoice_uid` — path · `page` — query · `per_page` — query · `direction` — query
- **Returns (parsed)**: `ConsolidatedInvoice`
- **Returns (raw)**: `ApiResult[ConsolidatedInvoice, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `maxio_advanced_billing/models/enums/direction.py` |
| `ConsolidatedInvoice` | `maxio_advanced_billing/models/consolidated_invoice.py` |

### client.invoices.list_credit_notes

- **Route**: `GET /credit_notes.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_credit_notes(*, subscription_id: int | None = None, date_field: CreditNoteDateFieldOrStr | None = CreditNoteDateField.ISSUE_DATE, start_date: str | None = None, end_date: str | None = None, start_datetime: str | None = None, end_datetime: str | None = None, page: int | None = 1, per_page: int | None = 20, direction: DirectionOrStr | None = Direction.DESC, line_items: bool | None = False, discounts: bool | None = False, taxes: bool | None = False, refunds: bool | None = False, applications: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `subscription_id` — query · `date_field` — query · `start_date` — query · `end_date` — query · `start_datetime` — query · `end_datetime` — query · `page` — query · `per_page` — query · `direction` — query · `line_items` — query · `discounts` — query · `taxes` — query · `refunds` — query · `applications` — query
- **Returns (parsed)**: `ListCreditNotesResponse`
- **Returns (raw)**: `ApiResult[ListCreditNotesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditNoteDateFieldOrStr` | `maxio_advanced_billing/models/enums/credit_note_date_field.py` |
| `DirectionOrStr` | `maxio_advanced_billing/models/enums/direction.py` |
| `ListCreditNotesResponse` | `maxio_advanced_billing/models/list_credit_notes_response.py` |

### client.invoices.list_invoice_events

- **Route**: `GET /invoices/events.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_invoice_events(*, since_date: str | None = None, since_id: int | None = None, page: int | None = 1, per_page: int | None = 100, invoice_uid: str | None = None, with_change_invoice_status: str | None = None, event_types: list[InvoiceEventTypeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `since_date` — query · `since_id` — query · `page` — query · `per_page` — query · `invoice_uid` — query · `with_change_invoice_status` — query · `event_types` — query
- **Returns (parsed)**: `ListInvoiceEventsResponse`
- **Returns (raw)**: `ApiResult[ListInvoiceEventsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvoiceEventTypeOrStr` | `maxio_advanced_billing/models/enums/invoice_event_type.py` |
| `ListInvoiceEventsResponse` | `maxio_advanced_billing/models/list_invoice_events_response.py` |

### client.invoices.list_invoices

- **Provider rules (Maxio)**: Request each nested array you need (`line_items=true`, ...) (R9). Use datetime filters only with `date_field` set to `created_at` or `updated_at`. Notes: `knowledge/operations/invoices.md#listinvoices`
- **Route**: `GET /invoices.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_invoices(*, start_date: str | None = None, end_date: str | None = None, status: InvoiceStatusOrStr | None = None, subscription_id: int | None = None, subscription_group_uid: str | None = None, consolidation_level: str | None = None, page: int | None = 1, per_page: int | None = 20, direction: DirectionOrStr | None = Direction.DESC, line_items: bool | None = False, discounts: bool | None = False, taxes: bool | None = False, credits_: bool | None = False, payments: bool | None = False, custom_fields: bool | None = False, refunds: bool | None = False, date_field: InvoiceDateFieldOrStr | None = InvoiceDateField.DUE_DATE, start_datetime: str | None = None, end_datetime: str | None = None, customer_ids: list[int] | None = None, number: list[str] | None = None, product_ids: list[int] | None = None, sort: InvoiceSortFieldOrStr | None = InvoiceSortField.NUMBER, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `start_date` — query · `end_date` — query · `status` — query · `subscription_id` — query · `subscription_group_uid` — query · `consolidation_level` — query · `page` — query · `per_page` — query · `direction` — query · `line_items` — query · `discounts` — query · `taxes` — query · `credits_` — query `credits` · `payments` — query · `custom_fields` — query · `refunds` — query · `date_field` — query · `start_datetime` — query · `end_datetime` — query · `customer_ids` — query · `number` — query · `product_ids` — query · `sort` — query
- **Returns (parsed)**: `ListInvoicesResponse`
- **Returns (raw)**: `ApiResult[ListInvoicesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvoiceStatusOrStr` | `maxio_advanced_billing/models/enums/invoice_status.py` |
| `DirectionOrStr` | `maxio_advanced_billing/models/enums/direction.py` |
| `InvoiceDateFieldOrStr` | `maxio_advanced_billing/models/enums/invoice_date_field.py` |
| `InvoiceSortFieldOrStr` | `maxio_advanced_billing/models/enums/invoice_sort_field.py` |
| `ListInvoicesResponse` | `maxio_advanced_billing/models/list_invoices_response.py` |

### client.invoices.preview_customer_information_changes

- **Route**: `POST /invoices/{uid}/customer_information/preview.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def preview_customer_information_changes(uid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path
- **Returns (parsed)**: `CustomerChangesPreviewResponse`
- **Returns (raw)**: `ApiResult[CustomerChangesPreviewResponse, PreviewCustomerInformationChangesErrorBody]`
- **Error**: `PreviewCustomerInformationChangesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CustomerChangesPreviewResponse` | `maxio_advanced_billing/models/customer_changes_preview_response.py` |
| `PreviewCustomerInformationChangesErrorBody` | `maxio_advanced_billing/errors/preview_customer_information_changes_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.read_credit_note

- **Route**: `GET /credit_notes/{uid}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_credit_note(uid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path
- **Returns (parsed)**: `CreditNote`
- **Returns (raw)**: `ApiResult[CreditNote, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditNote` | `maxio_advanced_billing/models/credit_note.py` |

### client.invoices.read_invoice

- **Route**: `GET /invoices/{uid}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_invoice(uid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path
- **Returns (parsed)**: `Invoice`
- **Returns (raw)**: `ApiResult[Invoice, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Invoice` | `maxio_advanced_billing/models/invoice.py` |

### client.invoices.record_payment_for_invoice

- **Provider rules (Maxio)**: Choose `type` on purpose: default `external` only records money taken elsewhere; `prepayment`/`service_credit` draw on that balance; `payment` with `payment_profile_id` collects from that profile. Keep `amount` ≤ `due_amount`. Notes: `knowledge/operations/invoices.md#recordpaymentforinvoice`
- **Route**: `POST /invoices/{uid}/payments.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def record_payment_for_invoice(uid: str, *, body: CreateInvoicePaymentRequest | CreateInvoicePaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path · `body` — JSON body
- **Returns (parsed)**: `Invoice`
- **Returns (raw)**: `ApiResult[Invoice, RecordPaymentForInvoiceErrorBody]`
- **Error**: `RecordPaymentForInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateInvoicePaymentRequest` | `maxio_advanced_billing/models/create_invoice_payment_request.py` |
| `CreateInvoicePaymentRequestDict` | `maxio_advanced_billing/models/create_invoice_payment_request.py` |
| `Invoice` | `maxio_advanced_billing/models/invoice.py` |
| `RecordPaymentForInvoiceErrorBody` | `maxio_advanced_billing/errors/record_payment_for_invoice_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.record_payment_for_multiple_invoices

- **Provider rules (Maxio)**: This records an external payment; it charges nothing (inferred). Give each invoice at most its due amount; to leave a prepayment, raise the total `amount` above the sum of `applications`. Never include a consolidated invoice. Notes: `knowledge/operations/invoices.md#recordpaymentformultipleinvoices`
- **Route**: `POST /invoices/payments.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def record_payment_for_multiple_invoices(*, body: CreateMultiInvoicePaymentRequest | CreateMultiInvoicePaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `MultiInvoicePaymentResponse`
- **Returns (raw)**: `ApiResult[MultiInvoicePaymentResponse, RecordPaymentForMultipleInvoicesErrorBody]`
- **Error**: `RecordPaymentForMultipleInvoicesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateMultiInvoicePaymentRequest` | `maxio_advanced_billing/models/create_multi_invoice_payment_request.py` |
| `CreateMultiInvoicePaymentRequestDict` | `maxio_advanced_billing/models/create_multi_invoice_payment_request.py` |
| `MultiInvoicePaymentResponse` | `maxio_advanced_billing/models/multi_invoice_payment_response.py` |
| `RecordPaymentForMultipleInvoicesErrorBody` | `maxio_advanced_billing/errors/record_payment_for_multiple_invoices_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.record_payment_for_subscription

- **Provider notes (Maxio)**: `knowledge/operations/invoices.md#recordpaymentforsubscription`
- **Route**: `POST /subscriptions/{subscription_id}/payments.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def record_payment_for_subscription(subscription_id: int, *, body: RecordPaymentRequest | RecordPaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `RecordPaymentResponse`
- **Returns (raw)**: `ApiResult[RecordPaymentResponse, RecordPaymentForSubscriptionErrorBody]`
- **Error**: `RecordPaymentForSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RecordPaymentRequest` | `maxio_advanced_billing/models/record_payment_request.py` |
| `RecordPaymentRequestDict` | `maxio_advanced_billing/models/record_payment_request.py` |
| `RecordPaymentResponse` | `maxio_advanced_billing/models/record_payment_response.py` |
| `RecordPaymentForSubscriptionErrorBody` | `maxio_advanced_billing/errors/record_payment_for_subscription_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.refund_invoice

- **Provider rules (Maxio)**: Send `external: true` only to record a refund made elsewhere (D15). Send `void_invoice: true` only with `apply_credit: false` and a full refund. On consolidated invoices send `segment_uids`. Notes: `knowledge/operations/invoices.md#refundinvoice`
- **Route**: `POST /invoices/{uid}/refunds.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def refund_invoice(uid: str, *, body: RefundInvoiceRequest | RefundInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path · `body` — JSON body
- **Returns (parsed)**: `Invoice`
- **Returns (raw)**: `ApiResult[Invoice, RefundInvoiceErrorBody]`
- **Error**: `RefundInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RefundInvoiceRequest` | `maxio_advanced_billing/models/refund_invoice_request.py` |
| `RefundInvoiceRequestDict` | `maxio_advanced_billing/models/refund_invoice_request.py` |
| `Invoice` | `maxio_advanced_billing/models/invoice.py` |
| `RefundInvoiceErrorBody` | `maxio_advanced_billing/errors/refund_invoice_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.reopen_invoice

- **Provider notes (Maxio)**: `knowledge/operations/invoices.md#reopeninvoice`
- **Route**: `POST /invoices/{uid}/reopen.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def reopen_invoice(uid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path
- **Returns (parsed)**: `Invoice`
- **Returns (raw)**: `ApiResult[Invoice, ReopenInvoiceErrorBody]`
- **Error**: `ReopenInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `Any | None` [404] · `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Invoice` | `maxio_advanced_billing/models/invoice.py` |
| `ReopenInvoiceErrorBody` | `maxio_advanced_billing/errors/reopen_invoice_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.send_invoice

- **Route**: `POST /invoices/{uid}/deliveries.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def send_invoice(uid: str, *, body: SendInvoiceRequest | SendInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SendInvoiceErrorBody]`
- **Error**: `SendInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SendInvoiceRequest` | `maxio_advanced_billing/models/send_invoice_request.py` |
| `SendInvoiceRequestDict` | `maxio_advanced_billing/models/send_invoice_request.py` |
| `SendInvoiceErrorBody` | `maxio_advanced_billing/errors/send_invoice_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.update_customer_information

- **Route**: `PUT /invoices/{uid}/customer_information.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_customer_information(uid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path
- **Returns (parsed)**: `Invoice`
- **Returns (raw)**: `ApiResult[Invoice, UpdateCustomerInformationErrorBody]`
- **Error**: `UpdateCustomerInformationErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Invoice` | `maxio_advanced_billing/models/invoice.py` |
| `UpdateCustomerInformationErrorBody` | `maxio_advanced_billing/errors/update_customer_information_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.invoices.update_invoice

- **Provider rules (Maxio)**: Send `coupons` only to replace every discount on the invoice: the list you send replaces them all, and `[]` removes them. Send each existing line item with its `uid`; a line without `uid` is added as new. Notes: `knowledge/operations/invoices.md#updateinvoice`
- **Route**: `PUT /subscriptions/{subscription_id}/invoices/{uid}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_invoice(subscription_id: int, uid: str, *, body: UpdateInvoiceRequest | UpdateInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `uid`
- **Params**: `subscription_id` — path · `uid` — path · `body` — JSON body
- **Returns (parsed)**: `InvoiceResponse`
- **Returns (raw)**: `ApiResult[InvoiceResponse, UpdateInvoiceErrorBody]`
- **Error**: `UpdateInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [404] · `ErrorArrayMapResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateInvoiceRequest` | `maxio_advanced_billing/models/update_invoice_request.py` |
| `UpdateInvoiceRequestDict` | `maxio_advanced_billing/models/update_invoice_request.py` |
| `InvoiceResponse` | `maxio_advanced_billing/models/invoice_response.py` |
| `UpdateInvoiceErrorBody` | `maxio_advanced_billing/errors/update_invoice_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |
| `ErrorArrayMapResponse1` | `maxio_advanced_billing/models/error_array_map_response1.py` |

### client.invoices.void_invoice

- **Provider rules (Maxio)**: Void only `open`, `canceled` or non-consolidated `pending` invoices (D16). No operation reverses a void. Refund a `paid` invoice with `refund_invoice` instead. Notes: `knowledge/operations/invoices.md#voidinvoice`
- **Route**: `POST /invoices/{uid}/void.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def void_invoice(uid: str, *, body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`
- **Params**: `uid` — path · `body` — JSON body
- **Returns (parsed)**: `Invoice`
- **Returns (raw)**: `ApiResult[Invoice, VoidInvoiceErrorBody]`
- **Error**: `VoidInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `Any | None` [404] · `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VoidInvoiceRequest` | `maxio_advanced_billing/models/void_invoice_request.py` |
| `VoidInvoiceRequestDict` | `maxio_advanced_billing/models/void_invoice_request.py` |
| `Invoice` | `maxio_advanced_billing/models/invoice.py` |
| `VoidInvoiceErrorBody` | `maxio_advanced_billing/errors/void_invoice_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

