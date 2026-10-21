import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type EnableWebhooksRequest = {
  webhooksEnabled: boolean;
};

export const enableWebhooksRequestSchema: Schema<EnableWebhooksRequest> = s.object<EnableWebhooksRequest>({
  webhooksEnabled: s.boolean(),
  _keysMap: {
    webhooksEnabled: "webhooks_enabled",
  },
});
