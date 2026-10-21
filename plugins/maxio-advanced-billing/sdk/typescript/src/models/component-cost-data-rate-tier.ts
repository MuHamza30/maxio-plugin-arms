import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ComponentCostDataRateTier = {
  startingQuantity?: number;
  endingQuantity?: number | null;
  quantity?: string;
  unitPrice?: string;
  amount?: string;
};

export const componentCostDataRateTierSchema: Schema<ComponentCostDataRateTier> =
  s.object<ComponentCostDataRateTier>({
    startingQuantity: s.optional(s.int()),
    endingQuantity: s.optionalNullable(s.int()),
    quantity: s.optional(s.string()),
    unitPrice: s.optional(s.string()),
    amount: s.optional(s.string()),
    _keysMap: {
      startingQuantity: "starting_quantity",
      endingQuantity: "ending_quantity",
      unitPrice: "unit_price",
    },
  });
