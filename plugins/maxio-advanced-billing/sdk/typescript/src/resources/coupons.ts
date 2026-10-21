import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  couponCurrencyRequestSchema,
  type CouponCurrencyRequest,
} from "../models/coupon-currency-request.js";
import {
  couponCurrencyResponseSchema,
  type CouponCurrencyResponse,
} from "../models/coupon-currency-response.js";
import { couponRequestSchema, type CouponRequest } from "../models/coupon-request.js";
import { couponResponseSchema, type CouponResponse } from "../models/coupon-response.js";
import {
  couponSubcodesResponseSchema,
  type CouponSubcodesResponse,
} from "../models/coupon-subcodes-response.js";
import { couponSubcodesSchema, type CouponSubcodes } from "../models/coupon-subcodes.js";
import { couponUsageSchema, type CouponUsage } from "../models/coupon-usage.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  errorStringMapResponse1Schema,
  type ErrorStringMapResponse1,
} from "../models/error-string-map-response1.js";
import { listCouponsFilterSchema, type ListCouponsFilter } from "../models/list-coupons-filter.js";
import {
  singleStringErrorResponse1Schema,
  type SingleStringErrorResponse1,
} from "../models/single-string-error-response1.js";
import type { Servers } from "../servers.js";

/**
 * The Coupon object defines a discount, either a percentage or a fixed amount, that can be applied
 * to a subscription to reduce the subscription's billing amount.
 *
 * Coupons can be restricted to a specific Product Family, limited to a date range, and configured
 * to apply once or recur over a set duration. For more information, see [Understand
 * Coupons](https://docs.maxio.com/billing/catalog/coupons/understand-coupons).
 */
