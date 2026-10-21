import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { errors1Schema, type Errors1 } from "./unions/errors1.js";

export type CustomerErrorResponse = {
  errors?: Errors1;
};

export const customerErrorResponseSchema: Schema<CustomerErrorResponse> = s.object<CustomerErrorResponse>({
  errors: s.optional(s.lazy(() => errors1Schema)),
});
