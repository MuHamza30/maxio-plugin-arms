import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { paymentMethodApplePaySchema, type PaymentMethodApplePay } from "../payment-method-apple-pay.js";
import {
  paymentMethodBankAccountSchema,
  type PaymentMethodBankAccount,
} from "../payment-method-bank-account.js";
import {
  paymentMethodCreditCardSchema,
  type PaymentMethodCreditCard,
} from "../payment-method-credit-card.js";
import { paymentMethodExternalSchema, type PaymentMethodExternal } from "../payment-method-external.js";
import { paymentMethodPaypalSchema, type PaymentMethodPaypal } from "../payment-method-paypal.js";

/** A nested data structure detailing the method of payment */
export type InvoiceEventPayment1 =
  | (PaymentMethodApplePay & { type: "apple_pay" })
  | (PaymentMethodBankAccount & { type: "bank_account" })
  | (PaymentMethodCreditCard & { type: "credit_card" })
  | (PaymentMethodExternal & { type: "external" })
  | (PaymentMethodPaypal & { type: "paypal_account" });

export const invoiceEventPayment1Schema: Schema<InvoiceEventPayment1> =
  s.discriminatedUnion<InvoiceEventPayment1>("type", {
    apple_pay: paymentMethodApplePaySchema,
    bank_account: paymentMethodBankAccountSchema,
    credit_card: paymentMethodCreditCardSchema,
    external: paymentMethodExternalSchema,
    paypal_account: paymentMethodPaypalSchema,
  });
