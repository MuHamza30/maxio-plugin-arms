import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionGroupSignupErrorSchema,
  type SubscriptionGroupSignupError,
} from "./subscription-group-signup-error.js";

export type SubscriptionGroupSignupErrorResponse1 = {
  errors: SubscriptionGroupSignupError;
};

export const subscriptionGroupSignupErrorResponse1Schema: Schema<SubscriptionGroupSignupErrorResponse1> =
  s.object<SubscriptionGroupSignupErrorResponse1>({
    errors: subscriptionGroupSignupErrorSchema,
  });
