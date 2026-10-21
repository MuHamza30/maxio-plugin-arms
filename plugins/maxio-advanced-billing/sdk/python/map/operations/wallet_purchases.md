<!-- Generated file — do not edit; regenerated with the SDK. -->

# WalletPurchases — operations

Accessor: `client.wallet_purchases` · Source: `maxio_advanced_billing/apis/wallet_purchases.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wallet_purchases.create_wallet_purchase

- **Route**: `POST /wallets/{wallet_id}/purchases.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_wallet_purchase(wallet_id: int, *, body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wallet_id`
- **Params**: `wallet_id` — path · `body` — JSON body
- **Returns (parsed)**: `WalletPurchaseResultResponse`
- **Returns (raw)**: `ApiResult[WalletPurchaseResultResponse, CreateWalletPurchaseErrorBody]`
- **Error**: `CreateWalletPurchaseErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404, 422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateWalletPurchaseRequest` | `maxio_advanced_billing/models/create_wallet_purchase_request.py` |
| `CreateWalletPurchaseRequestDict` | `maxio_advanced_billing/models/create_wallet_purchase_request.py` |
| `WalletPurchaseResultResponse` | `maxio_advanced_billing/models/wallet_purchase_result_response.py` |
| `CreateWalletPurchaseErrorBody` | `maxio_advanced_billing/errors/create_wallet_purchase_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

### client.wallet_purchases.preview_wallet_purchase

- **Route**: `POST /wallets/{wallet_id}/purchases/preview.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def preview_wallet_purchase(wallet_id: int, *, body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wallet_id`
- **Params**: `wallet_id` — path · `body` — JSON body
- **Returns (parsed)**: `WalletPurchasePreviewResponse`
- **Returns (raw)**: `ApiResult[WalletPurchasePreviewResponse, PreviewWalletPurchaseErrorBody]`
- **Error**: `PreviewWalletPurchaseErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404, 422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateWalletPurchaseRequest` | `maxio_advanced_billing/models/create_wallet_purchase_request.py` |
| `CreateWalletPurchaseRequestDict` | `maxio_advanced_billing/models/create_wallet_purchase_request.py` |
| `WalletPurchasePreviewResponse` | `maxio_advanced_billing/models/wallet_purchase_preview_response.py` |
| `PreviewWalletPurchaseErrorBody` | `maxio_advanced_billing/errors/preview_wallet_purchase_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

