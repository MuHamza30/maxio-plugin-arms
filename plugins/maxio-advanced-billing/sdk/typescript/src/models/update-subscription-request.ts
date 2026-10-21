import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateSubscriptionSchema, type UpdateSubscription } from "./update-subscription.js";

export type UpdateSubscriptionRequest = {
  subscription: UpdateSubscription;
};

export const updateSubscriptionRequestSchema: Schema<UpdateSubscriptionRequest> =
  s.object<UpdateSubscriptionRequest>({
    subscription: updateSubscriptionSchema,
  });
