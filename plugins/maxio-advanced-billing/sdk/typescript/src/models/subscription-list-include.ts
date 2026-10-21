import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SubscriptionListInclude = {
  SelfServicePageToken: "self_service_page_token",
  CurrentAccountBalanceInCents: "current_account_balance_in_cents",
  CurrentBillingAmount: "current_billing_amount",
  Coupons: "coupons",
} as const;
export type SubscriptionListInclude =
  | (typeof SubscriptionListInclude)[keyof typeof SubscriptionListInclude]
  | (string & {});

export const subscriptionListIncludeSchema: EnumSchema<SubscriptionListInclude> =
  s.enumOf<SubscriptionListInclude>(SubscriptionListInclude);
