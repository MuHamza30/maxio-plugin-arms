import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  activateSubscriptionRequestSchema,
  type ActivateSubscriptionRequest,
} from "../models/activate-subscription-request.js";
import { addCouponsRequestSchema, type AddCouponsRequest } from "../models/add-coupons-request.js";
import { collectionMethod1Schema, type CollectionMethod1 } from "../models/collection-method1.js";
import {
  createSubscriptionRequestSchema,
  type CreateSubscriptionRequest,
} from "../models/create-subscription-request.js";
import {
  errorArrayMapResponse1Schema,
  type ErrorArrayMapResponse1,
} from "../models/error-array-map-response1.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { groupStatusSchema, type GroupStatus } from "../models/group-status.js";
import {
  overrideSubscriptionRequestSchema,
  type OverrideSubscriptionRequest,
} from "../models/override-subscription-request.js";
import {
  prepaidConfigurationResponseSchema,
  type PrepaidConfigurationResponse,
} from "../models/prepaid-configuration-response.js";
import { qScopeSchema, type QScope } from "../models/qscope.js";
import { singleErrorResponse1Schema, type SingleErrorResponse1 } from "../models/single-error-response1.js";
import { sortingDirectionSchema, type SortingDirection } from "../models/sorting-direction.js";
import {
  subscriptionAddCouponError1Schema,
  type SubscriptionAddCouponError1,
} from "../models/subscription-add-coupon-error1.js";
import {
  subscriptionDateFieldSchema,
  type SubscriptionDateField,
} from "../models/subscription-date-field.js";
import { subscriptionIncludeSchema, type SubscriptionInclude } from "../models/subscription-include.js";
import {
  subscriptionListIncludeSchema,
  type SubscriptionListInclude,
} from "../models/subscription-list-include.js";
import {
  subscriptionPreviewResponseSchema,
  type SubscriptionPreviewResponse,
} from "../models/subscription-preview-response.js";
import {
  subscriptionPurgeTypeSchema,
  type SubscriptionPurgeType,
} from "../models/subscription-purge-type.js";
import {
  subscriptionRemoveCouponErrors1Schema,
  type SubscriptionRemoveCouponErrors1,
} from "../models/subscription-remove-coupon-errors1.js";
import { subscriptionResponseSchema, type SubscriptionResponse } from "../models/subscription-response.js";
import { SubscriptionSort, subscriptionSortSchema } from "../models/subscription-sort.js";
import {
  subscriptionStateFilterSchema,
  type SubscriptionStateFilter,
} from "../models/subscription-state-filter.js";
import {
  prepaidConfigurationErrorResponseSchema,
  type PrepaidConfigurationErrorResponse,
} from "../models/unions/prepaid-configuration-error-response.js";
import { product1Schema, type Product1 } from "../models/unions/product1.js";
import {
  updateSubscriptionRequestSchema,
  type UpdateSubscriptionRequest,
} from "../models/update-subscription-request.js";
import {
  upsertPrepaidConfigurationRequestSchema,
  type UpsertPrepaidConfigurationRequest,
} from "../models/upsert-prepaid-configuration-request.js";
import type { Servers } from "../servers.js";

