import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  cancelGroupedSubscriptionsRequestSchema,
  type CancelGroupedSubscriptionsRequest,
} from "../models/cancel-grouped-subscriptions-request.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  reactivateSubscriptionGroupRequestSchema,
  type ReactivateSubscriptionGroupRequest,
} from "../models/reactivate-subscription-group-request.js";
import {
  reactivateSubscriptionGroupResponseSchema,
  type ReactivateSubscriptionGroupResponse,
} from "../models/reactivate-subscription-group-response.js";
import type { Servers } from "../servers.js";

export class SubscriptionGroupStatus {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Cancel Delayed Group Cancellation
   *
   * @remarks
   * Removes the delayed cancellation on a subscription group.
   *
   * Removing the delayed cancellation on a subscription group will ensure that the subscriptions do
   * not get canceled at the end of the period. The request will reset the `cancel_at_end_of_period`
   * flag to false on each member in the group.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroupStatus.CancelDelayedCancellationForGroupError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  cancelDelayedCancellationForGroup(
    request: SubscriptionGroupStatus.CancelDelayedCancellationForGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, SubscriptionGroupStatus.CancelDelayedCancellationForGroupError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/delayed_cancel.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: SubscriptionGroupStatus.CancelDelayedCancellationForGroupError,
      },
      options,
    );
  }

  /**
   * Cancel Grouped Subscriptions
   *
   * @remarks
   * Cancels all subscriptions within the specified group immediately. The group is identified by
   * the `uid` that is passed in the URL. To successfully cancel the group, the primary subscription
   * must be on automatic billing. The group members must be on automatic billing or prepaid.
   *
   * To cancel a subscription group while also charging for any unbilled usage on metered or prepaid
   * components, the `charge_unbilled_usage=true` parameter must be included in the request.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroupStatus.CancelSubscriptionsInGroupError} when the API answers
   * with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  cancelSubscriptionsInGroup(
    request: SubscriptionGroupStatus.CancelSubscriptionsInGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, SubscriptionGroupStatus.CancelSubscriptionsInGroupError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/cancel.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => cancelGroupedSubscriptionsRequestSchema)),
        },
      },
      {
        success: { kind: "empty" },
        errorFactory: SubscriptionGroupStatus.CancelSubscriptionsInGroupError,
      },
      options,
    );
  }

  /**
   * Initiate Delayed Group Cancellation
   *
   * @remarks
   * Schedules all subscriptions within the specified group to be canceled at the end of their
   * billing period. The group is identified by its uid passed in the URL.
   *
   * All subscriptions in the group must be on automatic billing in order to successfully cancel
   * them, and the group must not be in a "past_due" state.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroupStatus.InitiateDelayedCancellationForGroupError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  initiateDelayedCancellationForGroup(
    request: SubscriptionGroupStatus.InitiateDelayedCancellationForGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, SubscriptionGroupStatus.InitiateDelayedCancellationForGroupError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/delayed_cancel.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: SubscriptionGroupStatus.InitiateDelayedCancellationForGroupError,
      },
      options,
    );
  }

  /**
   * Reactivate / Resume Subscription Group
   *
   * @remarks
   * Reactivates or resumes a cancelled subscription group. Upon reactivation, any canceled invoices
   * created after the beginning of the primary subscription's billing period will be reopened and
   * payment will be attempted on them. If the subscription group is being reactivated (as opposed
   * to resumed), new charges will also be assessed for the new billing period.
   *
   * Whether a subscription group is reactivated (a new billing period is created) or resumed (the
   * current billing period is respected) will depend on the parameters that are sent with the
   * request as well as the date of the request relative to the primary subscription's period.
   *
   * ## Reactivating within the current period
   *
   * If a subscription group is cancelled and reactivated within the primary subscription's current
   * period, we can choose to either start a new billing period or maintain the existing one. If we
   * want to maintain the existing billing period, the `resume=true` option must be passed in
   * request parameters.
   *
   * An exception to the above are subscriptions that are on calendar billing. These subscriptions
   * cannot be reactivated within the current period. If the `resume=true` option is not passed, the
   * request will return an error.
   *
   * The `resume_members` option is ignored in this case. All eligible group members will be
   * automatically resumed.
   *
   *
   * ## Reactivating beyond the current period
   *
   * In this case, a subscription group can only be reactivated with a new billing period. If the
   * `resume=true` option is passed it will be ignored.
   *
   * Member subscriptions can have billing periods that are longer than the primary (e.g. a monthly
   * primary with annual group members). If the primary subscription in a group cannot be
   * reactivated within the current period, but other group members can be, passing
   * `resume_members=true` will resume the existing billing period for eligible group members. The
   * primary subscription will begin a new billing period.
   *
   * For calendar billing subscriptions, the new billing period created will be a partial one,
   * spanning from the date of reactivation to the next corresponding calendar renewal date.
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
   * @returns OK
   *
   * @throws {@link SubscriptionGroupStatus.ReactivateSubscriptionGroupError} when the API answers
   * with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  reactivateSubscriptionGroup(
    request: SubscriptionGroupStatus.ReactivateSubscriptionGroupRequestParams,
    options?: RequestOptions,
  ): ApiPromise<
    ReactivateSubscriptionGroupResponse,
    SubscriptionGroupStatus.ReactivateSubscriptionGroupError
  > {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/reactivate.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => reactivateSubscriptionGroupRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: reactivateSubscriptionGroupResponseSchema },
        errorFactory: SubscriptionGroupStatus.ReactivateSubscriptionGroupError,
      },
      options,
    );
  }
}

export namespace SubscriptionGroupStatus {
  export type CancelDelayedCancellationForGroupRequest = {
    /** The uid of the subscription group */
    uid: string;
  };

  export class CancelDelayedCancellationForGroupError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CancelDelayedCancellationForGroupError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CancelSubscriptionsInGroupRequest = {
    /** The uid of the subscription group */
    uid: string;
    body?: CancelGroupedSubscriptionsRequest;
  };

  export class CancelSubscriptionsInGroupError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CancelSubscriptionsInGroupError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type InitiateDelayedCancellationForGroupRequest = {
    /** The uid of the subscription group */
    uid: string;
  };

  export class InitiateDelayedCancellationForGroupError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<InitiateDelayedCancellationForGroupError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReactivateSubscriptionGroupRequestParams = {
    /** The uid of the subscription group */
    uid: string;
    body?: ReactivateSubscriptionGroupRequest;
  };

  export class ReactivateSubscriptionGroupError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ReactivateSubscriptionGroupError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
