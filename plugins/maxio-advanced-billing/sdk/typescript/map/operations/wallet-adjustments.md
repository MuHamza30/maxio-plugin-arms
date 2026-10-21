<!-- Generated file — do not edit; regenerated with the SDK. -->

# WalletAdjustments — operations

Accessor: `client.walletAdjustments` · Source: `src/resources/wallet-adjustments.ts` · 1 operation · Request and error types: namespace `WalletAdjustments`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createWalletAdjustment

- **Signature**: `createWalletAdjustment(request: WalletAdjustments.CreateWalletAdjustmentRequestParams, options?: RequestOptions): ApiPromise<WalletGrantResultResponse, WalletAdjustments.CreateWalletAdjustmentError>`
- **Wire**: `POST /wallets/{wallet_id}/adjustments.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletGrantResultResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletAdjustments.CreateWalletAdjustmentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"walletErrorResponse12"` [409] `WalletErrorResponse1` · `"walletErrorResponse13"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletAdjustments.CreateWalletAdjustmentRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `walletId` | `path` | `wallet_id` | `number` | yes |
| `body` | `body` | — | `CreateWalletAdjustmentRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateWalletAdjustmentRequest` | `createWalletAdjustmentRequestSchema` | `src/models/create-wallet-adjustment-request.ts` |
| `WalletGrantResultResponse` | `walletGrantResultResponseSchema` | `src/models/wallet-grant-result-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

