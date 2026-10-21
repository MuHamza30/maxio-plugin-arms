import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CustomerError = {
  customer?: string;
};

export const customerErrorSchema: Schema<CustomerError> = s.object<CustomerError>({
  customer: s.optional(s.string()),
});
