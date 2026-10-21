import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SingleErrorResponse = {
  error: string;
};

export const singleErrorResponseSchema: Schema<SingleErrorResponse> = s.object<SingleErrorResponse>({
  error: s.string(),
});
