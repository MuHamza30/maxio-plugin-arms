import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { webhookSubscriptionSchema, type WebhookSubscription } from "./webhook-subscription.js";

/** Used to Create or Update Endpoint. */
export type CreateOrUpdateEndpoint = {
  url: string;
  webhookSubscriptions: WebhookSubscription[];
};

export const createOrUpdateEndpointSchema: Schema<CreateOrUpdateEndpoint> = s.object<CreateOrUpdateEndpoint>({
  url: s.string(),
  webhookSubscriptions: s.array(s.lazy(() => webhookSubscriptionSchema)),
  _keysMap: {
    webhookSubscriptions: "webhook_subscriptions",
  },
});
