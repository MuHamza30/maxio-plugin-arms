import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type UpdateCurrencyPrice = {
  /** ID of the currency price record being updated */
  id: number;
  /** New price for the given currency */
  price: number;
};

export const updateCurrencyPriceSchema: Schema<UpdateCurrencyPrice> = s.object<UpdateCurrencyPrice>({
  id: s.int(),
  price: s.float64(),
});
