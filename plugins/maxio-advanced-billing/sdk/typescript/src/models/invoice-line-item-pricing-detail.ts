import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoiceLineItemPricingDetail = {
  label?: string;
  amount?: string;
};

export const invoiceLineItemPricingDetailSchema: Schema<InvoiceLineItemPricingDetail> =
  s.object<InvoiceLineItemPricingDetail>({
    label: s.optional(s.string()),
    amount: s.optional(s.string()),
  });
