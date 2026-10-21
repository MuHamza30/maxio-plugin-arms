import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { errors11Schema, type Errors11 } from "./unions/errors11.js";

export type SubscriptionGroupCreateErrorResponse1 = {
  errors: Errors11;
};

export const subscriptionGroupCreateErrorResponse1Schema: Schema<SubscriptionGroupCreateErrorResponse1> =
  s.object<SubscriptionGroupCreateErrorResponse1>({
    errors: errors11Schema,
  });
