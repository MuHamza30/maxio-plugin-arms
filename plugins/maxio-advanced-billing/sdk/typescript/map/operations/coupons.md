<!-- Generated file — do not edit; regenerated with the SDK. -->

# Coupons — operations

Accessor: `client.coupons` · Source: `src/resources/coupons.ts` · 14 operations · Request and error types: namespace `Coupons`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### archiveCoupon

- **Signature**: `archiveCoupon(request: Coupons.ArchiveCouponRequest, options?: RequestOptions): ApiPromise<CouponResponse, ApiError>`
- **Wire**: `DELETE /product_families/{product_family_id}/coupons/{coupon_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CouponResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Coupons.ArchiveCouponRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes |
| `couponId` | `path` | `coupon_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponResponse` | `couponResponseSchema` | `src/models/coupon-response.ts` |

### createCoupon

- **Signature**: `createCoupon(request: Coupons.CreateCouponRequest, options?: RequestOptions): ApiPromise<CouponResponse, Coupons.CreateCouponError>`
- **Wire**: `POST /product_families/{product_family_id}/coupons.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CouponResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Coupons.CreateCouponError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Coupons.CreateCouponRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes |
| `body` | `body` | — | `CouponRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponRequest` | `couponRequestSchema` | `src/models/coupon-request.ts` |
| `CouponResponse` | `couponResponseSchema` | `src/models/coupon-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createCouponSubcodes

- **Signature**: `createCouponSubcodes(request: Coupons.CreateCouponSubcodesRequest, options?: RequestOptions): ApiPromise<CouponSubcodesResponse, ApiError>`
- **Wire**: `POST /coupons/{coupon_id}/codes.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CouponSubcodesResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Coupons.CreateCouponSubcodesRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `couponId` | `path` | `coupon_id` | `number` | yes |
| `body` | `body` | — | `CouponSubcodes` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponSubcodes` | `couponSubcodesSchema` | `src/models/coupon-subcodes.ts` |
| `CouponSubcodesResponse` | `couponSubcodesResponseSchema` | `src/models/coupon-subcodes-response.ts` |

### createOrUpdateCouponCurrencyPrices

- **Signature**: `createOrUpdateCouponCurrencyPrices(request: Coupons.CreateOrUpdateCouponCurrencyPricesRequest, options?: RequestOptions): ApiPromise<CouponCurrencyResponse, Coupons.CreateOrUpdateCouponCurrencyPricesError>`
- **Wire**: `PUT /coupons/{coupon_id}/currency_prices.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CouponCurrencyResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Coupons.CreateOrUpdateCouponCurrencyPricesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorStringMapResponse1"` [422] `ErrorStringMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Coupons.CreateOrUpdateCouponCurrencyPricesRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `couponId` | `path` | `coupon_id` | `number` | yes |
| `body` | `body` | — | `CouponCurrencyRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponCurrencyRequest` | `couponCurrencyRequestSchema` | `src/models/coupon-currency-request.ts` |
| `CouponCurrencyResponse` | `couponCurrencyResponseSchema` | `src/models/coupon-currency-response.ts` |
| `ErrorStringMapResponse1` | `errorStringMapResponse1Schema` | `src/models/error-string-map-response1.ts` |

### deleteCouponSubcode

- **Signature**: `deleteCouponSubcode(request: Coupons.DeleteCouponSubcodeRequest, options?: RequestOptions): ApiPromise<undefined, Coupons.DeleteCouponSubcodeError>`
- **Wire**: `DELETE /coupons/{coupon_id}/codes/{subcode}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Coupons.DeleteCouponSubcodeError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Coupons.DeleteCouponSubcodeRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `couponId` | `path` | `coupon_id` | `number` | yes |
| `subcode` | `path` | — | `string` | yes |

### findCoupon

- **Signature**: `findCoupon(request?: Coupons.FindCouponRequest, options?: RequestOptions): ApiPromise<CouponResponse, ApiError>`
- **Wire**: `GET /coupons/find.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CouponResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Coupons.FindCouponRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `query` | `product_family_id` | `number` | no |
| `code` | `query` | — | `string` | no |
| `currencyPrices` | `query` | `currency_prices` | `boolean` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponResponse` | `couponResponseSchema` | `src/models/coupon-response.ts` |

### listCouponSubcodes

- **Signature**: `listCouponSubcodes(request: Coupons.ListCouponSubcodesRequest, options?: RequestOptions): ApiPromise<CouponSubcodes, ApiError>`
- **Wire**: `GET /coupons/{coupon_id}/codes.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CouponSubcodes`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Coupons.ListCouponSubcodesRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `couponId` | `path` | `coupon_id` | `number` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponSubcodes` | `couponSubcodesSchema` | `src/models/coupon-subcodes.ts` |

