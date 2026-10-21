import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateSubscriptionGroupSchema, type UpdateSubscriptionGroup } from "./update-subscription-group.js";

export type UpdateSubscriptionGroupRequest = {
  subscriptionGroup: UpdateSubscriptionGroup;
};

export const updateSubscriptionGroupRequestSchema: Schema<UpdateSubscriptionGroupRequest> =
  s.object<UpdateSubscriptionGroupRequest>({
    subscriptionGroup: updateSubscriptionGroupSchema,
    _keysMap: {
      subscriptionGroup: "subscription_group",
    },
  });
