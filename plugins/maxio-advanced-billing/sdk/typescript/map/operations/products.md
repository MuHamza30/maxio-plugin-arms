<!-- Generated file — do not edit; regenerated with the SDK. -->

# Products — operations

Accessor: `client.products` · Source: `src/resources/products.ts` · 6 operations · Request and error types: namespace `Products`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### archiveProduct

- **Provider notes (Maxio)**: `knowledge/operations/products.md#archiveproduct`
- **Signature**: `archiveProduct(request: Products.ArchiveProductRequest, options?: RequestOptions): ApiPromise<ProductResponse, Products.ArchiveProductError>`
- **Wire**: `DELETE /products/{product_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Products.ArchiveProductError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Products.ArchiveProductRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductResponse` | `productResponseSchema` | `src/models/product-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createProduct

- **Provider rules (Maxio)**: Set a `handle` (R6). For yearly billing send `interval: 12` with `interval_unit: "month"`. With a trial, set `trial_type` on purpose (L4). On new-Catalog sites never send `auto_create_signup_page`. Notes: `knowledge/operations/products.md#createproduct`
- **Signature**: `createProduct(request: Products.CreateProductRequest, options?: RequestOptions): ApiPromise<ProductResponse, Products.CreateProductError>`
- **Wire**: `POST /product_families/{product_family_id}/products.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Products.CreateProductError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Products.CreateProductRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `string` | yes |
| `body` | `body` | — | `CreateOrUpdateProductRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateOrUpdateProductRequest` | `createOrUpdateProductRequestSchema` | `src/models/create-or-update-product-request.ts` |
| `ProductResponse` | `productResponseSchema` | `src/models/product-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listProducts

- **Signature**: `listProducts(request: Products.ListProductsRequest, options?: RequestOptions): ApiPromise<ProductResponse[], ApiError>`
- **Wire**: `GET /products.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ProductResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Products.ListProductsRequest` (11):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `dateField` | `query` | `date_field` | `BasicDateField` | no | — |
| `filter` | `query` | — | `ListProductsFilter` | no | — |
| `endDate` | `query` | `end_date` | `string` (date) | no | — |
| `endDatetime` | `query` | `end_datetime` | `Date` (date-time) | no | — |
| `startDate` | `query` | `start_date` | `string` (date) | no | — |
| `startDatetime` | `query` | `start_datetime` | `Date` (date-time) | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `includeArchived` | `query` | `include_archived` | `boolean` | no | — |
| `include` | `query` | — | `ListProductsInclude` | no | — |
| `includeFeatures` | `query` | `include_features` | `boolean` | no | `false` |

| Type | Schema value | Source |
| --- | --- | --- |
| `BasicDateField` | `basicDateFieldSchema` | `src/models/basic-date-field.ts` |
| `ListProductsFilter` | `listProductsFilterSchema` | `src/models/list-products-filter.ts` |
| `ListProductsInclude` | `listProductsIncludeSchema` | `src/models/list-products-include.ts` |
| `ProductResponse` | `productResponseSchema` | `src/models/product-response.ts` |

### readProduct

- **Signature**: `readProduct(request: Products.ReadProductRequest, options?: RequestOptions): ApiPromise<ProductResponse, ApiError>`
- **Wire**: `GET /products/{product_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Products.ReadProductRequest` (2):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes | — |
| `includeFeatures` | `query` | `include_features` | `boolean` | no | `false` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductResponse` | `productResponseSchema` | `src/models/product-response.ts` |

### readProductByHandle

- **Provider rules (Maxio)**: Pass the bare handle; never a `handle:` prefix in this path. Notes: `knowledge/operations/products.md#readproductbyhandle`
- **Signature**: `readProductByHandle(request: Products.ReadProductByHandleRequest, options?: RequestOptions): ApiPromise<ProductResponse, ApiError>`
- **Wire**: `GET /products/handle/{api_handle}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Products.ReadProductByHandleRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `apiHandle` | `path` | `api_handle` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductResponse` | `productResponseSchema` | `src/models/product-response.ts` |

### updateProduct

- **Provider rules (Maxio)**: Treat every call as creating a new price point and making it the product's default; never use it to change a price (D9). The body requires the price and interval fields: send the current values unchanged. Notes: `knowledge/operations/products.md#updateproduct`
- **Signature**: `updateProduct(request: Products.UpdateProductRequest, options?: RequestOptions): ApiPromise<ProductResponse, Products.UpdateProductError>`
- **Wire**: `PUT /products/{product_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProductResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Products.UpdateProductError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Products.UpdateProductRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productId` | `path` | `product_id` | `number` | yes |
| `body` | `body` | — | `CreateOrUpdateProductRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateOrUpdateProductRequest` | `createOrUpdateProductRequestSchema` | `src/models/create-or-update-product-request.ts` |
| `ProductResponse` | `productResponseSchema` | `src/models/product-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

