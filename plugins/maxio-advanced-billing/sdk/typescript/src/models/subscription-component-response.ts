import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionComponentSchema, type SubscriptionComponent } from "./subscription-component.js";

export type SubscriptionComponentResponse = {
  component?: SubscriptionComponent;
};

export const subscriptionComponentResponseSchema: Schema<SubscriptionComponentResponse> =
  s.object<SubscriptionComponentResponse>({
    component: s.optional(s.lazy(() => subscriptionComponentSchema)),
  });
