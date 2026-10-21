import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { walletProduct1Schema, type WalletProduct1 } from "./wallet-product1.js";

/**
 * Only `name`, `description`, `taxable`, `tax_code`, `accounting_code`, and `item_category` are
 * mutable. `unit_name`, `handle`, `price_point`, and `price_points` are not accepted here: the
 * request still returns `200`, but those fields are silently ignored and nothing about them
 * changes. `handle` stays fixed because it's the Wallet Product's only stable identifier on a
 * surface with no product family in the path; `unit_name` stays fixed because a wallet's behavior
 * snapshots it into the wallet's own `unit` field and never re-derives it.
 */
export type UpdateWalletProductRequest = {
  walletProduct: WalletProduct1;
};

export const updateWalletProductRequestSchema: Schema<UpdateWalletProductRequest> =
  s.object<UpdateWalletProductRequest>({
    walletProduct: walletProduct1Schema,
    _keysMap: {
      walletProduct: "wallet_product",
    },
  });
