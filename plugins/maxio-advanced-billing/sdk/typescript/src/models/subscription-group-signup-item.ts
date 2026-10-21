import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { calendarBillingSchema, type CalendarBilling } from "./calendar-billing.js";
import { subscriptionCustomPriceSchema, type SubscriptionCustomPrice } from "./subscription-custom-price.js";
import {
  subscriptionGroupSignupComponentSchema,
  type SubscriptionGroupSignupComponent,
} from "./subscription-group-signup-component.js";

export type SubscriptionGroupSignupItem = {
  /**
   * The API Handle of the product for which you are creating a subscription. Required, unless a
   * `product_id` is given instead.
   */
  productHandle?: string;
  /**
   * The Product ID of the product for which you are creating a subscription. You can pass either
   * `product_id` or `product_handle`.
   */
  productId?: number;
  /** The ID of the particular price point on the product. */
  productPricePointId?: number;
  /** The user-friendly API handle of a product's particular price point. */
  productPricePointHandle?: string;
  /**
   * Use in place of passing product and component information to set up the subscription with an
   * existing offer. May be either the Chargify ID of the offer or its handle prefixed with
   * `handle:`.
   */
  offerId?: number;
  /** The reference value (provided by your app) for the subscription itself. */
  reference?: string;
  /** One of the subscriptions must be marked as primary in the group. */
  primary?: boolean;
  /**
   * (Optional) If Multi-Currency is enabled and the currency is configured in Chargify, pass it at
   * signup to create a subscription on a non-default currency. Note that you cannot update the
   * currency of an existing subscription.
   */
  currency?: string;
  /** An array for all the coupons attached to the subscription. */
  couponCodes?: string[];
  components?: SubscriptionGroupSignupComponent[];
  /**
   * (Optional) Used in place of `product_price_point_id` to define a custom price point unique to
   * the subscription. A subscription can have up to 30 custom price points. Exceeding this limit
   * will result in an API error.
   */
  customPrice?: SubscriptionCustomPrice;
  /** (Optional). Cannot be used when also specifying next_billing_at. */
  calendarBilling?: CalendarBilling;
  /**
   * (Optional) A set of key/value pairs representing custom fields and their values. Metafields
   * will be created “on-the-fly” in your site for a given key, if they have not been created yet.
   */
  metafields?: Record<string, string>;
};

export const subscriptionGroupSignupItemSchema: Schema<SubscriptionGroupSignupItem> =
  s.object<SubscriptionGroupSignupItem>({
    productHandle: s.optional(s.string()),
    productId: s.optional(s.int()),
    productPricePointId: s.optional(s.int()),
    productPricePointHandle: s.optional(s.string()),
    offerId: s.optional(s.int()),
    reference: s.optional(s.string()),
    primary: s.optional(s.boolean()),
    currency: s.optional(s.string()),
    couponCodes: s.optional(s.array(s.string())),
    components: s.optional(s.array(s.lazy(() => subscriptionGroupSignupComponentSchema))),
    customPrice: s.optional(s.lazy(() => subscriptionCustomPriceSchema)),
    calendarBilling: s.optional(s.lazy(() => calendarBillingSchema)),
    metafields: s.optional(s.record(s.string(), s.string())),
    _keysMap: {
      productHandle: "product_handle",
      productId: "product_id",
      productPricePointId: "product_price_point_id",
      productPricePointHandle: "product_price_point_handle",
      offerId: "offer_id",
      couponCodes: "coupon_codes",
      customPrice: "custom_price",
      calendarBilling: "calendar_billing",
    },
  });
