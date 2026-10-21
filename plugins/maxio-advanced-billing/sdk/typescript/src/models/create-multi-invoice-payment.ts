import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  createInvoicePaymentApplicationSchema,
  type CreateInvoicePaymentApplication,
} from "./create-invoice-payment-application.js";
import {
  invoicePaymentMethodTypeSchema,
  type InvoicePaymentMethodType,
} from "./invoice-payment-method-type.js";
import { amount1Schema, type Amount1 } from "./unions/amount1.js";

export type CreateMultiInvoicePayment = {
  /** A description to be attached to the payment. */
  memo?: string;
  /** Additional information related to the payment method (eg. Check #). */
  details?: string;
  /** The type of payment method used. Defaults to other. */
  method?: InvoicePaymentMethodType;
  /** Dollar amount of the sum of the invoices payment (eg. "10.50" => $10.50). */
  amount: Amount1;
  /** Date reflecting when the payment was received from a customer. Must be in the past. */
  receivedOn?: string;
  applications: CreateInvoicePaymentApplication[];
};

export const createMultiInvoicePaymentSchema: Schema<CreateMultiInvoicePayment> =
  s.object<CreateMultiInvoicePayment>({
    memo: s.optional(s.string()),
    details: s.optional(s.string()),
    method: s.optional(s.lazy(() => invoicePaymentMethodTypeSchema)),
    amount: amount1Schema,
    receivedOn: s.optional(s.string()),
    applications: s.array(s.lazy(() => createInvoicePaymentApplicationSchema)),
    _keysMap: {
      receivedOn: "received_on",
    },
  });
