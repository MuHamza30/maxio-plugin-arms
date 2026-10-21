import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** Defaults to personal */
export const BankAccountHolderType = {
  Personal: "personal",
  Business: "business",
} as const;
export type BankAccountHolderType =
  | (typeof BankAccountHolderType)[keyof typeof BankAccountHolderType]
  | (string & {});

export const bankAccountHolderTypeSchema: EnumSchema<BankAccountHolderType> =
  s.enumOf<BankAccountHolderType>(BankAccountHolderType);
