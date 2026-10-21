import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionGroupSignupSchema, type SubscriptionGroupSignup } from "./subscription-group-signup.js";

export type SubscriptionGroupSignupRequest = {
  subscriptionGroup: SubscriptionGroupSignup;
};

export const subscriptionGroupSignupRequestSchema: Schema<SubscriptionGroupSignupRequest> =
  s.object<SubscriptionGroupSignupRequest>({
    subscriptionGroup: subscriptionGroupSignupSchema,
    _keysMap: {
      subscriptionGroup: "subscription_group",
    },
  });
