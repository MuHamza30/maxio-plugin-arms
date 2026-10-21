<!-- Generated file — do not edit; regenerated with the SDK. -->

# WalletPurchases — operations

Accessor: `client.walletPurchases` · Source: `src/resources/wallet-purchases.ts` · 2 operations · Request and error types: namespace `WalletPurchases`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createWalletPurchase

- **Signature**: `createWalletPurchase(request: WalletPurchases.CreateWalletPurchaseRequestParams, options?: RequestOptions): ApiPromise<WalletPurchaseResultResponse, WalletPurchases.CreateWalletPurchaseError>`
- **Wire**: `POST /wallets/{wallet_id}/purchases.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletPurchaseResultResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletPurchases.CreateWalletPurchaseError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"walletErrorResponse12"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletPurchases.CreateWalletPurchaseRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `walletId` | `path` | `wallet_id` | `number` | yes |
| `body` | `body` | — | `CreateWalletPurchaseRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateWalletPurchaseRequest` | `createWalletPurchaseRequestSchema` | `src/models/create-wallet-purchase-request.ts` |
| `WalletPurchaseResultResponse` | `walletPurchaseResultResponseSchema` | `src/models/wallet-purchase-result-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### previewWalletPurchase

- **Signature**: `previewWalletPurchase(request: WalletPurchases.PreviewWalletPurchaseRequest, options?: RequestOptions): ApiPromise<WalletPurchasePreviewResponse, WalletPurchases.PreviewWalletPurchaseError>`
- **Wire**: `POST /wallets/{wallet_id}/purchases/preview.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletPurchasePreviewResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletPurchases.PreviewWalletPurchaseError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"walletErrorResponse12"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletPurchases.PreviewWalletPurchaseRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `walletId` | `path` | `wallet_id` | `number` | yes |
| `body` | `body` | — | `CreateWalletPurchaseRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateWalletPurchaseRequest` | `createWalletPurchaseRequestSchema` | `src/models/create-wallet-purchase-request.ts` |
| `WalletPurchasePreviewResponse` | `walletPurchasePreviewResponseSchema` | `src/models/wallet-purchase-preview-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

