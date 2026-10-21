import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { wallet1Schema, type Wallet1 } from "./wallet1.js";

export type CreateWalletRequest = {
  wallet: Wallet1;
};

export const createWalletRequestSchema: Schema<CreateWalletRequest> = s.object<CreateWalletRequest>({
  wallet: wallet1Schema,
});
