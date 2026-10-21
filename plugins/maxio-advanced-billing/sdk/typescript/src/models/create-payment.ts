import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoicePaymentMethodTypeSchema,
  type InvoicePaymentMethodType,
} from "./invoice-payment-method-type.js";

export type CreatePayment = {
  amount: string;
  memo: string;
  paymentDetails: string;
  /** The type of payment method used. Defaults to other. */
  paymentMethod: InvoicePaymentMethodType;
};

export const createPaymentSchema: Schema<CreatePayment> = s.object<CreatePayment>({
  amount: s.string(),
  memo: s.string(),
  paymentDetails: s.string(),
  paymentMethod: invoicePaymentMethodTypeSchema,
  _keysMap: {
    paymentDetails: "payment_details",
    paymentMethod: "payment_method",
  },
});
