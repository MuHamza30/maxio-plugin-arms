import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const InvoiceEventPaymentMethod = {
  ApplePay: "apple_pay",
  BankAccount: "bank_account",
  CreditCard: "credit_card",
  External: "external",
  PaypalAccount: "paypal_account",
} as const;
export type InvoiceEventPaymentMethod =
  | (typeof InvoiceEventPaymentMethod)[keyof typeof InvoiceEventPaymentMethod]
  | (string & {});

export const invoiceEventPaymentMethodSchema: EnumSchema<InvoiceEventPaymentMethod> =
  s.enumOf<InvoiceEventPaymentMethod>(InvoiceEventPaymentMethod);
