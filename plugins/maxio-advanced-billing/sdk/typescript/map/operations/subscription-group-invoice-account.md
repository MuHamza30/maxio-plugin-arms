<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionGroupInvoiceAccount — operations

Accessor: `client.subscriptionGroupInvoiceAccount` · Source: `src/resources/subscription-group-invoice-account.ts` · 4 operations · Request and error types: namespace `SubscriptionGroupInvoiceAccount`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createSubscriptionGroupPrepayment

- **Signature**: `createSubscriptionGroupPrepayment(request: SubscriptionGroupInvoiceAccount.CreateSubscriptionGroupPrepaymentRequest, options?: RequestOptions): ApiPromise<SubscriptionGroupPrepaymentResponse, SubscriptionGroupInvoiceAccount.CreateSubscriptionGroupPrepaymentError>`
- **Wire**: `POST /subscription_groups/{uid}/prepayments.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionGroupPrepaymentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroupInvoiceAccount.CreateSubscriptionGroupPrepaymentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroupInvoiceAccount.CreateSubscriptionGroupPrepaymentRequest` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |
| `body` | `body` | `SubscriptionGroupPrepaymentRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionGroupPrepaymentRequest` | `subscriptionGroupPrepaymentRequestSchema` | `src/models/subscription-group-prepayment-request.ts` |
| `SubscriptionGroupPrepaymentResponse` | `subscriptionGroupPrepaymentResponseSchema` | `src/models/subscription-group-prepayment-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### deductSubscriptionGroupServiceCredit

- **Signature**: `deductSubscriptionGroupServiceCredit(request: SubscriptionGroupInvoiceAccount.DeductSubscriptionGroupServiceCreditRequest, options?: RequestOptions): ApiPromise<ServiceCredit, SubscriptionGroupInvoiceAccount.DeductSubscriptionGroupServiceCreditError>`
- **Wire**: `POST /subscription_groups/{uid}/service_credit_deductions.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ServiceCredit`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroupInvoiceAccount.DeductSubscriptionGroupServiceCreditError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroupInvoiceAccount.DeductSubscriptionGroupServiceCreditRequest` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |
| `body` | `body` | `DeductServiceCreditRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `DeductServiceCreditRequest` | `deductServiceCreditRequestSchema` | `src/models/deduct-service-credit-request.ts` |
| `ServiceCredit` | `serviceCreditSchema` | `src/models/service-credit.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### issueSubscriptionGroupServiceCredit

- **Signature**: `issueSubscriptionGroupServiceCredit(request: SubscriptionGroupInvoiceAccount.IssueSubscriptionGroupServiceCreditRequest, options?: RequestOptions): ApiPromise<ServiceCreditResponse, SubscriptionGroupInvoiceAccount.IssueSubscriptionGroupServiceCreditError>`
- **Wire**: `POST /subscription_groups/{uid}/service_credits.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ServiceCreditResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroupInvoiceAccount.IssueSubscriptionGroupServiceCreditError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroupInvoiceAccount.IssueSubscriptionGroupServiceCreditRequest` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |
| `body` | `body` | `IssueServiceCreditRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `IssueServiceCreditRequest` | `issueServiceCreditRequestSchema` | `src/models/issue-service-credit-request.ts` |
| `ServiceCreditResponse` | `serviceCreditResponseSchema` | `src/models/service-credit-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listPrepaymentsForSubscriptionGroup

- **Signature**: `listPrepaymentsForSubscriptionGroup(request: SubscriptionGroupInvoiceAccount.ListPrepaymentsForSubscriptionGroupRequest, options?: RequestOptions): ApiPromise<ListSubscriptionGroupPrepaymentResponse, SubscriptionGroupInvoiceAccount.ListPrepaymentsForSubscriptionGroupError>`
- **Wire**: `GET /subscription_groups/{uid}/prepayments.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListSubscriptionGroupPrepaymentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroupInvoiceAccount.ListPrepaymentsForSubscriptionGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroupInvoiceAccount.ListPrepaymentsForSubscriptionGroupRequest` (4):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `uid` | `path` | — | `string` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `filter` | `query` | — | `ListPrepaymentsFilter` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListPrepaymentsFilter` | `listPrepaymentsFilterSchema` | `src/models/list-prepayments-filter.ts` |
| `ListSubscriptionGroupPrepaymentResponse` | `listSubscriptionGroupPrepaymentResponseSchema` | `src/models/list-subscription-group-prepayment-response.ts` |

