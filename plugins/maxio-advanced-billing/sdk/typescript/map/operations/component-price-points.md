<!-- Generated file — do not edit; regenerated with the SDK. -->

# ComponentPricePoints — operations

Accessor: `client.componentPricePoints` · Source: `src/resources/component-price-points.ts` · 12 operations · Request and error types: namespace `ComponentPricePoints`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### archiveComponentPricePoint

- **Provider notes (Maxio)**: `knowledge/operations/component-price-points.md#archivecomponentpricepoint`
- **Signature**: `archiveComponentPricePoint(request: ComponentPricePoints.ArchiveComponentPricePointRequest, options?: RequestOptions): ApiPromise<ComponentPricePointResponse, ComponentPricePoints.ArchiveComponentPricePointError>`
- **Wire**: `DELETE /components/{component_id}/price_points/{price_point_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentPricePointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentPricePoints.ArchiveComponentPricePointError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentPricePoints.ArchiveComponentPricePointRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `ComponentIdModel` | yes |
| `pricePointId` | `path` | `price_point_id` | `PricePointIdModel` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ComponentIdModel` | `componentIdModelSchema` | `src/models/unions/component-id-model.ts` |
| `PricePointIdModel` | `pricePointIdModelSchema` | `src/models/unions/price-point-id-model.ts` |
| `ComponentPricePointResponse` | `componentPricePointResponseSchema` | `src/models/component-price-point-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### bulkCreateComponentPricePoints

- **Signature**: `bulkCreateComponentPricePoints(request: ComponentPricePoints.BulkCreateComponentPricePointsRequest, options?: RequestOptions): ApiPromise<ComponentPricePointsResponse, ComponentPricePoints.BulkCreateComponentPricePointsError>`
- **Wire**: `POST /components/{component_id}/price_points/bulk.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentPricePointsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentPricePoints.BulkCreateComponentPricePointsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentPricePoints.BulkCreateComponentPricePointsRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `string` | yes |
| `body` | `body` | — | `CreateComponentPricePointsRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateComponentPricePointsRequest` | `createComponentPricePointsRequestSchema` | `src/models/create-component-price-points-request.ts` |
| `ComponentPricePointsResponse` | `componentPricePointsResponseSchema` | `src/models/component-price-points-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### cloneComponentPricePoint

- **Signature**: `cloneComponentPricePoint(request: ComponentPricePoints.CloneComponentPricePointRequestParams, options?: RequestOptions): ApiPromise<ComponentPricePointCurrencyOverageResponse, ComponentPricePoints.CloneComponentPricePointError>`
- **Wire**: `POST /components/{component_id}/price_points/{price_point_id}/clone.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentPricePointCurrencyOverageResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentPricePoints.CloneComponentPricePointError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentPricePoints.CloneComponentPricePointRequestParams` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `ComponentIdModel` | yes |
| `pricePointId` | `path` | `price_point_id` | `PricePointIdModel` | yes |
| `body` | `body` | — | `CloneComponentPricePointRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ComponentIdModel` | `componentIdModelSchema` | `src/models/unions/component-id-model.ts` |
| `PricePointIdModel` | `pricePointIdModelSchema` | `src/models/unions/price-point-id-model.ts` |
| `CloneComponentPricePointRequest` | `cloneComponentPricePointRequestSchema` | `src/models/clone-component-price-point-request.ts` |
| `ComponentPricePointCurrencyOverageResponse` | `componentPricePointCurrencyOverageResponseSchema` | `src/models/component-price-point-currency-overage-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createComponentPricePoint

