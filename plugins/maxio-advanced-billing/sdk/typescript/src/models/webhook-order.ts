import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const WebhookOrder = {
  NewestFirst: "newest_first",
  OldestFirst: "oldest_first",
} as const;
export type WebhookOrder = (typeof WebhookOrder)[keyof typeof WebhookOrder] | (string & {});

export const webhookOrderSchema: EnumSchema<WebhookOrder> = s.enumOf<WebhookOrder>(WebhookOrder);
