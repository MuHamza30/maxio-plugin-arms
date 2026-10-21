import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  bankAccountPaymentProfileSchema,
  type BankAccountPaymentProfile,
} from "./bank-account-payment-profile.js";

export type BankAccountResponse = {
  paymentProfile: BankAccountPaymentProfile;
};

export const bankAccountResponseSchema: Schema<BankAccountResponse> = s.object<BankAccountResponse>({
  paymentProfile: bankAccountPaymentProfileSchema,
  _keysMap: {
    paymentProfile: "payment_profile",
  },
});
