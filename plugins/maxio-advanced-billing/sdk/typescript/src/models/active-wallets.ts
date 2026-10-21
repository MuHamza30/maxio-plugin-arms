import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  walletProductActiveWalletSchema,
  type WalletProductActiveWallet,
} from "./wallet-product-active-wallet.js";

export type ActiveWallets = {
  /** Total count of active wallets drawing on this product. */
  total: number;
  /** Up to 50 of the most recently created active wallets, newest first. */
  sample: WalletProductActiveWallet[];
};

export const activeWalletsSchema: Schema<ActiveWallets> = s.object<ActiveWallets>({
  total: s.int(),
  sample: s.array(s.lazy(() => walletProductActiveWalletSchema)),
});
