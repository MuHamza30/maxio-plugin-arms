import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionPreviewSchema, type SubscriptionPreview } from "./subscription-preview.js";

export type SubscriptionPreviewResponse = {
  subscriptionPreview: SubscriptionPreview;
};

export const subscriptionPreviewResponseSchema: Schema<SubscriptionPreviewResponse> =
  s.object<SubscriptionPreviewResponse>({
    subscriptionPreview: subscriptionPreviewSchema,
    _keysMap: {
      subscriptionPreview: "subscription_preview",
    },
  });
