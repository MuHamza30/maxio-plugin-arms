import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionGroupSingleError = {
  subscriptionGroup: string;
};

export const subscriptionGroupSingleErrorSchema: Schema<SubscriptionGroupSingleError> =
  s.object<SubscriptionGroupSingleError>({
    subscriptionGroup: s.string(),
    _keysMap: {
      subscriptionGroup: "subscription_group",
    },
  });
