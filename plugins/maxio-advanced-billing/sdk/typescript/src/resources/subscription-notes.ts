import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  subscriptionNoteResponseSchema,
  type SubscriptionNoteResponse,
} from "../models/subscription-note-response.js";
import {
  updateSubscriptionNoteRequestSchema,
  type UpdateSubscriptionNoteRequest,
} from "../models/update-subscription-note-request.js";
import type { Servers } from "../servers.js";

export class SubscriptionNotes {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Subscription Note
   *
   * @remarks
   * Creates a note for a subscription.
   *
   * Notes allow you to record information about a particular Subscription in a free text format.
   *
   * If you have structured data such as birth date, color, etc., consider using
   * [Metadata]($e/Custom%20Fields/createMetadata) instead.
   *
   * For more information, see [Adding
   * Notes](https://docs.maxio.com/hc/en-us/articles/24251654953997-Understanding-the-Subscription-Summary-Page#billing-portal-status:~:text=documentation%20for%20more.-,Adding%20Notes,-Notes%20are%20optional)
   * in the product documentation.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionNotes.CreateSubscriptionNoteError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createSubscriptionNote(
    request: SubscriptionNotes.CreateSubscriptionNoteRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionNoteResponse, SubscriptionNotes.CreateSubscriptionNoteError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/notes.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateSubscriptionNoteRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionNoteResponseSchema },
        errorFactory: SubscriptionNotes.CreateSubscriptionNoteError,
      },
      options,
    );
  }

  /**
   * Delete Subscription Note
   *
   * @remarks
   * Deletes a note for a Subscription.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteSubscriptionNote(
    request: SubscriptionNotes.DeleteSubscriptionNoteRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/notes/{note_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "note_id", value: request.noteId, schema: s.int() },
        ],
        query: [],
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
   * List Subscription Notes
   *
   * @remarks
   * Retrieves a list of notes associated with a subscription. The response will be an array of
   * Notes.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionNotes.ListSubscriptionNotesError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSubscriptionNotes(
    request: SubscriptionNotes.ListSubscriptionNotesRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionNoteResponse[], SubscriptionNotes.ListSubscriptionNotesError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/notes.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => subscriptionNoteResponseSchema)) },
        errorFactory: SubscriptionNotes.ListSubscriptionNotesError,
      },
      options,
    );
  }

  /**
   * Read Subscription Note
   *
   * @remarks
   * Retrieves a specific note attached to a subscription.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readSubscriptionNote(
    request: SubscriptionNotes.ReadSubscriptionNoteRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionNoteResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/notes/{note_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "note_id", value: request.noteId, schema: s.int() },
        ],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionNoteResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Update Subscription Note
   *
   * @remarks
   * Updates a note for a subscription.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionNotes.UpdateSubscriptionNoteError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateSubscriptionNote(
    request: SubscriptionNotes.UpdateSubscriptionNoteRequestParams,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionNoteResponse, SubscriptionNotes.UpdateSubscriptionNoteError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/notes/{note_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "note_id", value: request.noteId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateSubscriptionNoteRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionNoteResponseSchema },
        errorFactory: SubscriptionNotes.UpdateSubscriptionNoteError,
      },
      options,
    );
  }
}

export namespace SubscriptionNotes {
  export type CreateSubscriptionNoteRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: UpdateSubscriptionNoteRequest;
  };

  export class CreateSubscriptionNoteError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CreateSubscriptionNoteError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type DeleteSubscriptionNoteRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The Advanced Billing id of the note */
    noteId: number;
  };

  export type ListSubscriptionNotesRequest = {
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
  };

  export class ListSubscriptionNotesError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ListSubscriptionNotesError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadSubscriptionNoteRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The Advanced Billing id of the note */
    noteId: number;
  };

  export type UpdateSubscriptionNoteRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The Advanced Billing id of the note */
    noteId: number;
    body?: UpdateSubscriptionNoteRequest;
  };

  export class UpdateSubscriptionNoteError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<UpdateSubscriptionNoteError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
