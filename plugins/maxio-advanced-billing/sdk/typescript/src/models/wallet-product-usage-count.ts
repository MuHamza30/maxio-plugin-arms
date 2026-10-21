import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** A rollup of what's using this Wallet Product, for the catalog listing. */
export type WalletProductUsageCount = {
  /**
   * Number of wallet templates billing through this product, whether or not any wallet has been
   * created from them yet.
   */
  walletConfigurations: number;
  /** Number of active (non-archived) wallets currently denominated by this product. */
  activeWallets: number;
};

export const walletProductUsageCountSchema: Schema<WalletProductUsageCount> =
  s.object<WalletProductUsageCount>({
    walletConfigurations: s.int(),
    activeWallets: s.int(),
    _keysMap: {
      walletConfigurations: "wallet_configurations",
      activeWallets: "active_wallets",
    },
  });
