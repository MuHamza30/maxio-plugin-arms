import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ErrorArrayMapResponse = {
  errors?: Record<string, Record<string, unknown>>;
};

export const errorArrayMapResponseSchema: Schema<ErrorArrayMapResponse> = s.object<ErrorArrayMapResponse>({
  errors: s.optional(s.record(s.string(), s.record(s.string(), s.unknown()))),
});
