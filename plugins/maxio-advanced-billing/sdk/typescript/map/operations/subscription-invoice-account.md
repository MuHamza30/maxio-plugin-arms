<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionInvoiceAccount — operations

Accessor: `client.subscriptionInvoiceAccount` · Source: `src/resources/subscription-invoice-account.ts` · 7 operations · Request and error types: namespace `SubscriptionInvoiceAccount`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createPrepayment

- **Signature**: `createPrepayment(request: SubscriptionInvoiceAccount.CreatePrepaymentRequestParams, options?: RequestOptions): ApiPromise<CreatePrepaymentResponse, SubscriptionInvoiceAccount.CreatePrepaymentError>`
- **Wire**: `POST /subscriptions/{subscription_id}/prepayments.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CreatePrepaymentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionInvoiceAccount.CreatePrepaymentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"createPrepaymentErrorResponse"` [422] `CreatePrepaymentErrorResponse` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionInvoiceAccount.CreatePrepaymentRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `CreatePrepaymentRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreatePrepaymentRequest` | `createPrepaymentRequestSchema` | `src/models/create-prepayment-request.ts` |
| `CreatePrepaymentResponse` | `createPrepaymentResponseSchema` | `src/models/create-prepayment-response.ts` |
| `CreatePrepaymentErrorResponse` | `createPrepaymentErrorResponseSchema` | `src/models/unions/create-prepayment-error-response.ts` |

### deductServiceCredit

- **Signature**: `deductServiceCredit(request: SubscriptionInvoiceAccount.DeductServiceCreditRequestParams, options?: RequestOptions): ApiPromise<undefined, SubscriptionInvoiceAccount.DeductServiceCreditError>`
- **Wire**: `POST /subscriptions/{subscription_id}/service_credit_deductions.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionInvoiceAccount.DeductServiceCreditError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"deductServiceCreditErrorResponse"` [422] `DeductServiceCreditErrorResponse` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionInvoiceAccount.DeductServiceCreditRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `DeductServiceCreditRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `DeductServiceCreditRequest` | `deductServiceCreditRequestSchema` | `src/models/deduct-service-credit-request.ts` |
| `DeductServiceCreditErrorResponse` | `deductServiceCreditErrorResponseSchema` | `src/models/unions/deduct-service-credit-error-response.ts` |

### issueServiceCredit

- **Signature**: `issueServiceCredit(request: SubscriptionInvoiceAccount.IssueServiceCreditRequestParams, options?: RequestOptions): ApiPromise<ServiceCredit, SubscriptionInvoiceAccount.IssueServiceCreditError>`
- **Wire**: `POST /subscriptions/{subscription_id}/service_credits.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ServiceCredit`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionInvoiceAccount.IssueServiceCreditError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"issueServiceCreditErrorResponse"` [422] `IssueServiceCreditErrorResponse` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionInvoiceAccount.IssueServiceCreditRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `IssueServiceCreditRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `IssueServiceCreditRequest` | `issueServiceCreditRequestSchema` | `src/models/issue-service-credit-request.ts` |
| `ServiceCredit` | `serviceCreditSchema` | `src/models/service-credit.ts` |
| `IssueServiceCreditErrorResponse` | `issueServiceCreditErrorResponseSchema` | `src/models/unions/issue-service-credit-error-response.ts` |

### listPrepayments

- **Signature**: `listPrepayments(request: SubscriptionInvoiceAccount.ListPrepaymentsRequest, options?: RequestOptions): ApiPromise<PrepaymentsResponse, SubscriptionInvoiceAccount.ListPrepaymentsError>`
- **Wire**: `GET /subscriptions/{subscription_id}/prepayments.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `PrepaymentsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionInvoiceAccount.ListPrepaymentsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionInvoiceAccount.ListPrepaymentsRequest` (4):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `filter` | `query` | — | `ListPrepaymentsFilter` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListPrepaymentsFilter` | `listPrepaymentsFilterSchema` | `src/models/list-prepayments-filter.ts` |
| `PrepaymentsResponse` | `prepaymentsResponseSchema` | `src/models/prepayments-response.ts` |

### listServiceCredits

- **Signature**: `listServiceCredits(request: SubscriptionInvoiceAccount.ListServiceCreditsRequest, options?: RequestOptions): ApiPromise<ListServiceCreditsResponse, SubscriptionInvoiceAccount.ListServiceCreditsError>`
- **Wire**: `GET /subscriptions/{subscription_id}/service_credits/list.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListServiceCreditsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionInvoiceAccount.ListServiceCreditsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionInvoiceAccount.ListServiceCreditsRequest` (4):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `direction` | `query` | — | `SortingDirection` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `SortingDirection` | `sortingDirectionSchema` | `src/models/sorting-direction.ts` |
| `ListServiceCreditsResponse` | `listServiceCreditsResponseSchema` | `src/models/list-service-credits-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readAccountBalances

- **Signature**: `readAccountBalances(request: SubscriptionInvoiceAccount.ReadAccountBalancesRequest, options?: RequestOptions): ApiPromise<AccountBalances, ApiError>`
- **Wire**: `GET /subscriptions/{subscription_id}/account_balances.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `AccountBalances`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionInvoiceAccount.ReadAccountBalancesRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `AccountBalances` | `accountBalancesSchema` | `src/models/account-balances.ts` |

### refundPrepayment

- **Signature**: `refundPrepayment(request: SubscriptionInvoiceAccount.RefundPrepaymentRequestParams, options?: RequestOptions): ApiPromise<PrepaymentResponse, SubscriptionInvoiceAccount.RefundPrepaymentError>`
- **Wire**: `POST /subscriptions/{subscription_id}/prepayments/{prepayment_id}/refunds.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `PrepaymentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionInvoiceAccount.RefundPrepaymentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"refundPrepaymentBaseErrorsResponse1"` [400] `RefundPrepaymentBaseErrorsResponse1` · `"error404"` [404] `string` · `"refundPrepaymentErrorResponse"` [422] `RefundPrepaymentErrorResponse` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionInvoiceAccount.RefundPrepaymentRequestParams` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `prepaymentId` | `path` | `prepayment_id` | `number` | yes |
| `body` | `body` | — | `RefundPrepaymentRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `RefundPrepaymentRequest` | `refundPrepaymentRequestSchema` | `src/models/refund-prepayment-request.ts` |
| `PrepaymentResponse` | `prepaymentResponseSchema` | `src/models/prepayment-response.ts` |
| `RefundPrepaymentBaseErrorsResponse1` | `refundPrepaymentBaseErrorsResponse1Schema` | `src/models/refund-prepayment-base-errors-response1.ts` |
| `RefundPrepaymentErrorResponse` | `refundPrepaymentErrorResponseSchema` | `src/models/unions/refund-prepayment-error-response.ts` |

