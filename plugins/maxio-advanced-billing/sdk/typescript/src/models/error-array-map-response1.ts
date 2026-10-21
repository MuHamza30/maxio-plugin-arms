import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ErrorArrayMapResponse1 = {
  errors?: Record<string, Record<string, unknown>>;
};

export const errorArrayMapResponse1Schema: Schema<ErrorArrayMapResponse1> = s.object<ErrorArrayMapResponse1>({
  errors: s.optional(s.record(s.string(), s.record(s.string(), s.unknown()))),
});
