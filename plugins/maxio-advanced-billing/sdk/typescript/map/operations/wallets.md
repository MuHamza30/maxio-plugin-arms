<!-- Generated file — do not edit; regenerated with the SDK. -->

# Wallets — operations

Accessor: `client.wallets` · Source: `src/resources/wallets.ts` · 5 operations · Request and error types: namespace `Wallets`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### archiveWallet

- **Signature**: `archiveWallet(request: Wallets.ArchiveWalletRequest, options?: RequestOptions): ApiPromise<WalletResponse, Wallets.ArchiveWalletError>`
- **Wire**: `DELETE /wallets/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Wallets.ArchiveWalletError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Wallets.ArchiveWalletRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `WalletResponse` | `walletResponseSchema` | `src/models/wallet-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### createWallet

- **Signature**: `createWallet(request?: Wallets.CreateWalletRequestParams, options?: RequestOptions): ApiPromise<WalletResponse, Wallets.CreateWalletError>`
- **Wire**: `POST /wallets.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Wallets.CreateWalletError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"walletErrorResponse12"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Wallets.CreateWalletRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateWalletRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateWalletRequest` | `createWalletRequestSchema` | `src/models/create-wallet-request.ts` |
| `WalletResponse` | `walletResponseSchema` | `src/models/wallet-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### listWallets

- **Signature**: `listWallets(request?: Wallets.ListWalletsRequest, options?: RequestOptions): ApiPromise<WalletsListResponse, Wallets.ListWalletsError>`
- **Wire**: `GET /wallets.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `WalletsListResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Wallets.ListWalletsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Wallets.ListWalletsRequest` (4):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `subscriptionId` | `query` | `subscription_id` | `number` | no | — |
| `status` | `query` | — | `Status2` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `Status2` | `status2Schema` | `src/models/status2.ts` |
| `WalletsListResponse` | `walletsListResponseSchema` | `src/models/wallets-list-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### readWallet

- **Signature**: `readWallet(request: Wallets.ReadWalletRequest, options?: RequestOptions): ApiPromise<WalletResponse, Wallets.ReadWalletError>`
- **Wire**: `GET /wallets/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `WalletResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Wallets.ReadWalletError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Wallets.ReadWalletRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `WalletResponse` | `walletResponseSchema` | `src/models/wallet-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### updateWallet

- **Signature**: `updateWallet(request: Wallets.UpdateWalletRequestParams, options?: RequestOptions): ApiPromise<WalletResponse, Wallets.UpdateWalletError>`
- **Wire**: `PATCH /wallets/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Wallets.UpdateWalletError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"walletErrorResponse12"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Wallets.UpdateWalletRequestParams` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |
| `body` | `body` | `UpdateWalletRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateWalletRequest` | `updateWalletRequestSchema` | `src/models/update-wallet-request.ts` |
| `WalletResponse` | `walletResponseSchema` | `src/models/wallet-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

