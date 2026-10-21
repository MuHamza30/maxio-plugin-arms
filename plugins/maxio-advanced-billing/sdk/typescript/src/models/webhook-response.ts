import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { webhookSchema, type Webhook } from "./webhook.js";

export type WebhookResponse = {
  webhook?: Webhook;
};

export const webhookResponseSchema: Schema<WebhookResponse> = s.object<WebhookResponse>({
  webhook: s.optional(s.lazy(() => webhookSchema)),
});
