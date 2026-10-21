import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { errors1Schema, type Errors1 } from "./unions/errors1.js";

export type CustomerErrorResponse1 = {
  errors?: Errors1;
};

export const customerErrorResponse1Schema: Schema<CustomerErrorResponse1> = s.object<CustomerErrorResponse1>({
  errors: s.optional(s.lazy(() => errors1Schema)),
});
