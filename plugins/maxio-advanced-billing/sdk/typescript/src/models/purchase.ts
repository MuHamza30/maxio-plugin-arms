import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { quantity4Schema, type Quantity4 } from "./unions/quantity4.js";

export type Purchase = {
  /**
   * The number of wallet units to purchase, as a decimal string with at most 8 fractional digits.
   * Send fractional values as strings: a JSON number with a decimal point is rejected with `422`,
   * because a double-precision float may already have lost precision before the request arrives.
   */
  quantity: Quantity4;
  /**
   * The price point to purchase at. Must belong to the wallet's billing product. Defaults to the
   * `price_point_id` set on the wallet.
   */
  pricePointId?: number;
  /** (Optional) A note recorded on the resulting grant's ledger row. */
  memo?: string | null;
};

export const purchaseSchema: Schema<Purchase> = s.object<Purchase>({
  quantity: quantity4Schema,
  pricePointId: s.optional(s.int()),
  memo: s.optionalNullable(s.string()),
  _keysMap: {
    pricePointId: "price_point_id",
  },
});
