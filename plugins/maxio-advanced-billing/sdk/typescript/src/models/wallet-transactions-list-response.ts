import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { listPublicKeysMetaSchema, type ListPublicKeysMeta } from "./list-public-keys-meta.js";
import { walletTransactionSchema, type WalletTransaction } from "./wallet-transaction.js";

export type WalletTransactionsListResponse = {
  walletTransactions: WalletTransaction[];
  meta: ListPublicKeysMeta;
};

export const walletTransactionsListResponseSchema: Schema<WalletTransactionsListResponse> =
  s.object<WalletTransactionsListResponse>({
    walletTransactions: s.array(s.lazy(() => walletTransactionSchema)),
    meta: listPublicKeysMetaSchema,
    _keysMap: {
      walletTransactions: "wallet_transactions",
    },
  });
