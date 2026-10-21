import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { customerErrorSchema, type CustomerError } from "../customer-error.js";

export type Errors1 = CustomerError | string[];

export const errors1Schema: Schema<Errors1> = s.of<Errors1>(
  s.union([s.lazy(() => customerErrorSchema), s.array(s.string())]),
);
