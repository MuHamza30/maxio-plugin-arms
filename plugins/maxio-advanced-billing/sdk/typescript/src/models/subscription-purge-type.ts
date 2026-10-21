import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SubscriptionPurgeType = {
  Customer: "customer",
  PaymentProfile: "payment_profile",
} as const;
export type SubscriptionPurgeType =
  | (typeof SubscriptionPurgeType)[keyof typeof SubscriptionPurgeType]
  | (string & {});

export const subscriptionPurgeTypeSchema: EnumSchema<SubscriptionPurgeType> =
  s.enumOf<SubscriptionPurgeType>(SubscriptionPurgeType);
