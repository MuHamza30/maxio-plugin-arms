import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionMrrBreakoutSchema, type SubscriptionMrrBreakout } from "./subscription-mrr-breakout.js";

export type SubscriptionMrr = {
  subscriptionId: number;
  mrrAmountInCents: number;
  breakouts?: SubscriptionMrrBreakout;
};

export const subscriptionMrrSchema: Schema<SubscriptionMrr> = s.object<SubscriptionMrr>({
  subscriptionId: s.int(),
  mrrAmountInCents: s.int(),
  breakouts: s.optional(s.lazy(() => subscriptionMrrBreakoutSchema)),
  _keysMap: {
    subscriptionId: "subscription_id",
    mrrAmountInCents: "mrr_amount_in_cents",
  },
});
