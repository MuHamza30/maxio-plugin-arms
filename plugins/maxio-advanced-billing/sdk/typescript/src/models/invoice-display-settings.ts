import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoiceDisplaySettings = {
  hideZeroSubtotalLines?: boolean;
  includeDiscountsOnLines?: boolean;
};

export const invoiceDisplaySettingsSchema: Schema<InvoiceDisplaySettings> = s.object<InvoiceDisplaySettings>({
  hideZeroSubtotalLines: s.optional(s.boolean()),
  includeDiscountsOnLines: s.optional(s.boolean()),
  _keysMap: {
    hideZeroSubtotalLines: "hide_zero_subtotal_lines",
    includeDiscountsOnLines: "include_discounts_on_lines",
  },
});
