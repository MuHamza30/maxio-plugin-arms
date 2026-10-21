import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import * as s from "../core/validation/index.js";
import { countResponseSchema, type CountResponse } from "../models/count-response.js";
import { Direction, directionSchema } from "../models/direction.js";
import { eventKeySchema, type EventKey } from "../models/event-key.js";
import { eventResponseSchema, type EventResponse } from "../models/event-response.js";
import { listEventsDateFieldSchema, type ListEventsDateField } from "../models/list-events-date-field.js";
import type { Servers } from "../servers.js";

export class Events {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * List Events
   *
   * @remarks
   * Lists events for a site.
   *
   * Events include various activity that happens around a Site. This information is **especially**
   * useful to track down issues that arise when subscriptions are not created due to errors.
   *
   * Within the UI, Events are referred to as Site Activity. For more information, see [Site
   * Activity](https://maxio.zendesk.com/hc/en-us/articles/24250671733517-Site-Activity).
   *
   * Use query string filters to narrow down results. You can use the `filter` parameter to filter
   * by event key.
   *
   * ### Legacy Filters
   *
   * The following keys are no longer supported.
   *
   * + `payment_failure_recreated`
   * + `payment_success_recreated`
   * + `renewal_failure_recreated`
   * + `renewal_success_recreated`
   * + `zferral_revenue_post_failure` - (Specific to the deprecated Zferral integration)
   * + `zferral_revenue_post_success` - (Specific to the deprecated Zferral integration)
   *
   * ## Event Key
   * The event type is identified by the key property. See [Event Key]($m/Event%20Key) for a
   * complete list of supported keys.
   *
   * ## Event Specific Data
   *
   * Different event types may include additional data in `event_specific_data` property. While some
   * events share the same schema for `event_specific_data`, others may not include it at all. For
   * precise mappings from key to event_specific_data, refer to [Event]($m/Event).
   *
   * ### Example
   * Here’s an example event for the `subscription_product_change` event:
   *
   * ```
   * {
   *     "event": {
   *         "id": 351,
   *         "key": "subscription_product_change",
   *         "message": "Product changed on Mark Alan's subscription from 'Basic' to 'Pro'",
   *         "subscription_id": 205,
   *         "event_specific_data": {
   *             "new_product_id": 3,
   *             "previous_product_id": 2
   *         },
   *         "created_at": "2012-01-30T10:43:31-05:00"
   *     }
   * }
   * ```
   *
   * Here’s an example event for the `subscription_state_change` event:
   *
   * ```
   *  {
   *      "event": {
   *          "id": 353,
   *          "key": "subscription_state_change",
   *          "message": "State changed on Mark Alan's subscription to Pro from trialing to active",
   *          "subscription_id": 205,
   *          "event_specific_data": {
   *              "new_subscription_state": "active",
   *              "previous_subscription_state": "trialing"
   *          },
   *          "created_at": "2012-01-30T10:43:33-05:00"
   *      }
   *  }
   * ```
   *
   * ## Enhanced Catalog Experience
   *
   * If you’re using the [enhanced Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology),
   * you’ll see updated naming in webhook events and messages.
   *
   * Event name changes:
   *
   * - subscription_product_change → subscription_plan_change
   * - component_allocation_change → allocation_change
   * - component_billing_date_change → product_billing_date_change
   *
   * Message updates:
   *
   * - “Plan changed on Subscription from previous plan to new plan”
   * - “Successful payment for allocation changes to Product on Subscription”
   * - “Failed payment for allocation changes to Product on Subscription”
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listEvents(
    request: Events.ListEventsRequest,
    options?: RequestOptions,
  ): ApiPromise<EventResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/events.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "since_id", value: request.sinceId, schema: s.optional(s.int()) },
          { name: "max_id", value: request.maxId, schema: s.optional(s.int()) },
          {
            name: "direction",
            value: request.direction,
            schema: s.defaulted(directionSchema, Direction.Desc),
          },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.array(s.lazy(() => eventKeySchema))),
          },
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => listEventsDateFieldSchema)),
          },
          { name: "start_date", value: request.startDate, schema: s.optional(s.string()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.string()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.string()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.string()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => eventResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Events for Subscription
   *
   * @remarks
   * Lists events for a subscription.
   *
   * ## Event Key
   * The event type is identified by the key property. See [Event Key]($m/Event%20Key) for a
   * complete list of supported keys.
   *
   * ## Event Specific Data
   *
   * Different event types may include additional data in `event_specific_data` property. While some
   * events share the same schema for `event_specific_data`, others may not include it at all. For
   * precise mappings from key to event_specific_data, refer to [Event]($m/Event).
   *
   * ## Enhanced Catalog Experience
   *
   * If you’re using the [enhanced Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology),
   * you’ll see updated naming in webhook events and messages.
   *
   * Event name changes:
   *
   * - subscription_product_change → subscription_plan_change
   * - component_allocation_change → allocation_change
   * - component_billing_date_change → product_billing_date_change
   *
   * Message updates:
   *
   * - “Successful payment for allocation changes to Product on Subscription”
   * - “Failed payment for allocation changes to Product on Subscription”
   * - “Plan changed on Subscription from previous plan to new plan”
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSubscriptionEvents(
    request: Events.ListSubscriptionEventsRequest,
    options?: RequestOptions,
  ): ApiPromise<EventResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/events.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "since_id", value: request.sinceId, schema: s.optional(s.int()) },
          { name: "max_id", value: request.maxId, schema: s.optional(s.int()) },
          {
            name: "direction",
            value: request.direction,
            schema: s.defaulted(directionSchema, Direction.Desc),
          },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.array(s.lazy(() => eventKeySchema))),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => eventResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Total Event Count
   *
   * @remarks
   * Returns the total count of events for a given site.
   *
   * If you’re using the [enhanced Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology),
   * you’ll see updated naming in webhook events and messages.
   *
   * Event name changes:
   *
   * - subscription_product_change → subscription_plan_change
   * - component_allocation_change → allocation_change
   * - component_billing_date_change → product_billing_date_change
   *
   * Message updates:
   *
   * - “Successful payment for allocation changes to Product on Subscription”
   * - “Failed payment for allocation changes to Product on Subscription”
   * - “Plan changed on Subscription from previous plan to new plan”
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readEventsCount(
    request: Events.ReadEventsCountRequest,
    options?: RequestOptions,
  ): ApiPromise<CountResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/events/count.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "since_id", value: request.sinceId, schema: s.optional(s.int()) },
          { name: "max_id", value: request.maxId, schema: s.optional(s.int()) },
          {
            name: "direction",
            value: request.direction,
            schema: s.defaulted(directionSchema, Direction.Desc),
          },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.array(s.lazy(() => eventKeySchema))),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: countResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }
}

