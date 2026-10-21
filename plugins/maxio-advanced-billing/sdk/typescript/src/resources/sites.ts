import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { CleanupScope, cleanupScopeSchema } from "../models/cleanup-scope.js";
import {
  listPublicKeysResponseSchema,
  type ListPublicKeysResponse,
} from "../models/list-public-keys-response.js";
import { siteResponseSchema, type SiteResponse } from "../models/site-response.js";
import type { Servers } from "../servers.js";

export class Sites {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Clear Site Data
   *
   * @remarks
   * Clears all data from a test site asynchronously. This call is asynchronous and there may be a
   * delay before the site data is fully deleted. If you are clearing site data for an automated
   * test, you will need to build in a delay and/or check that there are no products, etc., in the
   * site before proceeding.
   *
   * **This functionality will only work on sites in TEST mode. Attempts to perform this on sites in
   * “live” mode will result in a response of 403 FORBIDDEN.**
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  clearSite(request: Sites.ClearSiteRequest, options?: RequestOptions): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/sites/clear_data.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          {
            name: "cleanup_scope",
            value: request.cleanupScope,
            schema: s.defaulted(cleanupScopeSchema, CleanupScope.All),
          },
        ],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Maxio.js (formerly Chargify.js) Public Keys
   *
   * @remarks
   * Lists public keys used for Maxio.js (formerly Chargify.js).
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listChargifyJsPublicKeys(
    request: Sites.ListChargifyJsPublicKeysRequest,
    options?: RequestOptions,
  ): ApiPromise<ListPublicKeysResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/chargify_js_keys.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listPublicKeysResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Site
   *
   * @remarks
   * Retrieves site data.
   *
   * For more information, see
   * [Sites](https://maxio.zendesk.com/hc/en-us/sections/24250550707085-Sites) in the product
   * documentation. Specifically, the [Clearing Site
   * Data](https://maxio.zendesk.com/hc/en-us/articles/24250617028365-Clearing-Site-Data) section is
   * relevant to this endpoint.
   *
   * #### Relationship invoicing enabled
   * If the site has Relationship invoicing enabled, additional properties are returned in the
   * response:
   *
   * ```
   * "customer_hierarchy_enabled": true,
   * "whopays_enabled": true,
   * "whopays_default_payer": "self"
   * ```
   *
   * For more information, see [Who Pays & Customer
   * Hierarchy](https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays).
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readSite(options?: RequestOptions): ApiPromise<SiteResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/site.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: siteResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }
}

export namespace Sites {
  export type ClearSiteRequest = {
    /**
     * `all`: Will clear all products, customers, and related subscriptions from the site.
     * `customers`: Will clear only customers and related subscriptions (leaving the products
     * untouched) for the site. Revenue will also be reset to 0. Use in query `cleanup_scope=all`.
     *
     * @default CleanupScope.All
     */
    cleanupScope?: CleanupScope;
  };

  export type ListChargifyJsPublicKeysRequest = {
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
}
