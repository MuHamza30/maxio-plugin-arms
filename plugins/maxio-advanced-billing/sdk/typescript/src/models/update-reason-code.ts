import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type UpdateReasonCode = {
  /** The unique identifier for the ReasonCode */
  code?: string;
  /** The friendly summary of what the code signifies */
  description?: string;
  /** The order that code appears in lists */
  position?: number;
};

export const updateReasonCodeSchema: Schema<UpdateReasonCode> = s.object<UpdateReasonCode>({
  code: s.optional(s.string()),
  description: s.optional(s.string()),
  position: s.optional(s.int()),
});
