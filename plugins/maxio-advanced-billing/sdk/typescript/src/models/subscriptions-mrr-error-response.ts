import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { attributeErrorSchema, type AttributeError } from "./attribute-error.js";

export type SubscriptionsMrrErrorResponse = {
  errors: AttributeError;
};

export const subscriptionsMrrErrorResponseSchema: Schema<SubscriptionsMrrErrorResponse> =
  s.object<SubscriptionsMrrErrorResponse>({
    errors: attributeErrorSchema,
  });
