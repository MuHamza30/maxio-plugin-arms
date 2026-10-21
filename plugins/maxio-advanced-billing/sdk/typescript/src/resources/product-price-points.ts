import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  bulkCreateProductPricePointsRequestSchema,
  type BulkCreateProductPricePointsRequest,
} from "../models/bulk-create-product-price-points-request.js";
import {
  bulkCreateProductPricePointsResponseSchema,
  type BulkCreateProductPricePointsResponse,
} from "../models/bulk-create-product-price-points-response.js";
import {
  createProductCurrencyPricesRequestSchema,
  type CreateProductCurrencyPricesRequest,
} from "../models/create-product-currency-prices-request.js";
import {
  createProductPricePointRequestSchema,
  type CreateProductPricePointRequest,
} from "../models/create-product-price-point-request.js";
import {
  currencyPricesResponseSchema,
  type CurrencyPricesResponse,
} from "../models/currency-prices-response.js";
import {
  errorArrayMapResponse1Schema,
  type ErrorArrayMapResponse1,
} from "../models/error-array-map-response1.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  listPricePointsFilterSchema,
  type ListPricePointsFilter,
} from "../models/list-price-points-filter.js";
import {
  listProductPricePointsResponseSchema,
  type ListProductPricePointsResponse,
} from "../models/list-product-price-points-response.js";
import {
  listProductsPricePointsIncludeSchema,
  type ListProductsPricePointsInclude,
} from "../models/list-products-price-points-include.js";
import { pricePointTypeSchema, type PricePointType } from "../models/price-point-type.js";
import {
  productPricePointErrorResponse1Schema,
  type ProductPricePointErrorResponse1,
} from "../models/product-price-point-error-response1.js";
import {
  productPricePointResponseSchema,
  type ProductPricePointResponse,
} from "../models/product-price-point-response.js";
import { productResponseSchema, type ProductResponse } from "../models/product-response.js";
import { sortingDirectionSchema, type SortingDirection } from "../models/sorting-direction.js";
import { pricePointIdModelSchema, type PricePointIdModel } from "../models/unions/price-point-id-model.js";
import { productIdModelSchema, type ProductIdModel } from "../models/unions/product-id-model.js";
import {
  updateCurrencyPricesRequestSchema,
  type UpdateCurrencyPricesRequest,
} from "../models/update-currency-prices-request.js";
import {
  updateProductPricePointRequestSchema,
  type UpdateProductPricePointRequest,
} from "../models/update-product-price-point-request.js";
import type { Servers } from "../servers.js";

/**
 * The Product Price Point object defines a specific pricing configuration for a Product, including
 * price, billing interval, and trial terms.
 *
 * A single Product can have multiple price points, letting you offer different rates or terms for
 * the same product without creating separate products. For more information, see [Setting Up Plan
 * Price Points](https://docs.maxio.com/billing/catalog/plans/setting-up-plan-price-points).
 */
