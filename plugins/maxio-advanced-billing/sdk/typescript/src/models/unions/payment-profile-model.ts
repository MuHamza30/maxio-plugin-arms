import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import {
  getOneTimeTokenBankAccountPaymentProfileSchema,
  type GetOneTimeTokenBankAccountPaymentProfile,
} from "../get-one-time-token-bank-account-payment-profile.js";
import {
  getOneTimeTokenPaymentProfileSchema,
  type GetOneTimeTokenPaymentProfile,
} from "../get-one-time-token-payment-profile.js";

export type PaymentProfileModel =
  | (GetOneTimeTokenPaymentProfile & { paymentType: "credit_card" })
  | (GetOneTimeTokenBankAccountPaymentProfile & { paymentType: "bank_account" });

export const paymentProfileModelSchema: Schema<PaymentProfileModel> =
  s.discriminatedUnion<PaymentProfileModel>("payment_type", {
    credit_card: getOneTimeTokenPaymentProfileSchema,
    bank_account: getOneTimeTokenBankAccountPaymentProfileSchema,
  });
