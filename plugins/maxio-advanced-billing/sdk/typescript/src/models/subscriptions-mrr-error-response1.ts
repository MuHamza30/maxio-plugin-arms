import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { attributeErrorSchema, type AttributeError } from "./attribute-error.js";

export type SubscriptionsMrrErrorResponse1 = {
  errors: AttributeError;
};

export const subscriptionsMrrErrorResponse1Schema: Schema<SubscriptionsMrrErrorResponse1> =
  s.object<SubscriptionsMrrErrorResponse1>({
    errors: attributeErrorSchema,
  });
