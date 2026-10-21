import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { basicDateFieldSchema, type BasicDateField } from "../models/basic-date-field.js";
import {
  createProductFamilyRequestSchema,
  type CreateProductFamilyRequest,
} from "../models/create-product-family-request.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { listProductsFilterSchema, type ListProductsFilter } from "../models/list-products-filter.js";
import { listProductsIncludeSchema, type ListProductsInclude } from "../models/list-products-include.js";
import {
  productFamilyResponseSchema,
  type ProductFamilyResponse,
} from "../models/product-family-response.js";
import { productResponseSchema, type ProductResponse } from "../models/product-response.js";
import type { Servers } from "../servers.js";

export class ProductFamilies {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Product Family
   *
   * @remarks
   * Creates a Product Family within your site. Create a Product Family to act as a container for
   * your products, components, and coupons.
   *
   * Full documentation on how Product Families operate within the Advanced Billing UI can be
   * located [here](https://maxio.zendesk.com/hc/en-us/articles/24261098936205-Product-Families).
   *
   * @returns Created
   *
   * @throws {@link ProductFamilies.CreateProductFamilyError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createProductFamily(
    request: ProductFamilies.CreateProductFamilyRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ProductFamilyResponse, ProductFamilies.CreateProductFamilyError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/product_families.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createProductFamilyRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: productFamilyResponseSchema },
        errorFactory: ProductFamilies.CreateProductFamilyError,
      },
      options,
    );
  }

  /**
   * List Product Families
   *
   * @remarks
   * Lists Product Families for a site.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listProductFamilies(
    request: ProductFamilies.ListProductFamiliesRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductFamilyResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/product_families.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => basicDateFieldSchema)),
          },
          { name: "start_date", value: request.startDate, schema: s.optional(s.dateOnly()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.dateOnly()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.dateTime()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.dateTime()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => productFamilyResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Products for Product Family
   *
   * @remarks
   * Retrieves a list of Products belonging to a Product Family.
   *
   * @returns OK
   *
   * @throws {@link ProductFamilies.ListProductsForProductFamilyError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listProductsForProductFamily(
    request: ProductFamilies.ListProductsForProductFamilyRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductResponse[], ProductFamilies.ListProductsForProductFamilyError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/product_families/{product_family_id}/products.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.string() }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
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
          { name: "start_date", value: request.startDate, schema: s.optional(s.dateOnly()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.dateOnly()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.dateTime()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.dateTime()) },
          { name: "include_archived", value: request.includeArchived, schema: s.optional(s.boolean()) },
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.lazy(() => listProductsIncludeSchema)),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => productResponseSchema)) },
        errorFactory: ProductFamilies.ListProductsForProductFamilyError,
      },
      options,
    );
  }

  /**
   * Read Product Family
   *
   * @remarks
   * Retrieves a Product Family via the `product_family_id`. The response will contain a Product
   * Family object.
   *
   * The product family can be specified either with the id number, or with the `handle:my-family`
   * format.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readProductFamily(
    request: ProductFamilies.ReadProductFamilyRequest,
    options?: RequestOptions,
  ): ApiPromise<ProductFamilyResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/product_families/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: productFamilyResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }
}

export namespace ProductFamilies {
  export type CreateProductFamilyRequestParams = {
    body?: CreateProductFamilyRequest;
  };

  export class CreateProductFamilyError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CreateProductFamilyError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListProductFamiliesRequest = {
    /**
     * The type of filter you would like to apply to your search. Use in query:
     * `date_field=created_at`.
     */
    dateField?: BasicDateField;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with
     * a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
     * timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     */
    endDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns products with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of start_date.
     */
    startDatetime?: Date;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns products with a timestamp at or before exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of end_date.
     */
    endDatetime?: Date;
  };

  export type ListProductsForProductFamilyRequest = {
    /** Either the product family's id or its handle prefixed with `handle:` */
    productFamilyId: string;
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
    /**
     * The type of filter you would like to apply to your search. Use in query:
     * `date_field=created_at`.
     */
    dateField?: BasicDateField;
    /** Filter to use for List Products operations */
    filter?: ListProductsFilter;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with
     * a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
     * timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     */
    endDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns products with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of start_date.
     */
    startDatetime?: Date;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns products with a timestamp at or before exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of end_date.
     */
    endDatetime?: Date;
    /** Include archived products. */
    includeArchived?: boolean;
    /**
     * Allows including additional data in the response. Use in query
     * `include=prepaid_product_price_point`.
     */
    include?: ListProductsInclude;
  };

  export class ListProductsForProductFamilyError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", string>>;

    static readonly errors: ErrorDecoders<ListProductsForProductFamilyError> = [
      { on: 404, kind: "error404", decode: { kind: "json", schema: s.string() } },
    ];
  }

  export type ReadProductFamilyRequest = {
    /** The Advanced Billing id of the product family */
    id: number;
  };
}
