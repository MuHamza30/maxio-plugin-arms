import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionRemoveCouponErrors1 = {
  subscription: string[];
};

export const subscriptionRemoveCouponErrors1Schema: Schema<SubscriptionRemoveCouponErrors1> =
  s.object<SubscriptionRemoveCouponErrors1>({
    subscription: s.array(s.string()),
  });
