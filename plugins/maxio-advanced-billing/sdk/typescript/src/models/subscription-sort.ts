import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SubscriptionSort = {
  SignupDate: "signup_date",
  PeriodStart: "period_start",
  PeriodEnd: "period_end",
  NextAssessment: "next_assessment",
  UpdatedAt: "updated_at",
  CreatedAt: "created_at",
  TotalPayments: "total_payments",
  Id: "id",
  OpenBalance: "open_balance",
  ExpiresAt: "expires_at",
} as const;
export type SubscriptionSort = (typeof SubscriptionSort)[keyof typeof SubscriptionSort] | (string & {});

export const subscriptionSortSchema: EnumSchema<SubscriptionSort> =
  s.enumOf<SubscriptionSort>(SubscriptionSort);
