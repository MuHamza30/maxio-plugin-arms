import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionMrrBreakout = {
  planAmountInCents: number;
  usageAmountInCents: number;
};

export const subscriptionMrrBreakoutSchema: Schema<SubscriptionMrrBreakout> =
  s.object<SubscriptionMrrBreakout>({
    planAmountInCents: s.int(),
    usageAmountInCents: s.int(),
    _keysMap: {
      planAmountInCents: "plan_amount_in_cents",
      usageAmountInCents: "usage_amount_in_cents",
    },
  });
