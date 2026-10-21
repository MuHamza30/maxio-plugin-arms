<!-- Generated file — do not edit; regenerated with the SDK. -->

# Components — operations

Accessor: `client.components` · Source: `maxio_advanced_billing/apis/components.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.components.archive_component

- **Provider notes (Maxio)**: `knowledge/operations/components.md#archivecomponent`
- **Route**: `DELETE /product_families/{product_family_id}/components/{component_id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def archive_component(product_family_id: int, component_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`, `component_id`
- **Params**: `product_family_id` — path · `component_id` — path
- **Returns (parsed)**: `Component`
- **Returns (raw)**: `ApiResult[Component, ArchiveComponentErrorBody]`
- **Error**: `ArchiveComponentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Component` | `maxio_advanced_billing/models/component.py` |
| `ArchiveComponentErrorBody` | `maxio_advanced_billing/errors/archive_component_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.components.create_event_based_component

- **Provider rules (Maxio)**: Follow with `activate_event_based_component` for each subscription that should be billed; events streamed without it produce no charge and no error. Notes: `knowledge/operations/components.md#createeventbasedcomponent`
- **Route**: `POST /product_families/{product_family_id}/event_based_components.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_event_based_component(product_family_id: str, *, body: CreateEbbComponent | CreateEbbComponentDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`
- **Params**: `product_family_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComponentResponse`
- **Returns (raw)**: `ApiResult[ComponentResponse, CreateEventBasedComponentErrorBody]`
- **Error**: `CreateEventBasedComponentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateEbbComponent` | `maxio_advanced_billing/models/create_ebb_component.py` |
| `CreateEbbComponentDict` | `maxio_advanced_billing/models/create_ebb_component.py` |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |
| `CreateEventBasedComponentErrorBody` | `maxio_advanced_billing/errors/create_event_based_component_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.components.create_metered_component

- **Provider rules (Maxio)**: Send `unit_price` in decimal major units, not cents (R4). Send `prices` for any scheme other than `per_unit`, as contiguous, non-overlapping brackets. On new-Catalog sites give taxable components a `tax_code`. Notes: `knowledge/operations/components.md#createmeteredcomponent`
- **Route**: `POST /product_families/{product_family_id}/metered_components.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_metered_component(product_family_id: str, *, body: CreateMeteredComponent | CreateMeteredComponentDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`
- **Params**: `product_family_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComponentResponse`
- **Returns (raw)**: `ApiResult[ComponentResponse, CreateMeteredComponentErrorBody]`
- **Error**: `CreateMeteredComponentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateMeteredComponent` | `maxio_advanced_billing/models/create_metered_component.py` |
| `CreateMeteredComponentDict` | `maxio_advanced_billing/models/create_metered_component.py` |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |
| `CreateMeteredComponentErrorBody` | `maxio_advanced_billing/errors/create_metered_component_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.components.create_on_off_component

- **Provider notes (Maxio)**: `knowledge/operations/components.md#createonoffcomponent`
- **Route**: `POST /product_families/{product_family_id}/on_off_components.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_on_off_component(product_family_id: str, *, body: CreateOnOffComponent | CreateOnOffComponentDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`
- **Params**: `product_family_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComponentResponse`
- **Returns (raw)**: `ApiResult[ComponentResponse, CreateOnOffComponentErrorBody]`
- **Error**: `CreateOnOffComponentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateOnOffComponent` | `maxio_advanced_billing/models/create_on_off_component.py` |
| `CreateOnOffComponentDict` | `maxio_advanced_billing/models/create_on_off_component.py` |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |
| `CreateOnOffComponentErrorBody` | `maxio_advanced_billing/errors/create_on_off_component_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.components.create_prepaid_usage_component

- **Provider notes (Maxio)**: `knowledge/operations/components.md#createprepaidusagecomponent`
- **Route**: `POST /product_families/{product_family_id}/prepaid_usage_components.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_prepaid_usage_component(product_family_id: str, *, body: CreatePrepaidComponent | CreatePrepaidComponentDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`
- **Params**: `product_family_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComponentResponse`
- **Returns (raw)**: `ApiResult[ComponentResponse, CreatePrepaidUsageComponentErrorBody]`
- **Error**: `CreatePrepaidUsageComponentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `CreatePrepaidComponent` | `maxio_advanced_billing/models/create_prepaid_component.py` |
| `CreatePrepaidComponentDict` | `maxio_advanced_billing/models/create_prepaid_component.py` |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |
| `CreatePrepaidUsageComponentErrorBody` | `maxio_advanced_billing/errors/create_prepaid_usage_component_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.components.create_quantity_based_component

