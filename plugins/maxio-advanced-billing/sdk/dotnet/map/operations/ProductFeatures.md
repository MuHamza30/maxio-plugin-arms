<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProductFeatures — operations

Accessor: `client.ProductFeatures` · Source: `src/MaxioAdvancedBilling/Api/ProductFeatures.cs` · 6 operations

**Type sources**: the file declaring each type an operation names (`RawError` excluded — see sdk-map.md).

### CreateProductFeature

- **Provider rules (Maxio)**: Send `propagate_to_subscriptions: true` if existing subscribers should get the feature before their next subscription change. Send `value` as `"true"` or `"false"` for an access right, the limit itself for a usage limit. Notes: `knowledge/operations/product-features.md#createproductfeature`
- **Auth**: `options.BasicAuth`
- **Signature**: `CreateProductFeature(CreateProductFeatureRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductId`
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `ApiException<CreateProductFeatureError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [403, 422] · `TryGetNoContent(out RawError)` [404] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CreateProductFeatureRequest` | `src/MaxioAdvancedBilling/Requests/ProductFeatures/CreateProductFeatureRequest.cs` |
| `CreateFeatureCatalogItemRequest` | `src/MaxioAdvancedBilling/Models/CreateFeatureCatalogItemRequest.cs` |
| `FeatureCatalogItemResponse` | `src/MaxioAdvancedBilling/Models/FeatureCatalogItemResponse.cs` |
| `CreateProductFeatureError` | `src/MaxioAdvancedBilling/Errors/CreateProductFeatureError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### ListProductFeatures

- **Auth**: `options.BasicAuth`
- **Signature**: `ListProductFeatures(ListProductFeaturesRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductId`
- **Returns**: `FeatureCatalogItemsListResponse`
- **Error**: `ApiException<ListProductFeaturesError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [403] · `TryGetNoContent(out RawError)` [404] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `ListProductFeaturesRequest` | `src/MaxioAdvancedBilling/Requests/ProductFeatures/ListProductFeaturesRequest.cs` |
| `FeatureCatalogItemsListResponse` | `src/MaxioAdvancedBilling/Models/FeatureCatalogItemsListResponse.cs` |
| `ListProductFeaturesError` | `src/MaxioAdvancedBilling/Errors/ListProductFeaturesError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### ReadProductFeature

- **Auth**: `options.BasicAuth`
- **Signature**: `ReadProductFeature(ReadProductFeatureRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductId`, `Id`
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `ApiException<ReadProductFeatureError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [403] · `TryGetNoContent(out RawError)` [404] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `ReadProductFeatureRequest` | `src/MaxioAdvancedBilling/Requests/ProductFeatures/ReadProductFeatureRequest.cs` |
| `FeatureCatalogItemResponse` | `src/MaxioAdvancedBilling/Models/FeatureCatalogItemResponse.cs` |
| `ReadProductFeatureError` | `src/MaxioAdvancedBilling/Errors/ReadProductFeatureError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### RemoveProductFeature

- **Provider rules (Maxio)**: Send `destroy_entitlements=true` only to revoke access for good: it permanently deletes the catalog item and every entitlement it created. Without it the item is archived and subscribers keep their entitlements. Notes: `knowledge/operations/product-features.md#removeproductfeature`
- **Auth**: `options.BasicAuth`
- **Signature**: `RemoveProductFeature(RemoveProductFeatureRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductId`, `Id`
- **Query params (wire ← C#)**: `destroy_entitlements` ← `DestroyEntitlements`
- **Returns**: `void` (Task)
- **Error**: `ApiException<RemoveProductFeatureError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [403] · `TryGetNoContent(out RawError)` [404] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `RemoveProductFeatureRequest` | `src/MaxioAdvancedBilling/Requests/ProductFeatures/RemoveProductFeatureRequest.cs` |
| `RemoveProductFeatureError` | `src/MaxioAdvancedBilling/Errors/RemoveProductFeatureError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### RestoreProductFeature

- **Auth**: `options.BasicAuth`
- **Signature**: `RestoreProductFeature(RestoreProductFeatureRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductId`, `Id`
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `ApiException<RestoreProductFeatureError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [403, 422] · `TryGetNoContent(out RawError)` [404] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `RestoreProductFeatureRequest` | `src/MaxioAdvancedBilling/Requests/ProductFeatures/RestoreProductFeatureRequest.cs` |
| `FeatureCatalogItemResponse` | `src/MaxioAdvancedBilling/Models/FeatureCatalogItemResponse.cs` |
| `RestoreProductFeatureError` | `src/MaxioAdvancedBilling/Errors/RestoreProductFeatureError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### UpdateProductFeature

- **Provider rules (Maxio)**: Send `propagate_to_subscriptions: true` if existing subscribers must get the new value or periodicity. Left out, this call does not update the entitlements they already hold. Notes: `knowledge/operations/product-features.md#updateproductfeature`
- **Auth**: `options.BasicAuth`
- **Signature**: `UpdateProductFeature(UpdateProductFeatureRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `ProductId`, `Id`
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `ApiException<UpdateProductFeatureError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [403, 422] · `TryGetNoContent(out RawError)` [404] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `UpdateProductFeatureRequest` | `src/MaxioAdvancedBilling/Requests/ProductFeatures/UpdateProductFeatureRequest.cs` |
| `UpdateFeatureCatalogItemRequest` | `src/MaxioAdvancedBilling/Models/UpdateFeatureCatalogItemRequest.cs` |
| `FeatureCatalogItemResponse` | `src/MaxioAdvancedBilling/Models/FeatureCatalogItemResponse.cs` |
| `UpdateProductFeatureError` | `src/MaxioAdvancedBilling/Errors/UpdateProductFeatureError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

