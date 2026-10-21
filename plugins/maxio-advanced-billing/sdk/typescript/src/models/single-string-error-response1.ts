import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SingleStringErrorResponse1 = {
  errors?: string;
};

export const singleStringErrorResponse1Schema: Schema<SingleStringErrorResponse1> =
  s.object<SingleStringErrorResponse1>({
    errors: s.optional(s.string()),
  });
