import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type AllocatedQuantity1 = string | number;

export const allocatedQuantity1Schema: Schema<AllocatedQuantity1> = s.of<AllocatedQuantity1>(
  s.union([s.string(), s.int()]),
);
