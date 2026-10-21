<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProductPricePoints — operations

Accessor: `client.productPricePoints` · Source: `src/resources/product-price-points.ts` · 11 operations · Request and error types: namespace `ProductPricePoints`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### archiveProductPricePoint

- **Provider notes (Maxio)**: `knowledge/operations/product-price-points.md#archiveproductpricepoint`
- **Signature**: `archiveProductPricePoint(request: ProductPricePoints.ArchiveProductPricePointRequest, options?: RequestOptions): ApiPromise<ProductPricePointResponse, ProductPricePoints.ArchiveProductPricePointError>`
- **Wire**: `DELETE /products/{product_id}/price_points/{price_point_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProductPricePointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductPricePoints.ArchiveProductPricePointError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductPricePoints.ArchiveProductPricePointRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `ProductIdModel` | yes |
| `pricePointId` | `path` | `price_point_id` | `PricePointIdModel` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductIdModel` | `productIdModelSchema` | `src/models/unions/product-id-model.ts` |
| `PricePointIdModel` | `pricePointIdModelSchema` | `src/models/unions/price-point-id-model.ts` |
| `ProductPricePointResponse` | `productPricePointResponseSchema` | `src/models/product-price-point-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### bulkCreateProductPricePoints

- **Signature**: `bulkCreateProductPricePoints(request: ProductPricePoints.BulkCreateProductPricePointsRequestParams, options?: RequestOptions): ApiPromise<BulkCreateProductPricePointsResponse, ProductPricePoints.BulkCreateProductPricePointsError>`
- **Wire**: `POST /products/{product_id}/price_points/bulk.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `BulkCreateProductPricePointsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductPricePoints.BulkCreateProductPricePointsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error422"` [422] `Record<string, unknown>` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductPricePoints.BulkCreateProductPricePointsRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |
| `body` | `body` | — | `BulkCreateProductPricePointsRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `BulkCreateProductPricePointsRequest` | `bulkCreateProductPricePointsRequestSchema` | `src/models/bulk-create-product-price-points-request.ts` |
| `BulkCreateProductPricePointsResponse` | `bulkCreateProductPricePointsResponseSchema` | `src/models/bulk-create-product-price-points-response.ts` |

### createProductCurrencyPrices

- **Provider rules (Maxio)**: Send `price` in major units of the currency, not cents, although the price point itself is in cents (R4). Send a `baseline` row, plus a `trial` and an `initial` row when the price point has a trial or an initial charge. Notes: `knowledge/operations/product-price-points.md#createproductcurrencyprices`
- **Signature**: `createProductCurrencyPrices(request: ProductPricePoints.CreateProductCurrencyPricesRequestParams, options?: RequestOptions): ApiPromise<CurrencyPricesResponse, ProductPricePoints.CreateProductCurrencyPricesError>`
- **Wire**: `POST /product_price_points/{product_price_point_id}/currency_prices.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CurrencyPricesResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductPricePoints.CreateProductCurrencyPricesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorArrayMapResponse1"` [422] `ErrorArrayMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductPricePoints.CreateProductCurrencyPricesRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productPricePointId` | `path` | `product_price_point_id` | `number` | yes |
| `body` | `body` | — | `CreateProductCurrencyPricesRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateProductCurrencyPricesRequest` | `createProductCurrencyPricesRequestSchema` | `src/models/create-product-currency-prices-request.ts` |
| `CurrencyPricesResponse` | `currencyPricesResponseSchema` | `src/models/currency-prices-response.ts` |
| `ErrorArrayMapResponse1` | `errorArrayMapResponse1Schema` | `src/models/error-array-map-response1.ts` |

### createProductPricePoint

