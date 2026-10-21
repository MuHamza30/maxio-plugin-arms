import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type EndingQuantity = number | string;

export const endingQuantitySchema: Schema<EndingQuantity> = s.of<EndingQuantity>(
  s.union([s.int(), s.string()]),
);
