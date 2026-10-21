import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Error which contains list of messages. */
export type ErrorListResponse = {
  errors: string[];
};

export const errorListResponseSchema: Schema<ErrorListResponse> = s.object<ErrorListResponse>({
  errors: s.array(s.string()),
});