- **Provider rules (Maxio)**: Settle `interval`, the trial fields and `initial_charge_in_cents` now: `updateProductPricePoint` takes only `price_in_cents` and `handle`. Promote the price point if new signups should get it (D9). Notes: `knowledge/operations/product-price-points.md#createproductpricepoint`
- **Signature**: `createProductPricePoint(request: ProductPricePoints.CreateProductPricePointRequestParams, options?: RequestOptions): ApiPromise<ProductPricePointResponse, ProductPricePoints.CreateProductPricePointError>`
- **Wire**: `POST /products/{product_id}/price_points.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProductPricePointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductPricePoints.CreateProductPricePointError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"productPricePointErrorResponse1"` [422] `ProductPricePointErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductPricePoints.CreateProductPricePointRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `ProductIdModel` | yes |
| `body` | `body` | — | `CreateProductPricePointRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductIdModel` | `productIdModelSchema` | `src/models/unions/product-id-model.ts` |
| `CreateProductPricePointRequest` | `createProductPricePointRequestSchema` | `src/models/create-product-price-point-request.ts` |
| `ProductPricePointResponse` | `productPricePointResponseSchema` | `src/models/product-price-point-response.ts` |
| `ProductPricePointErrorResponse1` | `productPricePointErrorResponse1Schema` | `src/models/product-price-point-error-response1.ts` |

### listAllProductPricePoints

- **Signature**: `listAllProductPricePoints(request: ProductPricePoints.ListAllProductPricePointsRequest, options?: RequestOptions): ApiPromise<ListProductPricePointsResponse, ProductPricePoints.ListAllProductPricePointsError>`
- **Wire**: `GET /products_price_points.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListProductPricePointsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductPricePoints.ListAllProductPricePointsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductPricePoints.ListAllProductPricePointsRequest` (5):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `direction` | `query` | — | `SortingDirection` | no | — |
| `filter` | `query` | — | `ListPricePointsFilter` | no | — |
| `include` | `query` | — | `ListProductsPricePointsInclude` | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |

| Type | Schema value | Source |
| --- | --- | --- |
| `SortingDirection` | `sortingDirectionSchema` | `src/models/sorting-direction.ts` |
| `ListPricePointsFilter` | `listPricePointsFilterSchema` | `src/models/list-price-points-filter.ts` |
| `ListProductsPricePointsInclude` | `listProductsPricePointsIncludeSchema` | `src/models/list-products-price-points-include.ts` |
| `ListProductPricePointsResponse` | `listProductPricePointsResponseSchema` | `src/models/list-product-price-points-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listProductPricePoints

