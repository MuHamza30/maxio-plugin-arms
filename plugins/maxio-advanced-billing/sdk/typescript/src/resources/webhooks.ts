import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  createOrUpdateEndpointRequestSchema,
  type CreateOrUpdateEndpointRequest,
} from "../models/create-or-update-endpoint-request.js";
import {
  enableWebhooksRequestSchema,
  type EnableWebhooksRequest,
} from "../models/enable-webhooks-request.js";
import {
  enableWebhooksResponseSchema,
  type EnableWebhooksResponse,
} from "../models/enable-webhooks-response.js";
import { endpointResponseSchema, type EndpointResponse } from "../models/endpoint-response.js";
import { endpointSchema, type Endpoint } from "../models/endpoint.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  replayWebhooksRequestSchema,
  type ReplayWebhooksRequest,
} from "../models/replay-webhooks-request.js";
import {
  replayWebhooksResponseSchema,
  type ReplayWebhooksResponse,
} from "../models/replay-webhooks-response.js";
import { webhookOrderSchema, type WebhookOrder } from "../models/webhook-order.js";
import { webhookResponseSchema, type WebhookResponse } from "../models/webhook-response.js";
import { webhookStatusSchema, type WebhookStatus } from "../models/webhook-status.js";
import type { Servers } from "../servers.js";

/**
 * The Webhook object represents a single notification sent to your configured endpoint when an
 * event occurs.
 *
 * A webhook tracks delivery status, including when it was last sent, whether the merchant endpoint
 * accepted it, and any error from a failed attempt. For more information, see [Understand Webhooks
 * in Advanced
 * Billing](https://docs.maxio.com/configuration/advanced-billing/webhooks/understand-webhooks-in-advanced-billing).
 */
export class Webhooks {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Endpoint
   *
   * @remarks
   * Creates an endpoint and assigns a list of webhook subscriptions (events) to it. See the
   * [Webhooks Reference](page:introduction/webhooks/webhooks-reference#events) page for available
   * events.
   *
   * @returns OK
   *
   * @throws {@link Webhooks.CreateEndpointError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createEndpoint(
    request: Webhooks.CreateEndpointRequest,
    options?: RequestOptions,
  ): ApiPromise<EndpointResponse, Webhooks.CreateEndpointError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/endpoints.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createOrUpdateEndpointRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: endpointResponseSchema },
        errorFactory: Webhooks.CreateEndpointError,
      },
      options,
    );
  }

  /**
   * Enable Webhooks
   *
   * @remarks
   * Enables webhooks for your site.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  enableWebhooks(
    request: Webhooks.EnableWebhooksRequestParams,
    options?: RequestOptions,
  ): ApiPromise<EnableWebhooksResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/webhooks/settings.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => enableWebhooksRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: enableWebhooksResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Endpoints
   *
   * @remarks
   * Lists endpoints configured for a site.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listEndpoints(options?: RequestOptions): ApiPromise<Endpoint[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/endpoints.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => endpointSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Webhooks
   *
   * @remarks
   * Retrieves a list of webhooks. You can pass query parameters if you want to filter webhooks. See
   * the [Webhooks](page:introduction/webhooks/webhooks) documentation for more information.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listWebhooks(
    request: Webhooks.ListWebhooksRequest,
    options?: RequestOptions,
  ): ApiPromise<WebhookResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/webhooks.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "status", value: request.status, schema: s.optional(s.lazy(() => webhookStatusSchema)) },
          { name: "since_date", value: request.sinceDate, schema: s.optional(s.string()) },
          { name: "until_date", value: request.untilDate, schema: s.optional(s.string()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "order", value: request.order, schema: s.optional(s.lazy(() => webhookOrderSchema)) },
          { name: "subscription", value: request.subscription, schema: s.optional(s.int()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => webhookResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Replay Webhooks
   *
   * @remarks
   * Replays webhooks. Posting to this endpoint does not immediately resend the webhooks. They are
   * added to a queue and sent as soon as possible, depending on available system resources. You can
   * submit an array of up to 1000 webhook IDs in the replay request.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  replayWebhooks(
    request: Webhooks.ReplayWebhooksRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ReplayWebhooksResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/webhooks/replay.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => replayWebhooksRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: replayWebhooksResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Update Endpoint
   *
   * @remarks
   * Updates an Endpoint. You can change the `url` of your endpoint or the list of
   * `webhook_subscriptions` to which you are subscribed. See the [Webhooks
   * Reference](page:introduction/webhooks/webhooks-reference#events) page for available events.
   *
   * Always send a complete list of events to which you want to subscribe. Sending a PUT request for
   * an existing endpoint with an empty list of `webhook_subscriptions` will unsubscribe all events.
   *
   * If you want to unsubscribe from a specific event, send a list of `webhook_subscriptions`
   * without the specific event key.
   *
   * @returns OK
   *
   * @throws {@link Webhooks.UpdateEndpointError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateEndpoint(
    request: Webhooks.UpdateEndpointRequest,
    options?: RequestOptions,
  ): ApiPromise<EndpointResponse, Webhooks.UpdateEndpointError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/endpoints/{endpoint_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "endpoint_id", value: request.endpointId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createOrUpdateEndpointRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: endpointResponseSchema },
        errorFactory: Webhooks.UpdateEndpointError,
      },
      options,
    );
  }
}

export namespace Webhooks {
  export type CreateEndpointRequest = {
    body?: CreateOrUpdateEndpointRequest;
  };

  export class CreateEndpointError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CreateEndpointError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type EnableWebhooksRequestParams = {
    body?: EnableWebhooksRequest;
  };

  export type ListWebhooksRequest = {
    /** Webhooks with matching status would be returned. */
    status?: WebhookStatus;
    /**
     * Format YYYY-MM-DD. Returns Webhooks with the created_at date greater than or equal to the one
     * specified.
     */
    sinceDate?: string;
    /**
     * Format YYYY-MM-DD. Returns Webhooks with the created_at date less than or equal to the one
     * specified.
     */
    untilDate?: string;
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
    /** The order in which the Webhooks are returned. */
    order?: WebhookOrder;
    /** The Advanced Billing id of a subscription you'd like to filter for */
    subscription?: number;
  };

  export type ReplayWebhooksRequestParams = {
    body?: ReplayWebhooksRequest;
  };

  export type UpdateEndpointRequest = {
    /** The Advanced Billing id for the endpoint that should be updated */
    endpointId: number;
    body?: CreateOrUpdateEndpointRequest;
  };

  export class UpdateEndpointError extends ApiError {
    declare readonly payload:
      | Declared<"error404", undefined>
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<UpdateEndpointError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
