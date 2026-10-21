<!-- Generated file — do not edit; regenerated with the SDK. -->

# WalletTransactions — operations

Accessor: `client.wallet_transactions` · Source: `maxio_advanced_billing/apis/wallet_transactions.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wallet_transactions.create_wallet_transaction

- **Route**: `POST /wallets/{wallet_id}/transactions.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_wallet_transaction(wallet_id: int, *, body: CreateWalletTransactionRequest | CreateWalletTransactionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wallet_id`
- **Params**: `wallet_id` — path · `body` — JSON body
- **Returns (parsed)**: `WalletTransactionResultResponse`
- **Returns (raw)**: `ApiResult[WalletTransactionResultResponse, CreateWalletTransactionErrorBody]`
- **Error**: `CreateWalletTransactionErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404, 422, 500, 503] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateWalletTransactionRequest` | `maxio_advanced_billing/models/create_wallet_transaction_request.py` |
| `CreateWalletTransactionRequestDict` | `maxio_advanced_billing/models/create_wallet_transaction_request.py` |
| `WalletTransactionResultResponse` | `maxio_advanced_billing/models/wallet_transaction_result_response.py` |
| `CreateWalletTransactionErrorBody` | `maxio_advanced_billing/errors/create_wallet_transaction_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallet_transactions.list_wallet_transactions

- **Route**: `GET /wallets/{wallet_id}/transactions.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_wallet_transactions(wallet_id: int, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wallet_id`
- **Params**: `wallet_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `WalletTransactionsListResponse`
- **Returns (raw)**: `ApiResult[WalletTransactionsListResponse, ListWalletTransactionsErrorBody]`
- **Error**: `ListWalletTransactionsErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `WalletTransactionsListResponse` | `maxio_advanced_billing/models/wallet_transactions_list_response.py` |
| `ListWalletTransactionsErrorBody` | `maxio_advanced_billing/errors/list_wallet_transactions_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

