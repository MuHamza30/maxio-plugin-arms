import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoiceDiscountBreakout = {
  uid?: string;
  eligibleAmount?: string;
  discountAmount?: string;
};

export const invoiceDiscountBreakoutSchema: Schema<InvoiceDiscountBreakout> =
  s.object<InvoiceDiscountBreakout>({
    uid: s.optional(s.string()),
    eligibleAmount: s.optional(s.string()),
    discountAmount: s.optional(s.string()),
    _keysMap: {
      eligibleAmount: "eligible_amount",
      discountAmount: "discount_amount",
    },
  });
