import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type AllocatedQuantity = number | string;

export const allocatedQuantitySchema: Schema<AllocatedQuantity> = s.of<AllocatedQuantity>(
  s.union([s.int(), s.string()]),
);
