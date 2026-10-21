import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createSubscriptionSchema, type CreateSubscription } from "./create-subscription.js";

export type CreateSubscriptionRequest = {
  subscription: CreateSubscription;
};

export const createSubscriptionRequestSchema: Schema<CreateSubscriptionRequest> =
  s.object<CreateSubscriptionRequest>({
    subscription: createSubscriptionSchema,
  });
