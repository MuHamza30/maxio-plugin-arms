import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  deductServiceCreditRequestSchema,
  type DeductServiceCreditRequest,
} from "../models/deduct-service-credit-request.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  issueServiceCreditRequestSchema,
  type IssueServiceCreditRequest,
} from "../models/issue-service-credit-request.js";
import {
  listPrepaymentsFilterSchema,
  type ListPrepaymentsFilter,
} from "../models/list-prepayments-filter.js";
import {
  listSubscriptionGroupPrepaymentResponseSchema,
  type ListSubscriptionGroupPrepaymentResponse,
} from "../models/list-subscription-group-prepayment-response.js";
import {
  serviceCreditResponseSchema,
  type ServiceCreditResponse,
} from "../models/service-credit-response.js";
import { serviceCreditSchema, type ServiceCredit } from "../models/service-credit.js";
import {
  subscriptionGroupPrepaymentRequestSchema,
  type SubscriptionGroupPrepaymentRequest,
} from "../models/subscription-group-prepayment-request.js";
import {
  subscriptionGroupPrepaymentResponseSchema,
  type SubscriptionGroupPrepaymentResponse,
} from "../models/subscription-group-prepayment-response.js";
import type { Servers } from "../servers.js";

export class SubscriptionGroupInvoiceAccount {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Subscription Group Prepayment
   *
   * @remarks
   * Adds a prepayment for a subscription group. This endpoint requires an `amount`, `details`,
   * `method`, and `memo`. On success, the prepayment will be added to the group's prepayment
   * balance.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroupInvoiceAccount.CreateSubscriptionGroupPrepaymentError} when the
   * API answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createSubscriptionGroupPrepayment(
    request: SubscriptionGroupInvoiceAccount.CreateSubscriptionGroupPrepaymentRequest,
    options?: RequestOptions,
  ): ApiPromise<
    SubscriptionGroupPrepaymentResponse,
    SubscriptionGroupInvoiceAccount.CreateSubscriptionGroupPrepaymentError
  > {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/prepayments.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => subscriptionGroupPrepaymentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionGroupPrepaymentResponseSchema },
        errorFactory: SubscriptionGroupInvoiceAccount.CreateSubscriptionGroupPrepaymentError,
      },
      options,
    );
  }

  /**
   * Deduct Subscription Group Service Credit
   *
   * @remarks
   * Deducts service credit for a subscription group. Credit will be deducted from the group in the
   * amount specified in the request body.
   *
   * @returns Created
   *
   * @throws {@link SubscriptionGroupInvoiceAccount.DeductSubscriptionGroupServiceCreditError} when
   * the API answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deductSubscriptionGroupServiceCredit(
    request: SubscriptionGroupInvoiceAccount.DeductSubscriptionGroupServiceCreditRequest,
    options?: RequestOptions,
  ): ApiPromise<ServiceCredit, SubscriptionGroupInvoiceAccount.DeductSubscriptionGroupServiceCreditError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/service_credit_deductions.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => deductServiceCreditRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: serviceCreditSchema },
        errorFactory: SubscriptionGroupInvoiceAccount.DeductSubscriptionGroupServiceCreditError,
      },
      options,
    );
  }

  /**
   * Issue Subscription Group Service Credit
   *
   * @remarks
   * Issues service credit for a subscription group. Credit will be added to the group in the amount
   * specified in the request body. The credit will be applied to group member invoices as they are
   * generated.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroupInvoiceAccount.IssueSubscriptionGroupServiceCreditError} when
   * the API answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  issueSubscriptionGroupServiceCredit(
    request: SubscriptionGroupInvoiceAccount.IssueSubscriptionGroupServiceCreditRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ServiceCreditResponse,
    SubscriptionGroupInvoiceAccount.IssueSubscriptionGroupServiceCreditError
  > {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/service_credits.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => issueServiceCreditRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: serviceCreditResponseSchema },
        errorFactory: SubscriptionGroupInvoiceAccount.IssueSubscriptionGroupServiceCreditError,
      },
      options,
    );
  }

  /**
   * List Prepayments For Subscription Group
   *
   * @remarks
   * Lists a subscription group's prepayments.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroupInvoiceAccount.ListPrepaymentsForSubscriptionGroupError} when
   * the API answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listPrepaymentsForSubscriptionGroup(
    request: SubscriptionGroupInvoiceAccount.ListPrepaymentsForSubscriptionGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ListSubscriptionGroupPrepaymentResponse,
    SubscriptionGroupInvoiceAccount.ListPrepaymentsForSubscriptionGroupError
  > {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/prepayments.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listPrepaymentsFilterSchema)),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listSubscriptionGroupPrepaymentResponseSchema },
        errorFactory: SubscriptionGroupInvoiceAccount.ListPrepaymentsForSubscriptionGroupError,
      },
      options,
    );
  }
}

export namespace SubscriptionGroupInvoiceAccount {
  export type CreateSubscriptionGroupPrepaymentRequest = {
    /** The uid of the subscription group */
    uid: string;
    body?: SubscriptionGroupPrepaymentRequest;
  };

  export class CreateSubscriptionGroupPrepaymentError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CreateSubscriptionGroupPrepaymentError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type DeductSubscriptionGroupServiceCreditRequest = {
    /** The uid of the subscription group */
    uid: string;
    body?: DeductServiceCreditRequest;
  };

  export class DeductSubscriptionGroupServiceCreditError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<DeductSubscriptionGroupServiceCreditError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type IssueSubscriptionGroupServiceCreditRequest = {
    /** The uid of the subscription group */
    uid: string;
    body?: IssueServiceCreditRequest;
  };

  export class IssueSubscriptionGroupServiceCreditError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<IssueSubscriptionGroupServiceCreditError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListPrepaymentsForSubscriptionGroupRequest = {
    /** The uid of the subscription group */
    uid: string;
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
    /** Filter to use for List Prepayments operations */
    filter?: ListPrepaymentsFilter;
  };

  export class ListPrepaymentsForSubscriptionGroupError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ListPrepaymentsForSubscriptionGroupError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }
}
