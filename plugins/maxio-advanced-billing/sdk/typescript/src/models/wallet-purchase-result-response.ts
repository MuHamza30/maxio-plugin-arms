import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { walletPurchaseSchema, type WalletPurchase } from "./wallet-purchase.js";

export type WalletPurchaseResultResponse = {
  walletPurchases: WalletPurchase[];
  /** The wallet's new balance, as a decimal string. */
  balance: string;
};

export const walletPurchaseResultResponseSchema: Schema<WalletPurchaseResultResponse> =
  s.object<WalletPurchaseResultResponse>({
    walletPurchases: s.array(s.lazy(() => walletPurchaseSchema)),
    balance: s.string(),
    _keysMap: {
      walletPurchases: "wallet_purchases",
    },
  });
