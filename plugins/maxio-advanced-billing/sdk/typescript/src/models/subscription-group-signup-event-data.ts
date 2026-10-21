import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { customerSchema, type Customer } from "./customer.js";
import {
  subscriptionGroupSignupFailureDataSchema,
  type SubscriptionGroupSignupFailureData,
} from "./subscription-group-signup-failure-data.js";

export type SubscriptionGroupSignupEventData = {
  subscriptionGroup: SubscriptionGroupSignupFailureData;
  customer: Customer | null;
};

export const subscriptionGroupSignupEventDataSchema: Schema<SubscriptionGroupSignupEventData> =
  s.object<SubscriptionGroupSignupEventData>({
    subscriptionGroup: subscriptionGroupSignupFailureDataSchema,
    customer: s.nullable(s.lazy(() => customerSchema)),
    _keysMap: {
      subscriptionGroup: "subscription_group",
    },
  });
