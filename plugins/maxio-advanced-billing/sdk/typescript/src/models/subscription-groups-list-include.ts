import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SubscriptionGroupsListInclude = {
  AccountBalances: "account_balances",
} as const;
export type SubscriptionGroupsListInclude =
  | (typeof SubscriptionGroupsListInclude)[keyof typeof SubscriptionGroupsListInclude]
  | (string & {});

export const subscriptionGroupsListIncludeSchema: EnumSchema<SubscriptionGroupsListInclude> =
  s.enumOf<SubscriptionGroupsListInclude>(SubscriptionGroupsListInclude);
