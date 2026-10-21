import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Error which contains list of messages. */
export type ErrorListResponse1 = {
  errors: string[];
};

export const errorListResponse1Schema: Schema<ErrorListResponse1> = s.object<ErrorListResponse1>({
  errors: s.array(s.string()),
});
