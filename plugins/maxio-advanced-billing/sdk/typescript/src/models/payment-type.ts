import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const PaymentType = {
  CreditCard: "credit_card",
  BankAccount: "bank_account",
  PaypalAccount: "paypal_account",
  ApplePay: "apple_pay",
} as const;
export type PaymentType = (typeof PaymentType)[keyof typeof PaymentType] | (string & {});

export const paymentTypeSchema: EnumSchema<PaymentType> = s.enumOf<PaymentType>(PaymentType);
