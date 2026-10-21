import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { breakoutsSchema, type Breakouts } from "./breakouts.js";
import { movementLineItemSchema, type MovementLineItem } from "./movement-line-item.js";

export type Movement = {
  timestamp?: Date;
  amountInCents?: number;
  amountFormatted?: string;
  description?: string;
  category?: string;
  breakouts?: Breakouts;
  lineItems?: MovementLineItem[];
  subscriptionId?: number;
  subscriberName?: string;
};

export const movementSchema: Schema<Movement> = s.object<Movement>({
  timestamp: s.optional(s.dateTime()),
  amountInCents: s.optional(s.int()),
  amountFormatted: s.optional(s.string()),
  description: s.optional(s.string()),
  category: s.optional(s.string()),
  breakouts: s.optional(s.lazy(() => breakoutsSchema)),
  lineItems: s.optional(s.array(s.lazy(() => movementLineItemSchema))),
  subscriptionId: s.optional(s.int()),
  subscriberName: s.optional(s.string()),
  _keysMap: {
    amountInCents: "amount_in_cents",
    amountFormatted: "amount_formatted",
    lineItems: "line_items",
    subscriptionId: "subscription_id",
    subscriberName: "subscriber_name",
  },
});
