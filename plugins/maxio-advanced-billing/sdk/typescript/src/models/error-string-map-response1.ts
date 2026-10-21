import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ErrorStringMapResponse1 = {
  errors?: Record<string, string>;
};

export const errorStringMapResponse1Schema: Schema<ErrorStringMapResponse1> =
  s.object<ErrorStringMapResponse1>({
    errors: s.optional(s.record(s.string(), s.string())),
  });
