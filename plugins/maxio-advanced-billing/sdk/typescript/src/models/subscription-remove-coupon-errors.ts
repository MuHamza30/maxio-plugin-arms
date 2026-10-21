import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionRemoveCouponErrors = {
  subscription: string[];
};

export const subscriptionRemoveCouponErrorsSchema: Schema<SubscriptionRemoveCouponErrors> =
  s.object<SubscriptionRemoveCouponErrors>({
    subscription: s.array(s.string()),
  });
