import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceDiscountBreakoutSchema, type InvoiceDiscountBreakout } from "./invoice-discount-breakout.js";
import { invoiceDiscountTypeSchema, type InvoiceDiscountType } from "./invoice-discount-type.js";
import {
  proformaInvoiceDiscountSourceTypeSchema,
  type ProformaInvoiceDiscountSourceType,
} from "./proforma-invoice-discount-source-type.js";

export type ProformaInvoiceDiscount = {
  uid?: string;
  title?: string;
  code?: string;
  sourceType?: ProformaInvoiceDiscountSourceType;
  discountType?: InvoiceDiscountType;
  eligibleAmount?: string;
  discountAmount?: string;
  lineItemBreakouts?: InvoiceDiscountBreakout[];
};

export const proformaInvoiceDiscountSchema: Schema<ProformaInvoiceDiscount> =
  s.object<ProformaInvoiceDiscount>({
    uid: s.optional(s.string()),
    title: s.optional(s.string()),
    code: s.optional(s.string()),
    sourceType: s.optional(s.lazy(() => proformaInvoiceDiscountSourceTypeSchema)),
    discountType: s.optional(s.lazy(() => invoiceDiscountTypeSchema)),
    eligibleAmount: s.optional(s.string()),
    discountAmount: s.optional(s.string()),
    lineItemBreakouts: s.optional(s.array(s.lazy(() => invoiceDiscountBreakoutSchema))),
    _keysMap: {
      sourceType: "source_type",
      discountType: "discount_type",
      eligibleAmount: "eligible_amount",
      discountAmount: "discount_amount",
      lineItemBreakouts: "line_item_breakouts",
    },
  });
