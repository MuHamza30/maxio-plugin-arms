import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * Behavior at the hard-stop boundary. `discard` drains the wallet to zero and rejects the excess
 * (the default). `allow_negative` deducts the full amount, letting the balance go negative. The
 * excess past the wallet's grants is booked as an overdraft ledger row with `grant_id` set to
 * `null`.
 */
export const WalletHardStopOverflow = {
  Discard: "discard",
  AllowNegative: "allow_negative",
} as const;
export type WalletHardStopOverflow =
  | (typeof WalletHardStopOverflow)[keyof typeof WalletHardStopOverflow]
  | (string & {});

export const walletHardStopOverflowSchema: EnumSchema<WalletHardStopOverflow> =
  s.enumOf<WalletHardStopOverflow>(WalletHardStopOverflow);
