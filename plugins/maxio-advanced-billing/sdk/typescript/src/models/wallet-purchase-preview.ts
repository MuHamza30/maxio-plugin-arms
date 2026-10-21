import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** A price quote for a purchase, without charging anything. */
export type WalletPurchasePreview = {
  pricePointId: number;
  /**
   * The three-letter currency code the `amount` is denominated in, matching the subscription's
   * currency.
   */
  currency: string;
  /** The number of units the quote is for, as a decimal string. */
  quantity: string;
  /** The price for `quantity` units at this price point, as a decimal string. */
  amount: string;
};

export const walletPurchasePreviewSchema: Schema<WalletPurchasePreview> = s.object<WalletPurchasePreview>({
  pricePointId: s.int(),
  currency: s.string(),
  quantity: s.string(),
  amount: s.string(),
  _keysMap: {
    pricePointId: "price_point_id",
  },
});