export class Coupons {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Archive Coupon
   *
   * @remarks
   * Archives a coupon, making it unavailable for future use while remaining active on existing
   * subscriptions. Archiving makes that Coupon unavailable for future use, but allows it to remain
   * attached and functional on existing Subscriptions that are using it. The `archived_at` date and
   * time will be assigned.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  archiveCoupon(
    request: Coupons.ArchiveCouponRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/coupons/{coupon_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_family_id", value: request.productFamilyId, schema: s.int() },
          { name: "coupon_id", value: request.couponId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: couponResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Create Coupon
   *
   * @remarks
   * Creates a coupon under the specified product family.
   *
   * You can create either a flat amount coupon, by specifying `amount_in_cents`, or percentage
   * coupon by specifying `percentage`.
   *
   * See [Apply Coupons to
   * Subscriptions](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions)
   * for information on applying a coupon to a subscription in the Advanced Billing UI.
   *
   * @returns Created
   *
   * @throws {@link Coupons.CreateCouponError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createCoupon(
    request: Coupons.CreateCouponRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponResponse, Coupons.CreateCouponError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/product_families/{product_family_id}/coupons.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "json", value: request.body, schema: s.optional(s.lazy(() => couponRequestSchema)) },
      },
      {
        success: { kind: "json", schema: couponResponseSchema },
        errorFactory: Coupons.CreateCouponError,
      },
      options,
    );
  }

  /**
   * Create Coupon Subcodes
   *
   * @remarks
   * Creates subcodes for an existing coupon.
   *
   * Coupon Subcodes allow you to create a set of unique codes that allow you to expand the use of
   * one coupon.
   *
   * For example:
   *
   * Master Coupon Code:
   *
   * + SPRING2020
   *
   * Coupon Subcodes:
   *
   * + SPRING90210
   * + DP80302
   * + SPRINGBALTIMORE
   *
   * When creating a coupon subcode, you must specify a coupon to attach it to using the coupon_id.
   * Valid coupon subcodes are all capital letters, contain only letters and numbers, and do not
   * have any spaces. Lowercase letters are capitalized before the subcode is created.
   *
   * Note: If you are using any of the allowed special characters ("%", "@", "+", "-", "_", and
   * "."), you must encode them for use in the URL.
   *
   * % to %25 \@ to %40
   *     + to %2B
   *     - to %2D _ to %5F . to %2E
   *
   * So, if the coupon subcode is `20%OFF`, the URL to delete this coupon subcode would be:
   * `https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>`.
   *
   * For more information on coupon codes and applying coupons to subscriptions, see [Coupon
   * Codes](https://maxio.zendesk.com/hc/en-us/articles/24261208729229-Coupon-Codes) and [Coupons
   * and
   * Subscriptions](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions).
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createCouponSubcodes(
    request: Coupons.CreateCouponSubcodesRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponSubcodesResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/coupons/{coupon_id}/codes.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "coupon_id", value: request.couponId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "json", value: request.body, schema: s.optional(s.lazy(() => couponSubcodesSchema)) },
      },
      {
        success: { kind: "json", schema: couponSubcodesResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Create / Update Currency Prices
   *
   * @remarks
   * Creates and/or updates currency prices for an existing coupon. Multiple prices can be created
   * or updated in a single request but each of the currencies must be defined on the site level
   * already and the coupon must be an amount-based coupon, not percentage.
   *
   * Currency pricing for coupons must mirror the setup of the primary coupon pricing - if the
   * primary coupon is percentage based, you will not be able to define pricing in non-primary
   * currencies.
   *
   * @returns OK
   *
   * @throws {@link Coupons.CreateOrUpdateCouponCurrencyPricesError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createOrUpdateCouponCurrencyPrices(
    request: Coupons.CreateOrUpdateCouponCurrencyPricesRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponCurrencyResponse, Coupons.CreateOrUpdateCouponCurrencyPricesError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/coupons/{coupon_id}/currency_prices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "coupon_id", value: request.couponId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => couponCurrencyRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: couponCurrencyResponseSchema },
        errorFactory: Coupons.CreateOrUpdateCouponCurrencyPricesError,
      },
      options,
    );
  }

  /**
   * Delete Coupon Subcode
   *
   * @remarks
   * Deletes a specific subcode from a coupon.
   *
   * ## Example
   *
   * Given a coupon with an ID of 567, and a coupon subcode of 20OFF, the URL to `DELETE` this
   * coupon subcode would be:
   *
   * ```
   * http://subdomain.chargify.com/coupons/567/codes/20OFF.<format>
   * ```
   *
   * Note: If you are using any of the allowed special characters (“%”, “@”, “+”, “-”, “_”, and
   * “.”), you must encode them for use in the URL.
   *
   * | Special character | Encoding |
   * |-------------------|----------|
   * | %                 | %25      |
   * | @                 | %40      |
   * | +                 | %2B      |
   * | –                 | %2D      |
   * | _                 | %5F      |
   * | .                 | %2E      |
   *
   * ## Percent Encoding Example
   *
   * Or if the coupon subcode is 20%OFF, the URL to delete this coupon subcode would be:
   * \@https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>.
   *
   * @returns OK
   *
   * @throws {@link Coupons.DeleteCouponSubcodeError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteCouponSubcode(
    request: Coupons.DeleteCouponSubcodeRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, Coupons.DeleteCouponSubcodeError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/coupons/{coupon_id}/codes/{subcode}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "coupon_id", value: request.couponId, schema: s.int() },
          { name: "subcode", value: request.subcode, schema: s.string() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: Coupons.DeleteCouponSubcodeError,
      },
      options,
    );
  }

  /**
   * Find Coupon
   *
   * @remarks
   * Searches for a coupon by code.
   *
   * If you have more than one product family and if the coupon you are trying to find does not
   * belong to the default product family in your site, you need to specify (either in the URL or as
   * a query string param) the `product_family_id`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  findCoupon(
    request: Coupons.FindCouponRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/coupons/find.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "product_family_id", value: request.productFamilyId, schema: s.optional(s.int()) },
          { name: "code", value: request.code, schema: s.optional(s.string()) },
          { name: "currency_prices", value: request.currencyPrices, schema: s.optional(s.boolean()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: couponResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Coupon Subcodes
   *
   * @remarks
   * Lists the subcodes attached to a coupon.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listCouponSubcodes(
    request: Coupons.ListCouponSubcodesRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponSubcodes, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/coupons/{coupon_id}/codes.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "coupon_id", value: request.couponId, schema: s.int() }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: couponSubcodesSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Coupons
   *
   * @remarks
   * Lists coupons for a site.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listCoupons(
    request: Coupons.ListCouponsRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/coupons.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 30) },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listCouponsFilterSchema)),
          },
          { name: "currency_prices", value: request.currencyPrices, schema: s.optional(s.boolean()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => couponResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Coupons for Product Family
   *
   * @remarks
   * Lists coupons for a specific product family in a site.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listCouponsForProductFamily(
    request: Coupons.ListCouponsForProductFamilyRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/product_families/{product_family_id}/coupons.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.int() }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 30) },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listCouponsFilterSchema)),
          },
          { name: "currency_prices", value: request.currencyPrices, schema: s.optional(s.boolean()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => couponResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Coupon
   *
   * @remarks
   * Returns a coupon by its system-assigned ID. You must identify the Coupon in this call by the ID
   * parameter assigned to it.
   *
   * If instead you would like to find a Coupon using a Coupon code, use the [Find
   * Coupon]($e/Coupons/findCoupon) endpoint.
   *
   * If the coupon is set to `use_site_exchange_rate: true`, it returns pricing based on the current
   * exchange rate. If the flag is set to false, it returns all of the defined prices for each
   * currency.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readCoupon(
    request: Coupons.ReadCouponRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/coupons/{coupon_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_family_id", value: request.productFamilyId, schema: s.int() },
          { name: "coupon_id", value: request.couponId, schema: s.int() },
        ],
        query: [{ name: "currency_prices", value: request.currencyPrices, schema: s.optional(s.boolean()) }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: couponResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Coupon Usages
   *
   * @remarks
   * Lists coupon usage details, one entry per product.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readCouponUsage(
    request: Coupons.ReadCouponUsageRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponUsage[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/coupons/{coupon_id}/usage.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_family_id", value: request.productFamilyId, schema: s.int() },
          { name: "coupon_id", value: request.couponId, schema: s.int() },
        ],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => couponUsageSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Update Coupon
   *
   * @remarks
   * Updates a coupon.
   *
   * You can restrict a coupon to only apply to specific products / components by optionally passing
   * in hashes of `restricted_products` and/or `restricted_components` in the format: `{
   * "<product/component_id>": boolean_value }`
   *
   * @returns OK
   *
   * @throws {@link Coupons.UpdateCouponError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateCoupon(
    request: Coupons.UpdateCouponRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponResponse, Coupons.UpdateCouponError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/coupons/{coupon_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_family_id", value: request.productFamilyId, schema: s.int() },
          { name: "coupon_id", value: request.couponId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "json", value: request.body, schema: s.optional(s.lazy(() => couponRequestSchema)) },
      },
      {
        success: { kind: "json", schema: couponResponseSchema },
        errorFactory: Coupons.UpdateCouponError,
      },
      options,
    );
  }

  /**
   * Update Coupon Subcodes
   *
   * @remarks
   * Updates the subcodes for a coupon, replacing all existing subcodes with the new list. Send an
   * array of new coupon subcodes.
   *
   * **Note**: All current subcodes for that Coupon will be deleted first, and replaced with the
   * list of subcodes sent to this endpoint. The response will contain:
   *
   * + The created subcodes,
   *
   * + Subcodes that were not created because they already exist,
   *
   * + Any subcodes not created because they are invalid.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateCouponSubcodes(
    request: Coupons.UpdateCouponSubcodesRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponSubcodesResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/coupons/{coupon_id}/codes.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "coupon_id", value: request.couponId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "json", value: request.body, schema: s.optional(s.lazy(() => couponSubcodesSchema)) },
      },
      {
        success: { kind: "json", schema: couponSubcodesResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Validate Coupon
   *
   * @remarks
   * Verifies whether a specific coupon code is valid. This method is useful for validating coupon
   * codes that are entered by a customer.
   *
   * If you have more than one product family and if the coupon you are validating does not belong
   * to the first product family in your site, you need to specify the product family, either in the
   * URL or as a query string param. This can be done by supplying the id or the handle in the
   * `handle:my-family` format.
   *
   * Supplying the `product_family_handle` in the URL:
   *
   * ```
   * https://<subdomain>.chargify.com/product_families/handle:<product_family_handle>/coupons/validate.<format>?code=<coupon_code>
   * ```
   *
   * Supplying the `product_family_id` as a query parameter:
   *
   * ```
   * https://<subdomain>.chargify.com/coupons/validate.<format>?code=<coupon_code>&product_family_id=<id>
   * ```
   *
   * @returns OK
   *
   * @throws {@link Coupons.ValidateCouponError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  validateCoupon(
    request: Coupons.ValidateCouponRequest,
    options?: RequestOptions,
  ): ApiPromise<CouponResponse, Coupons.ValidateCouponError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/coupons/validate.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "code", value: request.code, schema: s.string() },
          { name: "product_family_id", value: request.productFamilyId, schema: s.optional(s.int()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: couponResponseSchema },
        errorFactory: Coupons.ValidateCouponError,
      },
      options,
    );
  }
}

export namespace Coupons {
  export type ArchiveCouponRequest = {
    /** The Advanced Billing id of the product family to which the coupon belongs */
    productFamilyId: number;
    /** The Advanced Billing id of the coupon */
    couponId: number;
  };

