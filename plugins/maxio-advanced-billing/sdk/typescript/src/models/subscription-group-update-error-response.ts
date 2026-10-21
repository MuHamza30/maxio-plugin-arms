import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionGroupUpdateErrorSchema,
  type SubscriptionGroupUpdateError,
} from "./subscription-group-update-error.js";

export type SubscriptionGroupUpdateErrorResponse = {
  errors?: SubscriptionGroupUpdateError;
};

export const subscriptionGroupUpdateErrorResponseSchema: Schema<SubscriptionGroupUpdateErrorResponse> =
  s.object<SubscriptionGroupUpdateErrorResponse>({
    errors: s.optional(s.lazy(() => subscriptionGroupUpdateErrorSchema)),
  });
