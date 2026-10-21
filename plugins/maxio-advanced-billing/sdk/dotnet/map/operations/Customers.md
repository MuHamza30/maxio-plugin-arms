<!-- Generated file — do not edit; regenerated with the SDK. -->

# Customers — operations

Accessor: `client.Customers` · Source: `src/MaxioAdvancedBilling/Api/Customers.cs` · 7 operations

**Type sources**: the file declaring each type an operation names (`RawError` excluded — see sdk-map.md).

### CreateCustomer

- **Provider rules (Maxio)**: If your app has a user id, send it as `reference`, call `ReadCustomerByReference` first and create only on a 404. On the duplicate-reference 422, read the existing customer back (L2). Notes: `knowledge/operations/customers.md#createcustomer`
- **Auth**: `options.BasicAuth`
- **Signature**: `CreateCustomer(CreateCustomerOperationRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
- **Returns**: `CustomerResponse`
- **Error**: `ApiException<CreateCustomerError>` — **Case A (typed)**
- **Error accessors**: `TryGetCustomerErrorResponse1(out CustomerErrorResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CreateCustomerOperationRequest` | `src/MaxioAdvancedBilling/Requests/Customers/CreateCustomerOperationRequest.cs` |
| `CreateCustomerRequest` | `src/MaxioAdvancedBilling/Models/CreateCustomerRequest.cs` |
| `CustomerResponse` | `src/MaxioAdvancedBilling/Models/CustomerResponse.cs` |
| `CreateCustomerError` | `src/MaxioAdvancedBilling/Errors/CreateCustomerError.cs` |
| `CustomerErrorResponse1` | `src/MaxioAdvancedBilling/Models/CustomerErrorResponse1.cs` |

### DeleteCustomer

- **Auth**: `options.BasicAuth`
- **Signature**: `DeleteCustomer(DeleteCustomerRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Id`
- **Returns**: `void` (Task)
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteCustomerRequest` | `src/MaxioAdvancedBilling/Requests/Customers/DeleteCustomerRequest.cs` |

### ListCustomerSubscriptions

- **Provider notes (Maxio)**: `knowledge/operations/customers.md#listcustomersubscriptions`
- **Auth**: `options.BasicAuth`
- **Signature**: `ListCustomerSubscriptions(ListCustomerSubscriptionsRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `CustomerId`
- **Returns**: `IReadOnlyList<SubscriptionResponse>`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `ListCustomerSubscriptionsRequest` | `src/MaxioAdvancedBilling/Requests/Customers/ListCustomerSubscriptionsRequest.cs` |
| `SubscriptionResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionResponse.cs` |

### ListCustomers

- **Provider rules (Maxio)**: Never take the first result of a `q` search as the customer; use `ReadCustomerByReference` for an exact match. For incremental sync send `date_field` with a start and an end; an unrecognized `date_field` is ignored (R9). Notes: `knowledge/operations/customers.md#listcustomers`
- **Auth**: `options.BasicAuth`
- **Signature**: `ListCustomers(ListCustomersRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
- **Query params (wire ← C#)**: `direction` ← `Direction`, `page` ← `Page`, `per_page` ← `PerPage`, `date_field` ← `DateField`, `start_date` ← `StartDate`, `end_date` ← `EndDate`, `start_datetime` ← `StartDatetime`, `end_datetime` ← `EndDatetime`, `q` ← `Q`
- **Returns**: `IReadOnlyList<CustomerResponse>`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `ListCustomersRequest` | `src/MaxioAdvancedBilling/Requests/Customers/ListCustomersRequest.cs` |
| `SortingDirection` | `src/MaxioAdvancedBilling/Models/Enums/SortingDirection.cs` |
| `BasicDateField` | `src/MaxioAdvancedBilling/Models/Enums/BasicDateField.cs` |
| `CustomerResponse` | `src/MaxioAdvancedBilling/Models/CustomerResponse.cs` |

### ReadCustomer

- **Auth**: `options.BasicAuth`
- **Signature**: `ReadCustomer(ReadCustomerRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Id`
- **Returns**: `CustomerResponse`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `ReadCustomerRequest` | `src/MaxioAdvancedBilling/Requests/Customers/ReadCustomerRequest.cs` |
| `CustomerResponse` | `src/MaxioAdvancedBilling/Models/CustomerResponse.cs` |

### ReadCustomerByReference

- **Provider notes (Maxio)**: `knowledge/operations/customers.md#readcustomerbyreference`
- **Auth**: `options.BasicAuth`
- **Signature**: `ReadCustomerByReference(ReadCustomerByReferenceRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Reference`
- **Query params (wire ← C#)**: `reference` ← `Reference`
- **Returns**: `CustomerResponse`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `ReadCustomerByReferenceRequest` | `src/MaxioAdvancedBilling/Requests/Customers/ReadCustomerByReferenceRequest.cs` |
| `CustomerResponse` | `src/MaxioAdvancedBilling/Models/CustomerResponse.cs` |

### UpdateCustomer

- **Provider rules (Maxio)**: Pass the Maxio customer `id`, not your reference. Never send `entity_identifier_value` without `entity_identifier_kind`. The `vat_eu` and `national_tax` kinds also need `vat_country`; the other kinds do not. Notes: `knowledge/operations/customers.md#updatecustomer`
- **Auth**: `options.BasicAuth`
- **Signature**: `UpdateCustomer(UpdateCustomerOperationRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Id`
- **Returns**: `CustomerResponse`
- **Error**: `ApiException<UpdateCustomerError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetCustomerErrorResponse1(out CustomerErrorResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `UpdateCustomerOperationRequest` | `src/MaxioAdvancedBilling/Requests/Customers/UpdateCustomerOperationRequest.cs` |
| `UpdateCustomerRequest` | `src/MaxioAdvancedBilling/Models/UpdateCustomerRequest.cs` |
| `CustomerResponse` | `src/MaxioAdvancedBilling/Models/CustomerResponse.cs` |
| `UpdateCustomerError` | `src/MaxioAdvancedBilling/Errors/UpdateCustomerError.cs` |
| `CustomerErrorResponse1` | `src/MaxioAdvancedBilling/Models/CustomerErrorResponse1.cs` |

