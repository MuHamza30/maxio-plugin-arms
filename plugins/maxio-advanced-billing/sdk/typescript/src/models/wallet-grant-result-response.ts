import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { walletTransactionSchema, type WalletTransaction } from "./wallet-transaction.js";

/** Returned by an adjustment: the ledger row written, plus the wallet's new balance. */
export type WalletGrantResultResponse = {
  walletTransactions: WalletTransaction[];
  /** The wallet's new balance, as a decimal string. */
  balance: string;
};

export const walletGrantResultResponseSchema: Schema<WalletGrantResultResponse> =
  s.object<WalletGrantResultResponse>({
    walletTransactions: s.array(s.lazy(() => walletTransactionSchema)),
    balance: s.string(),
    _keysMap: {
      walletTransactions: "wallet_transactions",
    },
  });