export class Subscriptions {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Activate Subscription
   *
   * @remarks
   * Activates awaiting signup and trialing subscriptions. This feature is only available on the
   * Relationship Invoicing architecture. Subscriptions in a group cannot be activated immediately.
   *
   * The `revert_on_failure` parameter controls the behavior upon activation failure.
   * - If set to `true` and something goes wrong i.e. payment fails, the subscription's state does
   *   not change. The subscription’s billing period also remains the same.
   * - If set to `false` and something goes wrong i.e. payment fails, the activation continues and
   *   enters an end of life state. For trialing subscriptions, that is either trial ended (if the
   *   trial is no obligation), past due (if the trial has an obligation), or canceled (if the site
   *   has no dunning strategy, or has a strategy that says to cancel immediately). For awaiting
   *   signup subscriptions, that is always canceled.
   *
   * The default activation failure behavior can be configured per activation attempt, or you can
   * set a default value under Config > Settings > Subscription Activation Settings.
   *
   * ## Activation Scenarios
   *
   * ### Activate Awaiting Signup subscription
   *
   * - Given you have a product without trial
   * - Given you have a site without dunning strategy
   *
   * ```mermaid
   *   flowchart LR
   *     AS[Awaiting Signup] --> A{Activate}
   *     A -->|Success| Active
   *     A -->|Failure| ROF{revert_on_failure}
   *     ROF -->|true| AS
   *     ROF -->|false| Canceled
   * ```
   *
   * - Given you have a product with trial
   * - Given you have a site with dunning strategy
   *
   * ```mermaid
   *   flowchart LR
   *     AS[Awaiting Signup] --> A{Activate}
   *     A -->|Success| Trialing
   *     A -->|Failure| ROF{revert_on_failure}
   *     ROF -->|true| AS
   *     ROF -->|false| PD[Past Due]
   * ```
   *
   * ### Activate Trialing subscription
   *
   * For more information about the behavior of trialing subscriptions, see [Trialing
   * Subscriptions](https://maxio.zendesk.com/hc/en-us/articles/24252155721869-Trialing-Subscriptions).
   * When the `revert_on_failure` parameter is set to `true`, the subscription's state remains
   * Trialing; the invoice from activation is voided, and any prepayments and credits applied to the
   * invoice are returned to the subscription.
   *
   * @returns OK
   *
   * @throws {@link Subscriptions.ActivateSubscriptionError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  activateSubscription(
    request: Subscriptions.ActivateSubscriptionRequestParams,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, Subscriptions.ActivateSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/activate.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => activateSubscriptionRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: Subscriptions.ActivateSubscriptionError,
      },
      options,
    );
  }

