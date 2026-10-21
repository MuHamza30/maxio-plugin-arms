import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type MrrMovement = {
  amount?: number;
  category?: string;
  subscriberDelta?: number;
  leadDelta?: number;
};

export const mrrMovementSchema: Schema<MrrMovement> = s.object<MrrMovement>({
  amount: s.optional(s.int()),
  category: s.optional(s.string()),
  subscriberDelta: s.optional(s.int()),
  leadDelta: s.optional(s.int()),
  _keysMap: {
    subscriberDelta: "subscriber_delta",
    leadDelta: "lead_delta",
  },
});
