<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionProducts — operations

Accessor: `client.SubscriptionProducts` · Source: `src/MaxioAdvancedBilling/Api/SubscriptionProducts.cs` · 2 operations

**Type sources**: the file declaring each type an operation names (`RawError` excluded — see sdk-map.md).

### MigrateSubscriptionProduct

- **Provider rules (Maxio)**: Send `preserve_period` explicitly: `true` prorates and keeps the billing date; omitted resets the period and charges in full (D13). Preview first (`trialing`: D13). One random `uniqueness_token` per change, never computed (R12). Notes: `knowledge/operations/subscription-products.md#migratesubscriptionproduct`
- **Auth**: `options.BasicAuth`
- **Signature**: `MigrateSubscriptionProduct(MigrateSubscriptionProductRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `SubscriptionResponse`
- **Error**: `ApiException<MigrateSubscriptionProductError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `MigrateSubscriptionProductRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionProducts/MigrateSubscriptionProductRequest.cs` |
| `SubscriptionProductMigrationRequest` | `src/MaxioAdvancedBilling/Models/SubscriptionProductMigrationRequest.cs` |
| `SubscriptionResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionResponse.cs` |
| `MigrateSubscriptionProductError` | `src/MaxioAdvancedBilling/Errors/MigrateSubscriptionProductError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### PreviewSubscriptionProductMigration

- **Provider notes (Maxio)**: `knowledge/operations/subscription-products.md#previewsubscriptionproductmigration`
- **Auth**: `options.BasicAuth`
- **Signature**: `PreviewSubscriptionProductMigration(PreviewSubscriptionProductMigrationRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `SubscriptionMigrationPreviewResponse`
- **Error**: `ApiException<PreviewSubscriptionProductMigrationError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `PreviewSubscriptionProductMigrationRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionProducts/PreviewSubscriptionProductMigrationRequest.cs` |
| `SubscriptionMigrationPreviewRequest` | `src/MaxioAdvancedBilling/Models/SubscriptionMigrationPreviewRequest.cs` |
| `SubscriptionMigrationPreviewResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionMigrationPreviewResponse.cs` |
| `PreviewSubscriptionProductMigrationError` | `src/MaxioAdvancedBilling/Errors/PreviewSubscriptionProductMigrationError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

