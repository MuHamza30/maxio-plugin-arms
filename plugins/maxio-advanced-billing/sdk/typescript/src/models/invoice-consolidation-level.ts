import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * Consolidation level of the invoice, which is applicable to invoice consolidation. It will hold
 * one of the following values:
 *
 * * "none": A normal invoice with no consolidation.
 * * "child": An invoice segment which has been combined into a consolidated invoice.
 * * "parent": A consolidated invoice, whose contents are composed of invoice segments.
 *
 * "Parent" invoices do not have lines of their own, but they have subtotals and totals which
 * aggregate the member invoice segments.
 *
 * See also the [invoice consolidation
 * documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation).
 */
export const InvoiceConsolidationLevel = {
  None: "none",
  Child: "child",
  Parent: "parent",
} as const;
export type InvoiceConsolidationLevel =
  | (typeof InvoiceConsolidationLevel)[keyof typeof InvoiceConsolidationLevel]
  | (string & {});

export const invoiceConsolidationLevelSchema: EnumSchema<InvoiceConsolidationLevel> =
  s.enumOf<InvoiceConsolidationLevel>(InvoiceConsolidationLevel);
