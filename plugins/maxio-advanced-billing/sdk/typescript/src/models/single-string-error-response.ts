import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SingleStringErrorResponse = {
  errors?: string;
};

export const singleStringErrorResponseSchema: Schema<SingleStringErrorResponse> =
  s.object<SingleStringErrorResponse>({
    errors: s.optional(s.string()),
  });