- **Provider rules (Maxio)**: Never take `[0]` as the default; use `filter[type]=default` or the product's `default_product_price_point_id` (R9). Request at most 200 per page (R8). Notes: `knowledge/operations/product-price-points.md#listproductpricepoints`
- **Signature**: `listProductPricePoints(request: ProductPricePoints.ListProductPricePointsRequest, options?: RequestOptions): ApiPromise<ListProductPricePointsResponse, ApiError>`
- **Wire**: `GET /products/{product_id}/price_points.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListProductPricePointsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ProductPricePoints.ListProductPricePointsRequest` (6):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `ProductIdModel` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `10` |
| `currencyPrices` | `query` | `currency_prices` | `boolean` | no | — |
| `filterType` | `query` | `filter[type]` | `PricePointType[]` | no | — |
| `archived` | `query` | — | `boolean` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductIdModel` | `productIdModelSchema` | `src/models/unions/product-id-model.ts` |
| `PricePointType` | `pricePointTypeSchema` | `src/models/price-point-type.ts` |
| `ListProductPricePointsResponse` | `listProductPricePointsResponseSchema` | `src/models/list-product-price-points-response.ts` |

### promoteProductPricePointToDefault

- **Provider notes (Maxio)**: `knowledge/operations/product-price-points.md#promoteproductpricepointtodefault`
- **Signature**: `promoteProductPricePointToDefault(request: ProductPricePoints.PromoteProductPricePointToDefaultRequest, options?: RequestOptions): ApiPromise<ProductResponse, ApiError>`
- **Wire**: `PATCH /products/{product_id}/price_points/{price_point_id}/default.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ProductPricePoints.PromoteProductPricePointToDefaultRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |
| `pricePointId` | `path` | `price_point_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductResponse` | `productResponseSchema` | `src/models/product-response.ts` |

### readProductPricePoint

- **Signature**: `readProductPricePoint(request: ProductPricePoints.ReadProductPricePointRequest, options?: RequestOptions): ApiPromise<ProductPricePointResponse, ApiError>`
- **Wire**: `GET /products/{product_id}/price_points/{price_point_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ProductPricePointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ProductPricePoints.ReadProductPricePointRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `ProductIdModel` | yes |
| `pricePointId` | `path` | `price_point_id` | `PricePointIdModel` | yes |
| `currencyPrices` | `query` | `currency_prices` | `boolean` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductIdModel` | `productIdModelSchema` | `src/models/unions/product-id-model.ts` |
| `PricePointIdModel` | `pricePointIdModelSchema` | `src/models/unions/price-point-id-model.ts` |
| `ProductPricePointResponse` | `productPricePointResponseSchema` | `src/models/product-price-point-response.ts` |

### unarchiveProductPricePoint

- **Signature**: `unarchiveProductPricePoint(request: ProductPricePoints.UnarchiveProductPricePointRequest, options?: RequestOptions): ApiPromise<ProductPricePointResponse, ApiError>`
- **Wire**: `PATCH /products/{product_id}/price_points/{price_point_id}/unarchive.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProductPricePointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ProductPricePoints.UnarchiveProductPricePointRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |
| `pricePointId` | `path` | `price_point_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductPricePointResponse` | `productPricePointResponseSchema` | `src/models/product-price-point-response.ts` |

### updateProductCurrencyPrices

- **Signature**: `updateProductCurrencyPrices(request: ProductPricePoints.UpdateProductCurrencyPricesRequest, options?: RequestOptions): ApiPromise<CurrencyPricesResponse, ProductPricePoints.UpdateProductCurrencyPricesError>`
- **Wire**: `PUT /product_price_points/{product_price_point_id}/currency_prices.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CurrencyPricesResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductPricePoints.UpdateProductCurrencyPricesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorArrayMapResponse1"` [422] `ErrorArrayMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductPricePoints.UpdateProductCurrencyPricesRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productPricePointId` | `path` | `product_price_point_id` | `number` | yes |
| `body` | `body` | — | `UpdateCurrencyPricesRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateCurrencyPricesRequest` | `updateCurrencyPricesRequestSchema` | `src/models/update-currency-prices-request.ts` |
| `CurrencyPricesResponse` | `currencyPricesResponseSchema` | `src/models/currency-prices-response.ts` |
| `ErrorArrayMapResponse1` | `errorArrayMapResponse1Schema` | `src/models/error-array-map-response1.ts` |

### updateProductPricePoint

- **Provider rules (Maxio)**: This reprices every subscription on the price point (inferred). For new customers only, create and promote a new price point instead (D9). Notes: `knowledge/operations/product-price-points.md#updateproductpricepoint`
- **Signature**: `updateProductPricePoint(request: ProductPricePoints.UpdateProductPricePointRequestParams, options?: RequestOptions): ApiPromise<ProductPricePointResponse, ApiError>`
- **Wire**: `PUT /products/{product_id}/price_points/{price_point_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProductPricePointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ProductPricePoints.UpdateProductPricePointRequestParams` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `ProductIdModel` | yes |
| `pricePointId` | `path` | `price_point_id` | `PricePointIdModel` | yes |
| `body` | `body` | — | `UpdateProductPricePointRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductIdModel` | `productIdModelSchema` | `src/models/unions/product-id-model.ts` |
| `PricePointIdModel` | `pricePointIdModelSchema` | `src/models/unions/price-point-id-model.ts` |
| `UpdateProductPricePointRequest` | `updateProductPricePointRequestSchema` | `src/models/update-product-price-point-request.ts` |
| `ProductPricePointResponse` | `productPricePointResponseSchema` | `src/models/product-price-point-response.ts` |

