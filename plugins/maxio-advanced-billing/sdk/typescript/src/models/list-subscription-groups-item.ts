import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { groupTypeSchema, type GroupType } from "./group-type.js";
import {
  subscriptionGroupBalancesSchema,
  type SubscriptionGroupBalances,
} from "./subscription-group-balances.js";

export type ListSubscriptionGroupsItem = {
  uid?: string;
  scheme?: number;
  customerId?: number;
  paymentProfileId?: number;
  subscriptionIds?: number[];
  primarySubscriptionId?: number;
  nextAssessmentAt?: Date;
  state?: string;
  cancelAtEndOfPeriod?: boolean;
  accountBalances?: SubscriptionGroupBalances;
  groupType?: GroupType;
};

export const listSubscriptionGroupsItemSchema: Schema<ListSubscriptionGroupsItem> =
  s.object<ListSubscriptionGroupsItem>({
    uid: s.optional(s.string()),
    scheme: s.optional(s.int()),
    customerId: s.optional(s.int()),
    paymentProfileId: s.optional(s.int()),
    subscriptionIds: s.optional(s.array(s.int())),
    primarySubscriptionId: s.optional(s.int()),
    nextAssessmentAt: s.optional(s.dateTime()),
    state: s.optional(s.string()),
    cancelAtEndOfPeriod: s.optional(s.boolean()),
    accountBalances: s.optional(s.lazy(() => subscriptionGroupBalancesSchema)),
    groupType: s.optional(s.lazy(() => groupTypeSchema)),
    _keysMap: {
      customerId: "customer_id",
      paymentProfileId: "payment_profile_id",
      subscriptionIds: "subscription_ids",
      primarySubscriptionId: "primary_subscription_id",
      nextAssessmentAt: "next_assessment_at",
      cancelAtEndOfPeriod: "cancel_at_end_of_period",
      accountBalances: "account_balances",
      groupType: "group_type",
    },
  });