- **Provider rules (Maxio)**: Send `recurring: false` only for a one-time charge (inferred; D10). In `stairstep`, send each bracket's `unit_price` as the flat charge for the whole band (D17). Notes: `knowledge/operations/components.md#createquantitybasedcomponent`
- **Route**: `POST /product_families/{product_family_id}/quantity_based_components.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_quantity_based_component(product_family_id: str, *, body: CreateQuantityBasedComponent | CreateQuantityBasedComponentDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`
- **Params**: `product_family_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComponentResponse`
- **Returns (raw)**: `ApiResult[ComponentResponse, CreateQuantityBasedComponentErrorBody]`
- **Error**: `CreateQuantityBasedComponentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateQuantityBasedComponent` | `maxio_advanced_billing/models/create_quantity_based_component.py` |
| `CreateQuantityBasedComponentDict` | `maxio_advanced_billing/models/create_quantity_based_component.py` |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |
| `CreateQuantityBasedComponentErrorBody` | `maxio_advanced_billing/errors/create_quantity_based_component_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.components.find_component

- **Route**: `GET /components/lookup.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def find_component(handle: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `handle`
- **Params**: `handle` — query
- **Returns (parsed)**: `ComponentResponse`
- **Returns (raw)**: `ApiResult[ComponentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |

### client.components.list_components

- **Route**: `GET /components.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_components(*, date_field: BasicDateFieldOrStr | None = None, start_date: str | None = None, end_date: str | None = None, start_datetime: str | None = None, end_datetime: str | None = None, include_archived: bool | None = None, page: int | None = 1, per_page: int | None = 20, filter_: ListComponentsFilter | ListComponentsFilterDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `date_field` — query · `start_date` — query · `end_date` — query · `start_datetime` — query · `end_datetime` — query · `include_archived` — query · `page` — query · `per_page` — query · `filter_` — query `filter`
- **Returns (parsed)**: `list[ComponentResponse]`
- **Returns (raw)**: `ApiResult[list[ComponentResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BasicDateFieldOrStr` | `maxio_advanced_billing/models/enums/basic_date_field.py` |
| `ListComponentsFilter` | `maxio_advanced_billing/models/list_components_filter.py` |
| `ListComponentsFilterDict` | `maxio_advanced_billing/models/list_components_filter.py` |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |

### client.components.list_components_for_product_family

- **Route**: `GET /product_families/{product_family_id}/components.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_components_for_product_family(product_family_id: int, *, include_archived: bool | None = None, page: int | None = 1, per_page: int | None = 20, filter_: ListComponentsFilter | ListComponentsFilterDict | None = None, date_field: BasicDateFieldOrStr | None = None, end_date: str | None = None, end_datetime: str | None = None, start_date: str | None = None, start_datetime: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`
- **Params**: `product_family_id` — path · `include_archived` — query · `page` — query · `per_page` — query · `filter_` — query `filter` · `date_field` — query · `end_date` — query · `end_datetime` — query · `start_date` — query · `start_datetime` — query
- **Returns (parsed)**: `list[ComponentResponse]`
- **Returns (raw)**: `ApiResult[list[ComponentResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListComponentsFilter` | `maxio_advanced_billing/models/list_components_filter.py` |
| `ListComponentsFilterDict` | `maxio_advanced_billing/models/list_components_filter.py` |
| `BasicDateFieldOrStr` | `maxio_advanced_billing/models/enums/basic_date_field.py` |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |

### client.components.read_component

- **Route**: `GET /product_families/{product_family_id}/components/{component_id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_component(product_family_id: int, component_id: str, *, include_features: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`, `component_id`
- **Params**: `product_family_id` — path · `component_id` — path · `include_features` — query
- **Returns (parsed)**: `ComponentResponse`
- **Returns (raw)**: `ApiResult[ComponentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |

### client.components.update_component

- **Provider notes (Maxio)**: `knowledge/operations/components.md#updatecomponent`
- **Route**: `PUT /components/{component_id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_component(component_id: str, *, body: UpdateComponentRequest | UpdateComponentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`
- **Params**: `component_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComponentResponse`
- **Returns (raw)**: `ApiResult[ComponentResponse, UpdateComponentErrorBody]`
- **Error**: `UpdateComponentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateComponentRequest` | `maxio_advanced_billing/models/update_component_request.py` |
| `UpdateComponentRequestDict` | `maxio_advanced_billing/models/update_component_request.py` |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |
| `UpdateComponentErrorBody` | `maxio_advanced_billing/errors/update_component_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.components.update_product_family_component

- **Route**: `PUT /product_families/{product_family_id}/components/{component_id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_product_family_component(product_family_id: int, component_id: str, *, body: UpdateComponentRequest | UpdateComponentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`, `component_id`
- **Params**: `product_family_id` — path · `component_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComponentResponse`
- **Returns (raw)**: `ApiResult[ComponentResponse, UpdateProductFamilyComponentErrorBody]`
- **Error**: `UpdateProductFamilyComponentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateComponentRequest` | `maxio_advanced_billing/models/update_component_request.py` |
| `UpdateComponentRequestDict` | `maxio_advanced_billing/models/update_component_request.py` |
| `ComponentResponse` | `maxio_advanced_billing/models/component_response.py` |
| `UpdateProductFamilyComponentErrorBody` | `maxio_advanced_billing/errors/update_product_family_component_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

