import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { endingQuantitySchema, type EndingQuantity } from "./unions/ending-quantity.js";
import { startingQuantitySchema, type StartingQuantity } from "./unions/starting-quantity.js";
import { unitPriceSchema, type UnitPrice } from "./unions/unit-price.js";

export type UpdatePrice = {
  id?: number;
  endingQuantity?: EndingQuantity;
  /** The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065 */
  unitPrice?: UnitPrice;
  destroy?: boolean;
  startingQuantity?: StartingQuantity;
};

export const updatePriceSchema: Schema<UpdatePrice> = s.object<UpdatePrice>({
  id: s.optional(s.int()),
  endingQuantity: s.optional(s.lazy(() => endingQuantitySchema)),
  unitPrice: s.optional(s.lazy(() => unitPriceSchema)),
  destroy: s.optional(s.boolean()),
  startingQuantity: s.optional(s.lazy(() => startingQuantitySchema)),
  _keysMap: {
    endingQuantity: "ending_quantity",
    unitPrice: "unit_price",
    destroy: "_destroy",
    startingQuantity: "starting_quantity",
  },
});
