import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionComponentSchema, type SubscriptionComponent } from "./subscription-component.js";

export type ListSubscriptionComponentsResponse = {
  subscriptionsComponents: SubscriptionComponent[];
};

export const listSubscriptionComponentsResponseSchema: Schema<ListSubscriptionComponentsResponse> =
  s.object<ListSubscriptionComponentsResponse>({
    subscriptionsComponents: s.array(s.lazy(() => subscriptionComponentSchema)),
    _keysMap: {
      subscriptionsComponents: "subscriptions_components",
    },
  });
