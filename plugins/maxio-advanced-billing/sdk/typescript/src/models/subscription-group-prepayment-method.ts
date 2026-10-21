import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SubscriptionGroupPrepaymentMethod = {
  Check: "check",
  Cash: "cash",
  MoneyOrder: "money_order",
  Ach: "ach",
  PaypalAccount: "paypal_account",
  Other: "other",
} as const;
export type SubscriptionGroupPrepaymentMethod =
  | (typeof SubscriptionGroupPrepaymentMethod)[keyof typeof SubscriptionGroupPrepaymentMethod]
  | (string & {});

export const subscriptionGroupPrepaymentMethodSchema: EnumSchema<SubscriptionGroupPrepaymentMethod> =
  s.enumOf<SubscriptionGroupPrepaymentMethod>(SubscriptionGroupPrepaymentMethod);
