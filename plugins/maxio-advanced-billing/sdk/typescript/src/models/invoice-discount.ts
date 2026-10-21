import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceDiscountBreakoutSchema, type InvoiceDiscountBreakout } from "./invoice-discount-breakout.js";
import {
  invoiceDiscountSourceTypeSchema,
  type InvoiceDiscountSourceType,
} from "./invoice-discount-source-type.js";
import { invoiceDiscountTypeSchema, type InvoiceDiscountType } from "./invoice-discount-type.js";

export type InvoiceDiscount = {
  uid?: string;
  title?: string;
  description?: string | null;
  code?: string;
  sourceType?: InvoiceDiscountSourceType;
  sourceId?: number;
  discountType?: InvoiceDiscountType;
  percentage?: string;
  eligibleAmount?: string;
  discountAmount?: string;
  transactionId?: number;
  lineItemBreakouts?: InvoiceDiscountBreakout[];
};

export const invoiceDiscountSchema: Schema<InvoiceDiscount> = s.object<InvoiceDiscount>({
  uid: s.optional(s.string()),
  title: s.optional(s.string()),
  description: s.optionalNullable(s.string()),
  code: s.optional(s.string()),
  sourceType: s.optional(s.lazy(() => invoiceDiscountSourceTypeSchema)),
  sourceId: s.optional(s.int()),
  discountType: s.optional(s.lazy(() => invoiceDiscountTypeSchema)),
  percentage: s.optional(s.string()),
  eligibleAmount: s.optional(s.string()),
  discountAmount: s.optional(s.string()),
  transactionId: s.optional(s.int()),
  lineItemBreakouts: s.optional(s.array(s.lazy(() => invoiceDiscountBreakoutSchema))),
  _keysMap: {
    sourceType: "source_type",
    sourceId: "source_id",
    discountType: "discount_type",
    eligibleAmount: "eligible_amount",
    discountAmount: "discount_amount",
    transactionId: "transaction_id",
    lineItemBreakouts: "line_item_breakouts",
  },
});
