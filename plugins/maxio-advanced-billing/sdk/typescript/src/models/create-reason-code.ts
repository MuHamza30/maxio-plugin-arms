import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreateReasonCode = {
  /** The unique identifier for the ReasonCode */
  code: string;
  /** The friendly summary of what the code signifies */
  description: string;
  /** The order that code appears in lists */
  position?: number;
};

export const createReasonCodeSchema: Schema<CreateReasonCode> = s.object<CreateReasonCode>({
  code: s.string(),
  description: s.string(),
  position: s.optional(s.int()),
});
