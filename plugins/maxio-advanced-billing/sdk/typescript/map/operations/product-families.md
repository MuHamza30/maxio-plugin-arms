<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProductFamilies — operations

Accessor: `client.productFamilies` · Source: `src/resources/product-families.ts` · 4 operations · Request and error types: namespace `ProductFamilies`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createProductFamily

- **Signature**: `createProductFamily(request: ProductFamilies.CreateProductFamilyRequestParams, options?: RequestOptions): ApiPromise<ProductFamilyResponse, ProductFamilies.CreateProductFamilyError>`
- **Wire**: `POST /product_families.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ProductFamilyResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductFamilies.CreateProductFamilyError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductFamilies.CreateProductFamilyRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateProductFamilyRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateProductFamilyRequest` | `createProductFamilyRequestSchema` | `src/models/create-product-family-request.ts` |
| `ProductFamilyResponse` | `productFamilyResponseSchema` | `src/models/product-family-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listProductFamilies

- **Signature**: `listProductFamilies(request: ProductFamilies.ListProductFamiliesRequest, options?: RequestOptions): ApiPromise<ProductFamilyResponse[], ApiError>`
- **Wire**: `GET /product_families.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ProductFamilyResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ProductFamilies.ListProductFamiliesRequest` (5):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `dateField` | `query` | `date_field` | `BasicDateField` | no |
| `startDate` | `query` | `start_date` | `string` (date) | no |
| `endDate` | `query` | `end_date` | `string` (date) | no |
| `startDatetime` | `query` | `start_datetime` | `Date` (date-time) | no |
| `endDatetime` | `query` | `end_datetime` | `Date` (date-time) | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `BasicDateField` | `basicDateFieldSchema` | `src/models/basic-date-field.ts` |
| `ProductFamilyResponse` | `productFamilyResponseSchema` | `src/models/product-family-response.ts` |

### listProductsForProductFamily

- **Signature**: `listProductsForProductFamily(request: ProductFamilies.ListProductsForProductFamilyRequest, options?: RequestOptions): ApiPromise<ProductResponse[], ProductFamilies.ListProductsForProductFamilyError>`
- **Wire**: `GET /product_families/{product_family_id}/products.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ProductResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ProductFamilies.ListProductsForProductFamilyError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] `string` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ProductFamilies.ListProductsForProductFamilyRequest` (11):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `string` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `dateField` | `query` | `date_field` | `BasicDateField` | no | — |
| `filter` | `query` | — | `ListProductsFilter` | no | — |
| `startDate` | `query` | `start_date` | `string` (date) | no | — |
| `endDate` | `query` | `end_date` | `string` (date) | no | — |
| `startDatetime` | `query` | `start_datetime` | `Date` (date-time) | no | — |
| `endDatetime` | `query` | `end_datetime` | `Date` (date-time) | no | — |
| `includeArchived` | `query` | `include_archived` | `boolean` | no | — |
| `include` | `query` | — | `ListProductsInclude` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `BasicDateField` | `basicDateFieldSchema` | `src/models/basic-date-field.ts` |
| `ListProductsFilter` | `listProductsFilterSchema` | `src/models/list-products-filter.ts` |
| `ListProductsInclude` | `listProductsIncludeSchema` | `src/models/list-products-include.ts` |
| `ProductResponse` | `productResponseSchema` | `src/models/product-response.ts` |

### readProductFamily

- **Signature**: `readProductFamily(request: ProductFamilies.ReadProductFamilyRequest, options?: RequestOptions): ApiPromise<ProductFamilyResponse, ApiError>`
- **Wire**: `GET /product_families/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ProductFamilyResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ProductFamilies.ReadProductFamilyRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ProductFamilyResponse` | `productFamilyResponseSchema` | `src/models/product-family-response.ts` |

