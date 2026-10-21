import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ReplayWebhooksResponse = {
  status?: string;
};

export const replayWebhooksResponseSchema: Schema<ReplayWebhooksResponse> = s.object<ReplayWebhooksResponse>({
  status: s.optional(s.string()),
});
