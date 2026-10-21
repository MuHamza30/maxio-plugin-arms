import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionComponentAllocationErrorItemSchema,
  type SubscriptionComponentAllocationErrorItem,
} from "./subscription-component-allocation-error-item.js";

export type SubscriptionComponentAllocationError = {
  errors?: SubscriptionComponentAllocationErrorItem[];
};

export const subscriptionComponentAllocationErrorSchema: Schema<SubscriptionComponentAllocationError> =
  s.object<SubscriptionComponentAllocationError>({
    errors: s.optional(s.array(s.lazy(() => subscriptionComponentAllocationErrorItemSchema))),
  });
