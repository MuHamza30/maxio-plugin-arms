import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionMrrSchema, type SubscriptionMrr } from "./subscription-mrr.js";

export type SubscriptionMrrResponse = {
  subscriptionsMrr: SubscriptionMrr[];
};

export const subscriptionMrrResponseSchema: Schema<SubscriptionMrrResponse> =
  s.object<SubscriptionMrrResponse>({
    subscriptionsMrr: s.array(s.lazy(() => subscriptionMrrSchema)),
    _keysMap: {
      subscriptionsMrr: "subscriptions_mrr",
    },
  });