export class ProductPricePoints {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Archive Product Price Point
   *
   * @remarks
   * Archives a product price point.
   *
   * @returns OK
   *
   * @throws {@link ProductPricePoints.ArchiveProductPricePointError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  archiveProductPricePoint(
    request: ProductPricePoints.ArchiveProductPricePointRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductPricePointResponse, ProductPricePoints.ArchiveProductPricePointError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/products/{product_id}/price_points/{price_point_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_id", value: request.productId, schema: productIdModelSchema },
          { name: "price_point_id", value: request.pricePointId, schema: pricePointIdModelSchema },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: productPricePointResponseSchema },
        errorFactory: ProductPricePoints.ArchiveProductPricePointError,
      },
      options,
    );
  }

  /**
   * Bulk Create Product Price Points
   *
   * @remarks
   * Creates multiple product price points in one request.
   *
   * @returns Created
   *
   * @throws {@link ProductPricePoints.BulkCreateProductPricePointsError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  bulkCreateProductPricePoints(
    request: ProductPricePoints.BulkCreateProductPricePointsRequestParams,
    options?: RequestOptions,
  ): ApiPromise<BulkCreateProductPricePointsResponse, ProductPricePoints.BulkCreateProductPricePointsError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/products/{product_id}/price_points/bulk.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_id", value: request.productId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => bulkCreateProductPricePointsRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: bulkCreateProductPricePointsResponseSchema },
        errorFactory: ProductPricePoints.BulkCreateProductPricePointsError,
      },
      options,
    );
  }

  /**
   * Create Product Currency Prices
   *
   * @remarks
   * Creates currency prices for a given currency that has been defined on the site level in your
   * settings.
   *
   * When creating currency prices, they need to mirror the structure of your primary pricing. If
   * the product price point defines a trial and/or setup fee, each currency must also define a
   * trial and/or setup fee.
   *
   * Note: Currency Prices are not able to be created for custom product price points.
   *
   * @returns OK
   *
   * @throws {@link ProductPricePoints.CreateProductCurrencyPricesError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createProductCurrencyPrices(
    request: ProductPricePoints.CreateProductCurrencyPricesRequestParams,
    options?: RequestOptions,
  ): ApiPromise<CurrencyPricesResponse, ProductPricePoints.CreateProductCurrencyPricesError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/product_price_points/{product_price_point_id}/currency_prices.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_price_point_id", value: request.productPricePointId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createProductCurrencyPricesRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: currencyPricesResponseSchema },
        errorFactory: ProductPricePoints.CreateProductCurrencyPricesError,
      },
      options,
    );
  }

  /**
   * Create Product Price Point
   *
   * @remarks
   * Creates a Product Price Point. See the [Product Price
   * Point](https://maxio.zendesk.com/hc/en-us/articles/24261111947789-Product-Price-Points)
   * documentation for details.
   *
   * @returns Created
   *
   * @throws {@link ProductPricePoints.CreateProductPricePointError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createProductPricePoint(
    request: ProductPricePoints.CreateProductPricePointRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ProductPricePointResponse, ProductPricePoints.CreateProductPricePointError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/products/{product_id}/price_points.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_id", value: request.productId, schema: productIdModelSchema }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createProductPricePointRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: productPricePointResponseSchema },
        errorFactory: ProductPricePoints.CreateProductPricePointError,
      },
      options,
    );
  }

  /**
   * List All Products Price Points
   *
   * @remarks
   * Lists Product Price Points belonging to a site.
   *
   * @returns OK
   *
   * @throws {@link ProductPricePoints.ListAllProductPricePointsError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listAllProductPricePoints(
    request: ProductPricePoints.ListAllProductPricePointsRequest = {},
    options?: RequestOptions,
  ): ApiPromise<ListProductPricePointsResponse, ProductPricePoints.ListAllProductPricePointsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/products_price_points.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          {
            name: "direction",
            value: request.direction,
            schema: s.optional(s.lazy(() => sortingDirectionSchema)),
          },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listPricePointsFilterSchema)),
          },
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.lazy(() => listProductsPricePointsIncludeSchema)),
          },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listProductPricePointsResponseSchema },
        errorFactory: ProductPricePoints.ListAllProductPricePointsError,
      },
      options,
    );
  }

  /**
   * List Product Price Points
   *
   * @remarks
   * Retrieves a list of product price points.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listProductPricePoints(
    request: ProductPricePoints.ListProductPricePointsRequest,
    options?: RequestOptions,
  ): ApiPromise<ListProductPricePointsResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/products/{product_id}/price_points.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_id", value: request.productId, schema: productIdModelSchema }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 10) },
          { name: "currency_prices", value: request.currencyPrices, schema: s.optional(s.boolean()) },
          {
            name: "filter[type]",
            value: request.filterType,
            schema: s.optional(s.array(s.lazy(() => pricePointTypeSchema))),
          },
          { name: "archived", value: request.archived, schema: s.optional(s.boolean()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listProductPricePointsResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Promote Product Price Point to Default
   *
   * @remarks
   * Sets a product price point as the default for the product.
   *
   * Note: Custom product price points cannot be set as the default for a product.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  promoteProductPricePointToDefault(
    request: ProductPricePoints.PromoteProductPricePointToDefaultRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "PATCH",
        urlTemplate: this.#servers.production(
          "/products/{product_id}/price_points/{price_point_id}/default.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_id", value: request.productId, schema: s.int() },
          { name: "price_point_id", value: request.pricePointId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: productResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Product Price Point
   *
   * @remarks
   * Returns details for a specific product price point. You can achieve this by using either the
   * product price point ID or handle.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readProductPricePoint(
    request: ProductPricePoints.ReadProductPricePointRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductPricePointResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/products/{product_id}/price_points/{price_point_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_id", value: request.productId, schema: productIdModelSchema },
          { name: "price_point_id", value: request.pricePointId, schema: pricePointIdModelSchema },
        ],
        query: [{ name: "currency_prices", value: request.currencyPrices, schema: s.optional(s.boolean()) }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: productPricePointResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Unarchive Product Price Point
   *
   * @remarks
   * Unarchives an archived product price point.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  unarchiveProductPricePoint(
    request: ProductPricePoints.UnarchiveProductPricePointRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductPricePointResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "PATCH",
        urlTemplate: this.#servers.production(
          "/products/{product_id}/price_points/{price_point_id}/unarchive.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_id", value: request.productId, schema: s.int() },
          { name: "price_point_id", value: request.pricePointId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: productPricePointResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Update Product Currency Prices
   *
   * @remarks
   * Updates the `price`s of currency prices for a given currency that exists on the product price
   * point.
   *
   * When updating the pricing, it needs to mirror the structure of your primary pricing. If the
   * product price point defines a trial and/or setup fee, each currency must also define a trial
   * and/or setup fee.
   *
   * Note: Currency Prices cannot be updated for custom product price points.
   *
   * @returns OK
   *
   * @throws {@link ProductPricePoints.UpdateProductCurrencyPricesError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateProductCurrencyPrices(
    request: ProductPricePoints.UpdateProductCurrencyPricesRequest,
    options?: RequestOptions,
  ): ApiPromise<CurrencyPricesResponse, ProductPricePoints.UpdateProductCurrencyPricesError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/product_price_points/{product_price_point_id}/currency_prices.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_price_point_id", value: request.productPricePointId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateCurrencyPricesRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: currencyPricesResponseSchema },
        errorFactory: ProductPricePoints.UpdateProductCurrencyPricesError,
      },
      options,
    );
  }

  /**
   * Update Product Price Point
   *
   * @remarks
   * Updates a product price point.
   *
   * Note: Custom product price points cannot be updated.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateProductPricePoint(
    request: ProductPricePoints.UpdateProductPricePointRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ProductPricePointResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/products/{product_id}/price_points/{price_point_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_id", value: request.productId, schema: productIdModelSchema },
          { name: "price_point_id", value: request.pricePointId, schema: pricePointIdModelSchema },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateProductPricePointRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: productPricePointResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }
}

export namespace ProductPricePoints {
  export type ArchiveProductPricePointRequest = {
    /**
     * The id or handle of the product. When using the handle, it must be prefixed with `handle:`.
     * Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle.
     */
    productId: ProductIdModel;
    /**
     * The id or handle of the price point. When using the handle, it must be prefixed with
     * `handle:`. Example: `123` for an integer ID, or `handle:example-product-price-point-handle`
     * for a string handle.
     */
    pricePointId: PricePointIdModel;
  };

  export class ArchiveProductPricePointError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<ArchiveProductPricePointError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type BulkCreateProductPricePointsRequestParams = {
    /** The Advanced Billing id of the product to which the price points belong */
    productId: number;
    body?: BulkCreateProductPricePointsRequest;
  };

  export class BulkCreateProductPricePointsError extends ApiError {
    declare readonly payload: Declared<"error422", Record<string, unknown>> | Undeclared;

    static readonly errors: ErrorDecoders<BulkCreateProductPricePointsError> = [
      { on: 422, kind: "error422", decode: { kind: "json", schema: s.record(s.string(), s.unknown()) } },
    ];
  }

  export type CreateProductCurrencyPricesRequestParams = {
    /** The Advanced Billing id of the product price point */
    productPricePointId: number;
    body?: CreateProductCurrencyPricesRequest;
  };

  export class CreateProductCurrencyPricesError extends ApiError {
    declare readonly payload: Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CreateProductCurrencyPricesError> = [
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type CreateProductPricePointRequestParams = {
    /**
     * The id or handle of the product. When using the handle, it must be prefixed with `handle:`
     */
    productId: ProductIdModel;
    body?: CreateProductPricePointRequest;
  };

  export class CreateProductPricePointError extends ApiError {
    declare readonly payload:
      | Declared<"productPricePointErrorResponse1", ProductPricePointErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<CreateProductPricePointError> = [
      {
        on: 422,
        kind: "productPricePointErrorResponse1",
        decode: { kind: "json", schema: productPricePointErrorResponse1Schema },
      },
    ];
  }

  export type ListAllProductPricePointsRequest = {
    /** Controls the order in which results are returned. Use in query `direction=asc`. */
    direction?: SortingDirection;
    /** Filter to use for List PricePoints operations */
    filter?: ListPricePointsFilter;
    /**
     * Allows including additional data in the response. Use in query: `include=currency_prices`.
     */
    include?: ListProductsPricePointsInclude;
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

  export class ListAllProductPricePointsError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<ListAllProductPricePointsError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListProductPricePointsRequest = {
    /**
     * The id or handle of the product. When using the handle, it must be prefixed with `handle:`
     */
    productId: ProductIdModel;
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
     * This parameter indicates how many records to fetch in each request. Default value is 10. The
     * maximum allowed values is 200; any per_page value over 200 will be changed to 200.
     *
     * @default 10
     */
    perPage?: number;
    /**
     * (Optional) If you have defined multiple currencies at the site level, you can pass
     * ?currency_prices=true to include an array of currency price data in the response. If the
     * product price point is set to use_site_exchange_rate: true, it will return pricing based on
     * the current exchange rate. If the flag is set to false, it will return all of the defined
     * prices for each currency.
     */
    currencyPrices?: boolean;
    /** Use in query: `filter[type]=catalog,default`. */
    filterType?: PricePointType[];
    /** Set to include archived price points in the response. */
    archived?: boolean;
  };

  export type PromoteProductPricePointToDefaultRequest = {
    /** The Advanced Billing id of the product to which the price point belongs */
    productId: number;
    /** The Advanced Billing id of the product price point */
    pricePointId: number;
  };

  export type ReadProductPricePointRequest = {
    /**
     * The id or handle of the product. When using the handle, it must be prefixed with `handle:`.
     * Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle.
     */
    productId: ProductIdModel;
    /**
     * The id or handle of the price point. When using the handle, it must be prefixed with
     * `handle:`. Example: `123` for an integer ID, or `handle:example-product-price-point-handle`
     * for a string handle.
     */
    pricePointId: PricePointIdModel;
    /**
     * (Optional) If you have defined multiple currencies at the site level, you can pass
     * ?currency_prices=true to include an array of currency price data in the response. If the
     * product price point is set to use_site_exchange_rate: true, it will return pricing based on
     * the current exchange rate. If the flag is set to false, it will return all of the defined
     * prices for each currency.
     */
    currencyPrices?: boolean;
  };

  export type UnarchiveProductPricePointRequest = {
    /** The Advanced Billing id of the product to which the price point belongs */
    productId: number;
    /** The Advanced Billing id of the product price point */
    pricePointId: number;
  };

  export type UpdateProductCurrencyPricesRequest = {
    /** The Advanced Billing id of the product price point */
    productPricePointId: number;
    body?: UpdateCurrencyPricesRequest;
  };

  export class UpdateProductCurrencyPricesError extends ApiError {
    declare readonly payload: Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<UpdateProductCurrencyPricesError> = [
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type UpdateProductPricePointRequestParams = {
    /**
     * The id or handle of the product. When using the handle, it must be prefixed with `handle:`.
     * Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle.
     */
    productId: ProductIdModel;
    /**
     * The id or handle of the price point. When using the handle, it must be prefixed with
     * `handle:`. Example: `123` for an integer ID, or `handle:example-product-price-point-handle`
     * for a string handle.
     */
    pricePointId: PricePointIdModel;
    body?: UpdateProductPricePointRequest;
  };
}
