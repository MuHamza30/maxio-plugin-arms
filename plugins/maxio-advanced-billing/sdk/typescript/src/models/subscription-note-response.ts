import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionNoteSchema, type SubscriptionNote } from "./subscription-note.js";

export type SubscriptionNoteResponse = {
  note: SubscriptionNote;
};

export const subscriptionNoteResponseSchema: Schema<SubscriptionNoteResponse> =
  s.object<SubscriptionNoteResponse>({
    note: subscriptionNoteSchema,
  });
