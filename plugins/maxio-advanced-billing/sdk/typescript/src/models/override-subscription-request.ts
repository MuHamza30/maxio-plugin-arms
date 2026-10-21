import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { overrideSubscriptionSchema, type OverrideSubscription } from "./override-subscription.js";

export type OverrideSubscriptionRequest = {
  subscription: OverrideSubscription;
};

export const overrideSubscriptionRequestSchema: Schema<OverrideSubscriptionRequest> =
  s.object<OverrideSubscriptionRequest>({
    subscription: overrideSubscriptionSchema,
  });
