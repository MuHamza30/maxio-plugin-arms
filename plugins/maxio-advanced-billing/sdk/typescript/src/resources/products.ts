import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { basicDateFieldSchema, type BasicDateField } from "../models/basic-date-field.js";
import {
  createOrUpdateProductRequestSchema,
  type CreateOrUpdateProductRequest,
} from "../models/create-or-update-product-request.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { listProductsFilterSchema, type ListProductsFilter } from "../models/list-products-filter.js";
import { listProductsIncludeSchema, type ListProductsInclude } from "../models/list-products-include.js";
import { productResponseSchema, type ProductResponse } from "../models/product-response.js";
import type { Servers } from "../servers.js";

export class Products {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Archive Product
   *
   * @remarks
   * Archives the product. All current subscribers will be unaffected; their subscription/purchase
   * will continue to be charged monthly.
   *
   * This will restrict the option to chose the product for purchase via the Billing Portal, as well
   * as disable Public Signup Pages for the product.
   *
   * @returns OK
   *
   * @throws {@link Products.ArchiveProductError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  archiveProduct(
    request: Products.ArchiveProductRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductResponse, Products.ArchiveProductError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/products/{product_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_id", value: request.productId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: productResponseSchema },
        errorFactory: Products.ArchiveProductError,
      },
      options,
    );
  }

  /**
   * Create Product
   *
   * @remarks
   * Creates a product in your site.
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, the `auto_create_signup_page` parameter is not supported. If `auto_create_signup_page`
   * is included (with any value) an error is returned.
   *
   * For more information, see:
   *
   * + [Products
   *   Overview](https://maxio.zendesk.com/hc/en-us/articles/24261090117645-Products-Overview)
   * + [Changing a Subscription's
   *   Product](https://maxio.zendesk.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations)
   *
   * @returns Created
   *
   * @throws {@link Products.CreateProductError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createProduct(
    request: Products.CreateProductRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductResponse, Products.CreateProductError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/product_families/{product_family_id}/products.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createOrUpdateProductRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: productResponseSchema },
        errorFactory: Products.CreateProductError,
      },
      options,
    );
  }

  /**
   * List Products
   *
   * @remarks
   * Lists products belonging to a site.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listProducts(
    request: Products.ListProductsRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/products.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => basicDateFieldSchema)),
          },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listProductsFilterSchema)),
          },
          { name: "end_date", value: request.endDate, schema: s.optional(s.dateOnly()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.dateTime()) },
          { name: "start_date", value: request.startDate, schema: s.optional(s.dateOnly()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.dateTime()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "include_archived", value: request.includeArchived, schema: s.optional(s.boolean()) },
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.lazy(() => listProductsIncludeSchema)),
          },
          {
            name: "include_features",
            value: request.includeFeatures,
            schema: s.defaulted(s.boolean(), false),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => productResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Product
   *
   * @remarks
   * Reads the current details of a product.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readProduct(
    request: Products.ReadProductRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/products/{product_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_id", value: request.productId, schema: s.int() }],
        query: [
          {
            name: "include_features",
            value: request.includeFeatures,
            schema: s.defaulted(s.boolean(), false),
          },
        ],
        headers: [],
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
   * Read Product by Handle
   *
   * @remarks
   * Retrieves a Product object by its `api_handle`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readProductByHandle(
    request: Products.ReadProductByHandleRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/products/handle/{api_handle}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "api_handle", value: request.apiHandle, schema: s.string() }],
        query: [],
        headers: [],
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
   * Update Product
   *
   * @remarks
   * Updates aspects of an existing product.
   *
   * ### Input Attributes Update Notes
   *
   * + `update_return_params` The parameters we will append to your `update_return_url`. See Return
   *   URLs and Parameters
   *
   * ### Product Price Point
   *
   * Updating a product using this endpoint will create a new price point and set it as the default
   * price point for this product. If you should like to update an existing product price point,
   * that must be done separately.
   *
   * @returns OK
   *
   * @throws {@link Products.UpdateProductError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateProduct(
    request: Products.UpdateProductRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductResponse, Products.UpdateProductError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/products/{product_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_id", value: request.productId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createOrUpdateProductRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: productResponseSchema },
        errorFactory: Products.UpdateProductError,
      },
      options,
    );
  }
}

export namespace Products {
  export type ArchiveProductRequest = {
    /** The Advanced Billing id of the product */
    productId: number;
  };

  export class ArchiveProductError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ArchiveProductError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateProductRequest = {
    /** Either the product family's id or its handle prefixed with `handle:` */
    productFamilyId: string;
    body?: CreateOrUpdateProductRequest;
  };

  export class CreateProductError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CreateProductError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListProductsRequest = {
    /**
     * The type of filter you would like to apply to your search. Use in query:
     * `date_field=created_at`.
     */
    dateField?: BasicDateField;
    /** Filter to use for List Products operations */
    filter?: ListProductsFilter;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
     * timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     */
    endDate?: string;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns products with a timestamp at or before exact time provided in query. You can specify
     * timezone in query - otherwise your site''s time zone will be used. If provided, this
     * parameter will be used instead of end_date.
     */
    endDatetime?: Date;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with
     * a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns products with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site''s time zone will be used. If provided, this
     * parameter will be used instead of start_date.
     */
    startDatetime?: Date;
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
    /** Include archived products. Use in query: `include_archived=true`. */
    includeArchived?: boolean;
    /**
     * Allows including additional data in the response. Use in query
     * `include=prepaid_product_price_point`.
     */
    include?: ListProductsInclude;
    /**
     * When `true`, embeds the active feature catalog items for each result in a `features` array.
     * Default value is `false`.
     *
     * @default false
     */
    includeFeatures?: boolean;
  };

  export type ReadProductRequest = {
    /** The Advanced Billing id of the product */
    productId: number;
    /**
     * When `true`, embeds the active feature catalog items for each result in a `features` array.
     * Default value is `false`.
     *
     * @default false
     */
    includeFeatures?: boolean;
  };

  export type ReadProductByHandleRequest = {
    /** The handle of the product */
    apiHandle: string;
  };

  export type UpdateProductRequest = {
    /** The Advanced Billing id of the product */
    productId: number;
    body?: CreateOrUpdateProductRequest;
  };

  export class UpdateProductError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<UpdateProductError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
