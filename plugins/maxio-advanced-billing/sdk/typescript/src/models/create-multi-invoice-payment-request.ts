import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  createMultiInvoicePaymentSchema,
  type CreateMultiInvoicePayment,
} from "./create-multi-invoice-payment.js";

export type CreateMultiInvoicePaymentRequest = {
  payment: CreateMultiInvoicePayment;
};

export const createMultiInvoicePaymentRequestSchema: Schema<CreateMultiInvoicePaymentRequest> =
  s.object<CreateMultiInvoicePaymentRequest>({
    payment: createMultiInvoicePaymentSchema,
  });
