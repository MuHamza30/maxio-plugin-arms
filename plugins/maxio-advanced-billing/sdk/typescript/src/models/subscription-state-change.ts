import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionStateChange = {
  previousSubscriptionState: string;
  newSubscriptionState: string;
};

export const subscriptionStateChangeSchema: Schema<SubscriptionStateChange> =
  s.object<SubscriptionStateChange>({
    previousSubscriptionState: s.string(),
    newSubscriptionState: s.string(),
    _keysMap: {
      previousSubscriptionState: "previous_subscription_state",
      newSubscriptionState: "new_subscription_state",
    },
  });