  export type CreateCouponRequest = {
    /** The Advanced Billing id of the product family to which the coupon belongs */
    productFamilyId: number;
    body?: CouponRequest;
  };

  export class CreateCouponError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CreateCouponError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateCouponSubcodesRequest = {
    /** The Advanced Billing id of the coupon */
    couponId: number;
    body?: CouponSubcodes;
  };

  export type CreateOrUpdateCouponCurrencyPricesRequest = {
    /** The Advanced Billing id of the coupon */
    couponId: number;
    body?: CouponCurrencyRequest;
  };

  export class CreateOrUpdateCouponCurrencyPricesError extends ApiError {
    declare readonly payload: Declared<"errorStringMapResponse1", ErrorStringMapResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CreateOrUpdateCouponCurrencyPricesError> = [
      {
        on: 422,
        kind: "errorStringMapResponse1",
        decode: { kind: "json", schema: errorStringMapResponse1Schema },
      },
    ];
  }

  export type DeleteCouponSubcodeRequest = {
    /** The Advanced Billing id of the coupon to which the subcode belongs */
    couponId: number;
    /** The subcode of the coupon */
    subcode: string;
  };

  export class DeleteCouponSubcodeError extends ApiError {
    declare readonly payload: Declared<"error404", undefined> | Undeclared;

