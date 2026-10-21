import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditCardAttributesSchema, type CreditCardAttributes } from "./credit-card-attributes.js";
import { subscriptionCustomPriceSchema, type SubscriptionCustomPrice } from "./subscription-custom-price.js";
import { netTerms1Schema, type NetTerms1 } from "./unions/net-terms1.js";
import { snapDay1Schema, type SnapDay1 } from "./unions/snap-day1.js";
import {
  updateSubscriptionComponentSchema,
  type UpdateSubscriptionComponent,
} from "./update-subscription-component.js";

export type UpdateSubscription = {
  creditCardAttributes?: CreditCardAttributes;
  /** Set to the handle of a different product to change the subscription's product. */
  productHandle?: string;
  /** Set to the id of a different product to change the subscription's product. */
  productId?: number;
  productChangeDelayed?: boolean;
  /** Set to an empty string to cancel a delayed product change. */
  nextProductId?: string;
  nextProductPricePointId?: string;
  /** A day of month that subscription will be processed on. Can be 1 up to 28 or 'end'. */
  snapDay?: SnapDay1;
  /**
   * (Optional) Set this attribute to a future date/time to update a subscription in the Awaiting
   * Signup Date state, to Awaiting Signup. In the Awaiting Signup state, a subscription behaves
   * like any other. It can be canceled, allocated to, or have its billing date changed, etc. When
   * the `initial_billing_at` date hits, the subscription will transition to the expected state. If
   * the product has a trial, the subscription will enter a trial, otherwise it will go active.
   * Setup fees will be respected either before or after the trial, as configured on the price
   * point. If the payment is due at the initial_billing_at and it fails the subscription will be
   * immediately canceled. You can omit the initial_billing_at date to activate the subscription
   * immediately. See the [subscription
   * import](https://maxio.zendesk.com/hc/en-us/articles/24251489107213-Advanced-Billing-Subscription-Imports#date-format)
   * documentation for more information about Date/Time formats.
   */
  initialBillingAt?: Date;
  /**
   * (Optional) Set this attribute to true to move the subscription from Awaiting Signup, to
   * Awaiting Signup Date. Use this when you want to update a subscription that has an unknown
   * initial billing date. When the first billing date is known, update a subscription to set the
   * `initial_billing_at` date. The subscription moves to the awaiting signup with a scheduled
   * initial billing date. You can omit the initial_billing_at date to activate the subscription
   * immediately. See [Subscription
   * States](https://maxio-chargify.zendesk.com/hc/en-us/articles/5404222005773-Subscription-States)
   * for more information.
   *
   * @default false
   */
  deferSignup?: boolean;
  nextBillingAt?: Date;
  /**
   * The ID of the Branding Theme to assign to this subscription. When set, this subscription-level
   * Branding Theme is used instead of the customer's default Branding Theme for
   * subscription-related documents and communications that use subscription theming. Pass null or
   * an empty value to clear the subscription-level Branding Theme. Available only when Branding
   * Themes are enabled for the site. Not returned in the response.
   */
  brandingThemeId?: number | null;
  /**
   * Timestamp giving the expiration date of this subscription (if any). You may manually change the
   * expiration date at any point during a subscription period.
   */
  expiresAt?: Date;
  paymentCollectionMethod?: string;
  receivesInvoiceEmails?: boolean;
  netTerms?: NetTerms1;
  storedCredentialTransactionId?: number;
  reference?: string;
  /**
   * (Optional) Used in place of `product_price_point_id` to define a custom price point unique to
   * the subscription. A subscription can have up to 30 custom price points. Exceeding this limit
   * will result in an API error.
   */
  customPrice?: SubscriptionCustomPrice;
  /** (Optional) An array of component ids and custom prices to be added to the subscription. */
  components?: UpdateSubscriptionComponent[];
  /**
   * Enable Communication Delay feature, making sure no communication (email or SMS) is sent to the
   * Customer between 9PM and 8AM in time zone set by the `dunning_communication_delay_time_zone`
   * attribute.
   */
  dunningCommunicationDelayEnabled?: boolean;
  /** Time zone for the Dunning Communication Delay feature. */
  dunningCommunicationDelayTimeZone?: string | null;
  /** Set to change the current product's price point. */
  productPricePointId?: number;
  /** Set to change the current product's price point. */
  productPricePointHandle?: string;
};

export const updateSubscriptionSchema: Schema<UpdateSubscription> = s.object<UpdateSubscription>({
  creditCardAttributes: s.optional(s.lazy(() => creditCardAttributesSchema)),
  productHandle: s.optional(s.string()),
  productId: s.optional(s.int()),
  productChangeDelayed: s.optional(s.boolean()),
  nextProductId: s.optional(s.string()),
  nextProductPricePointId: s.optional(s.string()),
  snapDay: s.optional(s.lazy(() => snapDay1Schema)),
  initialBillingAt: s.optional(s.dateTime()),
  deferSignup: s.defaulted(s.boolean(), false),
  nextBillingAt: s.optional(s.dateTime()),
  brandingThemeId: s.optionalNullable(s.int()),
  expiresAt: s.optional(s.dateTime()),
  paymentCollectionMethod: s.optional(s.string()),
  receivesInvoiceEmails: s.optional(s.boolean()),
  netTerms: s.optional(s.lazy(() => netTerms1Schema)),
  storedCredentialTransactionId: s.optional(s.int()),
  reference: s.optional(s.string()),
  customPrice: s.optional(s.lazy(() => subscriptionCustomPriceSchema)),
  components: s.optional(s.array(s.lazy(() => updateSubscriptionComponentSchema))),
  dunningCommunicationDelayEnabled: s.optional(s.boolean()),
  dunningCommunicationDelayTimeZone: s.optionalNullable(s.string()),
  productPricePointId: s.optional(s.int()),
  productPricePointHandle: s.optional(s.string()),
  _keysMap: {
    creditCardAttributes: "credit_card_attributes",
    productHandle: "product_handle",
    productId: "product_id",
    productChangeDelayed: "product_change_delayed",
    nextProductId: "next_product_id",
    nextProductPricePointId: "next_product_price_point_id",
    snapDay: "snap_day",
    initialBillingAt: "initial_billing_at",
    deferSignup: "defer_signup",
    nextBillingAt: "next_billing_at",
    brandingThemeId: "branding_theme_id",
    expiresAt: "expires_at",
    paymentCollectionMethod: "payment_collection_method",
    receivesInvoiceEmails: "receives_invoice_emails",
    netTerms: "net_terms",
    storedCredentialTransactionId: "stored_credential_transaction_id",
    customPrice: "custom_price",
    dunningCommunicationDelayEnabled: "dunning_communication_delay_enabled",
    dunningCommunicationDelayTimeZone: "dunning_communication_delay_time_zone",
    productPricePointId: "product_price_point_id",
    productPricePointHandle: "product_price_point_handle",
  },
});
