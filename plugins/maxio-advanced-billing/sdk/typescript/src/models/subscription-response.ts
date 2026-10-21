import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionSchema, type Subscription } from "./subscription.js";

export type SubscriptionResponse = {
  subscription?: Subscription;
};

export const subscriptionResponseSchema: Schema<SubscriptionResponse> = s.object<SubscriptionResponse>({
  subscription: s.optional(s.lazy(() => subscriptionSchema)),
});
