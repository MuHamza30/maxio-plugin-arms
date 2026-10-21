<!-- Generated file — do not edit; regenerated with the SDK. -->

# FeatureTemplates — operations

Accessor: `client.feature_templates` · Source: `maxio_advanced_billing/apis/feature_templates.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.feature_templates.archive_feature_template

- **Provider rules (Maxio)**: Send `remove_from_catalog=true` only to revoke access for good: it destroys the template's catalog items and their entitlements at once, and `restore_feature_template` does not bring them back. Notes: `knowledge/operations/feature-templates.md#archivefeaturetemplate`
- **Route**: `DELETE /features/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def archive_feature_template(id_: int, *, remove_from_catalog: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `remove_from_catalog` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, ArchiveFeatureTemplateErrorBody]`
- **Error**: `ArchiveFeatureTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `ArchiveFeatureTemplateErrorBody` | `maxio_advanced_billing/errors/archive_feature_template_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.feature_templates.create_feature_template

- **Provider rules (Maxio)**: Settle `key` and `kind` before creating: `key` is rejected on every later update, and `kind` once any feature catalog item uses the template. Notes: `knowledge/operations/feature-templates.md#createfeaturetemplate`
- **Route**: `POST /features.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_feature_template(*, body: CreateFeatureTemplateRequest | CreateFeatureTemplateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FeatureTemplateResponse`
- **Returns (raw)**: `ApiResult[FeatureTemplateResponse, CreateFeatureTemplateErrorBody]`
- **Error**: `CreateFeatureTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateFeatureTemplateRequest` | `maxio_advanced_billing/models/create_feature_template_request.py` |
| `CreateFeatureTemplateRequestDict` | `maxio_advanced_billing/models/create_feature_template_request.py` |
| `FeatureTemplateResponse` | `maxio_advanced_billing/models/feature_template_response.py` |
| `CreateFeatureTemplateErrorBody` | `maxio_advanced_billing/errors/create_feature_template_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.feature_templates.list_feature_templates

- **Route**: `GET /features.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_feature_templates(*, page: int | None = 1, per_page: int | None = 20, status: Status1OrStr | None = Status1.ACTIVE, q: str | None = None, kind: KindOrStr | None = None, updated_from: Date | None = None, updated_to: Date | None = None, sort_by: SortByOrStr | None = SortBy.NAME, sort_direction: SortDirectionOrStr | None = SortDirection.ASC, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query · `status` — query · `q` — query · `kind` — query · `updated_from` — query · `updated_to` — query · `sort_by` — query · `sort_direction` — query
- **Returns (parsed)**: `FeatureTemplatesListResponse`
- **Returns (raw)**: `ApiResult[FeatureTemplatesListResponse, ListFeatureTemplatesErrorBody]`
- **Error**: `ListFeatureTemplatesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Status1OrStr` | `maxio_advanced_billing/models/enums/status1.py` |
| `KindOrStr` | `maxio_advanced_billing/models/enums/kind.py` |
| `SortByOrStr` | `maxio_advanced_billing/models/enums/sort_by.py` |
| `SortDirectionOrStr` | `maxio_advanced_billing/models/enums/sort_direction.py` |
| `FeatureTemplatesListResponse` | `maxio_advanced_billing/models/feature_templates_list_response.py` |
| `ListFeatureTemplatesErrorBody` | `maxio_advanced_billing/errors/list_feature_templates_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.feature_templates.read_feature_template

- **Route**: `GET /features/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_feature_template(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `FeatureTemplateResponse`
- **Returns (raw)**: `ApiResult[FeatureTemplateResponse, ReadFeatureTemplateErrorBody]`
- **Error**: `ReadFeatureTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `FeatureTemplateResponse` | `maxio_advanced_billing/models/feature_template_response.py` |
| `ReadFeatureTemplateErrorBody` | `maxio_advanced_billing/errors/read_feature_template_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.feature_templates.restore_feature_template

- **Route**: `POST /features/{id}/restore.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def restore_feature_template(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `FeatureTemplateResponse`
- **Returns (raw)**: `ApiResult[FeatureTemplateResponse, RestoreFeatureTemplateErrorBody]`
- **Error**: `RestoreFeatureTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403, 422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `FeatureTemplateResponse` | `maxio_advanced_billing/models/feature_template_response.py` |
| `RestoreFeatureTemplateErrorBody` | `maxio_advanced_billing/errors/restore_feature_template_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.feature_templates.update_feature_template

- **Route**: `PUT /features/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_feature_template(id_: int, *, body: UpdateFeatureTemplateRequest | UpdateFeatureTemplateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `FeatureTemplateResponse`
- **Returns (raw)**: `ApiResult[FeatureTemplateResponse, UpdateFeatureTemplateErrorBody]`
- **Error**: `UpdateFeatureTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [403, 422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateFeatureTemplateRequest` | `maxio_advanced_billing/models/update_feature_template_request.py` |
| `UpdateFeatureTemplateRequestDict` | `maxio_advanced_billing/models/update_feature_template_request.py` |
| `FeatureTemplateResponse` | `maxio_advanced_billing/models/feature_template_response.py` |
| `UpdateFeatureTemplateErrorBody` | `maxio_advanced_billing/errors/update_feature_template_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

