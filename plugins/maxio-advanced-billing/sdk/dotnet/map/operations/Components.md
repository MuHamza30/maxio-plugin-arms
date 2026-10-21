<!-- Generated file — do not edit; regenerated with the SDK. -->

# Components — operations

Accessor: `client.Components` · Source: `src/MaxioAdvancedBilling/Api/Components.cs` · 12 operations

**Type sources**: the file declaring each type an operation names (`RawError` excluded — see sdk-map.md).

### ArchiveComponent

- **Provider notes (Maxio)**: `knowledge/operations/components.md#archivecomponent`
- **Auth**: `options.BasicAuth`
- **Signature**: `ArchiveComponent(ArchiveComponentRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductFamilyId`, `ComponentId`
- **Returns**: `Component`
- **Error**: `ApiException<ArchiveComponentError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `ArchiveComponentRequest` | `src/MaxioAdvancedBilling/Requests/Components/ArchiveComponentRequest.cs` |
| `Component` | `src/MaxioAdvancedBilling/Models/Component.cs` |
| `ArchiveComponentError` | `src/MaxioAdvancedBilling/Errors/ArchiveComponentError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### CreateEventBasedComponent

- **Provider rules (Maxio)**: Follow with `ActivateEventBasedComponent` for each subscription that should be billed; events streamed without it produce no charge and no error. Notes: `knowledge/operations/components.md#createeventbasedcomponent`
- **Auth**: `options.BasicAuth`
- **Signature**: `CreateEventBasedComponent(CreateEventBasedComponentRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductFamilyId`
- **Returns**: `ComponentResponse`
- **Error**: `ApiException<CreateEventBasedComponentError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CreateEventBasedComponentRequest` | `src/MaxioAdvancedBilling/Requests/Components/CreateEventBasedComponentRequest.cs` |
| `CreateEbbComponent` | `src/MaxioAdvancedBilling/Models/CreateEbbComponent.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |
| `CreateEventBasedComponentError` | `src/MaxioAdvancedBilling/Errors/CreateEventBasedComponentError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### CreateMeteredComponent

- **Provider rules (Maxio)**: Send `unit_price` in decimal major units, not cents (R4). Send `prices` for any scheme other than `per_unit`, as contiguous, non-overlapping brackets. On new-Catalog sites give taxable components a `tax_code`. Notes: `knowledge/operations/components.md#createmeteredcomponent`
- **Auth**: `options.BasicAuth`
- **Signature**: `CreateMeteredComponent(CreateMeteredComponentRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductFamilyId`
- **Returns**: `ComponentResponse`
- **Error**: `ApiException<CreateMeteredComponentError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CreateMeteredComponentRequest` | `src/MaxioAdvancedBilling/Requests/Components/CreateMeteredComponentRequest.cs` |
| `CreateMeteredComponent` | `src/MaxioAdvancedBilling/Models/CreateMeteredComponent.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |
| `CreateMeteredComponentError` | `src/MaxioAdvancedBilling/Errors/CreateMeteredComponentError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### CreateOnOffComponent

- **Provider notes (Maxio)**: `knowledge/operations/components.md#createonoffcomponent`
- **Auth**: `options.BasicAuth`
- **Signature**: `CreateOnOffComponent(CreateOnOffComponentRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductFamilyId`
- **Returns**: `ComponentResponse`
- **Error**: `ApiException<CreateOnOffComponentError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CreateOnOffComponentRequest` | `src/MaxioAdvancedBilling/Requests/Components/CreateOnOffComponentRequest.cs` |
| `CreateOnOffComponent` | `src/MaxioAdvancedBilling/Models/CreateOnOffComponent.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |
| `CreateOnOffComponentError` | `src/MaxioAdvancedBilling/Errors/CreateOnOffComponentError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### CreatePrepaidUsageComponent

- **Provider notes (Maxio)**: `knowledge/operations/components.md#createprepaidusagecomponent`
- **Auth**: `options.BasicAuth`
- **Signature**: `CreatePrepaidUsageComponent(CreatePrepaidUsageComponentRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductFamilyId`
- **Returns**: `ComponentResponse`
- **Error**: `ApiException<CreatePrepaidUsageComponentError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CreatePrepaidUsageComponentRequest` | `src/MaxioAdvancedBilling/Requests/Components/CreatePrepaidUsageComponentRequest.cs` |
| `CreatePrepaidComponent` | `src/MaxioAdvancedBilling/Models/CreatePrepaidComponent.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |
| `CreatePrepaidUsageComponentError` | `src/MaxioAdvancedBilling/Errors/CreatePrepaidUsageComponentError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### CreateQuantityBasedComponent