### listCoupons

- **Signature**: `listCoupons(request?: Coupons.ListCouponsRequest, options?: RequestOptions): ApiPromise<CouponResponse[], ApiError>`
- **Wire**: `GET /coupons.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CouponResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Coupons.ListCouponsRequest` (4):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `30` |
| `filter` | `query` | — | `ListCouponsFilter` | no | — |
| `currencyPrices` | `query` | `currency_prices` | `boolean` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListCouponsFilter` | `listCouponsFilterSchema` | `src/models/list-coupons-filter.ts` |
| `CouponResponse` | `couponResponseSchema` | `src/models/coupon-response.ts` |

### listCouponsForProductFamily

- **Signature**: `listCouponsForProductFamily(request: Coupons.ListCouponsForProductFamilyRequest, options?: RequestOptions): ApiPromise<CouponResponse[], ApiError>`
- **Wire**: `GET /product_families/{product_family_id}/coupons.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CouponResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Coupons.ListCouponsForProductFamilyRequest` (5):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `30` |
| `filter` | `query` | — | `ListCouponsFilter` | no | — |
| `currencyPrices` | `query` | `currency_prices` | `boolean` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListCouponsFilter` | `listCouponsFilterSchema` | `src/models/list-coupons-filter.ts` |
| `CouponResponse` | `couponResponseSchema` | `src/models/coupon-response.ts` |

### readCoupon

- **Signature**: `readCoupon(request: Coupons.ReadCouponRequest, options?: RequestOptions): ApiPromise<CouponResponse, ApiError>`
- **Wire**: `GET /product_families/{product_family_id}/coupons/{coupon_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CouponResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Coupons.ReadCouponRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes |
| `couponId` | `path` | `coupon_id` | `number` | yes |
| `currencyPrices` | `query` | `currency_prices` | `boolean` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponResponse` | `couponResponseSchema` | `src/models/coupon-response.ts` |

### readCouponUsage

- **Signature**: `readCouponUsage(request: Coupons.ReadCouponUsageRequest, options?: RequestOptions): ApiPromise<CouponUsage[], ApiError>`
- **Wire**: `GET /product_families/{product_family_id}/coupons/{coupon_id}/usage.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CouponUsage[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Coupons.ReadCouponUsageRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes |
| `couponId` | `path` | `coupon_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponUsage` | `couponUsageSchema` | `src/models/coupon-usage.ts` |

### updateCoupon

- **Signature**: `updateCoupon(request: Coupons.UpdateCouponRequest, options?: RequestOptions): ApiPromise<CouponResponse, Coupons.UpdateCouponError>`
- **Wire**: `PUT /product_families/{product_family_id}/coupons/{coupon_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CouponResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Coupons.UpdateCouponError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Coupons.UpdateCouponRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes |
| `couponId` | `path` | `coupon_id` | `number` | yes |
| `body` | `body` | — | `CouponRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponRequest` | `couponRequestSchema` | `src/models/coupon-request.ts` |
| `CouponResponse` | `couponResponseSchema` | `src/models/coupon-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### updateCouponSubcodes

- **Signature**: `updateCouponSubcodes(request: Coupons.UpdateCouponSubcodesRequest, options?: RequestOptions): ApiPromise<CouponSubcodesResponse, ApiError>`
- **Wire**: `PUT /coupons/{coupon_id}/codes.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CouponSubcodesResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Coupons.UpdateCouponSubcodesRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `couponId` | `path` | `coupon_id` | `number` | yes |
| `body` | `body` | — | `CouponSubcodes` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponSubcodes` | `couponSubcodesSchema` | `src/models/coupon-subcodes.ts` |
| `CouponSubcodesResponse` | `couponSubcodesResponseSchema` | `src/models/coupon-subcodes-response.ts` |

### validateCoupon

- **Signature**: `validateCoupon(request: Coupons.ValidateCouponRequest, options?: RequestOptions): ApiPromise<CouponResponse, Coupons.ValidateCouponError>`
- **Wire**: `GET /coupons/validate.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CouponResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Coupons.ValidateCouponError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"singleStringErrorResponse1"` [404] `SingleStringErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Coupons.ValidateCouponRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `code` | `query` | — | `string` | yes |
| `productFamilyId` | `query` | `product_family_id` | `number` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CouponResponse` | `couponResponseSchema` | `src/models/coupon-response.ts` |
| `SingleStringErrorResponse1` | `singleStringErrorResponse1Schema` | `src/models/single-string-error-response1.ts` |