- **Provider rules (Maxio)**: For `per_unit`, send `prices` as one open bracket: `[{"starting_quantity": 1, "unit_price": X}]`. Keep brackets contiguous and non-overlapping. Hybrid pricing also needs `overage_pricing_scheme`, or the overage block is ignored. Notes: `knowledge/operations/component-price-points.md#createcomponentpricepoint`
- **Signature**: `createComponentPricePoint(request: ComponentPricePoints.CreateComponentPricePointRequestParams, options?: RequestOptions): ApiPromise<ComponentPricePointResponse, ComponentPricePoints.CreateComponentPricePointError>`
- **Wire**: `POST /components/{component_id}/price_points.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentPricePointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentPricePoints.CreateComponentPricePointError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorArrayMapResponse1"` [422] `ErrorArrayMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentPricePoints.CreateComponentPricePointRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes |
| `body` | `body` | — | `CreateComponentPricePointRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateComponentPricePointRequest` | `createComponentPricePointRequestSchema` | `src/models/create-component-price-point-request.ts` |
| `ComponentPricePointResponse` | `componentPricePointResponseSchema` | `src/models/component-price-point-response.ts` |
| `ErrorArrayMapResponse1` | `errorArrayMapResponse1Schema` | `src/models/error-array-map-response1.ts` |

### createCurrencyPrices

- **Provider rules (Maxio)**: Send one row per price bracket of the price point (`price_id`) for the currency. `price` is in major units of that currency, like `unit_price`, not cents (R4). Notes: `knowledge/operations/component-price-points.md#createcurrencyprices`
- **Signature**: `createCurrencyPrices(request: ComponentPricePoints.CreateCurrencyPricesRequestParams, options?: RequestOptions): ApiPromise<ComponentCurrencyPricesResponse, ComponentPricePoints.CreateCurrencyPricesError>`
- **Wire**: `POST /price_points/{price_point_id}/currency_prices.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentCurrencyPricesResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentPricePoints.CreateCurrencyPricesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorArrayMapResponse1"` [422] `ErrorArrayMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentPricePoints.CreateCurrencyPricesRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `pricePointId` | `path` | `price_point_id` | `number` | yes |
| `body` | `body` | — | `CreateCurrencyPricesRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateCurrencyPricesRequest` | `createCurrencyPricesRequestSchema` | `src/models/create-currency-prices-request.ts` |
| `ComponentCurrencyPricesResponse` | `componentCurrencyPricesResponseSchema` | `src/models/component-currency-prices-response.ts` |
| `ErrorArrayMapResponse1` | `errorArrayMapResponse1Schema` | `src/models/error-array-map-response1.ts` |

### listAllComponentPricePoints

- **Signature**: `listAllComponentPricePoints(request: ComponentPricePoints.ListAllComponentPricePointsRequest, options?: RequestOptions): ApiPromise<ListComponentsPricePointsResponse, ComponentPricePoints.ListAllComponentPricePointsError>`
- **Wire**: `GET /components_price_points.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListComponentsPricePointsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentPricePoints.ListAllComponentPricePointsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentPricePoints.ListAllComponentPricePointsRequest` (5):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `include` | `query` | — | `ListComponentsPricePointsInclude` | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `direction` | `query` | — | `SortingDirection` | no | — |
| `filter` | `query` | — | `ListPricePointsFilter` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListComponentsPricePointsInclude` | `listComponentsPricePointsIncludeSchema` | `src/models/list-components-price-points-include.ts` |
| `SortingDirection` | `sortingDirectionSchema` | `src/models/sorting-direction.ts` |
| `ListPricePointsFilter` | `listPricePointsFilterSchema` | `src/models/list-price-points-filter.ts` |
| `ListComponentsPricePointsResponse` | `listComponentsPricePointsResponseSchema` | `src/models/list-components-price-points-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listComponentPricePoints

- **Signature**: `listComponentPricePoints(request: ComponentPricePoints.ListComponentPricePointsRequest, options?: RequestOptions): ApiPromise<ComponentPricePointsResponse, ApiError>`
- **Wire**: `GET /components/{component_id}/price_points.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ComponentPricePointsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ComponentPricePoints.ListComponentPricePointsRequest` (5):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes | — |
| `currencyPrices` | `query` | `currency_prices` | `boolean` | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `filterType` | `query` | `filter[type]` | `PricePointType[]` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `PricePointType` | `pricePointTypeSchema` | `src/models/price-point-type.ts` |
| `ComponentPricePointsResponse` | `componentPricePointsResponseSchema` | `src/models/component-price-points-response.ts` |

### promoteComponentPricePointToDefault

- **Provider notes (Maxio)**: `knowledge/operations/component-price-points.md#promotecomponentpricepointtodefault`
- **Signature**: `promoteComponentPricePointToDefault(request: ComponentPricePoints.PromoteComponentPricePointToDefaultRequest, options?: RequestOptions): ApiPromise<ComponentResponse, ApiError>`
- **Wire**: `PUT /components/{component_id}/price_points/{price_point_id}/default.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ComponentPricePoints.PromoteComponentPricePointToDefaultRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes |
| `pricePointId` | `path` | `price_point_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |

### readComponentPricePoint

