import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import * as s from "../core/validation/index.js";
import { listSaleRepItemSchema, type ListSaleRepItem } from "../models/list-sale-rep-item.js";
import { saleRepSettingsSchema, type SaleRepSettings } from "../models/sale-rep-settings.js";
import { saleRepSchema, type SaleRep } from "../models/sale-rep.js";
import type { Servers } from "../servers.js";

export class SalesCommissions {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * List Sales Commission Settings
   *
   * @remarks
   * Lists subscriptions with associated sales reps.
   *
   * ## Modified Authentication Process
   *
   * The Sales Commission API differs from other Chargify API endpoints. This resource is associated
   * with the seller itself. Up to now all available resources were at the level of the site,
   * therefore creating the API Key per site was a sufficient solution. To share resources at the
   * seller level, a new authentication method was introduced, which is user authentication.
   * Creating an API Key for a user is a required step to correctly use the Sales Commission API,
   * more details
   * [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).
   *
   * Access to the Sales Commission API endpoints is available to users with financial access, where
   * the seller has the Advanced Analytics component enabled. For further information on getting
   * access to Advanced Analytics contact Maxio support.
   *
   * > Note: The request is at seller level, it means `<<subdomain>>` variable will be replaced by
   * `app`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSalesCommissionSettings(
    request: SalesCommissions.ListSalesCommissionSettingsRequest,
    options?: RequestOptions,
  ): ApiPromise<SaleRepSettings[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/sellers/{seller_id}/sales_commission_settings.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "seller_id", value: request.sellerId, schema: s.string() }],
        query: [
          { name: "live_mode", value: request.liveMode, schema: s.optional(s.boolean()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 100) },
        ],
        headers: [
          {
            name: "Authorization",
            value: request.authorization,
            schema: s.defaulted(s.string(), "Bearer <<apiKey>>"),
          },
        ],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => saleRepSettingsSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Sales Reps
   *
   * @remarks
   * Lists sales reps with details.
   *
   * ## Modified Authentication Process
   *
   * The Sales Commission API differs from other Chargify API endpoints. This resource is associated
   * with the seller itself. Up to now all available resources were at the level of the site,
   * therefore creating the API Key per site was a sufficient solution. To share resources at the
   * seller level, a new authentication method was introduced, which is user authentication.
   * Creating an API Key for a user is a required step to correctly use the Sales Commission API,
   * more details
   * [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).
   *
   * Access to the Sales Commission API endpoints is available to users with financial access, where
   * the seller has the Advanced Analytics component enabled. For further information on getting
   * access to Advanced Analytics contact Maxio support.
   *
   * > Note: The request is at seller level, it means `<<subdomain>>` variable will be replaced by
   * `app`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSalesReps(
    request: SalesCommissions.ListSalesRepsRequest,
    options?: RequestOptions,
  ): ApiPromise<ListSaleRepItem[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/sellers/{seller_id}/sales_reps.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "seller_id", value: request.sellerId, schema: s.string() }],
        query: [
          { name: "live_mode", value: request.liveMode, schema: s.optional(s.boolean()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 100) },
        ],
        headers: [
          {
            name: "Authorization",
            value: request.authorization,
            schema: s.defaulted(s.string(), "Bearer <<apiKey>>"),
          },
        ],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => listSaleRepItemSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Sales Rep
   *
   * @remarks
   * Returns a sales rep and attached subscription details.
   *
   * ## Modified Authentication Process
   *
   * The Sales Commission API differs from other Chargify API endpoints. This resource is associated
   * with the seller itself. Up to now all available resources were at the level of the site,
   * therefore creating the API Key per site was a sufficient solution. To share resources at the
   * seller level, a new authentication method was introduced, which is user authentication.
   * Creating an API Key for a user is a required step to correctly use the Sales Commission API,
   * more details
   * [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).
   *
   * Access to the Sales Commission API endpoints is available to users with financial access, where
   * the seller has the Advanced Analytics component enabled. For further information on getting
   * access to Advanced Analytics contact Maxio support.
   *
   * > Note: The request is at seller level, it means `<<subdomain>>` variable will be replaced by
   * `app`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readSalesRep(
    request: SalesCommissions.ReadSalesRepRequest,
    options?: RequestOptions,
  ): ApiPromise<SaleRep, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/sellers/{seller_id}/sales_reps/{sales_rep_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "seller_id", value: request.sellerId, schema: s.string() },
          { name: "sales_rep_id", value: request.salesRepId, schema: s.string() },
        ],
        query: [
          { name: "live_mode", value: request.liveMode, schema: s.optional(s.boolean()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 100) },
        ],
        headers: [
          {
            name: "Authorization",
            value: request.authorization,
            schema: s.defaulted(s.string(), "Bearer <<apiKey>>"),
          },
        ],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: saleRepSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }
}

export namespace SalesCommissions {
  export type ListSalesCommissionSettingsRequest = {
    /** The Chargify id of your seller account */
    sellerId: string;
    /**
     * This parameter indicates if records should be fetched from live mode sites. Default value is
     * true.
     */
    liveMode?: boolean;
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
     * This parameter indicates how many records to fetch in each request. Default value is 100.
     *
     * @default 100
     */
    perPage?: number;
    /**
     * For authorization use user API key. See details
     * [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).
     *
     * @default "Bearer <<apiKey>>"
     */
    authorization?: string;
  };

  export type ListSalesRepsRequest = {
    /** The Chargify id of your seller account */
    sellerId: string;
    /**
     * This parameter indicates if records should be fetched from live mode sites. Default value is
     * true.
     */
    liveMode?: boolean;
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
     * This parameter indicates how many records to fetch in each request. Default value is 100.
     *
     * @default 100
     */
    perPage?: number;
    /**
     * For authorization use user API key. See details
     * [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).
     *
     * @default "Bearer <<apiKey>>"
     */
    authorization?: string;
  };

  export type ReadSalesRepRequest = {
    /** The Chargify id of your seller account */
    sellerId: string;
    /** The Advanced Billing id of sales rep. */
    salesRepId: string;
    /**
     * This parameter indicates if records should be fetched from live mode sites. Default value is
     * true.
     */
    liveMode?: boolean;
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
     * This parameter indicates how many records to fetch in each request. Default value is 100.
     *
     * @default 100
     */
    perPage?: number;
    /**
     * For authorization use user API key. See details
     * [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).
     *
     * @default "Bearer <<apiKey>>"
     */
    authorization?: string;
  };
}
