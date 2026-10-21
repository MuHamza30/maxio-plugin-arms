import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { walletTransactionSchema, type WalletTransaction } from "./wallet-transaction.js";

/**
 * Returned by [Create Wallet Transaction]($e/Wallet%20Transactions/createWalletTransaction).
 * `wallet_transactions` and `balance` are always present. `requested_amount`, `drained_amount`, and
 * `rejected_amount` are present only when the request's `kind` was `debit`.
 */
export type WalletTransactionResultResponse = {
  walletTransactions: WalletTransaction[];
  /** `kind: debit` only. The amount that was requested, as a decimal string. */
  requestedAmount?: string;
  /**
   * `kind: debit` only. The amount actually drained from the wallet's grants, as a decimal string.
   */
  drainedAmount?: string;
  /**
   * `kind: debit` only, as a decimal string. Under `hard_stop_overflow: discard`, this is the
   * requested amount minus what the wallet could cover (`"0.0"` on a full drain). Always `"0.0"`
   * under `allow_negative`; nothing is rejected, and the balance goes negative instead.
   */
  rejectedAmount?: string;
  /** The wallet's new balance, as a decimal string. */
  balance: string;
};

export const walletTransactionResultResponseSchema: Schema<WalletTransactionResultResponse> =
  s.object<WalletTransactionResultResponse>({
    walletTransactions: s.array(s.lazy(() => walletTransactionSchema)),
    requestedAmount: s.optional(s.string()),
    drainedAmount: s.optional(s.string()),
    rejectedAmount: s.optional(s.string()),
    balance: s.string(),
    _keysMap: {
      walletTransactions: "wallet_transactions",
      requestedAmount: "requested_amount",
      drainedAmount: "drained_amount",
      rejectedAmount: "rejected_amount",
    },
  });
