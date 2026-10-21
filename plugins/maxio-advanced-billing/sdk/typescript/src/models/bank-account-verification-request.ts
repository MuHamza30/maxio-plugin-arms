import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { bankAccountVerificationSchema, type BankAccountVerification } from "./bank-account-verification.js";

export type BankAccountVerificationRequest = {
  bankAccountVerification: BankAccountVerification;
};

export const bankAccountVerificationRequestSchema: Schema<BankAccountVerificationRequest> =
  s.object<BankAccountVerificationRequest>({
    bankAccountVerification: bankAccountVerificationSchema,
    _keysMap: {
      bankAccountVerification: "bank_account_verification",
    },
  });
