import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  bankAccountPaymentProfileSchema,
  type BankAccountPaymentProfile,
} from "./bank-account-payment-profile.js";
import { cancellationMethodSchema, type CancellationMethod } from "./cancellation-method.js";
import { collectionMethodSchema, type CollectionMethod } from "./collection-method.js";
import {
  creditCardPaymentProfileSchema,
  type CreditCardPaymentProfile,
} from "./credit-card-payment-profile.js";
import { customerSchema, type Customer } from "./customer.js";
import { nestedSubscriptionGroupSchema, type NestedSubscriptionGroup } from "./nested-subscription-group.js";
import { prepaidConfigurationSchema, type PrepaidConfiguration } from "./prepaid-configuration.js";
import { pricePointTypeSchema, type PricePointType } from "./price-point-type.js";
import { productSchema, type Product } from "./product.js";
import {
  subscriptionIncludedCouponSchema,
  type SubscriptionIncludedCoupon,
} from "./subscription-included-coupon.js";
import { subscriptionStateSchema, type SubscriptionState } from "./subscription-state.js";

export type Subscription = {
  /** The subscription unique id within Chargify. */
  id?: number;
  /**
   * The state of a subscription.
   * * **Live States**
   *     * `active` - A normal, active subscription. It is not in a trial and is paid and up to
   *       date.
   *     * `assessing` - An internal (transient) state that indicates a subscription is in the
   *       middle of periodic assessment. Do not base any access decisions in your app on this
   *       state, as it may not always be exposed.
   *     * `pending` - An internal (transient) state that indicates a subscription is in the
   *       creation process. Do not base any access decisions in your app on this state, as it may
   *       not always be exposed.
   *     * `trialing` - A subscription in trialing state has a valid trial subscription. This type
   *       of subscription may transition to active once payment is received when the trial has
   *       ended. Otherwise, it may go to a Problem or End of Life state.
   *     * `paused` - An internal state that indicates that your account with Advanced Billing is in
   *       arrears.
   * * **Problem States**
   *     * `past_due` - Indicates that the most recent payment has failed, and payment is past due
   *       for this subscription. If you have enabled our automated dunning, this subscription will
   *       be in the dunning process (additional status and callbacks from the dunning process will
   *       be available in the future). If you are handling dunning and payment updates yourself,
   *       you will want to use this state to initiate a payment update from your customers.
   *     * `soft_failure` - Indicates that normal assessment/processing of the subscription has
   *       failed for a reason that cannot be fixed by the Customer. For example, a Soft Fail may
   *       result from a timeout at the gateway or incorrect credentials on your part. The
   *       subscriptions should be retried automatically. An interface is being built for you to
   *       review problems resulting from these events to take manual action when needed.
   *     * `unpaid` - Indicates an unpaid subscription. A subscription is marked unpaid if the retry
   *       period expires and you have configured your
   *       [Dunning](https://maxio.zendesk.com/hc/en-us/articles/24287076583565-Dunning-Overview)
   *       settings to have a Final Action of `mark the subscription unpaid`.
   * * **End of Life States**
   *     * `canceled` - Indicates a canceled subscription. This may happen at your request (via the
   *       API or the web interface) or due to the expiration of the
   *       [Dunning](https://maxio.zendesk.com/hc/en-us/articles/24287076583565-Dunning-Overview)
   *       process without payment. See the
   *       [Reactivation](https://maxio.zendesk.com/hc/en-us/articles/24252109503629-Reactivating-and-Resuming)
   *       documentation for info on how to restart a canceled subscription. While a subscription is
   *       canceled, its period will not advance, it will not accrue any new charges, and Advanced
   *       Billing will not attempt to collect the overdue balance.
   *     * `expired` - Indicates a subscription that has expired due to running its normal life
   *       cycle. Some products may be configured to have an expiration period. An expired
   *       subscription then is one that stayed active until it fulfilled its full period.
   *     * `failed_to_create` - Indicates that signup has failed. (You may see this state in a
   *       signup_failure webhook.)
   *     * `on_hold` - Indicates that a subscription’s billing has been temporarily stopped. While
   *       it is expected that the subscription will resume and return to active status, this is
   *       still treated as an “End of Life” state because the customer is not paying for services
   *       during this time.
   *     * `suspended` - Indicates that a prepaid subscription has used up all their prepayment
   *       balance. If a prepayment is applied, it will return to an active state.
   *     * `trial_ended` - A subscription in a trial_ended state is a subscription that completed a
   *       no-obligation trial and did not have a card on file at the expiration of the trial
   *       period. See [Product Pricing – No Obligation
   *       Trials](https://maxio.zendesk.com/hc/en-us/articles/24261076617869-Product-Editing) for
   *       more details.
   *
   * See [Subscription
   * States](https://maxio.zendesk.com/hc/en-us/articles/24252119027853-Subscription-States) for
   * more info about subscription states and state transitions.
   */
  state?: SubscriptionState;
  /** Gives the current outstanding subscription balance in the number of cents. */
  balanceInCents?: number;
  /** Gives the total revenue from the subscription in the number of cents. */
  totalRevenueInCents?: number;
  /**
   * (Added Nov 5 2013) The recurring amount of the product (and version), currently subscribed.
   * NOTE: this may differ from the current price of the product, if you’ve changed the price of the
   * product but haven’t moved this subscription to a newer version.
   */
  productPriceInCents?: number;
  /**
   * The version of the product for the subscription. Note that this is a deprecated field kept for
   * backwards-compatibility.
   */
  productVersionNumber?: number;
  /**
   * Timestamp relating to the end of the current (recurring) period (i.e., when the next regularly
   * scheduled attempted charge will occur)
   */
  currentPeriodEndsAt?: Date | null;
  /**
   * Timestamp that indicates when capture of payment will be tried or retried. This value will
   * usually track the current_period_ends_at, but will diverge if a renewal payment fails and must
   * be retried. In that case, the current_period_ends_at will advance to the end of the next period
   * (time doesn’t stop because a payment was missed) but the next_assessment_at will be scheduled
   * for the auto-retry time (e.g., 24 hours in the future, in some cases).
   */
  nextAssessmentAt?: Date | null;
  /** Timestamp for when the trial period (if any) began */
  trialStartedAt?: Date | null;
  /** Timestamp for when the trial period (if any) ended */
  trialEndedAt?: Date | null;
  /**
   * Timestamp for when the subscription began (i.e., when it came out of trial, or when it began in
   * the case of no trial)
   */
  activatedAt?: Date | null;
  /** Timestamp giving the expiration date of this subscription (if any) */
  expiresAt?: Date | null;
  /** The creation date for this subscription */
  createdAt?: Date;
  /** The date of last update for this subscription */
  updatedAt?: Date;
  /** Seller-provided reason for, or note about, the cancellation. */
  cancellationMessage?: string | null;
  /**
   * The process used to cancel the subscription, if the subscription has been canceled. It is nil
   * if the subscription's state is not canceled.
   */
  cancellationMethod?: CancellationMethod | null;
  /** Whether or not the subscription will (or has) canceled at the end of the period. */
  cancelAtEndOfPeriod?: boolean | null;
  /** The timestamp of the most recent cancellation */
  canceledAt?: Date | null;
  /** Timestamp relating to the start of the current (recurring) period */
  currentPeriodStartedAt?: Date | null;
  /**
   * Only valid for webhook payloads The previous state for webhooks that have indicated a change in
   * state. For normal API calls, this will always be the same as the state (current state).
   */
  previousState?: SubscriptionState;
  /** The ID of the transaction that generated the revenue */
  signupPaymentId?: number;
  /**
   * The revenue, formatted as a string of decimal separated dollars and cents, from the
   * subscription signup ($50.00 would be formatted as 50.00)
   */
  signupRevenue?: string;
  /** Timestamp for when the subscription is currently set to cancel. */
  delayedCancelAt?: Date | null;
  /**
   * (deprecated) The coupon code of the single coupon currently applied to the subscription. See
   * coupon_codes instead as subscriptions can now have more than one coupon.
   *
   * @deprecated
   */
  couponCode?: string | null;
  /** A day of month that subscription will be processed on. Can be 1 up to 28 or 'end'. */
  snapDay?: string | null;
  /**
   * The type of payment collection to be used in the subscription. For legacy Statements
   * Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing
   * Architecture valid options are - `remittance`, `automatic`, `prepaid`.
   */
  paymentCollectionMethod?: CollectionMethod;
  customer?: Customer;
  product?: Product;
  creditCard?: CreditCardPaymentProfile;
  group?: NestedSubscriptionGroup | null;
  bankAccount?: BankAccountPaymentProfile;
  /** The payment profile type for the active profile on file. */
  paymentType?: string | null;
  /** The subscription's unique code that can be given to referrals. */
  referralCode?: string | null;
  /**
   * If a delayed product change is scheduled, the ID of the product that the subscription will be
   * changed to at the next renewal.
   */
  nextProductId?: number | null;
  /**
   * If a delayed product change is scheduled, the handle of the product that the subscription will
   * be changed to at the next renewal.
   */
  nextProductHandle?: string | null;
  /**
   * (deprecated) How many times the subscription's single coupon has been used. This field has no
   * replacement for multiple coupons.
   *
   * @deprecated
   */
  couponUseCount?: number | null;
  /**
   * (deprecated) How many times the subscription's single coupon may be used. This field has no
   * replacement for multiple coupons.
   *
   * @deprecated
   */
  couponUsesAllowed?: number | null;
  /** The churn reason code associated to a canceled subscription. */
  reasonCode?: string | null;
  /** The date the subscription is scheduled to automatically resume from the on_hold state. */
  automaticallyResumeAt?: Date | null;
  /** An array for all the coupons attached to the subscription. */
  couponCodes?: string[];
  /** The ID of the offer associated with the subscription. */
  offerId?: number | null;
  /**
   * On Relationship Invoicing, the ID of the individual paying for the subscription. Defaults to
   * the Customer ID unless the 'Customer Hierarchies & WhoPays' feature is enabled.
   */
  payerId?: number | null;
  /**
   * The balance in cents plus the estimated renewal amount in cents. Returned ONLY for the
   * readSubscription operation as it's a compute intensive operation.
   */
  currentBillingAmountInCents?: number;
  /** The product price point currently subscribed to. */
  productPricePointId?: number;
  /**
   * Price point type. We expose the following types:
   * 1. **default**: a price point that is marked as a default price for a certain product.
   * 2. **custom**: a custom price point.
   * 3. **catalog**: a price point that is **not** marked as a default price for a certain product
   *    and is **not** a custom one.
   */
  productPricePointType?: PricePointType;
  /**
   * If a delayed product change is scheduled, the ID of the product price point that the
   * subscription will be changed to at the next renewal.
   */
  nextProductPricePointId?: number | null;
  /** On Relationship Invoicing, the number of days before a renewal invoice is due. */
  netTerms?: number | null;
  /**
   * For European sites subject to PSD2 and using 3D Secure, this can be used to reference a
   * previous transaction for the customer. This will ensure the card will be charged successfully
   * at renewal.
   */
  storedCredentialTransactionId?: number | null;
  /** The reference value (provided by your app) for the subscription itself. */
  reference?: string | null;
  /** The timestamp of the most recent on hold action. */
  onHoldAt?: Date | null;
  /**
   * Boolean representing whether the subscription is prepaid and currently in dunning. Only
   * returned for Relationship Invoicing sites with the feature enabled.
   */
  prepaidDunning?: boolean;
  /**
   * Additional coupon data. To use this data you also have to include the following param in the
   * request: `include[]=coupons`. Only in Read Subscription Endpoint.
   */
  coupons?: SubscriptionIncludedCoupon[];
  /**
   * Enable Communication Delay feature, making sure no communication (email or SMS) is sent to the
   * Customer between 9PM and 8AM in time zone set by the `dunning_communication_delay_time_zone`
   * attribute.
   */
  dunningCommunicationDelayEnabled?: boolean;
  /** Time zone for the Dunning Communication Delay feature. */
  dunningCommunicationDelayTimeZone?: string | null;
  receivesInvoiceEmails?: boolean | null;
  locale?: string | null;
  currency?: string;
  scheduledCancellationAt?: Date | null;
  creditBalanceInCents?: number;
  prepaymentBalanceInCents?: number;
  prepaidConfiguration?: PrepaidConfiguration | null;
  /**
   * Returned only for list/read Subscription operation when `include[]=self_service_page_token`
   * parameter is provided.
   */
  selfServicePageToken?: string;
};

