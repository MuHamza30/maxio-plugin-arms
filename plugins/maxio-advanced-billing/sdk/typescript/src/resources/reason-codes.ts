import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  createReasonCodeRequestSchema,
  type CreateReasonCodeRequest,
} from "../models/create-reason-code-request.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { okResponseSchema, type OkResponse } from "../models/ok-response.js";
import { reasonCodeResponseSchema, type ReasonCodeResponse } from "../models/reason-code-response.js";
import {
  updateReasonCodeRequestSchema,
  type UpdateReasonCodeRequest,
} from "../models/update-reason-code-request.js";
import type { Servers } from "../servers.js";

/**
 * The Reason Code object defines a churn reason that can be presented to customers when they cancel
 * a subscription, such as "too expensive" or "switching providers."
 *
 * Reason codes give merchants visibility into why subscribers are canceling. For more information,
 * see [Configure Churn Reason
 * Codes](https://docs.maxio.com/configuration/advanced-billing/settings/churn-reason-codes).
 */
export class ReasonCodes {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Reason Code
   *
   * @remarks
   * Creates a reason code for a given site.
   *
   * Reason Codes are a way to gain a high-level view of why your customers are cancelling the
   * subscription to your product or service.
   *
   * Add a set of churn reason codes to be displayed in-app and/or the Maxio Billing Portal. As your
   * subscribers decide to cancel their subscription, learn why they decided to cancel.
   *
   * For more information, see [Churn Reason
   * Codes](https://maxio.zendesk.com/hc/en-us/articles/24286647554701-Churn-Reason-Codes).
   *
   * @returns OK
   *
   * @throws {@link ReasonCodes.CreateReasonCodeError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createReasonCode(
    request: ReasonCodes.CreateReasonCodeRequestParams = {},
    options?: RequestOptions,
  ): ApiPromise<ReasonCodeResponse, ReasonCodes.CreateReasonCodeError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/reason_codes.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createReasonCodeRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: reasonCodeResponseSchema },
        errorFactory: ReasonCodes.CreateReasonCodeError,
      },
      options,
    );
  }

  /**
   * Delete Reason Code
   *
   * @remarks
   * Deletes a reason code from the Churn Reason Codes. This code will be immediately removed. This
   * action is not reversible.
   *
   * @returns OK
   *
   * @throws {@link ReasonCodes.DeleteReasonCodeError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteReasonCode(
    request: ReasonCodes.DeleteReasonCodeRequest,
    options?: RequestOptions,
  ): ApiPromise<OkResponse, ReasonCodes.DeleteReasonCodeError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/reason_codes/{reason_code_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "reason_code_id", value: request.reasonCodeId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: okResponseSchema },
        errorFactory: ReasonCodes.DeleteReasonCodeError,
      },
      options,
    );
  }

  /**
   * List Reason Codes
   *
   * @remarks
   * Lists all current churn codes for a given site.
   *
   * @returns OK
   *
   * @throws {@link ReasonCodes.ListReasonCodesError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listReasonCodes(
    request: ReasonCodes.ListReasonCodesRequest = {},
    options?: RequestOptions,
  ): ApiPromise<ReasonCodeResponse[], ReasonCodes.ListReasonCodesError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/reason_codes.json"),
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
        success: { kind: "json", schema: s.array(s.lazy(() => reasonCodeResponseSchema)) },
        errorFactory: ReasonCodes.ListReasonCodesError,
      },
      options,
    );
  }

  /**
   * Read Reason Code
   *
   * @remarks
   * Returns a particular churn reason code for a given site by its unique ID.
   *
   * @returns OK
   *
   * @throws {@link ReasonCodes.ReadReasonCodeError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readReasonCode(
    request: ReasonCodes.ReadReasonCodeRequest,
    options?: RequestOptions,
  ): ApiPromise<ReasonCodeResponse, ReasonCodes.ReadReasonCodeError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/reason_codes/{reason_code_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "reason_code_id", value: request.reasonCodeId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: reasonCodeResponseSchema },
        errorFactory: ReasonCodes.ReadReasonCodeError,
      },
      options,
    );
  }

  /**
   * Update Reason Code
   *
   * @remarks
   * Updates an existing reason code for a given site.
   *
   * @returns OK
   *
   * @throws {@link ReasonCodes.UpdateReasonCodeError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateReasonCode(
    request: ReasonCodes.UpdateReasonCodeRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ReasonCodeResponse, ReasonCodes.UpdateReasonCodeError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/reason_codes/{reason_code_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "reason_code_id", value: request.reasonCodeId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateReasonCodeRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: reasonCodeResponseSchema },
        errorFactory: ReasonCodes.UpdateReasonCodeError,
      },
      options,
    );
  }
}

export namespace ReasonCodes {
  export type CreateReasonCodeRequestParams = {
    body?: CreateReasonCodeRequest;
  };

  export class CreateReasonCodeError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CreateReasonCodeError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type DeleteReasonCodeRequest = {
    /** The Advanced Billing id of the reason code */
    reasonCodeId: number;
  };

  export class DeleteReasonCodeError extends ApiError {
    declare readonly payload: Declared<"error404", undefined> | Undeclared;

    static readonly errors: ErrorDecoders<DeleteReasonCodeError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ListReasonCodesRequest = {
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

  export class ListReasonCodesError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<ListReasonCodesError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadReasonCodeRequest = {
    /** The Advanced Billing id of the reason code */
    reasonCodeId: number;
  };

  export class ReadReasonCodeError extends ApiError {
    declare readonly payload: Declared<"error404", undefined> | Undeclared;

    static readonly errors: ErrorDecoders<ReadReasonCodeError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type UpdateReasonCodeRequestParams = {
    /** The Advanced Billing id of the reason code */
    reasonCodeId: number;
    body?: UpdateReasonCodeRequest;
  };

  export class UpdateReasonCodeError extends ApiError {
    declare readonly payload:
      | Declared<"error404", undefined>
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<UpdateReasonCodeError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
