import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SingleErrorResponse1 = {
  error: string;
};

export const singleErrorResponse1Schema: Schema<SingleErrorResponse1> = s.object<SingleErrorResponse1>({
  error: s.string(),
});
