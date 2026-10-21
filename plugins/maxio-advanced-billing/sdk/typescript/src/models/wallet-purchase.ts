import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** A completed unit purchase. */
export type WalletPurchase = {
  /**
   * The id of the grant this purchase created. When the wallet was overdrawn by at least the
   * purchased quantity, the units repay the debt and the grant is still created, with `remaining`
   * of `0` and `original` equal to the purchased quantity.
   */
  id: number;
  /** The price point the purchase was priced at. */
  pricePointId: number;
  /** The uid of the invoice created to collect payment for this purchase. */
  invoiceUid: string;
  /** The number of units purchased, as a decimal string. */
  quantity: string;
  /**
   * When the purchased units expire, following the funding entitlement's grant expiration policy.
   * `null` when the wallet has no funding entitlement or its entitlements disagree on an expiration
   * policy.
   */
  expiresAt: Date | null;
};

export const walletPurchaseSchema: Schema<WalletPurchase> = s.object<WalletPurchase>({
  id: s.int(),
  pricePointId: s.int(),
  invoiceUid: s.string(),
  quantity: s.string(),
  expiresAt: s.nullable(s.dateTime()),
  _keysMap: {
    pricePointId: "price_point_id",
    invoiceUid: "invoice_uid",
    expiresAt: "expires_at",
  },
});
