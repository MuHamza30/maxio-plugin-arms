import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { accountBalancesSchema, type AccountBalances } from "../models/account-balances.js";
import {
  createPrepaymentRequestSchema,
  type CreatePrepaymentRequest,
} from "../models/create-prepayment-request.js";
import {
  createPrepaymentResponseSchema,
  type CreatePrepaymentResponse,
} from "../models/create-prepayment-response.js";
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
  listServiceCreditsResponseSchema,
  type ListServiceCreditsResponse,
} from "../models/list-service-credits-response.js";
import { prepaymentResponseSchema, type PrepaymentResponse } from "../models/prepayment-response.js";
import { prepaymentsResponseSchema, type PrepaymentsResponse } from "../models/prepayments-response.js";
import {
  refundPrepaymentBaseErrorsResponse1Schema,
  type RefundPrepaymentBaseErrorsResponse1,
} from "../models/refund-prepayment-base-errors-response1.js";
import {
  refundPrepaymentRequestSchema,
  type RefundPrepaymentRequest,
} from "../models/refund-prepayment-request.js";
import { serviceCreditSchema, type ServiceCredit } from "../models/service-credit.js";
import { sortingDirectionSchema, type SortingDirection } from "../models/sorting-direction.js";
import {
  createPrepaymentErrorResponseSchema,
  type CreatePrepaymentErrorResponse,
} from "../models/unions/create-prepayment-error-response.js";
import {
  deductServiceCreditErrorResponseSchema,
  type DeductServiceCreditErrorResponse,
} from "../models/unions/deduct-service-credit-error-response.js";
import {
  issueServiceCreditErrorResponseSchema,
  type IssueServiceCreditErrorResponse,
} from "../models/unions/issue-service-credit-error-response.js";
import {
  refundPrepaymentErrorResponseSchema,
  type RefundPrepaymentErrorResponse,
} from "../models/unions/refund-prepayment-error-response.js";
import type { Servers } from "../servers.js";

