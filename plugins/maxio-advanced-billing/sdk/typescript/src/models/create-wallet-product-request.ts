import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { walletProductSchema, type WalletProduct } from "./wallet-product.js";

/**
 * Does not accept `product_family_id`: a Wallet Product never belongs to a product family. The
 * underlying endpoint accepts the param, but only to reject it; sending one returns `422` ("Product
 * family cannot be set on a wallet product") rather than silently ignoring it.
 */
export type CreateWalletProductRequest = {
  walletProduct: WalletProduct;
};

export const createWalletProductRequestSchema: Schema<CreateWalletProductRequest> =
  s.object<CreateWalletProductRequest>({
    walletProduct: walletProductSchema,
    _keysMap: {
      walletProduct: "wallet_product",
    },
  });
