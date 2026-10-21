import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentSchema, type Component } from "./component.js";

/**
 * A Wallet Product is a Component created with no product family, so it returns the full Component
 * field set under a `wallet_product` root instead of `component`.
 */
export type WalletProductResponse = {
  walletProduct: Component;
};

export const walletProductResponseSchema: Schema<WalletProductResponse> = s.object<WalletProductResponse>({
  walletProduct: componentSchema,
  _keysMap: {
    walletProduct: "wallet_product",
  },
});
