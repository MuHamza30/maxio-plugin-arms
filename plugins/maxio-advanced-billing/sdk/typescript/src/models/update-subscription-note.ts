import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Updatable fields for Subscription Note */
export type UpdateSubscriptionNote = {
  body: string;
  sticky: boolean;
};

export const updateSubscriptionNoteSchema: Schema<UpdateSubscriptionNote> = s.object<UpdateSubscriptionNote>({
  body: s.string(),
  sticky: s.boolean(),
});
