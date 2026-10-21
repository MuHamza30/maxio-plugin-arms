import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { wallet2Schema, type Wallet2 } from "./wallet2.js";

export type UpdateWalletRequest = {
  wallet: Wallet2;
};

export const updateWalletRequestSchema: Schema<UpdateWalletRequest> = s.object<UpdateWalletRequest>({
  wallet: wallet2Schema,
});
