import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type Price1 = {
  startingQuantity?: number;
  endingQuantity?: number | null;
  unitPrice?: string;
};

export const price1Schema: Schema<Price1> = s.object<Price1>({
  startingQuantity: s.optional(s.int()),
  endingQuantity: s.optionalNullable(s.int()),
  unitPrice: s.optional(s.string()),
  _keysMap: {
    startingQuantity: "starting_quantity",
    endingQuantity: "ending_quantity",
    unitPrice: "unit_price",
  },
});
