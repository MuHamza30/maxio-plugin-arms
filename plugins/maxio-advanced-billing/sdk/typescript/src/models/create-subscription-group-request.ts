import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createSubscriptionGroupSchema, type CreateSubscriptionGroup } from "./create-subscription-group.js";

export type CreateSubscriptionGroupRequest = {
  subscriptionGroup: CreateSubscriptionGroup;
};

export const createSubscriptionGroupRequestSchema: Schema<CreateSubscriptionGroupRequest> =
  s.object<CreateSubscriptionGroupRequest>({
    subscriptionGroup: createSubscriptionGroupSchema,
    _keysMap: {
      subscriptionGroup: "subscription_group",
    },
  });
