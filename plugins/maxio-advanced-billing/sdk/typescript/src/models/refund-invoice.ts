import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Refund an invoice or a segment of a consolidated invoice. */
export type RefundInvoice = {
  /**
   * The amount to be refunded in decimal format as a string. Example: "10.50". Must not exceed the
   * remaining refundable balance of the payment.
   */
  amount: string;
  /** A description that will be attached to the refund */
  memo: string;
  /** The ID of the payment to be refunded */
  paymentId: number;
  /**
   * Flag that marks refund as external (no money is returned to the customer). Defaults to `false`.
   */
  external?: boolean;
  /** If set to true, creates credit and applies it to an invoice. Defaults to `false`. */
  applyCredit?: boolean;
  /**
   * If `apply_credit` is set to false and refunding full amount, if `void_invoice` is set to true,
   * invoice will be voided after refund. Defaults to `false`.
   */
  voidInvoice?: boolean;
};

export const refundInvoiceSchema: Schema<RefundInvoice> = s.object<RefundInvoice>({
  amount: s.string(),
  memo: s.string(),
  paymentId: s.int(),
  external: s.optional(s.boolean()),
  applyCredit: s.optional(s.boolean()),
  voidInvoice: s.optional(s.boolean()),
  _keysMap: {
    paymentId: "payment_id",
    applyCredit: "apply_credit",
    voidInvoice: "void_invoice",
  },
});
