<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProductFeatures — operations

Accessor: `client.productFeatures` · Source: `src/resources/product-features.ts` · 6 operations · Request and error types: namespace `ProductFeatures`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createProductFeature

- **Signature**: `createProductFeature(request: ProductFeatures.CreateProductFeatureRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemResponse, ProductFeatures.CreateProductFeatureError>`
- **Wire**: `POST /products/{product_id}/features.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductFeatures.CreateProductFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"errorListResponse12"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductFeatures.CreateProductFeatureRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |
| `body` | `body` | — | `CreateFeatureCatalogItemRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateFeatureCatalogItemRequest` | `createFeatureCatalogItemRequestSchema` | `src/models/create-feature-catalog-item-request.ts` |
| `FeatureCatalogItemResponse` | `featureCatalogItemResponseSchema` | `src/models/feature-catalog-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listProductFeatures

- **Signature**: `listProductFeatures(request: ProductFeatures.ListProductFeaturesRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemsListResponse, ProductFeatures.ListProductFeaturesError>`
- **Wire**: `GET /products/{product_id}/features.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `FeatureCatalogItemsListResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductFeatures.ListProductFeaturesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductFeatures.ListProductFeaturesRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `FeatureCatalogItemsListResponse` | `featureCatalogItemsListResponseSchema` | `src/models/feature-catalog-items-list-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readProductFeature

- **Signature**: `readProductFeature(request: ProductFeatures.ReadProductFeatureRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemResponse, ProductFeatures.ReadProductFeatureError>`
- **Wire**: `GET /products/{product_id}/features/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductFeatures.ReadProductFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductFeatures.ReadProductFeatureRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `FeatureCatalogItemResponse` | `featureCatalogItemResponseSchema` | `src/models/feature-catalog-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### removeProductFeature

- **Signature**: `removeProductFeature(request: ProductFeatures.RemoveProductFeatureRequest, options?: RequestOptions): ApiPromise<undefined, ProductFeatures.RemoveProductFeatureError>`
- **Wire**: `DELETE /products/{product_id}/features/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductFeatures.RemoveProductFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductFeatures.RemoveProductFeatureRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes | — |
| `id` | `path` | — | `number` | yes | — |
| `destroyEntitlements` | `query` | `destroy_entitlements` | `boolean` | no | `false` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### restoreProductFeature

- **Signature**: `restoreProductFeature(request: ProductFeatures.RestoreProductFeatureRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemResponse, ProductFeatures.RestoreProductFeatureError>`
- **Wire**: `POST /products/{product_id}/features/{id}/restore.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductFeatures.RestoreProductFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"errorListResponse12"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductFeatures.RestoreProductFeatureRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `FeatureCatalogItemResponse` | `featureCatalogItemResponseSchema` | `src/models/feature-catalog-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### updateProductFeature

- **Signature**: `updateProductFeature(request: ProductFeatures.UpdateProductFeatureRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemResponse, ProductFeatures.UpdateProductFeatureError>`
- **Wire**: `PUT /products/{product_id}/features/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductFeatures.UpdateProductFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"errorListResponse12"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductFeatures.UpdateProductFeatureRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |
| `body` | `body` | — | `UpdateFeatureCatalogItemRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateFeatureCatalogItemRequest` | `updateFeatureCatalogItemRequestSchema` | `src/models/update-feature-catalog-item-request.ts` |
| `FeatureCatalogItemResponse` | `featureCatalogItemResponseSchema` | `src/models/feature-catalog-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