    static readonly errors: ErrorDecoders<DeleteCouponSubcodeError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type FindCouponRequest = {
    /** The Advanced Billing id of the product family to which the coupon belongs */
    productFamilyId?: number;
    /** The code of the coupon */
    code?: string;
    /**
     * (Optional) If you have defined multiple currencies at the site level, you can pass
     * `?currency_prices=true` to include an array of currency price data in the response.
     */
    currencyPrices?: boolean;
  };

  export type ListCouponSubcodesRequest = {
    /** The Advanced Billing id of the coupon */
    couponId: number;
    /**
     * Result records are organized in pages. By default, the first page of results is displayed.
     * The page parameter specifies a page number of results to fetch. You can start navigating
     * through the pages to consume the results. You do this by passing in a page parameter.
     * Retrieve the next page by adding ?page=2 to the query string. If there are no results to
     * return, then an empty result set will be returned. Use in query `page=1`.
     *
     * @default 1
     */
    page?: number;
    /**
     * This parameter indicates how many records to fetch in each request. Default value is 20. The
     * maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in
     * query `per_page=200`.
     *
     * @default 20
     */
    perPage?: number;
  };

  export type ListCouponsRequest = {
    /**
     * Result records are organized in pages. By default, the first page of results is displayed.
     * The page parameter specifies a page number of results to fetch. You can start navigating
     * through the pages to consume the results. You do this by passing in a page parameter.
     * Retrieve the next page by adding ?page=2 to the query string. If there are no results to
     * return, then an empty result set will be returned. Use in query `page=1`.
     *
     * @default 1
     */
    page?: number;
    /**
     * This parameter indicates how many records to fetch in each request. Default value is 30. The
     * maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in
     * query `per_page=200`.
     *
     * @default 30
     */
    perPage?: number;
    /** Filter to use for List Coupons operations */
    filter?: ListCouponsFilter;
    /**
     * (Optional) If you have defined multiple currencies at the site level, you can pass
     * `?currency_prices=true` to include an array of currency price data in the response. Use in
     * query `currency_prices=true`.
     */
    currencyPrices?: boolean;
  };

