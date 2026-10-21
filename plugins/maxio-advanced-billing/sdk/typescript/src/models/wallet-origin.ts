import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * How the wallet came to exist. `manual` for a wallet created directly with [Create
 * Wallet]($e/Wallets/createWallet). `feature` for a wallet auto-provisioned because a subscription
 * resolved a usage-limit entitlement whose Feature has `wallet_behavior` configured.
 */
export const WalletOrigin = {
  Manual: "manual",
  Feature: "feature",
} as const;
export type WalletOrigin = (typeof WalletOrigin)[keyof typeof WalletOrigin] | (string & {});

export const walletOriginSchema: EnumSchema<WalletOrigin> = s.enumOf<WalletOrigin>(WalletOrigin);
