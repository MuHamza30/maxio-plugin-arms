import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { bankAccountResponseSchema, type BankAccountResponse } from "../models/bank-account-response.js";
import {
  bankAccountVerificationRequestSchema,
  type BankAccountVerificationRequest,
} from "../models/bank-account-verification-request.js";
import {
  createPaymentProfileRequestSchema,
  type CreatePaymentProfileRequest,
} from "../models/create-payment-profile-request.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  errorStringMapResponse1Schema,
  type ErrorStringMapResponse1,
} from "../models/error-string-map-response1.js";
import {
  getOneTimeTokenRequestSchema,
  type GetOneTimeTokenRequest,
} from "../models/get-one-time-token-request.js";
import {
  paymentProfileResponseSchema,
  type PaymentProfileResponse,
} from "../models/payment-profile-response.js";
import {
  updatePaymentProfileRequestSchema,
  type UpdatePaymentProfileRequest,
} from "../models/update-payment-profile-request.js";
import type { Servers } from "../servers.js";

export class PaymentProfiles {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Change Subscription Default Payment Profile
   *
   * @remarks
   * Changes the default payment profile on the subscription to the existing payment profile with
   * the specified ID.
   *
   * You must elect to change the existing payment profile to a new payment profile ID in order to
   * receive a satisfactory response from this endpoint.
   *
   * @returns Created
   *
   * @throws {@link PaymentProfiles.ChangeSubscriptionDefaultPaymentProfileError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  changeSubscriptionDefaultPaymentProfile(
    request: PaymentProfiles.ChangeSubscriptionDefaultPaymentProfileRequest,
    options?: RequestOptions,
  ): ApiPromise<PaymentProfileResponse, PaymentProfiles.ChangeSubscriptionDefaultPaymentProfileError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}/change_payment_profile.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "payment_profile_id", value: request.paymentProfileId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: paymentProfileResponseSchema },
        errorFactory: PaymentProfiles.ChangeSubscriptionDefaultPaymentProfileError,
      },
      options,
    );
  }

  /**
   * Change Subscription Group Default Payment Profile
   *
   * @remarks
   * Changes the default payment profile on the subscription group to the existing payment profile
   * with the specified ID.
   *
   * You must elect to change the existing payment profile to a new payment profile ID in order to
   * receive a satisfactory response from this endpoint.
   *
   * The new payment profile must belong to the subscription group's customer, otherwise you will
   * receive an error.
   *
   * @returns Created
   *
   * @throws {@link PaymentProfiles.ChangeSubscriptionGroupDefaultPaymentProfileError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  changeSubscriptionGroupDefaultPaymentProfile(
    request: PaymentProfiles.ChangeSubscriptionGroupDefaultPaymentProfileRequest,
    options?: RequestOptions,
  ): ApiPromise<PaymentProfileResponse, PaymentProfiles.ChangeSubscriptionGroupDefaultPaymentProfileError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/subscription_groups/{uid}/payment_profiles/{payment_profile_id}/change_payment_profile.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "uid", value: request.uid, schema: s.string() },
          { name: "payment_profile_id", value: request.paymentProfileId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: paymentProfileResponseSchema },
        errorFactory: PaymentProfiles.ChangeSubscriptionGroupDefaultPaymentProfileError,
      },
      options,
    );
  }

  /**
   * Create Payment Profile
   *
   * @remarks
   * Creates a payment profile for a customer.
   *
   * When you create a new payment profile for a customer via the API, it does not automatically
   * make the profile current for any of the customer’s subscriptions. To use the payment profile as
   * the default, you must set it explicitly for the subscription or subscription group.
   *
   * Select an option from the **Request Examples** drop-down on the right side of the portal to see
   * examples of common scenarios for creating payment profiles.
   *
   * Do not use real card information for testing. See the Sites articles that cover [testing your
   * site
   * setup](https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0)
   * for more details on testing in your sandbox.
   *
   * Note that collecting and sending raw card details in production requires [PCI
   * compliance](https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0)
   * on your end. If your business is not PCI compliant, use [Maxio.js (formerly
   * Chargify.js)](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0)
   * to collect credit card or bank account information.
   *
   * See the following articles to learn more about subscriptions and payments:
   *
   * + [Subscriber Payment
   *   Details](https://maxio.zendesk.com/hc/en-us/articles/24251599929613-Subscription-Summary-Payment-Details-Tab)
   * + [Self Service
   *   Pages](https://maxio.zendesk.com/hc/en-us/articles/24261425318541-Self-Service-Pages) (Allows
   *   credit card updates by Subscriber)
   * + [Public Signup Pages payment
   *   settings](https://maxio.zendesk.com/hc/en-us/articles/24261368332557-Individual-Page-Settings)
   * + [Taxes](https://developers.chargify.com/docs/developer-docs/d2e9e34db740e-signups#taxes)
   * + [Maxio.js (formerly
   *   Chargify.js)](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview)
   *     + [Maxio.js with GoCardless - minimal
   *       example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQZKCER8CFK40MR6XJ)
   *     + [Maxio.js with GoCardless - full
   *       example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QR09JVHWW0MCA7HVJV)
   *     + [Maxio.js with Stripe Direct Debit - minimal
   *       example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQFKKN8Z7B7DZ9AJS5)
   *     + [Maxio.js with Stripe Direct Debit - full
   *       example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QRECQQ4ECS3ZA55GY7)
   *     + [Maxio.js with Stripe BECS Direct Debit - minimal
   *       example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#minimal-example-with-sepa-or-becs-direct-debit-stripe-gateway)
   *     + [Maxio.js with Stripe BECS Direct Debit - full
   *       example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#full-example-with-sepa-direct-debit-stripe-gateway)
   * + [Full documentation on
   *   GoCardless](https://maxio.zendesk.com/hc/en-us/articles/24176159136909-GoCardless)
   * + [Full documentation on Stripe SEPA Direct
   *   Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit)
   * + [Full documentation on Stripe BECS Direct
   *   Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit)
   * + [Full documentation on Stripe BACS Direct
   *   Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit)
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
   * @throws {@link PaymentProfiles.CreatePaymentProfileError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createPaymentProfile(
    request: PaymentProfiles.CreatePaymentProfileRequestParams,
    options?: RequestOptions,
  ): ApiPromise<PaymentProfileResponse, PaymentProfiles.CreatePaymentProfileError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/payment_profiles.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createPaymentProfileRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: paymentProfileResponseSchema },
        errorFactory: PaymentProfiles.CreatePaymentProfileError,
      },
      options,
    );
  }

  /**
   * Delete Subscription Group Payment Profile
   *
   * @remarks
   * Deletes a Payment Profile belonging to a Subscription Group.
   *
   * **Note**: If the Payment Profile belongs to multiple Subscription Groups and/or Subscriptions,
   * it will be removed from all of them.
   *
   * @returns No Content
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteSubscriptionGroupPaymentProfile(
    request: PaymentProfiles.DeleteSubscriptionGroupPaymentProfileRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production(
          "/subscription_groups/{uid}/payment_profiles/{payment_profile_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "uid", value: request.uid, schema: s.string() },
          { name: "payment_profile_id", value: request.paymentProfileId, schema: s.int() },
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
   * Delete Subscription Payment Profile
   *
   * @remarks
   * Deletes a payment profile belonging to the customer on the subscription.
   *
   * If the customer has multiple subscriptions, the payment profile is removed from all of them.
   *
   * If you delete the default payment profile for a subscription, you need to specify another
   * payment profile to be the default through the API, or either prompt the user to enter a card in
   * the billing portal or on the self-service page, or visit the Payment Details tab on the
   * subscription in the Admin UI and use the “Add New Credit Card” or “Make Active Payment Method”
   * link, (depending on whether there are other cards present).
   *
   * @returns No Content
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteSubscriptionsPaymentProfile(
    request: PaymentProfiles.DeleteSubscriptionsPaymentProfileRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "payment_profile_id", value: request.paymentProfileId, schema: s.int() },
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
   * Delete Unused Payment Profile
   *
   * @remarks
   * Deletes an unused payment profile.
   *
   * If the payment profile is in use by one or more subscriptions or groups, an error message is
   * returned.
   *
   * @returns No Content
   *
   * @throws {@link PaymentProfiles.DeleteUnusedPaymentProfileError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteUnusedPaymentProfile(
    request: PaymentProfiles.DeleteUnusedPaymentProfileRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, PaymentProfiles.DeleteUnusedPaymentProfileError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/payment_profiles/{payment_profile_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "payment_profile_id", value: request.paymentProfileId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: PaymentProfiles.DeleteUnusedPaymentProfileError,
      },
      options,
    );
  }

  /**
   * List Payment Profiles
   *
   * @remarks
   * Lists all active payment profiles for a site, or for one customer within a site. If no payment
   * profiles are found, this endpoint returns an empty array.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listPaymentProfiles(
    request: PaymentProfiles.ListPaymentProfilesRequest,
    options?: RequestOptions,
  ): ApiPromise<PaymentProfileResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/payment_profiles.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "customer_id", value: request.customerId, schema: s.optional(s.int()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => paymentProfileResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read one time token details
   *
   * @remarks
   * Returns the one-time token data, including credit card or ACH details, associated with the
   * provided token ID. One Time Tokens aka Advanced Billing Tokens house the credit card or ACH
   * (Authorize.Net or Stripe only) data for a customer.
   *
   * You can use One Time Tokens while creating a subscription or payment profile instead of passing
   * all bank account or credit card data directly to a given API endpoint.
   *
   * To obtain a One Time Token you have to use
   * [Chargify.js](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0).
   *
   * @returns OK
   *
   * @throws {@link PaymentProfiles.ReadOneTimeTokenError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readOneTimeToken(
    request: PaymentProfiles.ReadOneTimeTokenRequest,
    options?: RequestOptions,
  ): ApiPromise<GetOneTimeTokenRequest, PaymentProfiles.ReadOneTimeTokenError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/one_time_tokens/{chargify_token}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "chargify_token", value: request.chargifyToken, schema: s.string() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: getOneTimeTokenRequestSchema },
        errorFactory: PaymentProfiles.ReadOneTimeTokenError,
      },
      options,
    );
  }

  /**
   * Read Payment Profile
   *
   * @remarks
   * Returns a payment profile identified by its unique ID.
   *
   * Note that a different JSON object will be returned if the card method on file is a bank
   * account.
   *
   * ### Response for Bank Account
   *
   * Example response for Bank Account:
   *
   * ```
   * {
   *   "payment_profile": {
   *     "id": 10089892,
   *     "first_name": "Chester",
   *     "last_name": "Tester",
   *     "created_at": "2025-01-01T00:00:00-05:00",
   *     "updated_at": "2025-01-01T00:00:00-05:00",
   *     "customer_id": 14543792,
   *     "current_vault": "bogus",
   *     "vault_token": "0011223344",
   *     "billing_address": "456 Juniper Court",
   *     "billing_city": "Boulder",
   *     "billing_state": "CO",
   *     "billing_zip": "80302",
   *     "billing_country": "US",
   *     "customer_vault_token": null,
   *     "billing_address_2": "",
   *     "bank_name": "Bank of Kansas City",
   *     "masked_bank_routing_number": "XXXX6789",
   *     "masked_bank_account_number": "XXXX3344",
   *     "bank_account_type": "checking",
   *     "bank_account_holder_type": "personal",
   *     "payment_type": "bank_account",
   *     "site_gateway_setting_id": 1,
   *     "gateway_handle": null
   *   }
   * }
   * ```
   *
   * @returns OK
   *
   * @throws {@link PaymentProfiles.ReadPaymentProfileError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readPaymentProfile(
    request: PaymentProfiles.ReadPaymentProfileRequest,
    options?: RequestOptions,
  ): ApiPromise<PaymentProfileResponse, PaymentProfiles.ReadPaymentProfileError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/payment_profiles/{payment_profile_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "payment_profile_id", value: request.paymentProfileId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: paymentProfileResponseSchema },
        errorFactory: PaymentProfiles.ReadPaymentProfileError,
      },
      options,
    );
  }

  /**
   * Send request payment update email
   *
   * @remarks
   * Sends a "request payment update" email to the customer associated with the subscription.
   *
   * If you attempt to send a "request payment update" email more than five times within a 30-minute
   * period, you will receive a `422` response with an error message in the body. This error message
   * will indicate that the request has been rejected due to excessive attempts, and will provide
   * instructions on how to resubmit the request.
   *
   * Additionally, if you attempt to send a "request payment update" email for a subscription that
   * does not exist, you will receive a `404` error response. This error message will indicate that
   * the subscription could not be found, and will provide instructions on how to correct the error
   * and resubmit the request.
   *
   * These error responses are designed to prevent excessive or invalid requests, and to provide
   * clear and helpful information to users who encounter errors during the request process.
   *
   * @returns Created
   *
   * @throws {@link PaymentProfiles.SendRequestUpdatePaymentEmailError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  sendRequestUpdatePaymentEmail(
    request: PaymentProfiles.SendRequestUpdatePaymentEmailRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, PaymentProfiles.SendRequestUpdatePaymentEmailError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/request_payment_profiles_update.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: PaymentProfiles.SendRequestUpdatePaymentEmailError,
      },
      options,
    );
  }

  /**
   * Update Payment Profile
   *
   * @remarks
   * Updates a payment profile.
   *
   * ## Partial Card Updates
   *
   * In the event that you are using the Authorize.net, Stripe, Cybersource, Forte or Braintree Blue
   * payment gateways, you can update just the billing and contact information for a payment method.
   * Note the lack of credit-card related data contained in the JSON payload.
   *
   * In this case, the following JSON is acceptable:
   *
   * ```
   * {
   *   "payment_profile": {
   *     "first_name": "Kelly",
   *     "last_name": "Test",
   *     "billing_address": "789 Juniper Court",
   *     "billing_city": "Boulder",
   *     "billing_state": "CO",
   *     "billing_zip": "80302",
   *     "billing_country": "US",
   *     "billing_address_2": null
   *   }
   * }
   * ```
   *
   * The result will be that you have updated the billing information for the card, yet retained the
   * original card number data.
   *
   * ## Specific notes on updating payment profiles
   *
   * - Merchants with **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or
   *   **Stripe** as their payment gateway can update their Customer’s credit cards without passing
   *   in the full credit card number and CVV.
   *
   * - If you are using **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or
   *   **Stripe**, Advanced Billing will ignore the credit card number and CVV when processing an
   *   update via the API, and attempt a partial update instead. If you wish to change the card
   *   number on a payment profile, you will need to create a new payment profile for the given
   *   customer.
   *
   * - A Payment Profile cannot be updated with the attributes of another type of Payment Profile.
   *   For example, if the payment profile you are attempting to update is a credit card, you cannot
   *   pass in bank account attributes (like `bank_account_number`), and vice versa.
   *
   * - Updating a payment profile directly will not trigger an attempt to capture a past-due
   *   balance. If this is the intent, update the card details via the Subscription instead.
   *
   * - If you are using Authorize.net or Stripe, you may elect to manually trigger a retry for a
   *   past due subscription after a partial update.
   *
   * @returns OK
   *
   * @throws {@link PaymentProfiles.UpdatePaymentProfileError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updatePaymentProfile(
    request: PaymentProfiles.UpdatePaymentProfileRequestParams,
    options?: RequestOptions,
  ): ApiPromise<PaymentProfileResponse, PaymentProfiles.UpdatePaymentProfileError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/payment_profiles/{payment_profile_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "payment_profile_id", value: request.paymentProfileId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updatePaymentProfileRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: paymentProfileResponseSchema },
        errorFactory: PaymentProfiles.UpdatePaymentProfileError,
      },
      options,
    );
  }

  /**
   * Verify Bank Account
   *
   * @remarks
   * Verifies a bank account. Submit the two small deposit amounts the customer received in their
   * bank account to verify the bank account. (Stripe only)
   *
   * @returns OK
   *
   * @throws {@link PaymentProfiles.VerifyBankAccountError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  verifyBankAccount(
    request: PaymentProfiles.VerifyBankAccountRequest,
    options?: RequestOptions,
  ): ApiPromise<BankAccountResponse, PaymentProfiles.VerifyBankAccountError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/bank_accounts/{bank_account_id}/verification.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "bank_account_id", value: request.bankAccountId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => bankAccountVerificationRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: bankAccountResponseSchema },
        errorFactory: PaymentProfiles.VerifyBankAccountError,
      },
      options,
    );
  }
}

export namespace PaymentProfiles {
  export type ChangeSubscriptionDefaultPaymentProfileRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The Chargify id of the payment profile */
    paymentProfileId: number;
  };

  export class ChangeSubscriptionDefaultPaymentProfileError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<ChangeSubscriptionDefaultPaymentProfileError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ChangeSubscriptionGroupDefaultPaymentProfileRequest = {
    /** The uid of the subscription group */
    uid: string;
    /** The Chargify id of the payment profile */
    paymentProfileId: number;
  };

  export class ChangeSubscriptionGroupDefaultPaymentProfileError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ChangeSubscriptionGroupDefaultPaymentProfileError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreatePaymentProfileRequestParams = {
    /**
     * When following the IBAN or the Local Bank details examples, a customer, bank account and
     * mandate will be created in your current vault. If the customer, bank account, and mandate
     * already exist in your vault, follow the Import example to link the payment profile into
     * Advanced Billing.
     */
    body?: CreatePaymentProfileRequest;
  };

  export class CreatePaymentProfileError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<CreatePaymentProfileError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type DeleteSubscriptionGroupPaymentProfileRequest = {
    /** The uid of the subscription group */
    uid: string;
    /** The Chargify id of the payment profile */
    paymentProfileId: number;
  };

  export type DeleteSubscriptionsPaymentProfileRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The Chargify id of the payment profile */
    paymentProfileId: number;
  };

  export type DeleteUnusedPaymentProfileRequest = {
    /** The Chargify id of the payment profile */
    paymentProfileId: number;
  };

  export class DeleteUnusedPaymentProfileError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<DeleteUnusedPaymentProfileError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListPaymentProfilesRequest = {
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
    /** The ID of the customer for which you wish to list payment profiles */
    customerId?: number;
  };

  export type ReadOneTimeTokenRequest = {
    /** Advanced Billing Token */
    chargifyToken: string;
  };

  export class ReadOneTimeTokenError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ReadOneTimeTokenError> = [
      { on: 404, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadPaymentProfileRequest = {
    /** The Chargify id of the payment profile */
    paymentProfileId: number;
  };

  export class ReadPaymentProfileError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ReadPaymentProfileError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type SendRequestUpdatePaymentEmailRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export class SendRequestUpdatePaymentEmailError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<SendRequestUpdatePaymentEmailError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdatePaymentProfileRequestParams = {
    /** The Chargify id of the payment profile */
    paymentProfileId: number;
    body?: UpdatePaymentProfileRequest;
  };

  export class UpdatePaymentProfileError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorStringMapResponse1", ErrorStringMapResponse1>
    >;

    static readonly errors: ErrorDecoders<UpdatePaymentProfileError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "errorStringMapResponse1",
        decode: { kind: "json", schema: errorStringMapResponse1Schema },
      },
    ];
  }

  export type VerifyBankAccountRequest = {
    /** Identifier of the bank account in the system. */
    bankAccountId: number;
    body?: BankAccountVerificationRequest;
  };

  export class VerifyBankAccountError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<VerifyBankAccountError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
