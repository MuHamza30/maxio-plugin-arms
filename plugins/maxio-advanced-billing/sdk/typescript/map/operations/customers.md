<!-- Generated file — do not edit; regenerated with the SDK. -->

# Customers — operations

Accessor: `client.customers` · Source: `src/resources/customers.ts` · 7 operations · Request and error types: namespace `Customers`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createCustomer

- **Signature**: `createCustomer(request?: Customers.CreateCustomerRequestParams, options?: RequestOptions): ApiPromise<CustomerResponse, Customers.CreateCustomerError>`
- **Wire**: `POST /customers.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CustomerResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Customers.CreateCustomerError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"customerErrorResponse1"` [422] `CustomerErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Customers.CreateCustomerRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateCustomerRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateCustomerRequest` | `createCustomerRequestSchema` | `src/models/create-customer-request.ts` |
| `CustomerResponse` | `customerResponseSchema` | `src/models/customer-response.ts` |
| `CustomerErrorResponse1` | `customerErrorResponse1Schema` | `src/models/customer-error-response1.ts` |

### deleteCustomer

- **Signature**: `deleteCustomer(request: Customers.DeleteCustomerRequest, options?: RequestOptions): ApiPromise<undefined, ApiError>`
- **Wire**: `DELETE /customers/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Customers.DeleteCustomerRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |

### listCustomerSubscriptions

- **Signature**: `listCustomerSubscriptions(request: Customers.ListCustomerSubscriptionsRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse[], ApiError>`
- **Wire**: `GET /customers/{customer_id}/subscriptions.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `SubscriptionResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Customers.ListCustomerSubscriptionsRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `customerId` | `path` | `customer_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |

### listCustomers

- **Signature**: `listCustomers(request?: Customers.ListCustomersRequest, options?: RequestOptions): ApiPromise<CustomerResponse[], ApiError>`
- **Wire**: `GET /customers.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CustomerResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Customers.ListCustomersRequest` (9):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `direction` | `query` | — | `SortingDirection` | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `50` |
| `dateField` | `query` | `date_field` | `BasicDateField` | no | — |
| `startDate` | `query` | `start_date` | `string` | no | — |
| `endDate` | `query` | `end_date` | `string` | no | — |
| `startDatetime` | `query` | `start_datetime` | `string` | no | — |
| `endDatetime` | `query` | `end_datetime` | `string` | no | — |
| `q` | `query` | — | `string` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `SortingDirection` | `sortingDirectionSchema` | `src/models/sorting-direction.ts` |
| `BasicDateField` | `basicDateFieldSchema` | `src/models/basic-date-field.ts` |
| `CustomerResponse` | `customerResponseSchema` | `src/models/customer-response.ts` |

### readCustomer

- **Signature**: `readCustomer(request: Customers.ReadCustomerRequest, options?: RequestOptions): ApiPromise<CustomerResponse, ApiError>`
- **Wire**: `GET /customers/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CustomerResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Customers.ReadCustomerRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `CustomerResponse` | `customerResponseSchema` | `src/models/customer-response.ts` |

### readCustomerByReference

- **Signature**: `readCustomerByReference(request: Customers.ReadCustomerByReferenceRequest, options?: RequestOptions): ApiPromise<CustomerResponse, ApiError>`
- **Wire**: `GET /customers/lookup.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CustomerResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Customers.ReadCustomerByReferenceRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `reference` | `query` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `CustomerResponse` | `customerResponseSchema` | `src/models/customer-response.ts` |

### updateCustomer

- **Signature**: `updateCustomer(request: Customers.UpdateCustomerRequestParams, options?: RequestOptions): ApiPromise<CustomerResponse, Customers.UpdateCustomerError>`
- **Wire**: `PUT /customers/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CustomerResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Customers.UpdateCustomerError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"customerErrorResponse1"` [422] `CustomerErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Customers.UpdateCustomerRequestParams` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |
| `body` | `body` | `UpdateCustomerRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateCustomerRequest` | `updateCustomerRequestSchema` | `src/models/update-customer-request.ts` |
| `CustomerResponse` | `customerResponseSchema` | `src/models/customer-response.ts` |
| `CustomerErrorResponse1` | `customerErrorResponse1Schema` | `src/models/customer-error-response1.ts` |

