import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionSchema, type Subscription } from "./subscription.js";

export type SubscriptionResponseError = {
  subscription?: Subscription;
};

export const subscriptionResponseErrorSchema: Schema<SubscriptionResponseError> =
  s.object<SubscriptionResponseError>({
    subscription: s.optional(s.lazy(() => subscriptionSchema)),
  });
