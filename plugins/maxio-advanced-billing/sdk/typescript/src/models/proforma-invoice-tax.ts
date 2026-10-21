import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceTaxBreakoutSchema, type InvoiceTaxBreakout } from "./invoice-tax-breakout.js";
import {
  proformaInvoiceTaxSourceTypeSchema,
  type ProformaInvoiceTaxSourceType,
} from "./proforma-invoice-tax-source-type.js";

export type ProformaInvoiceTax = {
  uid?: string;
  title?: string;
  sourceType?: ProformaInvoiceTaxSourceType;
  percentage?: string;
  taxableAmount?: string;
  taxAmount?: string;
  lineItemBreakouts?: InvoiceTaxBreakout[];
};

export const proformaInvoiceTaxSchema: Schema<ProformaInvoiceTax> = s.object<ProformaInvoiceTax>({
  uid: s.optional(s.string()),
  title: s.optional(s.string()),
  sourceType: s.optional(s.lazy(() => proformaInvoiceTaxSourceTypeSchema)),
  percentage: s.optional(s.string()),
  taxableAmount: s.optional(s.string()),
  taxAmount: s.optional(s.string()),
  lineItemBreakouts: s.optional(s.array(s.lazy(() => invoiceTaxBreakoutSchema))),
  _keysMap: {
    sourceType: "source_type",
    taxableAmount: "taxable_amount",
    taxAmount: "tax_amount",
    lineItemBreakouts: "line_item_breakouts",
  },
});
