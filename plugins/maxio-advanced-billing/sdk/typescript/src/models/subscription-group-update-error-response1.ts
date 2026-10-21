import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionGroupUpdateErrorSchema,
  type SubscriptionGroupUpdateError,
} from "./subscription-group-update-error.js";

export type SubscriptionGroupUpdateErrorResponse1 = {
  errors?: SubscriptionGroupUpdateError;
};

export const subscriptionGroupUpdateErrorResponse1Schema: Schema<SubscriptionGroupUpdateErrorResponse1> =
  s.object<SubscriptionGroupUpdateErrorResponse1>({
    errors: s.optional(s.lazy(() => subscriptionGroupUpdateErrorSchema)),
  });
