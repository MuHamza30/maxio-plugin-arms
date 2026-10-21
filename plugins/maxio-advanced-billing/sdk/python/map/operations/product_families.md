<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProductFamilies — operations

Accessor: `client.product_families` · Source: `maxio_advanced_billing/apis/product_families.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.product_families.create_product_family

- **Provider rules (Maxio)**: Set a stable `handle` you will keep (R6). Send `surcharging: false` if the family's products must not carry surcharges. Notes: `knowledge/operations/product-families.md#createproductfamily`
- **Route**: `POST /product_families.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_product_family(*, body: CreateProductFamilyRequest | CreateProductFamilyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProductFamilyResponse`
- **Returns (raw)**: `ApiResult[ProductFamilyResponse, CreateProductFamilyErrorBody]`
- **Error**: `CreateProductFamilyErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateProductFamilyRequest` | `maxio_advanced_billing/models/create_product_family_request.py` |
| `CreateProductFamilyRequestDict` | `maxio_advanced_billing/models/create_product_family_request.py` |
| `ProductFamilyResponse` | `maxio_advanced_billing/models/product_family_response.py` |
| `CreateProductFamilyErrorBody` | `maxio_advanced_billing/errors/create_product_family_error.py` |
| `ErrorListResponse1` | `maxio_advanced_billing/models/error_list_response1.py` |

### client.product_families.list_product_families

- **Route**: `GET /product_families.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_product_families(*, date_field: BasicDateFieldOrStr | None = None, start_date: Date | None = None, end_date: Date | None = None, start_datetime: RFC3339DateTime | None = None, end_datetime: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `date_field` — query · `start_date` — query · `end_date` — query · `start_datetime` — query · `end_datetime` — query
- **Returns (parsed)**: `list[ProductFamilyResponse]`
- **Returns (raw)**: `ApiResult[list[ProductFamilyResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BasicDateFieldOrStr` | `maxio_advanced_billing/models/enums/basic_date_field.py` |
| `ProductFamilyResponse` | `maxio_advanced_billing/models/product_family_response.py` |

### client.product_families.list_products_for_product_family

- **Provider notes (Maxio)**: `knowledge/operations/product-families.md#listproductsforproductfamily`
- **Route**: `GET /product_families/{product_family_id}/products.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_products_for_product_family(product_family_id: str, *, page: int | None = 1, per_page: int | None = 20, date_field: BasicDateFieldOrStr | None = None, filter_: ListProductsFilter | ListProductsFilterDict | None = None, start_date: Date | None = None, end_date: Date | None = None, start_datetime: RFC3339DateTime | None = None, end_datetime: RFC3339DateTime | None = None, include_archived: bool | None = None, include: ListProductsIncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_family_id`
- **Params**: `product_family_id` — path · `page` — query · `per_page` — query · `date_field` — query · `filter_` — query `filter` · `start_date` — query · `end_date` — query · `start_datetime` — query · `end_datetime` — query · `include_archived` — query · `include` — query
- **Returns (parsed)**: `list[ProductResponse]`
- **Returns (raw)**: `ApiResult[list[ProductResponse], ListProductsForProductFamilyErrorBody]`
- **Error**: `ListProductsForProductFamilyErrorBody` — **Case A (typed)**
- **Error arms**: `str` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BasicDateFieldOrStr` | `maxio_advanced_billing/models/enums/basic_date_field.py` |
| `ListProductsFilter` | `maxio_advanced_billing/models/list_products_filter.py` |
| `ListProductsFilterDict` | `maxio_advanced_billing/models/list_products_filter.py` |
| `ListProductsIncludeOrStr` | `maxio_advanced_billing/models/enums/list_products_include.py` |
| `ProductResponse` | `maxio_advanced_billing/models/product_response.py` |
| `ListProductsForProductFamilyErrorBody` | `maxio_advanced_billing/errors/list_products_for_product_family_error.py` |

### client.product_families.read_product_family

- **Provider notes (Maxio)**: `knowledge/operations/product-families.md#readproductfamily`
- **Route**: `GET /product_families/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_product_family(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `ProductFamilyResponse`
- **Returns (raw)**: `ApiResult[ProductFamilyResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProductFamilyResponse` | `maxio_advanced_billing/models/product_family_response.py` |

