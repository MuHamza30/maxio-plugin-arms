import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { endingQuantitySchema, type EndingQuantity } from "./unions/ending-quantity.js";
import { startingQuantitySchema, type StartingQuantity } from "./unions/starting-quantity.js";
import { unitPriceSchema, type UnitPrice } from "./unions/unit-price.js";

export type Price = {
  startingQuantity: StartingQuantity;
  endingQuantity?: EndingQuantity | null;
  /** The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065 */
  unitPrice: UnitPrice;
};

export const priceSchema: Schema<Price> = s.object<Price>({
  startingQuantity: startingQuantitySchema,
  endingQuantity: s.optionalNullable(s.lazy(() => endingQuantitySchema)),
  unitPrice: unitPriceSchema,
  _keysMap: {
    startingQuantity: "starting_quantity",
    endingQuantity: "ending_quantity",
    unitPrice: "unit_price",
  },
});
