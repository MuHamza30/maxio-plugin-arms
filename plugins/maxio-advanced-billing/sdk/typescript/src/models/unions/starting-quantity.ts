import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type StartingQuantity = number | string;

export const startingQuantitySchema: Schema<StartingQuantity> = s.of<StartingQuantity>(
  s.union([s.int(), s.string()]),
);
