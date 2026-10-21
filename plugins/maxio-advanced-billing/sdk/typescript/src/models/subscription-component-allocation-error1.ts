import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionComponentAllocationErrorItemSchema,
  type SubscriptionComponentAllocationErrorItem,
} from "./subscription-component-allocation-error-item.js";

export type SubscriptionComponentAllocationError1 = {
  errors?: SubscriptionComponentAllocationErrorItem[];
};

export const subscriptionComponentAllocationError1Schema: Schema<SubscriptionComponentAllocationError1> =
  s.object<SubscriptionComponentAllocationError1>({
    errors: s.optional(s.array(s.lazy(() => subscriptionComponentAllocationErrorItemSchema))),
  });
