import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionIncludedCoupon = {
  code?: string;
  useCount?: number;
  usesAllowed?: number;
  expiresAt?: string | null;
  recurring?: boolean;
  amountInCents?: number | null;
  percentage?: string | null;
};

export const subscriptionIncludedCouponSchema: Schema<SubscriptionIncludedCoupon> =
  s.object<SubscriptionIncludedCoupon>({
    code: s.optional(s.string()),
    useCount: s.optional(s.int()),
    usesAllowed: s.optional(s.int()),
    expiresAt: s.optionalNullable(s.string()),
    recurring: s.optional(s.boolean()),
    amountInCents: s.optionalNullable(s.int()),
    percentage: s.optionalNullable(s.string()),
    _keysMap: {
      useCount: "use_count",
      usesAllowed: "uses_allowed",
      expiresAt: "expires_at",
      amountInCents: "amount_in_cents",
    },
  });
