import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { errors11Schema, type Errors11 } from "./unions/errors11.js";

export type SubscriptionGroupCreateErrorResponse = {
  errors: Errors11;
};

export const subscriptionGroupCreateErrorResponseSchema: Schema<SubscriptionGroupCreateErrorResponse> =
  s.object<SubscriptionGroupCreateErrorResponse>({
    errors: errors11Schema,
  });