export namespace Events {
  export type ListEventsRequest = {
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
    /** Returns events with an id greater than or equal to the one specified. */
    sinceId?: number;
    /** Returns events with an id less than or equal to the one specified. */
    maxId?: number;
    /** The sort direction of the returned events. @default Direction.Desc */
    direction?: Direction;
    /**
     * You can pass multiple event keys after comma. Use in query
     * `filter=signup_success,payment_success`.
     */
    filter?: EventKey[];
    /** The type of filter you would like to apply to your search. */
    dateField?: ListEventsDateField;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components
     * with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
     * a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     */
    endDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of start_date.
     */
    startDatetime?: string;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or before exact time provided in query. You can
     * specify timezone in query - otherwise your site's time zone will be used. If provided, this
     * parameter will be used instead of end_date.
     */
    endDatetime?: string;
  };

  export type ListSubscriptionEventsRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
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
    /** Returns events with an id greater than or equal to the one specified. */
    sinceId?: number;
    /** Returns events with an id less than or equal to the one specified. */
    maxId?: number;
    /** The sort direction of the returned events. @default Direction.Desc */
    direction?: Direction;
    /**
     * You can pass multiple event keys after comma. Use in query
     * `filter=signup_success,payment_success`.
     */
    filter?: EventKey[];
  };

  export type ReadEventsCountRequest = {
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
    /** Returns events with an id greater than or equal to the one specified. */
    sinceId?: number;
    /** Returns events with an id less than or equal to the one specified. */
    maxId?: number;
    /** The sort direction of the returned events. @default Direction.Desc */
    direction?: Direction;
    /**
     * You can pass multiple event keys after comma. Use in query
     * `filter=signup_success,payment_success`.
     */
    filter?: EventKey[];
  };
}
