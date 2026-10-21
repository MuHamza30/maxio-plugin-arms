import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateSubscriptionNoteSchema, type UpdateSubscriptionNote } from "./update-subscription-note.js";

/** Updatable fields for Subscription Note */
export type UpdateSubscriptionNoteRequest = {
  /** Updatable fields for Subscription Note */
  note: UpdateSubscriptionNote;
};

export const updateSubscriptionNoteRequestSchema: Schema<UpdateSubscriptionNoteRequest> =
  s.object<UpdateSubscriptionNoteRequest>({
    note: updateSubscriptionNoteSchema,
  });
