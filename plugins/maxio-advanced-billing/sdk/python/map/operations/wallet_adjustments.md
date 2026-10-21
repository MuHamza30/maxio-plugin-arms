<!-- Generated file — do not edit; regenerated with the SDK. -->

# WalletAdjustments — operations

Accessor: `client.wallet_adjustments` · Source: `maxio_advanced_billing/apis/wallet_adjustments.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wallet_adjustments.create_wallet_adjustment

- **Route**: `POST /wallets/{wallet_id}/adjustments.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_wallet_adjustment(wallet_id: int, *, body: CreateWalletAdjustmentRequest | CreateWalletAdjustmentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wallet_id`
- **Params**: `wallet_id` — path · `body` — JSON body
- **Returns (parsed)**: `WalletGrantResultResponse`
- **Returns (raw)**: `ApiResult[WalletGrantResultResponse, CreateWalletAdjustmentErrorBody]`
- **Error**: `CreateWalletAdjustmentErrorBody` — **Case A (typed)**
- **Error arms**: `WalletErrorResponse1` [404, 409, 422] · `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateWalletAdjustmentRequest` | `maxio_advanced_billing/models/create_wallet_adjustment_request.py` |
| `CreateWalletAdjustmentRequestDict` | `maxio_advanced_billing/models/create_wallet_adjustment_request.py` |
| `WalletGrantResultResponse` | `maxio_advanced_billing/models/wallet_grant_result_response.py` |
| `CreateWalletAdjustmentErrorBody` | `maxio_advanced_billing/errors/create_wallet_adjustment_error.py` |
| `WalletErrorResponse1` | `maxio_advanced_billing/models/wallet_error_response1.py` |