- **Provider rules (Maxio)**: Send `recurring: false` only for a one-time charge (inferred; D10). In `stairstep`, send each bracket's `unit_price` as the flat charge for the whole band (D17). Notes: `knowledge/operations/components.md#createquantitybasedcomponent`
- **Auth**: `options.BasicAuth`
- **Signature**: `CreateQuantityBasedComponent(CreateQuantityBasedComponentRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductFamilyId`
- **Returns**: `ComponentResponse`
- **Error**: `ApiException<CreateQuantityBasedComponentError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CreateQuantityBasedComponentRequest` | `src/MaxioAdvancedBilling/Requests/Components/CreateQuantityBasedComponentRequest.cs` |
| `CreateQuantityBasedComponent` | `src/MaxioAdvancedBilling/Models/CreateQuantityBasedComponent.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |
| `CreateQuantityBasedComponentError` | `src/MaxioAdvancedBilling/Errors/CreateQuantityBasedComponentError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### FindComponent

- **Auth**: `options.BasicAuth`
- **Signature**: `FindComponent(FindComponentRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Handle`
- **Query params (wire ← C#)**: `handle` ← `Handle`
- **Returns**: `ComponentResponse`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `FindComponentRequest` | `src/MaxioAdvancedBilling/Requests/Components/FindComponentRequest.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |

### ListComponents

- **Auth**: `options.BasicAuth`
- **Signature**: `ListComponents(ListComponentsRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
- **Query params (wire ← C#)**: `date_field` ← `DateField`, `start_date` ← `StartDate`, `end_date` ← `EndDate`, `start_datetime` ← `StartDatetime`, `end_datetime` ← `EndDatetime`, `include_archived` ← `IncludeArchived`, `page` ← `Page`, `per_page` ← `PerPage`, `filter` ← `Filter`
- **Returns**: `IReadOnlyList<ComponentResponse>`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `ListComponentsRequest` | `src/MaxioAdvancedBilling/Requests/Components/ListComponentsRequest.cs` |
| `BasicDateField` | `src/MaxioAdvancedBilling/Models/Enums/BasicDateField.cs` |
| `ListComponentsFilter` | `src/MaxioAdvancedBilling/Models/ListComponentsFilter.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |

### ListComponentsForProductFamily

- **Auth**: `options.BasicAuth`
- **Signature**: `ListComponentsForProductFamily(ListComponentsForProductFamilyRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductFamilyId`
- **Query params (wire ← C#)**: `include_archived` ← `IncludeArchived`, `page` ← `Page`, `per_page` ← `PerPage`, `filter` ← `Filter`, `date_field` ← `DateField`, `end_date` ← `EndDate`, `end_datetime` ← `EndDatetime`, `start_date` ← `StartDate`, `start_datetime` ← `StartDatetime`
- **Returns**: `IReadOnlyList<ComponentResponse>`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `ListComponentsForProductFamilyRequest` | `src/MaxioAdvancedBilling/Requests/Components/ListComponentsForProductFamilyRequest.cs` |
| `ListComponentsFilter` | `src/MaxioAdvancedBilling/Models/ListComponentsFilter.cs` |
| `BasicDateField` | `src/MaxioAdvancedBilling/Models/Enums/BasicDateField.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |

### ReadComponent

- **Auth**: `options.BasicAuth`
- **Signature**: `ReadComponent(ReadComponentRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductFamilyId`, `ComponentId`
- **Query params (wire ← C#)**: `include_features` ← `IncludeFeatures`
- **Returns**: `ComponentResponse`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `ReadComponentRequest` | `src/MaxioAdvancedBilling/Requests/Components/ReadComponentRequest.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |

### UpdateComponent

- **Provider notes (Maxio)**: `knowledge/operations/components.md#updatecomponent`
- **Auth**: `options.BasicAuth`
- **Signature**: `UpdateComponent(UpdateComponentOperationRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ComponentId`
- **Returns**: `ComponentResponse`
- **Error**: `ApiException<UpdateComponentError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `UpdateComponentOperationRequest` | `src/MaxioAdvancedBilling/Requests/Components/UpdateComponentOperationRequest.cs` |
| `UpdateComponentRequest` | `src/MaxioAdvancedBilling/Models/UpdateComponentRequest.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |
| `UpdateComponentError` | `src/MaxioAdvancedBilling/Errors/UpdateComponentError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### UpdateProductFamilyComponent

- **Auth**: `options.BasicAuth`
- **Signature**: `UpdateProductFamilyComponent(UpdateProductFamilyComponentRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductFamilyId`, `ComponentId`
- **Returns**: `ComponentResponse`
- **Error**: `ApiException<UpdateProductFamilyComponentError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `UpdateProductFamilyComponentRequest` | `src/MaxioAdvancedBilling/Requests/Components/UpdateProductFamilyComponentRequest.cs` |
| `UpdateComponentRequest` | `src/MaxioAdvancedBilling/Models/UpdateComponentRequest.cs` |
| `ComponentResponse` | `src/MaxioAdvancedBilling/Models/ComponentResponse.cs` |
| `UpdateProductFamilyComponentError` | `src/MaxioAdvancedBilling/Errors/UpdateProductFamilyComponentError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

