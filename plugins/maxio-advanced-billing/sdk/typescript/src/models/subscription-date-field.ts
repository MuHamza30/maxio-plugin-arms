import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SubscriptionDateField = {
  CurrentPeriodEndsAt: "current_period_ends_at",
  CurrentPeriodStartsAt: "current_period_starts_at",
  CreatedAt: "created_at",
  ActivatedAt: "activated_at",
  CanceledAt: "canceled_at",
  ExpiresAt: "expires_at",
  TrialStartedAt: "trial_started_at",
  TrialEndedAt: "trial_ended_at",
  UpdatedAt: "updated_at",
} as const;
export type SubscriptionDateField =
  | (typeof SubscriptionDateField)[keyof typeof SubscriptionDateField]
  | (string & {});

export const subscriptionDateFieldSchema: EnumSchema<SubscriptionDateField> =
  s.enumOf<SubscriptionDateField>(SubscriptionDateField);
