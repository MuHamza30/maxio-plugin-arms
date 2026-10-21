import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { cancellationRequestSchema, type CancellationRequest } from "../models/cancellation-request.js";
import {
  delayedCancellationResponseSchema,
  type DelayedCancellationResponse,
} from "../models/delayed-cancellation-response.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { pauseRequestSchema, type PauseRequest } from "../models/pause-request.js";
import {
  reactivateSubscriptionRequestSchema,
  type ReactivateSubscriptionRequest,
} from "../models/reactivate-subscription-request.js";
import {
  renewalPreviewRequestSchema,
  type RenewalPreviewRequest,
} from "../models/renewal-preview-request.js";
import {
  renewalPreviewResponseSchema,
  type RenewalPreviewResponse,
} from "../models/renewal-preview-response.js";
import { ResumptionCharge, resumptionChargeSchema } from "../models/resumption-charge.js";
import { subscriptionResponseSchema, type SubscriptionResponse } from "../models/subscription-response.js";
import {
  cancelSubscriptionErrorResponseSchema,
  type CancelSubscriptionErrorResponse,
} from "../models/unions/cancel-subscription-error-response.js";
import type { Servers } from "../servers.js";

export class SubscriptionStatus {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Cancel Delayed Cancellation
   *
   * @remarks
   * Removes the delayed cancellation from a subscription, ensuring it is not canceled at the end of
   * the current period. The request will reset the `cancel_at_end_of_period` flag to `false`.
   *
   * This endpoint is idempotent. If the subscription was not set to cancel in the future, removing
   * the delayed cancellation has no effect and the call will be successful.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionStatus.CancelDelayedCancellationError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  cancelDelayedCancellation(
    request: SubscriptionStatus.CancelDelayedCancellationRequest,
    options?: RequestOptions,
  ): ApiPromise<DelayedCancellationResponse, SubscriptionStatus.CancelDelayedCancellationError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/delayed_cancel.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: delayedCancellationResponseSchema },
        errorFactory: SubscriptionStatus.CancelDelayedCancellationError,
      },
      options,
    );
  }

  /**
   * Cancel Dunning
   *
   * @remarks
   * Cancels the active dunning process for a subscription and sets it to active.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionStatus.CancelDunningError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  cancelDunning(
    request: SubscriptionStatus.CancelDunningRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, SubscriptionStatus.CancelDunningError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/cancel_dunning.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: SubscriptionStatus.CancelDunningError,
      },
      options,
    );
  }

  /**
   * Cancel Subscription
   *
   * @remarks
   * Cancels the Subscription. The Delete method sets the Subscription state to `canceled`. To
   * cancel the subscription immediately, omit any schedule parameters from the request. To use the
   * schedule options, the Schedule Subscription Cancellation feature must be enabled on your site.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionStatus.CancelSubscriptionError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  cancelSubscription(
    request: SubscriptionStatus.CancelSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, SubscriptionStatus.CancelSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => cancellationRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: SubscriptionStatus.CancelSubscriptionError,
      },
      options,
    );
  }

  /**
   * Initiate Delayed Cancellation
   *
   * @remarks
   * Cancels a subscription at the end of the current billing period based on the subscription's
   * current product. You cannot set `cancel_at_end_of_period` at subscription creation, or if the
   * subscription is past due.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionStatus.InitiateDelayedCancellationError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  initiateDelayedCancellation(
    request: SubscriptionStatus.InitiateDelayedCancellationRequest,
    options?: RequestOptions,
  ): ApiPromise<DelayedCancellationResponse, SubscriptionStatus.InitiateDelayedCancellationError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/delayed_cancel.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => cancellationRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: delayedCancellationResponseSchema },
        errorFactory: SubscriptionStatus.InitiateDelayedCancellationError,
      },
      options,
    );
  }

  /**
   * Hold / Pause Subscription
   *
   * @remarks
   * Places the subscription on hold, preventing it from renewing.
   *
   * ## Limitations
   *
   * You may not place a subscription on hold if the `next_billing_at` date is within 24 hours.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionStatus.PauseSubscriptionError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  pauseSubscription(
    request: SubscriptionStatus.PauseSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, SubscriptionStatus.PauseSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/hold.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "json", value: request.body, schema: s.optional(s.lazy(() => pauseRequestSchema)) },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: SubscriptionStatus.PauseSubscriptionError,
      },
      options,
    );
  }

  /**
   * Preview Renewal
   *
   * @remarks
   * Previews a subscription’s next renewal assessment. Renewal Preview is an object representing a
   * subscription’s next assessment. You can retrieve it to see a snapshot of how much your customer
   * will be charged on their next renewal.
   *
   * The "Next Billing" amount and "Next Billing" date are already represented in the UI on each
   * Subscriber's Summary. For more information, see [Subscriber Interface
   * Overview](https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview).
   *
   * ## Optional Component Fields
   *
   * This endpoint is particularly useful because it returns the computed billing amount for the
   * base product and the components which are in use by a subscriber.
   *
   * By default, the preview includes billing details for all components _at their **current**
   * quantities_. This means:
   *
   * * Current `allocated_quantity` for quantity-based components
   * * Current enabled/disabled status for on/off components
   * * Current metered usage `unit_balance` for metered components
   * * Current metric quantity value for events recorded thus far for events-based components
   *
   * In the above statements, "current" means the quantity or value as of the call to the renewal
   * preview endpoint. End-of-period values for components are not predicted, so metered or
   * events-based usage may be less than it will eventually be at the end of the period.
   *
   * Optionally, **you can provide your own custom quantities** for any component to see a billing
   * preview for non-current quantities. This is accomplished by sending a request body with data
   * under the `components` key. See the request body documentation below.
   *
   * ## Preview Behavior
   *
   * Sending a `POST` request to this endpoint returns preview data without modifying the
   * subscription. This method previews data, but does not log any changes against a subscription.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionStatus.PreviewRenewalError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  previewRenewal(
    request: SubscriptionStatus.PreviewRenewalRequest,
    options?: RequestOptions,
  ): ApiPromise<RenewalPreviewResponse, SubscriptionStatus.PreviewRenewalError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/renewals/preview.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => renewalPreviewRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: renewalPreviewResponseSchema },
        errorFactory: SubscriptionStatus.PreviewRenewalError,
      },
      options,
    );
  }

  /**
   * Reactivate Subscription
   *
   * @remarks
   * Reactivates a previously canceled subscription. For details on how the reactivation works, and
   * how to reactivate subscriptions through the application, see
   * [reactivation](https://maxio.zendesk.com/hc/en-us/articles/24252109503629-Reactivating-and-Resuming).
   *
   * **Note: The term "resume" is used also during another process in Advanced Billing. This occurs
   * when an on-hold subscription is "resumed". This returns the subscription to an active state.**
   *
   * + The response returns the subscription object in the `active` or `trialing` state.
   * + The `canceled_at` and `cancellation_message` fields do not have values.
   * + The method works for "Canceled" or "Trial Ended" subscriptions.
   * + It will not work for items not marked as "Canceled", "Unpaid", or "Trial Ended".
   *
   * ## Resume the current billing period for a subscription
   *
   * A subscription is considered "resumable" if you are attempting to reactivate within the billing
   * period the subscription was canceled in.
   *
   * A resumed subscription's billing date remains the same as before it was canceled. In other
   * words, it does not start a new billing period. Payment may or may not be collected for a
   * resumed subscription, depending on whether or not the subscription had a balance when it was
   * canceled (for example, if it was canceled because of dunning).
   *
   * Consider a subscription which was created on June 1st, and would renew on July 1st. The
   * subscription is then canceled on June 15.
   *
   * If a reactivation with `resume: true` were attempted _before_ what would have been the next
   * billing date of July 1st, then Advanced Billing would resume the subscription.
   *
   * If a reactivation with `resume: true` were attempted _after_ what would have been the next
   * billing date of July 1st, then Advanced Billing would not resume the subscription, and instead
   * it would be reactivated with a new billing period.
   *
   * If a reactivation with `resume: false`, or where 'resume' is omitted were attempted, then
   * Advanced Billing would reactivate the subscription with a new billing period regardless of
   * whether or not resuming the previous billing period was possible.
   *
   * | Canceled | Reactivation | Resumable? |
   * |---|---|---|
   * | Jun 15 | June 28 | Yes |
   * | Jun 15 | July 2 | No |
   *
   * ## Reactivation Scenarios
   *
   * ### Reactivating Canceled Subscription While Preserving Balance
   *
   * + Given you have a product that costs $20
   * + Given you have a canceled subscription to the $20 product
   *     + 1 charge should exist for $20
   *     + 1 payment should exist for $20
   * + When the subscription has canceled due to dunning, it retained a negative balance of $20
   *
   * #### Results
   *
   * The resulting charges upon reactivation will be:
   * + 1 charge for $20 for the new product
   * + 1 charge for $20 for the balance due
   * + Total charges = $40
   *
   * + The subscription will transition to active
   * + The subscription balance will be zero
   *
   * ### Reactivating a Canceled Subscription With Coupon
   *
   * + Given you have a canceled subscription
   * + It has no current period defined
   * + You have a coupon code "EARLYBIRD"
   * + The coupon is set to recur for 6 periods
   *
   * PUT request sent to:
   * `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?coupon_code=EARLYBIRD`
   *
   * #### Results
   *
   * + The subscription will transition to active
   * + The subscription should have applied a coupon with code "EARLYBIRD"
   *
   * ### Reactivating Canceled Subscription With a Trial, Without the include_trial Flag
   *
   * + Given you have a canceled subscription
   * + The product associated with the subscription has a trial
   *
   * + PUT request to `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json`
   *
   *
   * #### Results
   * + The subscription will transition to active
   *
   * ### Reactivating Canceled Subscription With Trial, With the include_trial Flag
   *
   * + Given you have a canceled subscription
   * + The product associated with the subscription has a trial
   *
   * + Send a PUT request to
   *   `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?include_trial=1`
   *
   *
   * #### Results
   *
   * + The subscription will transition to trialing
   *
   * ### Reactivating Trial Ended Subscription
   *
   * + Given you have a trial_ended subscription
   * + Send a PUT request to
   *   `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json`
   *
   * #### Results
   *
   * + The subscription will transition to active
   *
   * ### Resuming a Canceled Subscription
   *
   * + Given you have a `canceled` subscription and it is resumable
   * + Send a PUT request to
   *   `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true`
   *
   * #### Results
   *
   * + The subscription will transition to active
   * + The next billing date should not have changed
   *
   * ### Attempting to resume a subscription which is not resumable
   *
   * + Given you have a `canceled` subscription, and it is not resumable
   * + Send a PUT request to
   *   `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true`
   *
   * #### Results
   *
   * + The subscription will transition to active, with a new billing period.
   *
   * ### Attempting to resume but not reactivate a subscription which is not resumable
   *
   * + Given you have a `canceled` subscription, and it is not resumable
   * + Send a PUT request to
   *   `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume[require_resume]=true`
   * + The response status should be "422 UNPROCESSABLE ENTITY"
   * + The subscription should be canceled with the following response
   * ```
   *   {
   *     "errors": ["Request was 'resume only', but this subscription cannot be resumed."]
   *   }
   * ```
   *
   * #### Results
   *
   * + The subscription should remain `canceled`
   * + The next billing date should not have changed
   *
   * ### Resuming Subscription Which Was Trialing
   *
   * + Given you have a `trial_ended` subscription, and it is resumable
   * + And the subscription was canceled in the middle of a trial
   * + And there is still time left on the trial
   * + Send a PUT request to
   *   `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true`
   *
   * #### Results
   *
   * + The subscription will transition to trialing
   * + The next billing date should not have changed
   *
   * ### Resuming Subscription Which Was trial_ended
   *
   * + Given you have a `trial_ended` subscription, and it is resumable
   * + Send a PUT request to
   *   `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true`
   *
   * #### Results
   *
   * + The subscription will transition to active
   * + The next billing date should not have changed
   * + Any product-related charges should have been collected
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
   * @throws {@link SubscriptionStatus.ReactivateSubscriptionError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  reactivateSubscription(
    request: SubscriptionStatus.ReactivateSubscriptionRequestParams,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, SubscriptionStatus.ReactivateSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/reactivate.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => reactivateSubscriptionRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: SubscriptionStatus.ReactivateSubscriptionError,
      },
      options,
    );
  }

  /**
   * Resume Subscription
   *
   * @remarks
   * Resumes a paused (on-hold) subscription. If the normal next renewal date has not passed, the
   * subscription will return to active and will renew on that date. Otherwise, it will behave like
   * a reactivation, setting the billing date to 'now' and charging the subscriber.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionStatus.ResumeSubscriptionError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  resumeSubscription(
    request: SubscriptionStatus.ResumeSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, SubscriptionStatus.ResumeSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/resume.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [
          {
            name: "calendar_billing['resumption_charge']",
            value: request.calendarBillingResumptionCharge,
            schema: s.defaulted(resumptionChargeSchema, ResumptionCharge.Prorated),
          },
        ],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: SubscriptionStatus.ResumeSubscriptionError,
      },
      options,
    );
  }

  /**
   * Retry Subscription
   *
   * @remarks
   * Retries collecting the balance due on a past-due subscription without waiting for the next
   * scheduled attempt.
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
   * @throws {@link SubscriptionStatus.RetrySubscriptionError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  retrySubscription(
    request: SubscriptionStatus.RetrySubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, SubscriptionStatus.RetrySubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/retry.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: SubscriptionStatus.RetrySubscriptionError,
      },
      options,
    );
  }

  /**
   * Update Automatic Subscription Resumption
   *
   * @remarks
   * Updates the date on which a paused subscription will automatically resume.
   *
   * To update a subscription's resume date, use this method to change or update the
   * `automatically_resume_at` date.
   *
   * ### Remove the resume date
   *
   * Alternatively, you can change the `automatically_resume_at` to `null` if you would like the
   * subscription to not have a resume date.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionStatus.UpdateAutomaticSubscriptionResumptionError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateAutomaticSubscriptionResumption(
    request: SubscriptionStatus.UpdateAutomaticSubscriptionResumptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, SubscriptionStatus.UpdateAutomaticSubscriptionResumptionError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/hold.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "json", value: request.body, schema: s.optional(s.lazy(() => pauseRequestSchema)) },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: SubscriptionStatus.UpdateAutomaticSubscriptionResumptionError,
      },
      options,
    );
  }
}

export namespace SubscriptionStatus {
  export type CancelDelayedCancellationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export class CancelDelayedCancellationError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<CancelDelayedCancellationError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type CancelDunningRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export class CancelDunningError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CancelDunningError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CancelSubscriptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: CancellationRequest;
  };

  export class CancelSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"error404", undefined>
      | Declared<"cancelSubscriptionErrorResponse", CancelSubscriptionErrorResponse>
    >;

    static readonly errors: ErrorDecoders<CancelSubscriptionError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "cancelSubscriptionErrorResponse",
        decode: { kind: "json", schema: cancelSubscriptionErrorResponseSchema },
      },
    ];
  }

  export type InitiateDelayedCancellationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: CancellationRequest;
  };

  export class InitiateDelayedCancellationError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<InitiateDelayedCancellationError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type PauseSubscriptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: PauseRequest;
  };

  export class PauseSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<PauseSubscriptionError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type PreviewRenewalRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: RenewalPreviewRequest;
  };

  export class PreviewRenewalError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<PreviewRenewalError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReactivateSubscriptionRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: ReactivateSubscriptionRequest;
  };

  export class ReactivateSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ReactivateSubscriptionError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ResumeSubscriptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /**
     * (For calendar billing subscriptions only) The way that the resumed subscription's charge
     * should be handled.
     *
     * @default ResumptionCharge.Prorated
     */
    calendarBillingResumptionCharge?: ResumptionCharge;
  };

  export class ResumeSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ResumeSubscriptionError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type RetrySubscriptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export class RetrySubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<RetrySubscriptionError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateAutomaticSubscriptionResumptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: PauseRequest;
  };

  export class UpdateAutomaticSubscriptionResumptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<UpdateAutomaticSubscriptionResumptionError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
