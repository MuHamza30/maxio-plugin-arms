import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const WebhookStatus = {
  Successful: "successful",
  Failed: "failed",
  Pending: "pending",
  Paused: "paused",
} as const;
export type WebhookStatus = (typeof WebhookStatus)[keyof typeof WebhookStatus] | (string & {});

export const webhookStatusSchema: EnumSchema<WebhookStatus> = s.enumOf<WebhookStatus>(WebhookStatus);
