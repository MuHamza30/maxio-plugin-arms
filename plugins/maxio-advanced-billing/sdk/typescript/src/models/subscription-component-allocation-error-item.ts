import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionComponentAllocationErrorItem = {
  kind?: string;
  message?: string;
};

export const subscriptionComponentAllocationErrorItemSchema: Schema<SubscriptionComponentAllocationErrorItem> =
  s.object<SubscriptionComponentAllocationErrorItem>({
    kind: s.optional(s.string()),
    message: s.optional(s.string()),
  });