- **Signature**: `readComponentPricePoint(request: ComponentPricePoints.ReadComponentPricePointRequest, options?: RequestOptions): ApiPromise<ComponentPricePointCurrencyOverageResponse, ApiError>`
- **Wire**: `GET /components/{component_id}/price_points/{price_point_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ComponentPricePointCurrencyOverageResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ComponentPricePoints.ReadComponentPricePointRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `ComponentIdModel` | yes |
| `pricePointId` | `path` | `price_point_id` | `PricePointIdModel` | yes |
| `currencyPrices` | `query` | `currency_prices` | `boolean` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ComponentIdModel` | `componentIdModelSchema` | `src/models/unions/component-id-model.ts` |
| `PricePointIdModel` | `pricePointIdModelSchema` | `src/models/unions/price-point-id-model.ts` |
| `ComponentPricePointCurrencyOverageResponse` | `componentPricePointCurrencyOverageResponseSchema` | `src/models/component-price-point-currency-overage-response.ts` |

### unarchiveComponentPricePoint

- **Signature**: `unarchiveComponentPricePoint(request: ComponentPricePoints.UnarchiveComponentPricePointRequest, options?: RequestOptions): ApiPromise<ComponentPricePointResponse, ApiError>`
- **Wire**: `PUT /components/{component_id}/price_points/{price_point_id}/unarchive.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentPricePointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `ComponentPricePoints.UnarchiveComponentPricePointRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes |
| `pricePointId` | `path` | `price_point_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ComponentPricePointResponse` | `componentPricePointResponseSchema` | `src/models/component-price-point-response.ts` |

### updateComponentPricePoint

- **Provider rules (Maxio)**: To change `prices`, get the bracket `id`s from `readComponentPricePoint`, then update or `_destroy: true` those; a fresh list is added beside the old one. For new customers only, create and promote a new price point (D9). Notes: `knowledge/operations/component-price-points.md#updatecomponentpricepoint`
- **Signature**: `updateComponentPricePoint(request: ComponentPricePoints.UpdateComponentPricePointRequestParams, options?: RequestOptions): ApiPromise<ComponentPricePointResponse, ComponentPricePoints.UpdateComponentPricePointError>`
- **Wire**: `PUT /components/{component_id}/price_points/{price_point_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentPricePointResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentPricePoints.UpdateComponentPricePointError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorArrayMapResponse1"` [422] `ErrorArrayMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentPricePoints.UpdateComponentPricePointRequestParams` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `ComponentIdModel` | yes |
| `pricePointId` | `path` | `price_point_id` | `PricePointIdModel` | yes |
| `body` | `body` | — | `UpdateComponentPricePointRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ComponentIdModel` | `componentIdModelSchema` | `src/models/unions/component-id-model.ts` |
| `PricePointIdModel` | `pricePointIdModelSchema` | `src/models/unions/price-point-id-model.ts` |
| `UpdateComponentPricePointRequest` | `updateComponentPricePointRequestSchema` | `src/models/update-component-price-point-request.ts` |
| `ComponentPricePointResponse` | `componentPricePointResponseSchema` | `src/models/component-price-point-response.ts` |
| `ErrorArrayMapResponse1` | `errorArrayMapResponse1Schema` | `src/models/error-array-map-response1.ts` |

### updateCurrencyPrices

- **Signature**: `updateCurrencyPrices(request: ComponentPricePoints.UpdateCurrencyPricesRequestParams, options?: RequestOptions): ApiPromise<ComponentCurrencyPricesResponse, ComponentPricePoints.UpdateCurrencyPricesError>`
- **Wire**: `PUT /price_points/{price_point_id}/currency_prices.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentCurrencyPricesResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentPricePoints.UpdateCurrencyPricesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorArrayMapResponse1"` [422] `ErrorArrayMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentPricePoints.UpdateCurrencyPricesRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `pricePointId` | `path` | `price_point_id` | `number` | yes |
| `body` | `body` | — | `UpdateCurrencyPricesRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateCurrencyPricesRequest` | `updateCurrencyPricesRequestSchema` | `src/models/update-currency-prices-request.ts` |
| `ComponentCurrencyPricesResponse` | `componentCurrencyPricesResponseSchema` | `src/models/component-currency-prices-response.ts` |
| `ErrorArrayMapResponse1` | `errorArrayMapResponse1Schema` | `src/models/error-array-map-response1.ts` |

