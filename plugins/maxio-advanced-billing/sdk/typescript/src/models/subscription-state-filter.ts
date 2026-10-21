import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** Allowed values for filtering by the current state of the subscription. */
export const SubscriptionStateFilter = {
  Active: "active",
  Canceled: "canceled",
  Expired: "expired",
  ExpiredCards: "expired_cards",
  ExpiredCardsLiveSubscriptions: "expired_cards_(live_subscriptions)",
  ExpiredCardsAllSubscriptions: "expired_cards_(all_subscriptions)",
  OnHold: "on_hold",
  AwaitingSignup: "awaiting_signup",
  AwaitingSignupDate: "awaiting_signup_date",
  PastDue: "past_due",
  PendingCancellation: "pending_cancellation",
  PendingRenewal: "pending_renewal",
  PrepaidDunning: "prepaid_dunning",
  Suspended: "suspended",
  TrialEnded: "trial_ended",
  Trialing: "trialing",
  Unpaid: "unpaid",
} as const;
export type SubscriptionStateFilter =
  | (typeof SubscriptionStateFilter)[keyof typeof SubscriptionStateFilter]
  | (string & {});

export const subscriptionStateFilterSchema: EnumSchema<SubscriptionStateFilter> =
  s.enumOf<SubscriptionStateFilter>(SubscriptionStateFilter);
