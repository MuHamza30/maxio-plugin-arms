import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoicePaymentMethodTypeSchema,
  type InvoicePaymentMethodType,
} from "./invoice-payment-method-type.js";
import { amountSchema, type Amount } from "./unions/amount.js";

export type CreateInvoicePayment = {
  /** A string of the dollar amount to be refunded (eg. "10.50" => $10.50) */
  amount?: Amount;
  /** A description to be attached to the payment. Applicable only to `external` payments. */
  memo?: string;
  /** The type of payment method used. Defaults to other. */
  method?: InvoicePaymentMethodType;
  /**
   * Additional information related to the payment method (eg. Check #). Applicable only to
   * `external` payments.
   */
  details?: string;
  /** The ID of the payment profile to be used for the payment. */
  paymentProfileId?: number;
  /**
   * Date reflecting when the payment was received from a customer. Must be in the past. Applicable
   * only to `external` payments.
   */
  receivedOn?: string;
};

export const createInvoicePaymentSchema: Schema<CreateInvoicePayment> = s.object<CreateInvoicePayment>({
  amount: s.optional(s.lazy(() => amountSchema)),
  memo: s.optional(s.string()),
  method: s.optional(s.lazy(() => invoicePaymentMethodTypeSchema)),
  details: s.optional(s.string()),
  paymentProfileId: s.optional(s.int()),
  receivedOn: s.optional(s.dateOnly()),
  _keysMap: {
    paymentProfileId: "payment_profile_id",
    receivedOn: "received_on",
  },
});
