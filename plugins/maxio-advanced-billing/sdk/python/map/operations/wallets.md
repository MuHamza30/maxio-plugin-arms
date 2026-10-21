<!-- Generated file — do not edit; regenerated with the SDK. -->

# Wallets — operations

Accessor: `client.wallets` · Source: `maxio_advanced_billing/apis/wallets.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wallets.archive_wallet

- **Route**: `DELETE /wallets/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def archive_wallet(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `WalletResponse`
- **Returns (raw)**: `ApiResult[WalletResponse, ArchiveWalletErrorBody]`
- **Error**: `ArchiveWalletErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `WalletResponse` | `maxio_advanced_billing/models/wallet_response.py` |
| `ArchiveWalletErrorBody` | `maxio_advanced_billing/errors/archive_wallet_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallets.create_wallet

- **Route**: `POST /wallets.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_wallet(*, body: CreateWalletRequest | CreateWalletRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WalletResponse`
- **Returns (raw)**: `ApiResult[WalletResponse, CreateWalletErrorBody]`
- **Error**: `CreateWalletErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404, 422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateWalletRequest` | `maxio_advanced_billing/models/create_wallet_request.py` |
| `CreateWalletRequestDict` | `maxio_advanced_billing/models/create_wallet_request.py` |
| `WalletResponse` | `maxio_advanced_billing/models/wallet_response.py` |
| `CreateWalletErrorBody` | `maxio_advanced_billing/errors/create_wallet_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallets.list_wallets

- **Route**: `GET /wallets.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_wallets(*, page: int | None = 1, per_page: int | None = 20, subscription_id: int | None = None, status: Status2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query · `subscription_id` — query · `status` — query
- **Returns (parsed)**: `WalletsListResponse`
- **Returns (raw)**: `ApiResult[WalletsListResponse, ListWalletsErrorBody]`
- **Error**: `ListWalletsErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `Status2OrStr` | `maxio_advanced_billing/models/enums/status2.py` |
| `WalletsListResponse` | `maxio_advanced_billing/models/wallets_list_response.py` |
| `ListWalletsErrorBody` | `maxio_advanced_billing/errors/list_wallets_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallets.read_wallet

- **Route**: `GET /wallets/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_wallet(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `WalletResponse`
- **Returns (raw)**: `ApiResult[WalletResponse, ReadWalletErrorBody]`
- **Error**: `ReadWalletErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `WalletResponse` | `maxio_advanced_billing/models/wallet_response.py` |
| `ReadWalletErrorBody` | `maxio_advanced_billing/errors/read_wallet_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallets.update_wallet

- **Route**: `PATCH /wallets/{id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_wallet(id_: int, *, body: UpdateWalletRequest | UpdateWalletRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `WalletResponse`
- **Returns (raw)**: `ApiResult[WalletResponse, UpdateWalletErrorBody]`
- **Error**: `UpdateWalletErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404, 422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateWalletRequest` | `maxio_advanced_billing/models/update_wallet_request.py` |
| `UpdateWalletRequestDict` | `maxio_advanced_billing/models/update_wallet_request.py` |
| `WalletResponse` | `maxio_advanced_billing/models/wallet_response.py` |
| `UpdateWalletErrorBody` | `maxio_advanced_billing/errors/update_wallet_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

