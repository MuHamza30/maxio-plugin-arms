import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ErrorStringMapResponse = {
  errors?: Record<string, string>;
};

export const errorStringMapResponseSchema: Schema<ErrorStringMapResponse> = s.object<ErrorStringMapResponse>({
  errors: s.optional(s.record(s.string(), s.string())),
});
