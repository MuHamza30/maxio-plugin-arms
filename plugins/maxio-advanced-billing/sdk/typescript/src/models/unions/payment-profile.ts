import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { applePayPaymentProfileSchema, type ApplePayPaymentProfile } from "../apple-pay-payment-profile.js";
import {
  bankAccountPaymentProfileSchema,
  type BankAccountPaymentProfile,
} from "../bank-account-payment-profile.js";
import {
  creditCardPaymentProfileSchema,
  type CreditCardPaymentProfile,
} from "../credit-card-payment-profile.js";
import { paypalPaymentProfileSchema, type PaypalPaymentProfile } from "../paypal-payment-profile.js";

export type PaymentProfile =
  | (ApplePayPaymentProfile & { paymentType: "apple_pay" })
  | (BankAccountPaymentProfile & { paymentType: "bank_account" })
  | (CreditCardPaymentProfile & { paymentType: "credit_card" })
  | (PaypalPaymentProfile & { paymentType: "paypal_account" });

export const paymentProfileSchema: Schema<PaymentProfile> = s.discriminatedUnion<PaymentProfile>(
  "payment_type",
  {
    apple_pay: applePayPaymentProfileSchema,
    bank_account: bankAccountPaymentProfileSchema,
    credit_card: creditCardPaymentProfileSchema,
    paypal_account: paypalPaymentProfileSchema,
  },
);
