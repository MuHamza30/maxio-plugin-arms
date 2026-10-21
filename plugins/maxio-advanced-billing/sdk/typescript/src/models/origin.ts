import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * How the grant was created. `recurring` comes from the wallet's automatic funding schedule (see
 * the wallet's `recurring_funding` array). `manual` comes from a one-time grant posted to [Create
 * Wallet Transaction]($e/Wallet%20Transactions/createWalletTransaction). `initial_balance` comes
 * from a non-zero `initial_balance` at wallet creation. `allowance_increase` comes from raising a
 * funding entitlement's allowance while it's already funding a wallet. `purchase` comes from
 * [Create Wallet Purchase]($e/Wallet%20Purchases/createWalletPurchase).
 */
export const Origin = {
  Recurring: "recurring",
  Manual: "manual",
  InitialBalance: "initial_balance",
  AllowanceIncrease: "allowance_increase",
  Purchase: "purchase",
} as const;
export type Origin = (typeof Origin)[keyof typeof Origin] | (string & {});

export const originSchema: EnumSchema<Origin> = s.enumOf<Origin>(Origin);
