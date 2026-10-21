import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SubscriptionGroupInclude = {
  CurrentBillingAmountInCents: "current_billing_amount_in_cents",
} as const;
export type SubscriptionGroupInclude =
  | (typeof SubscriptionGroupInclude)[keyof typeof SubscriptionGroupInclude]
  | (string & {});

export const subscriptionGroupIncludeSchema: EnumSchema<SubscriptionGroupInclude> =
  s.enumOf<SubscriptionGroupInclude>(SubscriptionGroupInclude);
