import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import * as s from "../core/validation/index.js";
import { directionSchema, type Direction } from "../models/direction.js";
import { listMrrFilterSchema, type ListMrrFilter } from "../models/list-mrr-filter.js";
import { listMrrResponseSchema, type ListMrrResponse } from "../models/list-mrr-response.js";
import { mrrResponseSchema, type MrrResponse } from "../models/mrr-response.js";
import { siteSummarySchema, type SiteSummary } from "../models/site-summary.js";
import { sortingDirectionSchema, type SortingDirection } from "../models/sorting-direction.js";
import {
  subscriptionMrrResponseSchema,
  type SubscriptionMrrResponse,
} from "../models/subscription-mrr-response.js";
import {
  subscriptionsMrrErrorResponse1Schema,
  type SubscriptionsMrrErrorResponse1,
} from "../models/subscriptions-mrr-error-response1.js";
import type { Servers } from "../servers.js";

/**
 * The Insights endpoints provide aggregate site-level statistics, such as customer and subscription
 * counts, giving a high-level snapshot of account activity.
 */
export class Insights {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * List MRR Movements
   *
   * @remarks
   * Lists your site's MRR movements.
   *
   * ## Understanding MRR movements
   *
   * This endpoint will aid in accessing your site's [MRR
   * Report](https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics) data.
   *
   * Whenever a subscription event occurs that causes your site's MRR to change (such as a signup or
   * upgrade), we record an MRR movement. These records are accessible via the MRR Movements
   * endpoint.
   *
   * Each MRR Movement belongs to a subscription and contains a timestamp, category, and an amount.
   * `line_items` represent the subscription's product configuration at the time of the movement.
   *
   * ### Plan & Usage Breakouts
   *
   * In the MRR Report UI, we support a setting to [include or
   * exclude](https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics#displaying-component-based-metered-usage-in-mrr)
   * usage revenue. In the MRR APIs, responses include `plan` and `usage` breakouts.
   *
   * Plan includes revenue from:
   * * Products
   * * Quantity-Based Components
   * * On/Off Components
   *
   * Usage includes revenue from:
   * * Metered Components
   * * Prepaid Usage Components
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   *
   * @deprecated
   */
  listMrrMovements(
    request: Insights.ListMrrMovementsRequest = {},
    options?: RequestOptions,
  ): ApiPromise<ListMrrResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/mrr_movements.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.optional(s.int()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 10) },
          {
            name: "direction",
            value: request.direction,
            schema: s.optional(s.lazy(() => sortingDirectionSchema)),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listMrrResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List MRR per subscription
   *
   * @remarks
   * Lists your site's current MRR, including plan and usage breakouts split per subscription.
   *
   * @returns OK
   *
   * @throws {@link Insights.ListMrrPerSubscriptionError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   *
   * @deprecated
   */
  listMrrPerSubscription(
    request: Insights.ListMrrPerSubscriptionRequest = {},
    options?: RequestOptions,
  ): ApiPromise<SubscriptionMrrResponse, Insights.ListMrrPerSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions_mrr.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "filter", value: request.filter, schema: s.optional(s.lazy(() => listMrrFilterSchema)) },
          { name: "at_time", value: request.atTime, schema: s.optional(s.string()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "direction", value: request.direction, schema: s.optional(s.lazy(() => directionSchema)) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionMrrResponseSchema },
        errorFactory: Insights.ListMrrPerSubscriptionError,
      },
      options,
    );
  }

  /**
   * Read MRR
   *
   * @remarks
   * Returns your site's current MRR, including plan and usage breakouts.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   *
   * @deprecated
   */
  readMrr(
    request: Insights.ReadMrrRequest = {},
    options?: RequestOptions,
  ): ApiPromise<MrrResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/mrr.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "at_time", value: request.atTime, schema: s.optional(s.dateTime()) },
          { name: "subscription_id", value: request.subscriptionId, schema: s.optional(s.int()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: mrrResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Site Stats
   *
   * @remarks
   * Returns basic site-level stats. This API call only answers with JSON responses. An XML version
   * is not provided.
   *
   * ## Stats Documentation
   *
   * There currently is not a complimentary matching set of documentation that compliments this
   * endpoint. However, each Site's dashboard will reflect the summary of information provided in
   * the Stats response.
   *
   * ```
   * https://subdomain.chargify.com/dashboard
   * ```
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readSiteStats(options?: RequestOptions): ApiPromise<SiteSummary, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/stats.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: siteSummarySchema },
        errorFactory: ApiError,
      },
      options,
    );
  }
}

export namespace Insights {
  export type ListMrrMovementsRequest = {
    /** (Optional) Filter results by subscription. */
    subscriptionId?: number;
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
     * maximum allowed values is 50; any per_page value over 50 will be changed to 50. Use in query
     * `per_page=20`.
     *
     * @default 10
     */
    perPage?: number;
    /** Controls the order in which results are returned. Use in query `direction=asc`. */
    direction?: SortingDirection;
  };

  export type ListMrrPerSubscriptionRequest = {
    /** Filter to use for List MRR per subscription operation */
    filter?: ListMrrFilter;
    /**
     * Submit a timestamp in ISO8601 format to request MRR for a historic time. Use in query:
     * `at_time=2022-01-10T10:00:00-05:00`.
     */
    atTime?: string;
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
     * Controls the order in which results are returned. Records are ordered by subscription_id in
     * ascending order by default. Use in query `direction=desc`.
     */
    direction?: Direction;
  };

  export class ListMrrPerSubscriptionError extends ApiError {
    declare readonly payload:
      | Declared<"subscriptionsMrrErrorResponse1", SubscriptionsMrrErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ListMrrPerSubscriptionError> = [
      {
        on: 400,
        kind: "subscriptionsMrrErrorResponse1",
        decode: { kind: "json", schema: subscriptionsMrrErrorResponse1Schema },
      },
    ];
  }

  export type ReadMrrRequest = {
    /** submit a timestamp in ISO8601 format to request MRR for a historic time. */
    atTime?: Date;
    /** submit the id of a subscription in order to limit results. */
    subscriptionId?: number;
  };
}
