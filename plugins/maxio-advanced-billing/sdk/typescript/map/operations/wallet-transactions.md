<!-- Generated file — do not edit; regenerated with the SDK. -->

# WalletTransactions — operations

Accessor: `client.walletTransactions` · Source: `src/resources/wallet-transactions.ts` · 2 operations · Request and error types: namespace `WalletTransactions`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createWalletTransaction

- **Signature**: `createWalletTransaction(request: WalletTransactions.CreateWalletTransactionRequestParams, options?: RequestOptions): ApiPromise<WalletTransactionResultResponse, WalletTransactions.CreateWalletTransactionError>`
- **Wire**: `POST /wallets/{wallet_id}/transactions.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletTransactionResultResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletTransactions.CreateWalletTransactionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"walletErrorResponse12"` [422] `WalletErrorResponse1` · `"walletErrorResponse13"` [500] `WalletErrorResponse1` · `"walletErrorResponse14"` [503] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletTransactions.CreateWalletTransactionRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `walletId` | `path` | `wallet_id` | `number` | yes |
| `body` | `body` | — | `CreateWalletTransactionRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateWalletTransactionRequest` | `createWalletTransactionRequestSchema` | `src/models/create-wallet-transaction-request.ts` |
| `WalletTransactionResultResponse` | `walletTransactionResultResponseSchema` | `src/models/wallet-transaction-result-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### listWalletTransactions

- **Signature**: `listWalletTransactions(request: WalletTransactions.ListWalletTransactionsRequest, options?: RequestOptions): ApiPromise<WalletTransactionsListResponse, WalletTransactions.ListWalletTransactionsError>`
- **Wire**: `GET /wallets/{wallet_id}/transactions.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `WalletTransactionsListResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletTransactions.ListWalletTransactionsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletTransactions.ListWalletTransactionsRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `walletId` | `path` | `wallet_id` | `number` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |

| Type | Schema value | Source |
| --- | --- | --- |
| `WalletTransactionsListResponse` | `walletTransactionsListResponseSchema` | `src/models/wallet-transactions-list-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

