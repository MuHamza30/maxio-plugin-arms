import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** The error is base if it is not directly associated with a single attribute. */
export type BaseStringError = {
  base?: string[];
};

export const baseStringErrorSchema: Schema<BaseStringError> = s.object<BaseStringError>({
  base: s.optional(s.array(s.string())),
});
