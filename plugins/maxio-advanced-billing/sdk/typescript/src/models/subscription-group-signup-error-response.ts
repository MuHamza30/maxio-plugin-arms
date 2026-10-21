import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionGroupSignupErrorSchema,
  type SubscriptionGroupSignupError,
} from "./subscription-group-signup-error.js";

export type SubscriptionGroupSignupErrorResponse = {
  errors: SubscriptionGroupSignupError;
};

export const subscriptionGroupSignupErrorResponseSchema: Schema<SubscriptionGroupSignupErrorResponse> =
  s.object<SubscriptionGroupSignupErrorResponse>({
    errors: subscriptionGroupSignupErrorSchema,
  });
