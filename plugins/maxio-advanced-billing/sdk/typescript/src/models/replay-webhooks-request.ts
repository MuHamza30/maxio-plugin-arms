import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ReplayWebhooksRequest = {
  ids: number[];
};

export const replayWebhooksRequestSchema: Schema<ReplayWebhooksRequest> = s.object<ReplayWebhooksRequest>({
  ids: s.array(s.int()),
});
