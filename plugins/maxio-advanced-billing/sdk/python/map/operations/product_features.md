<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProductFeatures — operations

Accessor: `client.product_features` · Source: `maxio_advanced_billing/apis/product_features.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.product_features.create_product_feature

- **Route**: `POST /products/{product_id}/features.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_product_feature(product_id: int, *, body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`
- **Params**: `product_id` — path · `body` — JSON body
- **Returns (parsed)**: `FeatureCatalogItemResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemResponse, CreateProductFeatureErrorBody]`
- **Error**: `CreateProductFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403, 422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateFeatureCatalogItemRequest` | `maxio_advanced_billing/models/create_feature_catalog_item_request.py` |
| `CreateFeatureCatalogItemRequestDict` | `maxio_advanced_billing/models/create_feature_catalog_item_request.py` |
| `FeatureCatalogItemResponse` | `maxio_advanced_billing/models/feature_catalog_item_response.py` |
| `CreateProductFeatureErrorBody` | `maxio_advanced_billing/errors/create_product_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.product_features.list_product_features

- **Route**: `GET /products/{product_id}/features.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_product_features(product_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`
- **Params**: `product_id` — path
- **Returns (parsed)**: `FeatureCatalogItemsListResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemsListResponse, ListProductFeaturesErrorBody]`
- **Error**: `ListProductFeaturesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `FeatureCatalogItemsListResponse` | `maxio_advanced_billing/models/feature_catalog_items_list_response.py` |
| `ListProductFeaturesErrorBody` | `maxio_advanced_billing/errors/list_product_features_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.product_features.read_product_feature

- **Route**: `GET /products/{product_id}/features/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_product_feature(product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `id_`
- **Params**: `product_id` — path · `id_` — path `id`
- **Returns (parsed)**: `FeatureCatalogItemResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemResponse, ReadProductFeatureErrorBody]`
- **Error**: `ReadProductFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `FeatureCatalogItemResponse` | `maxio_advanced_billing/models/feature_catalog_item_response.py` |
| `ReadProductFeatureErrorBody` | `maxio_advanced_billing/errors/read_product_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.product_features.remove_product_feature

- **Route**: `DELETE /products/{product_id}/features/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def remove_product_feature(product_id: int, id_: int, *, destroy_entitlements: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `id_`
- **Params**: `product_id` — path · `id_` — path `id` · `destroy_entitlements` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveProductFeatureErrorBody]`
- **Error**: `RemoveProductFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveProductFeatureErrorBody` | `maxio_advanced_billing/errors/remove_product_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.product_features.restore_product_feature

- **Route**: `POST /products/{product_id}/features/{id}/restore.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def restore_product_feature(product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `id_`
- **Params**: `product_id` — path · `id_` — path `id`
- **Returns (parsed)**: `FeatureCatalogItemResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemResponse, RestoreProductFeatureErrorBody]`
- **Error**: `RestoreProductFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403, 422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `FeatureCatalogItemResponse` | `maxio_advanced_billing/models/feature_catalog_item_response.py` |
| `RestoreProductFeatureErrorBody` | `maxio_advanced_billing/errors/restore_product_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.product_features.update_product_feature

- **Route**: `PUT /products/{product_id}/features/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_product_feature(product_id: int, id_: int, *, body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `id_`
- **Params**: `product_id` — path · `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `FeatureCatalogItemResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemResponse, UpdateProductFeatureErrorBody]`
- **Error**: `UpdateProductFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403, 422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateFeatureCatalogItemRequest` | `maxio_advanced_billing/models/update_feature_catalog_item_request.py` |
| `UpdateFeatureCatalogItemRequestDict` | `maxio_advanced_billing/models/update_feature_catalog_item_request.py` |
| `FeatureCatalogItemResponse` | `maxio_advanced_billing/models/feature_catalog_item_response.py` |
| `UpdateProductFeatureErrorBody` | `maxio_advanced_billing/errors/update_product_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