export class SubscriptionInvoiceAccount {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Prepayment
   *
   * @remarks
   * Creates a prepayment for a subscription.
   *
   * In order to specify a prepayment made against a subscription, specify the `amount, memo,
   * details, method`.
   *
   * When the `method` specified is `"credit_card_on_file"`, the prepayment amount will be collected
   * using the default credit card payment profile and applied to the prepayment account balance.
   * This is especially useful for manual replenishment of prepaid subscriptions.
   *
   * Note that passing `amount_in_cents` is now allowed.
   *
   * ## 3D Secure (3DS) Authentication post-authentication flow
   *
   * When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA),
   * the request enters a post-authentication flow where a 422 Unprocessable Entity status is
   * returned with an action_link that will direct the customer through 3DS Authentication.
   *
   * See the [3D Secure Post-Authentication
   * Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow)
   * article in the product documentation to learn how to manage the redirect flow.
   *
   * @returns Created
   *
   * @throws {@link SubscriptionInvoiceAccount.CreatePrepaymentError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createPrepayment(
    request: SubscriptionInvoiceAccount.CreatePrepaymentRequestParams,
    options?: RequestOptions,
  ): ApiPromise<CreatePrepaymentResponse, SubscriptionInvoiceAccount.CreatePrepaymentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/prepayments.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createPrepaymentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: createPrepaymentResponseSchema },
        errorFactory: SubscriptionInvoiceAccount.CreatePrepaymentError,
      },
      options,
    );
  }

  /**
   * Deduct Service Credit
   *
   * @remarks
   * Deducts a service credit from the subscription in the specified amount. The credit amount being
   * deducted must be equal to or less than the current credit balance.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionInvoiceAccount.DeductServiceCreditError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deductServiceCredit(
    request: SubscriptionInvoiceAccount.DeductServiceCreditRequestParams,
    options?: RequestOptions,
  ): ApiPromise<undefined, SubscriptionInvoiceAccount.DeductServiceCreditError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/service_credit_deductions.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => deductServiceCreditRequestSchema)),
        },
      },
      {
        success: { kind: "empty" },
        errorFactory: SubscriptionInvoiceAccount.DeductServiceCreditError,
      },
      options,
    );
  }

  /**
   * Issue Service Credit
   *
   * @remarks
   * Adds a service credit to the subscription in the specified amount. The credit is subsequently
   * applied to the next generated invoice.
   *
   * @returns Created
   *
   * @throws {@link SubscriptionInvoiceAccount.IssueServiceCreditError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  issueServiceCredit(
    request: SubscriptionInvoiceAccount.IssueServiceCreditRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ServiceCredit, SubscriptionInvoiceAccount.IssueServiceCreditError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/service_credits.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => issueServiceCreditRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: serviceCreditSchema },
        errorFactory: SubscriptionInvoiceAccount.IssueServiceCreditError,
      },
      options,
    );
  }

  /**
   * List Prepayments
   *
   * @remarks
   * Lists a subscription's prepayments.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionInvoiceAccount.ListPrepaymentsError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listPrepayments(
    request: SubscriptionInvoiceAccount.ListPrepaymentsRequest,
    options?: RequestOptions,
  ): ApiPromise<PrepaymentsResponse, SubscriptionInvoiceAccount.ListPrepaymentsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/prepayments.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
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
        success: { kind: "json", schema: prepaymentsResponseSchema },
        errorFactory: SubscriptionInvoiceAccount.ListPrepaymentsError,
      },
      options,
    );
  }

  /**
   * List Service Credits
   *
   * @remarks
   * Lists a subscription's service credits.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionInvoiceAccount.ListServiceCreditsError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listServiceCredits(
    request: SubscriptionInvoiceAccount.ListServiceCreditsRequest,
    options?: RequestOptions,
  ): ApiPromise<ListServiceCreditsResponse, SubscriptionInvoiceAccount.ListServiceCreditsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/service_credits/list.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
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
        success: { kind: "json", schema: listServiceCreditsResponseSchema },
        errorFactory: SubscriptionInvoiceAccount.ListServiceCreditsError,
      },
      options,
    );
  }

  /**
   * Read Account Balances
   *
   * @remarks
   * Returns the `balance_in_cents` of the Subscription's Pending Discount, Service Credit, and
   * Prepayment accounts, as well as the sum of the Subscription's open, payable invoices.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readAccountBalances(
    request: SubscriptionInvoiceAccount.ReadAccountBalancesRequest,
    options?: RequestOptions,
  ): ApiPromise<AccountBalances, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/account_balances.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: accountBalancesSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Refund Prepayment
   *
   * @remarks
   * Refunds a prepayment applied to a subscription, either fully or partially. The `prepayment_id`
   * will be the account transaction ID of the original payment. The prepayment must have some
   * amount remaining in order to be refunded.
   *
   * The amount may be passed either as a decimal, with `amount`, or an integer in cents, with
   * `amount_in_cents`.
   *
   * @returns Created
   *
   * @throws {@link SubscriptionInvoiceAccount.RefundPrepaymentError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  refundPrepayment(
    request: SubscriptionInvoiceAccount.RefundPrepaymentRequestParams,
    options?: RequestOptions,
  ): ApiPromise<PrepaymentResponse, SubscriptionInvoiceAccount.RefundPrepaymentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/prepayments/{prepayment_id}/refunds.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "prepayment_id", value: request.prepaymentId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => refundPrepaymentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: prepaymentResponseSchema },
        errorFactory: SubscriptionInvoiceAccount.RefundPrepaymentError,
      },
      options,
    );
  }
}

export namespace SubscriptionInvoiceAccount {
  export type CreatePrepaymentRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: CreatePrepaymentRequest;
  };

  export class CreatePrepaymentError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"createPrepaymentErrorResponse", CreatePrepaymentErrorResponse>
    >;

    static readonly errors: ErrorDecoders<CreatePrepaymentError> = [
      {
        on: 422,
        kind: "createPrepaymentErrorResponse",
        decode: { kind: "json", schema: createPrepaymentErrorResponseSchema },
      },
    ];
  }

  export type DeductServiceCreditRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: DeductServiceCreditRequest;
  };

  export class DeductServiceCreditError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"deductServiceCreditErrorResponse", DeductServiceCreditErrorResponse>
    >;

    static readonly errors: ErrorDecoders<DeductServiceCreditError> = [
      {
        on: 422,
        kind: "deductServiceCreditErrorResponse",
        decode: { kind: "json", schema: deductServiceCreditErrorResponseSchema },
      },
    ];
  }

  export type IssueServiceCreditRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: IssueServiceCreditRequest;
  };

  export class IssueServiceCreditError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"issueServiceCreditErrorResponse", IssueServiceCreditErrorResponse>
    >;

    static readonly errors: ErrorDecoders<IssueServiceCreditError> = [
      {
        on: 422,
        kind: "issueServiceCreditErrorResponse",
        decode: { kind: "json", schema: issueServiceCreditErrorResponseSchema },
      },
    ];
  }

  export type ListPrepaymentsRequest = {
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
    /** Filter to use for List Prepayments operations */
    filter?: ListPrepaymentsFilter;
  };

  export class ListPrepaymentsError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ListPrepaymentsError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ListServiceCreditsRequest = {
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
    /** Controls the order in which results are returned. Use in query `direction=asc`. */
    direction?: SortingDirection;
  };

  export class ListServiceCreditsError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<ListServiceCreditsError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadAccountBalancesRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export type RefundPrepaymentRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** id of prepayment */
    prepaymentId: number;
    body?: RefundPrepaymentRequest;
  };

  export class RefundPrepaymentError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"refundPrepaymentBaseErrorsResponse1", RefundPrepaymentBaseErrorsResponse1>
      | Declared<"error404", string>
      | Declared<"refundPrepaymentErrorResponse", RefundPrepaymentErrorResponse>
    >;

    static readonly errors: ErrorDecoders<RefundPrepaymentError> = [
      {
        on: 400,
        kind: "refundPrepaymentBaseErrorsResponse1",
        decode: { kind: "json", schema: refundPrepaymentBaseErrorsResponse1Schema },
      },
      { on: 404, kind: "error404", decode: { kind: "json", schema: s.string() } },
      {
        on: 422,
        kind: "refundPrepaymentErrorResponse",
        decode: { kind: "json", schema: refundPrepaymentErrorResponseSchema },
      },
    ];
  }
}
