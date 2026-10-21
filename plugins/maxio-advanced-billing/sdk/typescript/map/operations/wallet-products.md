<!-- Generated file — do not edit; regenerated with the SDK. -->

# WalletProducts — operations

Accessor: `client.walletProducts` · Source: `src/resources/wallet-products.ts` · 7 operations · Request and error types: namespace `WalletProducts`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### archiveWalletProduct

- **Signature**: `archiveWalletProduct(request: WalletProducts.ArchiveWalletProductRequest, options?: RequestOptions): ApiPromise<WalletProductResponse, WalletProducts.ArchiveWalletProductError>`
- **Wire**: `POST /wallet_products/{id}/archive.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletProducts.ArchiveWalletProductError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"walletErrorResponse12"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletProducts.ArchiveWalletProductRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `WalletProductResponse` | `walletProductResponseSchema` | `src/models/wallet-product-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### createWalletProduct

- **Signature**: `createWalletProduct(request?: WalletProducts.CreateWalletProductRequestParams, options?: RequestOptions): ApiPromise<WalletProductResponse, WalletProducts.CreateWalletProductError>`
- **Wire**: `POST /wallet_products.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletProducts.CreateWalletProductError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletProducts.CreateWalletProductRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateWalletProductRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateWalletProductRequest` | `createWalletProductRequestSchema` | `src/models/create-wallet-product-request.ts` |
| `WalletProductResponse` | `walletProductResponseSchema` | `src/models/wallet-product-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### listWalletProducts

- **Signature**: `listWalletProducts(request?: WalletProducts.ListWalletProductsRequest, options?: RequestOptions): ApiPromise<WalletProductsListResponse, WalletProducts.ListWalletProductsError>`
- **Wire**: `GET /wallet_products.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `WalletProductsListResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletProducts.ListWalletProductsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletProducts.ListWalletProductsRequest` (7):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `includeArchived` | `query` | `include_archived` | `boolean` | no | — |
| `status` | `query` | — | `Status1` | no | — |
| `q` | `query` | — | `string` | no | — |
| `sortBy` | `query` | `sort_by` | `SortBy1` | no | `SortBy1.Name` |
| `sortDirection` | `query` | `sort_direction` | `SortDirection` | no | `SortDirection.Asc` |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |

| Type | Schema value | Source |
| --- | --- | --- |
| `Status1` | `status1Schema` | `src/models/status1.ts` |
| `SortBy1` | `sortBy1Schema` | `src/models/sort-by1.ts` |
| `SortDirection` | `sortDirectionSchema` | `src/models/sort-direction.ts` |
| `WalletProductsListResponse` | `walletProductsListResponseSchema` | `src/models/wallet-products-list-response.ts` |

### readWalletProduct

- **Signature**: `readWalletProduct(request: WalletProducts.ReadWalletProductRequest, options?: RequestOptions): ApiPromise<WalletProductResponse, WalletProducts.ReadWalletProductError>`
- **Wire**: `GET /wallet_products/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `WalletProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletProducts.ReadWalletProductError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletProducts.ReadWalletProductRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `WalletProductResponse` | `walletProductResponseSchema` | `src/models/wallet-product-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### readWalletProductUsage

- **Signature**: `readWalletProductUsage(request: WalletProducts.ReadWalletProductUsageRequest, options?: RequestOptions): ApiPromise<WalletProductUsageResponse, WalletProducts.ReadWalletProductUsageError>`
- **Wire**: `GET /wallet_products/{id}/usage.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `WalletProductUsageResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletProducts.ReadWalletProductUsageError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletProducts.ReadWalletProductUsageRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `WalletProductUsageResponse` | `walletProductUsageResponseSchema` | `src/models/wallet-product-usage-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### unarchiveWalletProduct

- **Signature**: `unarchiveWalletProduct(request: WalletProducts.UnarchiveWalletProductRequest, options?: RequestOptions): ApiPromise<WalletProductResponse, WalletProducts.UnarchiveWalletProductError>`
- **Wire**: `POST /wallet_products/{id}/unarchive.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletProducts.UnarchiveWalletProductError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"walletErrorResponse12"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletProducts.UnarchiveWalletProductRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `WalletProductResponse` | `walletProductResponseSchema` | `src/models/wallet-product-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

### updateWalletProduct

- **Signature**: `updateWalletProduct(request: WalletProducts.UpdateWalletProductRequestParams, options?: RequestOptions): ApiPromise<WalletProductResponse, WalletProducts.UpdateWalletProductError>`
- **Wire**: `PUT /wallet_products/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `WalletProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `WalletProducts.UpdateWalletProductError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error403"` [403] no body · `"walletErrorResponse1"` [404] `WalletErrorResponse1` · `"walletErrorResponse12"` [422] `WalletErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `WalletProducts.UpdateWalletProductRequestParams` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `string` | yes |
| `body` | `body` | `UpdateWalletProductRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateWalletProductRequest` | `updateWalletProductRequestSchema` | `src/models/update-wallet-product-request.ts` |
| `WalletProductResponse` | `walletProductResponseSchema` | `src/models/wallet-product-response.ts` |
| `WalletErrorResponse1` | `walletErrorResponse1Schema` | `src/models/wallet-error-response1.ts` |

