import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { walletTransaction1Schema, type WalletTransaction1 } from "./wallet-transaction1.js";

export type CreateWalletTransactionRequest = {
  walletTransaction: WalletTransaction1;
};

export const createWalletTransactionRequestSchema: Schema<CreateWalletTransactionRequest> =
  s.object<CreateWalletTransactionRequest>({
    walletTransaction: walletTransaction1Schema,
    _keysMap: {
      walletTransaction: "wallet_transaction",
    },
  });
