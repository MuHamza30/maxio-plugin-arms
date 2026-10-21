import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { walletSchema, type Wallet } from "./wallet.js";

export type WalletResponse = {
  /**
   * A balance, denominated in the unit of a Wallet Product, owned by a subscription. Grants and
   * recurring funding schedules are embedded so a single read shows the full balance breakdown.
   */
  wallet: Wallet;
};

export const walletResponseSchema: Schema<WalletResponse> = s.object<WalletResponse>({
  wallet: walletSchema,
});
