import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceTaxBreakoutSchema, type InvoiceTaxBreakout } from "./invoice-tax-breakout.js";
import {
  invoiceTaxComponentBreakoutSchema,
  type InvoiceTaxComponentBreakout,
} from "./invoice-tax-component-breakout.js";
import {
  proformaInvoiceTaxSourceTypeSchema,
  type ProformaInvoiceTaxSourceType,
} from "./proforma-invoice-tax-source-type.js";

export type InvoiceTax = {
  uid?: string;
  title?: string;
  description?: string | null;
  sourceType?: ProformaInvoiceTaxSourceType;
  sourceId?: number;
  percentage?: string;
  taxableAmount?: string;
  taxAmount?: string;
  transactionId?: number;
  lineItemBreakouts?: InvoiceTaxBreakout[];
  taxComponentBreakouts?: InvoiceTaxComponentBreakout[];
  euVat?: boolean;
  type?: string;
  taxExemptAmount?: string;
};

export const invoiceTaxSchema: Schema<InvoiceTax> = s.object<InvoiceTax>({
  uid: s.optional(s.string()),
  title: s.optional(s.string()),
  description: s.optionalNullable(s.string()),
  sourceType: s.optional(s.lazy(() => proformaInvoiceTaxSourceTypeSchema)),
  sourceId: s.optional(s.int()),
  percentage: s.optional(s.string()),
  taxableAmount: s.optional(s.string()),
  taxAmount: s.optional(s.string()),
  transactionId: s.optional(s.int()),
  lineItemBreakouts: s.optional(s.array(s.lazy(() => invoiceTaxBreakoutSchema))),
  taxComponentBreakouts: s.optional(s.array(s.lazy(() => invoiceTaxComponentBreakoutSchema))),
  euVat: s.optional(s.boolean()),
  type: s.optional(s.string()),
  taxExemptAmount: s.optional(s.string()),
  _keysMap: {
    sourceType: "source_type",
    sourceId: "source_id",
    taxableAmount: "taxable_amount",
    taxAmount: "tax_amount",
    transactionId: "transaction_id",
    lineItemBreakouts: "line_item_breakouts",
    taxComponentBreakouts: "tax_component_breakouts",
    euVat: "eu_vat",
    taxExemptAmount: "tax_exempt_amount",
  },
});
