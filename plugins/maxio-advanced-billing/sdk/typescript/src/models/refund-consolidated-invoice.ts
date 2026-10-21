import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { segmentUidsSchema, type SegmentUids } from "./unions/segment-uids.js";

/** Refund consolidated invoice. */
export type RefundConsolidatedInvoice = {
  /** A description for the refund */
  memo: string;
  /** The ID of the payment to be refunded */
  paymentId: number;
  /**
   * An array of segment uids to refund or the string 'all' to indicate that all segments should be
   * refunded
   */
  segmentUids: SegmentUids;
  /**
   * Flag that marks refund as external (no money is returned to the customer). Defaults to `false`.
   */
  external?: boolean;
  /** If set to true, creates credit and applies it to an invoice. Defaults to `false`. */
  applyCredit?: boolean;
  /**
   * The amount of payment to be refunded in decimal format. Example: "10.50". This will default to
   * the full amount of the payment if not provided.
   */
  amount?: string;
};

export const refundConsolidatedInvoiceSchema: Schema<RefundConsolidatedInvoice> =
  s.object<RefundConsolidatedInvoice>({
    memo: s.string(),
    paymentId: s.int(),
    segmentUids: segmentUidsSchema,
    external: s.optional(s.boolean()),
    applyCredit: s.optional(s.boolean()),
    amount: s.optional(s.string()),
    _keysMap: {
      paymentId: "payment_id",
      segmentUids: "segment_uids",
      applyCredit: "apply_credit",
    },
  });
