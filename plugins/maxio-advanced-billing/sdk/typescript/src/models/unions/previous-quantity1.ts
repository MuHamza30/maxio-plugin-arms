import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type PreviousQuantity1 = number | string;

export const previousQuantity1Schema: Schema<PreviousQuantity1> = s.of<PreviousQuantity1>(
  s.union([s.int(), s.string()]),
);
