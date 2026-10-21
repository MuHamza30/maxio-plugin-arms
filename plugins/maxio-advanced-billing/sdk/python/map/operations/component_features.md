<!-- Generated file — do not edit; regenerated with the SDK. -->

# ComponentFeatures — operations

Accessor: `client.component_features` · Source: `maxio_advanced_billing/apis/component_features.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.component_features.create_component_feature

- **Route**: `POST /components/{component_id}/features.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_component_feature(component_id: int, *, body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`
- **Params**: `component_id` — path · `body` — JSON body
- **Returns (parsed)**: `FeatureCatalogItemResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemResponse, CreateComponentFeatureErrorBody]`
- **Error**: `CreateComponentFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403, 422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateFeatureCatalogItemRequest` | `maxio_advanced_billing/models/create_feature_catalog_item_request.py` |
| `CreateFeatureCatalogItemRequestDict` | `maxio_advanced_billing/models/create_feature_catalog_item_request.py` |
| `FeatureCatalogItemResponse` | `maxio_advanced_billing/models/feature_catalog_item_response.py` |
| `CreateComponentFeatureErrorBody` | `maxio_advanced_billing/errors/create_component_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.component_features.list_component_features

- **Route**: `GET /components/{component_id}/features.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_component_features(component_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`
- **Params**: `component_id` — path
- **Returns (parsed)**: `FeatureCatalogItemsListResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemsListResponse, ListComponentFeaturesErrorBody]`
- **Error**: `ListComponentFeaturesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `FeatureCatalogItemsListResponse` | `maxio_advanced_billing/models/feature_catalog_items_list_response.py` |
| `ListComponentFeaturesErrorBody` | `maxio_advanced_billing/errors/list_component_features_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.component_features.read_component_feature

- **Route**: `GET /components/{component_id}/features/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_component_feature(component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `id_`
- **Params**: `component_id` — path · `id_` — path `id`
- **Returns (parsed)**: `FeatureCatalogItemResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemResponse, ReadComponentFeatureErrorBody]`
- **Error**: `ReadComponentFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `FeatureCatalogItemResponse` | `maxio_advanced_billing/models/feature_catalog_item_response.py` |
| `ReadComponentFeatureErrorBody` | `maxio_advanced_billing/errors/read_component_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.component_features.remove_component_feature

- **Route**: `DELETE /components/{component_id}/features/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def remove_component_feature(component_id: int, id_: int, *, destroy_entitlements: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `id_`
- **Params**: `component_id` — path · `id_` — path `id` · `destroy_entitlements` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveComponentFeatureErrorBody]`
- **Error**: `RemoveComponentFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveComponentFeatureErrorBody` | `maxio_advanced_billing/errors/remove_component_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.component_features.restore_component_feature

- **Route**: `POST /components/{component_id}/features/{id}/restore.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def restore_component_feature(component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `id_`
- **Params**: `component_id` — path · `id_` — path `id`
- **Returns (parsed)**: `FeatureCatalogItemResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemResponse, RestoreComponentFeatureErrorBody]`
- **Error**: `RestoreComponentFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403, 422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `FeatureCatalogItemResponse` | `maxio_advanced_billing/models/feature_catalog_item_response.py` |
| `RestoreComponentFeatureErrorBody` | `maxio_advanced_billing/errors/restore_component_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.component_features.update_component_feature

- **Route**: `PUT /components/{component_id}/features/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_component_feature(component_id: int, id_: int, *, body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `id_`
- **Params**: `component_id` — path · `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `FeatureCatalogItemResponse`
- **Returns (raw)**: `ApiResult[FeatureCatalogItemResponse, UpdateComponentFeatureErrorBody]`
- **Error**: `UpdateComponentFeatureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403, 422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateFeatureCatalogItemRequest` | `maxio_advanced_billing/models/update_feature_catalog_item_request.py` |
| `UpdateFeatureCatalogItemRequestDict` | `maxio_advanced_billing/models/update_feature_catalog_item_request.py` |
| `FeatureCatalogItemResponse` | `maxio_advanced_billing/models/feature_catalog_item_response.py` |
| `UpdateComponentFeatureErrorBody` | `maxio_advanced_billing/errors/update_component_feature_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

