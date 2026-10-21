<!-- Generated file — do not edit; regenerated with the SDK. -->

# WalletProducts — operations

Accessor: `client.wallet_products` · Source: `maxio_advanced_billing/apis/wallet_products.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wallet_products.archive_wallet_product

- **Route**: `POST /wallet_products/{id}/archive.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def archive_wallet_product(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `WalletProductResponse`
- **Returns (raw)**: `ApiResult[WalletProductResponse, ArchiveWalletProductErrorBody]`
- **Error**: `ArchiveWalletProductErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404, 422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `WalletProductResponse` | `maxio_advanced_billing/models/wallet_product_response.py` |
| `ArchiveWalletProductErrorBody` | `maxio_advanced_billing/errors/archive_wallet_product_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallet_products.create_wallet_product

- **Route**: `POST /wallet_products.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_wallet_product(*, body: CreateWalletProductRequest | CreateWalletProductRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WalletProductResponse`
- **Returns (raw)**: `ApiResult[WalletProductResponse, CreateWalletProductErrorBody]`
- **Error**: `CreateWalletProductErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateWalletProductRequest` | `maxio_advanced_billing/models/create_wallet_product_request.py` |
| `CreateWalletProductRequestDict` | `maxio_advanced_billing/models/create_wallet_product_request.py` |
| `WalletProductResponse` | `maxio_advanced_billing/models/wallet_product_response.py` |
| `CreateWalletProductErrorBody` | `maxio_advanced_billing/errors/create_wallet_product_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallet_products.list_wallet_products

- **Route**: `GET /wallet_products.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_wallet_products(*, include_archived: bool | None = None, status: Status1OrStr | None = None, q: str | None = None, sort_by: SortBy1OrStr | None = SortBy1.NAME, sort_direction: SortDirectionOrStr | None = SortDirection.ASC, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include_archived` — query · `status` — query · `q` — query · `sort_by` — query · `sort_direction` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `WalletProductsListResponse`
- **Returns (raw)**: `ApiResult[WalletProductsListResponse, ListWalletProductsErrorBody]`
- **Error**: `ListWalletProductsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `Status1OrStr` | `maxio_advanced_billing/models/enums/status1.py` |
| `SortBy1OrStr` | `maxio_advanced_billing/models/enums/sort_by1.py` |
| `SortDirectionOrStr` | `maxio_advanced_billing/models/enums/sort_direction.py` |
| `WalletProductsListResponse` | `maxio_advanced_billing/models/wallet_products_list_response.py` |
| `ListWalletProductsErrorBody` | `maxio_advanced_billing/errors/list_wallet_products_error.py` |

### client.wallet_products.read_wallet_product

- **Route**: `GET /wallet_products/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_wallet_product(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `WalletProductResponse`
- **Returns (raw)**: `ApiResult[WalletProductResponse, ReadWalletProductErrorBody]`
- **Error**: `ReadWalletProductErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `WalletProductResponse` | `maxio_advanced_billing/models/wallet_product_response.py` |
| `ReadWalletProductErrorBody` | `maxio_advanced_billing/errors/read_wallet_product_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallet_products.read_wallet_product_usage

- **Route**: `GET /wallet_products/{id}/usage.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_wallet_product_usage(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `WalletProductUsageResponse`
- **Returns (raw)**: `ApiResult[WalletProductUsageResponse, ReadWalletProductUsageErrorBody]`
- **Error**: `ReadWalletProductUsageErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `WalletProductUsageResponse` | `maxio_advanced_billing/models/wallet_product_usage_response.py` |
| `ReadWalletProductUsageErrorBody` | `maxio_advanced_billing/errors/read_wallet_product_usage_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallet_products.unarchive_wallet_product

- **Route**: `POST /wallet_products/{id}/unarchive.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def unarchive_wallet_product(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `WalletProductResponse`
- **Returns (raw)**: `ApiResult[WalletProductResponse, UnarchiveWalletProductErrorBody]`
- **Error**: `UnarchiveWalletProductErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404, 422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `WalletProductResponse` | `maxio_advanced_billing/models/wallet_product_response.py` |
| `UnarchiveWalletProductErrorBody` | `maxio_advanced_billing/errors/unarchive_wallet_product_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallet_products.update_wallet_product

- **Route**: `PUT /wallet_products/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_wallet_product(id_: str, *, body: UpdateWalletProductRequest | UpdateWalletProductRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `WalletProductResponse`
- **Returns (raw)**: `ApiResult[WalletProductResponse, UpdateWalletProductErrorBody]`
- **Error**: `UpdateWalletProductErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404, 422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateWalletProductRequest` | `maxio_advanced_billing/models/update_wallet_product_request.py` |
| `UpdateWalletProductRequestDict` | `maxio_advanced_billing/models/update_wallet_product_request.py` |
| `WalletProductResponse` | `maxio_advanced_billing/models/wallet_product_response.py` |
| `UpdateWalletProductErrorBody` | `maxio_advanced_billing/errors/update_wallet_product_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