  /**
   * Apply Coupons to Subscription
   *
   * @remarks
   * Applies one or more coupon codes to an existing subscription.
   *
   * An existing subscription can accommodate multiple discounts/coupon codes. This is only
   * applicable if each coupon is stackable. For more information on stackable coupons, we recommend
   * reviewing our [coupon
   * documentation.](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#stackability-rules)
   *
   * ## Query Parameters vs Request Body Parameters
   *
   * Passing in a coupon code as a query parameter will add the code to the subscription, completely
   * replacing all existing coupon codes on the subscription.
   *
   * For this reason, using this query parameter on this endpoint has been deprecated in favor of
   * using the request body parameters as described below. When passing in request body parameters,
   * the list of coupon codes will simply be added to any existing list of codes on the
   * subscription.
   *
   * @returns OK
   *
   * @throws {@link Subscriptions.ApplyCouponsToSubscriptionError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  applyCouponsToSubscription(
    request: Subscriptions.ApplyCouponsToSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, Subscriptions.ApplyCouponsToSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/add_coupon.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [{ name: "code", value: request.code, schema: s.optional(s.string()) }],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => addCouponsRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: Subscriptions.ApplyCouponsToSubscriptionError,
      },
      options,
    );
  }

  /**
   * Create Subscription
   *
   * @remarks
   *
   * Creates a Subscription for a customer and product.
   *
   * Specify the product with `product_id` or `product_handle`. To set a specific product price
   * point, use `product_price_point_handle` or `product_price_point_id`.
   *
   * Identify an existing customer with `customer_id` or `customer_reference`. Optionally, include
   * an existing payment profile using `payment_profile_id`. To create a new customer, pass
   * customer_attributes.
   *
   * Select an option from the **Request Examples** drop-down on the right side of the portal to see
   * examples of common scenarios for creating subscriptions.
   *
   * ## List vs Sales Pricing
   *
   * When a subscription uses custom pricing as the sales price, you can optionally provide a list
   * price for any item. If omitted, the list price defaults to the sales price. The difference
   * between the list price and sales price is used to calculate implicit discounts, which appear on
   * Invoices and in reporting. List price can also support revenue allocations in [Advanced
   * Revenue](https://docs.maxio.com/hc/en-us/articles/24177001342861-Create-and-Configure-RevenueBooks).
   *
   * If your site has list pricing enabled, the API accepts `custom_price.list_price_point_id` for
   * custom pricing, validates and persists it, and returns list price metadata in subscription
   * responses. If list pricing is disabled, this input is ignored and related response fields are
   * omitted.
   *
   * When list pricing is enabled:
   *
   * - Subscription → Product `product_price_point_list_price_point_id` (integer)
   * - `product_price_point_list_price_point_handle` (string)
   * - Subscription Components (when components are included in the response, such as with
   *   subscriptions built from components or component serialization paths) `component_id`
   *   (integer)
   * - `price_point_id` (integer)
   * - `list_price_point_id` (integer)
   *
   * When list pricing is disabled:
   *
   * - Subscription → Product `product_price_point_list_price_point_id`: omitted
   * - `product_price_point_list_price_point_handle`: omitted
   * - Subscription Components `list_price_point_id`: omitted
   *
   * This functionality is supported in the API, but is not currently supported in SDKs.
   *
   * ## Subscriptions can now work independently from the catalog
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, you can create subscriptions without a `product_id` or `product_handle` using POST
   * /subscriptions, building them entirely from components.
   *
   * A valid subscription must include at least one active component with:
   * - a positive `allocated_quantity`,
   * - a positive `unit_balance`, or
   * - 'enabled: true' (for on/off components)
   * - a configured metered component
   *
   * `component_id` can be provided as a numeric ID or in handle: format. If `trial_interval` and
   * `trial_interval_unit` are included, they are applied at creation.
   *
   * In the response, product and product price point fields are null, and component details are
   * returned instead.
   *
   * This functionality is supported in the API, but is not currently supported in SDKs.
   *
   * ## Payment information
   *
   * Payment information may be required to create a subscription, depending on the options for the
   * Product being subscribed. See [product
   * options](https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products) for more
   * information. See the [Payments Profile]($e/Payment%20Profiles/createPaymentProfile) endpoint
   * for details on payment parameters. See the [Subscription
   * Signups](page:introduction/basic-concepts/subscription-signup) article for more information on
   * working with subscriptions in Advanced Billing.
   *
   * ## Payment information
   *
   * Payment information may be required to create a subscription, depending on the options for the
   * Product being subscribed. See [product
   * options](https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products) for more
   * information. See the [Payments Profile]($e/Payment%20Profiles/createPaymentProfile) endpoint
   * for details on payment parameters.
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
   * @throws {@link Subscriptions.CreateSubscriptionError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createSubscription(
    request: Subscriptions.CreateSubscriptionRequestParams,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, Subscriptions.CreateSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createSubscriptionRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: Subscriptions.CreateSubscriptionError,
      },
      options,
    );
  }

  /**
   * Find Subscription
   *
   * @remarks
   * Finds a subscription by its reference.
   *
   * @returns OK
   *
   * @throws {@link Subscriptions.FindSubscriptionError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  findSubscription(
    request: Subscriptions.FindSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, Subscriptions.FindSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/lookup.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [{ name: "reference", value: request.reference, schema: s.optional(s.string()) }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: Subscriptions.FindSubscriptionError,
      },
      options,
    );
  }

  /**
   * List Subscriptions
   *
   * @remarks
   * Lists subscriptions for a site. Use the query string filters and pagination to control
   * responses from the server.
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, some subscriptions may not have an associated product. For subscriptions without an
   * associated product, 'product', 'product_price_point_id', and 'product_price_point_type' are
   * returned as 'null'.
   *
   * ## Search for a subscription
   *
   * Use the query strings below to search for a subscription using the criteria available. The
   * return value will be an array.
   *
   * ## Self-Service Page token
   *
   * Self-Service Page token for the subscriptions is not returned by default. If this information
   * is desired, the include[]=self_service_page_token parameter must be provided with the request.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSubscriptions(
    request: Subscriptions.ListSubscriptionsRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "sort",
            value: request.sort,
            schema: s.defaulted(subscriptionSortSchema, SubscriptionSort.SignupDate),
          },
          {
            name: "direction",
            value: request.direction,
            schema: s.optional(s.lazy(() => sortingDirectionSchema)),
          },
          {
            name: "state",
            value: request.state,
            schema: s.optional(s.lazy(() => subscriptionStateFilterSchema)),
          },
          { name: "product", value: request.product, schema: s.optional(s.lazy(() => product1Schema)) },
          { name: "q", value: request.q, schema: s.optional(s.string()) },
          { name: "q_scope", value: request.qScope, schema: s.optional(s.lazy(() => qScopeSchema)) },
          { name: "customer_id", value: request.customerId, schema: s.optional(s.int()) },
          { name: "product_price_point_id", value: request.productPricePointId, schema: s.optional(s.int()) },
          { name: "coupon", value: request.coupon, schema: s.optional(s.int()) },
          { name: "coupon_code", value: request.couponCode, schema: s.optional(s.string()) },
          {
            name: "collection_method",
            value: request.collectionMethod,
            schema: s.optional(s.lazy(() => collectionMethod1Schema)),
          },
          { name: "branding_theme_id", value: request.brandingThemeId, schema: s.optional(s.int()) },
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => subscriptionDateFieldSchema)),
          },
          { name: "start_date", value: request.startDate, schema: s.optional(s.dateOnly()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.dateOnly()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.dateTime()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.dateTime()) },
          { name: "metadata", value: request.metadata, schema: s.optional(s.record(s.string(), s.string())) },
          {
            name: "group_status",
            value: request.groupStatus,
            schema: s.optional(s.lazy(() => groupStatusSchema)),
          },
          { name: "dunning_exemption", value: request.dunningExemption, schema: s.optional(s.boolean()) },
          { name: "payment_gateways", value: request.paymentGateways, schema: s.optional(s.string()) },
          { name: "currencies", value: request.currencies, schema: s.optional(s.string()) },
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.array(s.lazy(() => subscriptionListIncludeSchema))),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => subscriptionResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Override Subscription
   *
   * @remarks
   * Sets certain subscription fields that are usually managed automatically. Some of the fields can
   * be set via the normal Subscriptions Update API, but others can only be set using this endpoint.
   *
   * This endpoint is provided for cases where you need to “align” Advanced Billing data with data
   * that happened in your system, perhaps before you started using Advanced Billing. For example,
   * you may choose to import your historical subscription data, and would like the activation and
   * cancellation dates in Advanced Billing to match your existing historical dates. Advanced
   * Billing does not backfill historical events (i.e. from the Events API), but some static data
   * can be changed via this API.
   *
   * Why are some fields only settable from this endpoint, and not the normal subscription create
   * and update endpoints? Because we want users of this endpoint to be aware that these fields are
   * usually managed by Advanced Billing, and using this API means **you are stepping out on your
   * own.**
   *
   * Changing these fields will not affect any other attributes. For example, adding an expiration
   * date will not affect the next assessment date on the subscription.
   *
   * If you regularly need to override the current_period_starts_at for new subscriptions, this can
   * also be accomplished by setting both `previous_billing_at` and `next_billing_at` at
   * subscription creation. See the documentation on [Importing
   * Subscriptions](./b3A6MTQxMDgzODg-create-subscription#subscriptions-import) for more
   * information.
   *
   * ## Limitations
   *
   * When passing `current_period_starts_at` some validations are made:
   *
   * 1. The subscription needs to be unbilled (no statements or invoices).
   * 2. The value passed must be a valid date/time. We recommend using the iso 8601 format.
   * 3. The value passed must be before the current date/time.
   *
   * If unpermitted parameters are sent, a 400 HTTP response is sent along with a string giving the
   * reason for the problem.
   *
   * @returns No Content
   *
   * @throws {@link Subscriptions.OverrideSubscriptionError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  overrideSubscription(
    request: Subscriptions.OverrideSubscriptionRequestParams,
    options?: RequestOptions,
  ): ApiPromise<undefined, Subscriptions.OverrideSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/override.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => overrideSubscriptionRequestSchema)),
        },
      },
      {
        success: { kind: "empty" },
        errorFactory: Subscriptions.OverrideSubscriptionError,
      },
      options,
    );
  }

  /**
   * Preview Subscription
   *
   * @remarks
   * Previews a subscription by POSTing the same JSON or XML as for a subscription creation.
   *
   * The "Next Billing" amount and "Next Billing" date are represented in each Subscriber's Summary.
   *
   * This endpoint does not create a subscription; it is meant to serve as a prediction.
   *
   * For more information, see [Subscriber Interface
   * Overview](https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview).
   *
   * ## Subscriptions can now work independently from the catalog
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, you can create subscriptions without a `product_id` or `product_handle` using POST
   * /subscriptions, building them entirely from components.
   *
   * A valid subscription must include at least one active component with:
   * - a positive `allocated_quantity`,
   * - a positive `unit_balance`, or
   * - 'enabled: true' (for on/off components)
   *
   * `component_id` can be provided as a numeric ID or in handle: format. If `trial_interval` and
   * `trial_interval_unit` are included, they are applied at creation.
   *
   * In the response, product and product price point fields are null, and component details are
   * returned instead.
   *
   * This functionality is supported in the API, but is not currently supported in SDKs.
   *
   * ## Taxable Subscriptions
   *
   * This endpoint previews taxes applicable to a purchase. For taxes to be previewed, the following
   * conditions must be met:
   *
   * + Taxes must be configured on the subscription
   * + The preview must be for the purchase of a taxable product or component, or combination of the
   *   two.
   * + The subscription payload must contain a full billing or shipping address to calculate tax
   *
   * For more information about creating taxable previews, see
   * [Taxes](https://maxio.zendesk.com/hc/en-us/sections/24287012349325-Taxes).
   *
   * You do **not** need to include a card number to generate tax information when you are
   * previewing a subscription. However, when you actually want to create the subscription, you must
   * include the credit card information if you want the billing address to be stored. The billing
   * address and the credit card information are stored together within the payment profile object.
   * Also, you cannot send a billing address without payment profile information, as the address is
   * stored on the card.
   *
   * You can pass shipping and billing addresses and still decide not to calculate taxes. To do
   * that, pass `skip_billing_manifest_taxes: true` attribute.
   *
   * ## Non-taxable Subscriptions
   *
   * If you'd like to calculate subscriptions that do not include tax, you can leave off the billing
   * information.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  previewSubscription(
    request: Subscriptions.PreviewSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionPreviewResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/preview.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createSubscriptionRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionPreviewResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Purge Subscription
   *
   * @remarks
   * Purges an individual subscription for sites in test mode.
   *
   * Provide the subscription ID in the URL. To confirm, supply the customer ID in the query string
   * `ack` parameter. You may also delete the customer record and/or payment profiles by passing
   * `cascade` parameters. For example, to delete just the customer record, the query params would
   * be: `?ack={customer_id}&cascade[]=customer`
   *
   * If you need to remove subscriptions from a live site, contact support to discuss your use case.
   *
   * ### Delete customer and payment profile
   *
   * The query params will be: `?ack={customer_id}&cascade[]=customer&cascade[]=payment_profile`
   *
   * @returns OK
   *
   * @throws {@link Subscriptions.PurgeSubscriptionError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  purgeSubscription(
    request: Subscriptions.PurgeSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, Subscriptions.PurgeSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/purge.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [
          { name: "ack", value: request.ack, schema: s.int() },
          {
            name: "cascade",
            value: request.cascade,
            schema: s.optional(s.array(s.lazy(() => subscriptionPurgeTypeSchema))),
          },
        ],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: Subscriptions.PurgeSubscriptionError,
      },
      options,
    );
  }

  /**
   * Read Subscription
   *
   * @remarks
   * Retrieves subscription details.
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, some subscriptions may not have an associated product. For subscriptions without an
   * associated product, 'product', 'product_price_point_id', and 'product_price_point_type' are
   * returned as 'null'.
   *
   * ## Self-Service Page token
   *
   * Self-Service Page token for the subscription is not returned by default. If this information is
   * desired, the include[]=self_service_page_token parameter must be provided with the request.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readSubscription(
    request: Subscriptions.ReadSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.array(s.lazy(() => subscriptionIncludeSchema))),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Remove Coupon from Subscription
   *
   * @remarks
   * Removes a coupon from an existing subscription.
   *
   * For more information on the expected behavior of removing a coupon from a subscription, see
   * [Coupons and
   * Subscriptions](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#removing-a-coupon).
   *
   * @returns OK
   *
   * @throws {@link Subscriptions.RemoveCouponFromSubscriptionError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  removeCouponFromSubscription(
    request: Subscriptions.RemoveCouponFromSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<string, Subscriptions.RemoveCouponFromSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/remove_coupon.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [{ name: "coupon_code", value: request.couponCode, schema: s.optional(s.string()) }],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.string() },
        errorFactory: Subscriptions.RemoveCouponFromSubscriptionError,
      },
      options,
    );
  }

  /**
   * Update Prepaid Subscription Configuration
   *
   * @remarks
   * Updates a subscription's prepaid configuration.
   *
   * @returns OK
   *
   * @throws {@link Subscriptions.UpdatePrepaidSubscriptionConfigurationError} when the API answers
   * with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updatePrepaidSubscriptionConfiguration(
    request: Subscriptions.UpdatePrepaidSubscriptionConfigurationRequest,
    options?: RequestOptions,
  ): ApiPromise<PrepaidConfigurationResponse, Subscriptions.UpdatePrepaidSubscriptionConfigurationError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/prepaid_configurations.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => upsertPrepaidConfigurationRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: prepaidConfigurationResponseSchema },
        errorFactory: Subscriptions.UpdatePrepaidSubscriptionConfigurationError,
      },
      options,
    );
  }

  /**
   * Update Subscription
   *
   * @remarks
   * Updates one or more attributes of a subscription.
   *
   * ## Update Subscription Payment Method
   *
   * Change the card that your subscriber uses for their subscription. You can also use this method
   * to change the expiration date of the card **if your gateway allows**.
   *
   * Do not use real card information for testing. See the Sites articles that cover [testing your
   * site
   * setup](https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0)
   * for more details on testing in your sandbox.
   *
   * Note that collecting and sending raw card details in production requires [PCI
   * compliance](https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0)
   * on your end. If your business is not PCI compliant, use
   * [Chargify.js](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0)
   * to collect credit card or bank account information.
   *
   * > Note: Partial card updates for **Authorize.Net** are not allowed via this endpoint. The
   * existing Payment Profile must be directly updated instead.
   *
   * ## Update Product
   *
   * You also use this method to change the subscription to a different product by setting a new
   * value for product_handle. A product change can be done in two different ways, **product
   * change** or **delayed product change**.
   *
   * ### Product Change
   *
   * You can change a subscription's product. The new payment amount is calculated and charged at
   * the normal start of the next period. If you require complex product changes or prorated
   * upgrades and downgrades instead, please see the documentation on [Migrating Subscription
   * Products](https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations#product-changes-and-migrations-0-0).
   *
   * To perform a product change, set either the `product_handle` or `product_id` attribute to that
   * of a different product from the same site as the subscription. You can also change the price
   * point by passing in either `product_price_point_id` or `product_price_point_handle` - otherwise
   * the new product's default price point is used.
   *
   * ### Delayed Product Change
   *
   * This method also changes the product and/or price point, and the new payment amount is
   * calculated and charged at the normal start of the next period.
   *
   * This method schedules the product change to happen automatically at the subscription’s next
   * renewal date. To perform a delayed product change, set the `product_handle` attribute as you
   * would in a regular product change, but also set the `product_change_delayed` attribute to
   * `true`. No proration applies in this case.
   *
   * You can also perform a delayed change to the price point by passing in either
   * `product_price_point_id` or `product_price_point_handle`
   *
   * > **Note:** To cancel a delayed product change, set `next_product_id` to an empty string.
   *
   * ## Billing Date Changes
   *
   * You can update dates for a subscription.
   *
   * ### Regular Billing Date Changes
   *
   * Send the `next_billing_at` to set the next billing date for the subscription. After that date
   * passes and the subscription is processed, the following billing date will be set according to
   * the subscription's product period.
   *
   * > Note: If you pass an invalid date, the correct date is automatically set to the correct date.
   * For example, if February 30 is passed, the next billing would be set to March 2nd in a non-leap
   * year.
   *
   * The server response will not return data under the key/value pair of `next_billing_at`. View
   * the key/value pair of `current_period_ends_at` to verify that the `next_billing_at` date has
   * been changed successfully.
   *
   * ### Calendar Billing and Snap Day Changes
   *
   * For a subscription using Calendar Billing, setting the next billing date is a bit different.
   * Send the `snap_day` attribute to change the calendar billing date for **a subscription using a
   * product eligible for calendar billing**.
   *
   * > Note: If you change the product associated with a subscription that contains a `snap_day` and
   * immediately READ/GET the subscription data, it will still contain the original `snap_day`. The
   * `snap_day` will be reset to `null` on the next billing cycle. This is because a product change
   * is instantaneous and only affects the product associated with a subscription.
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, some subscriptions may not have an associated product. For subscriptions without an
   * associated product, `product`, `product_price_point_id`, and `product_price_point_type` are
   * returned as `null`.
   *
   * @returns OK
   *
   * @throws {@link Subscriptions.UpdateSubscriptionError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateSubscription(
    request: Subscriptions.UpdateSubscriptionRequestParams,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, Subscriptions.UpdateSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateSubscriptionRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: Subscriptions.UpdateSubscriptionError,
      },
      options,
    );
  }
}

export namespace Subscriptions {
  export type ActivateSubscriptionRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: ActivateSubscriptionRequest;
  };

  export class ActivateSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1>>;

    static readonly errors: ErrorDecoders<ActivateSubscriptionError> = [
      {
        on: 400,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type ApplyCouponsToSubscriptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /**
     * A code for the coupon that would be applied to a subscription
     *
     * @deprecated
     */
    code?: string;
    body?: AddCouponsRequest;
  };

  export class ApplyCouponsToSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"subscriptionAddCouponError1", SubscriptionAddCouponError1>
    >;

    static readonly errors: ErrorDecoders<ApplyCouponsToSubscriptionError> = [
      {
        on: 422,
        kind: "subscriptionAddCouponError1",
        decode: { kind: "json", schema: subscriptionAddCouponError1Schema },
      },
    ];
  }

  export type CreateSubscriptionRequestParams = {
    body?: CreateSubscriptionRequest;
  };

  export class CreateSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CreateSubscriptionError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type FindSubscriptionRequest = {
    /** Subscription reference */
    reference?: string;
  };

  export class FindSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<FindSubscriptionError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ListSubscriptionsRequest = {
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
    /** The attribute by which to sort @default SubscriptionSort.SignupDate */
    sort?: SubscriptionSort;
    /** Controls the order in which results are returned. Use in query `direction=asc`. */
    direction?: SortingDirection;
    /** The current state of the subscription */
    state?: SubscriptionStateFilter;
    /**
     * Filter subscriptions by product. Accepts product ID or exact product name. Product handle is
     * not supported.
     */
    product?: Product1;
    /** Search string. */
    q?: string;
    /** Scope of fields used by the q search. */
    qScope?: QScope;
    /** The Advanced Billing id of the customer. */
    customerId?: number;
    /** The ID of the product price point. If supplied, product is required. */
    productPricePointId?: number;
    /**
     * The numeric id of the coupon currently applied to the subscription. (This can be found in the
     * URL when editing a coupon. Note that the coupon code cannot be used.)
     */
    coupon?: number;
    /** The coupon code currently applied to the subscription */
    couponCode?: string;
    /** The collection method for the subscription. */
    collectionMethod?: CollectionMethod1;
    /**
     * Filter subscriptions by the ID of an assigned Branding Theme. Branding Themes is a beta
     * feature. See [Understand Branding
     * Themes](https://docs.maxio.com/hc/en-us/articles/43796895662093-Understand-Branding-Themes#understand-branding-themes-0-0)
     * for more information.
     */
    brandingThemeId?: number;
    /**
     * The type of filter you'd like to apply to your search. Allowed Values: ,
     * current_period_ends_at, current_period_starts_at, created_at, activated_at, canceled_at,
     * expires_at, trial_started_at, trial_ended_at, updated_at
     */
    dateField?: SubscriptionDateField;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
     * with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified. Use in query `start_date=2022-07-01`.
     */
    startDate?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
     * with a timestamp up to and including 11:59:59PM in your site’s time zone on the date
     * specified. Use in query `end_date=2022-08-01`.
     */
    endDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns subscriptions with a timestamp at or after exact time provided in query. You can
     * specify timezone in query - otherwise your site's time zone will be used. If provided, this
     * parameter will be used instead of start_date. Use in query `start_datetime=2022-07-01
     * 09:00:05`.
     */
    startDatetime?: Date;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns subscriptions with a timestamp at or before exact time provided in query. You can
     * specify timezone in query - otherwise your site's time zone will be used. If provided, this
     * parameter will be used instead of end_date. Use in query `end_datetime=2022-08-01 10:00:05`.
     */
    endDatetime?: Date;
    /**
     * The value of the metadata field specified in the parameter. Use in query
     * `metadata[my-field]=value&metadata[other-field]=another_value`.
     */
    metadata?: Record<string, string>;
    /** Filter by whether a subscription is in a group. */
    groupStatus?: GroupStatus;
    /** Filter by dunning exemption status. */
    dunningExemption?: boolean;
    /** Comma-separated payment gateway identifiers. */
    paymentGateways?: string;
    /** Comma-separated currency codes. */
    currencies?: string;
    /**
     * Allows including additional data in the response. Use in query:
     * `include[]=self_service_page_token`.
     */
    include?: SubscriptionListInclude[];
  };

  export type OverrideSubscriptionRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** Only these fields are available to be set. */
    body?: OverrideSubscriptionRequest;
  };

  export class OverrideSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"singleErrorResponse1", SingleErrorResponse1>>;

    static readonly errors: ErrorDecoders<OverrideSubscriptionError> = [
      { on: 422, kind: "singleErrorResponse1", decode: { kind: "json", schema: singleErrorResponse1Schema } },
    ];
  }

  export type PreviewSubscriptionRequest = {
    body?: CreateSubscriptionRequest;
  };

  export type PurgeSubscriptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** id of the customer. */
    ack: number;
    /**
     * Options are "customer" or "payment_profile". Use in query:
     * `cascade[]=customer&cascade[]=payment_profile`.
     */
    cascade?: SubscriptionPurgeType[];
  };

  export class PurgeSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"subscriptionResponse", SubscriptionResponse>>;

    static readonly errors: ErrorDecoders<PurgeSubscriptionError> = [
      { on: 400, kind: "subscriptionResponse", decode: { kind: "json", schema: subscriptionResponseSchema } },
    ];
  }

  export type ReadSubscriptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /**
     * Allows including additional data in the response. Use in query:
     * `include[]=coupons&include[]=self_service_page_token`.
     */
    include?: SubscriptionInclude[];
  };

  export type RemoveCouponFromSubscriptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The coupon code */
    couponCode?: string;
  };

  export class RemoveCouponFromSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"subscriptionRemoveCouponErrors1", SubscriptionRemoveCouponErrors1>
    >;

    static readonly errors: ErrorDecoders<RemoveCouponFromSubscriptionError> = [
      {
        on: 422,
        kind: "subscriptionRemoveCouponErrors1",
        decode: { kind: "json", schema: subscriptionRemoveCouponErrors1Schema },
      },
    ];
  }

  export type UpdatePrepaidSubscriptionConfigurationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: UpsertPrepaidConfigurationRequest;
  };

  export class UpdatePrepaidSubscriptionConfigurationError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"prepaidConfigurationErrorResponse", PrepaidConfigurationErrorResponse>
    >;

    static readonly errors: ErrorDecoders<UpdatePrepaidSubscriptionConfigurationError> = [
      {
        on: 422,
        kind: "prepaidConfigurationErrorResponse",
        decode: { kind: "json", schema: prepaidConfigurationErrorResponseSchema },
      },
    ];
  }

  export type UpdateSubscriptionRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: UpdateSubscriptionRequest;
  };

  export class UpdateSubscriptionError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<UpdateSubscriptionError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