  export type ListCouponsForProductFamilyRequest = {
    /** The Advanced Billing id of the product family to which the coupon belongs */
    productFamilyId: number;
    /**
     * Result records are organized in pages. By default, the first page of results is displayed.
     * The page parameter specifies a page number of results to fetch. You can start navigating
     * through the pages to consume the results. You do this by passing in a page parameter.
     * Retrieve the next page by adding ?page=2 to the query string. If there are no results to
     * return, then an empty result set will be returned. Use in query `page=1`.
     *
     * @default 1
     */
    page?: number;
    /**
     * This parameter indicates how many records to fetch in each request. Default value is 30. The
     * maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in
     * query `per_page=200`.
     *
     * @default 30
     */
    perPage?: number;
    /** Filter to use for List Coupons operations */
    filter?: ListCouponsFilter;
    /**
     * (Optional) If you have defined multiple currencies at the site level, you can pass
     * `?currency_prices=true` to include an array of currency price data in the response. Use in
     * query `currency_prices=true`.
     */
    currencyPrices?: boolean;
  };

  export type ReadCouponRequest = {
    /** The Advanced Billing id of the product family to which the coupon belongs */
    productFamilyId: number;
    /** The Advanced Billing id of the coupon */
    couponId: number;
    /**
     * (Optional) If you have defined multiple currencies at the site level, you can pass
     * `?currency_prices=true` to include an array of currency price data in the response.
     */
    currencyPrices?: boolean;
  };

  export type ReadCouponUsageRequest = {
    /** The Advanced Billing id of the product family to which the coupon belongs. */
    productFamilyId: number;
    /** The Advanced Billing id of the coupon. */
    couponId: number;
  };

  export type UpdateCouponRequest = {
    /** The Advanced Billing id of the product family to which the coupon belongs */
    productFamilyId: number;
    /** The Advanced Billing id of the coupon */
    couponId: number;
    body?: CouponRequest;
  };

  export class UpdateCouponError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<UpdateCouponError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateCouponSubcodesRequest = {
    /** The Advanced Billing id of the coupon */
    couponId: number;
    body?: CouponSubcodes;
  };

  export type ValidateCouponRequest = {
    /** The code of the coupon */
    code: string;
    /** The Advanced Billing id of the product family to which the coupon belongs */
    productFamilyId?: number;
  };

  export class ValidateCouponError extends ApiError {
    declare readonly payload: Declared<"singleStringErrorResponse1", SingleStringErrorResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<ValidateCouponError> = [
      {
        on: 404,
        kind: "singleStringErrorResponse1",
        decode: { kind: "json", schema: singleStringErrorResponse1Schema },
      },
    ];
  }
}