export const subscriptionSchema: Schema<Subscription> = s.object<Subscription>({
  id: s.optional(s.int()),
  state: s.optional(s.lazy(() => subscriptionStateSchema)),
  balanceInCents: s.optional(s.int()),
  totalRevenueInCents: s.optional(s.int()),
  productPriceInCents: s.optional(s.int()),
  productVersionNumber: s.optional(s.int()),
  currentPeriodEndsAt: s.optionalNullable(s.dateTime()),
  nextAssessmentAt: s.optionalNullable(s.dateTime()),
  trialStartedAt: s.optionalNullable(s.dateTime()),
  trialEndedAt: s.optionalNullable(s.dateTime()),
  activatedAt: s.optionalNullable(s.dateTime()),
  expiresAt: s.optionalNullable(s.dateTime()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  cancellationMessage: s.optionalNullable(s.string()),
  cancellationMethod: s.optionalNullable(s.lazy(() => cancellationMethodSchema)),
  cancelAtEndOfPeriod: s.optionalNullable(s.boolean()),
  canceledAt: s.optionalNullable(s.dateTime()),
  currentPeriodStartedAt: s.optionalNullable(s.dateTime()),
  previousState: s.optional(s.lazy(() => subscriptionStateSchema)),
  signupPaymentId: s.optional(s.int()),
  signupRevenue: s.optional(s.string()),
  delayedCancelAt: s.optionalNullable(s.dateTime()),
  couponCode: s.optionalNullable(s.string()),
  snapDay: s.optionalNullable(s.string()),
  paymentCollectionMethod: s.optional(s.lazy(() => collectionMethodSchema)),
  customer: s.optional(s.lazy(() => customerSchema)),
  product: s.optional(s.lazy(() => productSchema)),
  creditCard: s.optional(s.lazy(() => creditCardPaymentProfileSchema)),
  group: s.optionalNullable(s.lazy(() => nestedSubscriptionGroupSchema)),
  bankAccount: s.optional(s.lazy(() => bankAccountPaymentProfileSchema)),
  paymentType: s.optionalNullable(s.string()),
  referralCode: s.optionalNullable(s.string()),
  nextProductId: s.optionalNullable(s.int()),
  nextProductHandle: s.optionalNullable(s.string()),
  couponUseCount: s.optionalNullable(s.int()),
  couponUsesAllowed: s.optionalNullable(s.int()),
  reasonCode: s.optionalNullable(s.string()),
  automaticallyResumeAt: s.optionalNullable(s.dateTime()),
  couponCodes: s.optional(s.array(s.string())),
  offerId: s.optionalNullable(s.int()),
  payerId: s.optionalNullable(s.int()),
  currentBillingAmountInCents: s.optional(s.int()),
  productPricePointId: s.optional(s.int()),
  productPricePointType: s.optional(s.lazy(() => pricePointTypeSchema)),
  nextProductPricePointId: s.optionalNullable(s.int()),
  netTerms: s.optionalNullable(s.int()),
  storedCredentialTransactionId: s.optionalNullable(s.int()),
  reference: s.optionalNullable(s.string()),
  onHoldAt: s.optionalNullable(s.dateTime()),
  prepaidDunning: s.optional(s.boolean()),
  coupons: s.optional(s.array(s.lazy(() => subscriptionIncludedCouponSchema))),
  dunningCommunicationDelayEnabled: s.optional(s.boolean()),
  dunningCommunicationDelayTimeZone: s.optionalNullable(s.string()),
  receivesInvoiceEmails: s.optionalNullable(s.boolean()),
  locale: s.optionalNullable(s.string()),
  currency: s.optional(s.string()),
  scheduledCancellationAt: s.optionalNullable(s.dateTime()),
  creditBalanceInCents: s.optional(s.int()),
  prepaymentBalanceInCents: s.optional(s.int()),
  prepaidConfiguration: s.optionalNullable(s.lazy(() => prepaidConfigurationSchema)),
  selfServicePageToken: s.optional(s.string()),
  _keysMap: {
    balanceInCents: "balance_in_cents",
    totalRevenueInCents: "total_revenue_in_cents",
    productPriceInCents: "product_price_in_cents",
    productVersionNumber: "product_version_number",
    currentPeriodEndsAt: "current_period_ends_at",
    nextAssessmentAt: "next_assessment_at",
    trialStartedAt: "trial_started_at",
    trialEndedAt: "trial_ended_at",
    activatedAt: "activated_at",
    expiresAt: "expires_at",
    createdAt: "created_at",
    updatedAt: "updated_at",
    cancellationMessage: "cancellation_message",
    cancellationMethod: "cancellation_method",
    cancelAtEndOfPeriod: "cancel_at_end_of_period",
    canceledAt: "canceled_at",
    currentPeriodStartedAt: "current_period_started_at",
    previousState: "previous_state",
    signupPaymentId: "signup_payment_id",
    signupRevenue: "signup_revenue",
    delayedCancelAt: "delayed_cancel_at",
    couponCode: "coupon_code",
    snapDay: "snap_day",
    paymentCollectionMethod: "payment_collection_method",
    creditCard: "credit_card",
    bankAccount: "bank_account",
    paymentType: "payment_type",
    referralCode: "referral_code",
    nextProductId: "next_product_id",
    nextProductHandle: "next_product_handle",
    couponUseCount: "coupon_use_count",
    couponUsesAllowed: "coupon_uses_allowed",
    reasonCode: "reason_code",
    automaticallyResumeAt: "automatically_resume_at",
    couponCodes: "coupon_codes",
    offerId: "offer_id",
    payerId: "payer_id",
    currentBillingAmountInCents: "current_billing_amount_in_cents",
    productPricePointId: "product_price_point_id",
    productPricePointType: "product_price_point_type",
    nextProductPricePointId: "next_product_price_point_id",
    netTerms: "net_terms",
    storedCredentialTransactionId: "stored_credential_transaction_id",
    onHoldAt: "on_hold_at",
    prepaidDunning: "prepaid_dunning",
    dunningCommunicationDelayEnabled: "dunning_communication_delay_enabled",
    dunningCommunicationDelayTimeZone: "dunning_communication_delay_time_zone",
    receivesInvoiceEmails: "receives_invoice_emails",
    scheduledCancellationAt: "scheduled_cancellation_at",
    creditBalanceInCents: "credit_balance_in_cents",
    prepaymentBalanceInCents: "prepayment_balance_in_cents",
    prepaidConfiguration: "prepaid_configuration",
    selfServicePageToken: "self_service_page_token",
  },
});
