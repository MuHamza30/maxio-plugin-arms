import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionNote = {
  id?: number;
  body?: string;
  subscriptionId?: number;
  createdAt?: Date;
  updatedAt?: Date;
  sticky?: boolean;
};

export const subscriptionNoteSchema: Schema<SubscriptionNote> = s.object<SubscriptionNote>({
  id: s.optional(s.int()),
  body: s.optional(s.string()),
  subscriptionId: s.optional(s.int()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  sticky: s.optional(s.boolean()),
  _keysMap: {
    subscriptionId: "subscription_id",
    createdAt: "created_at",
    updatedAt: "updated_at",
  },
});
