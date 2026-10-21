import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type EnableWebhooksResponse = {
  webhooksEnabled?: boolean;
};

export const enableWebhooksResponseSchema: Schema<EnableWebhooksResponse> = s.object<EnableWebhooksResponse>({
  webhooksEnabled: s.optional(s.boolean()),
  _keysMap: {
    webhooksEnabled: "webhooks_enabled",
  },
});
