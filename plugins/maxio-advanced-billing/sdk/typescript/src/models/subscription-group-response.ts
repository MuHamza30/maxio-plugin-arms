import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionGroupSchema, type SubscriptionGroup } from "./subscription-group.js";

export type SubscriptionGroupResponse = {
  subscriptionGroup: SubscriptionGroup;
};

export const subscriptionGroupResponseSchema: Schema<SubscriptionGroupResponse> =
  s.object<SubscriptionGroupResponse>({
    subscriptionGroup: subscriptionGroupSchema,
    _keysMap: {
      subscriptionGroup: "subscription_group",
    },
  });
