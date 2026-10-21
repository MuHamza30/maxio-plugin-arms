import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const InvoiceDiscountType = {
  Percentage: "percentage",
  FlatAmount: "flat_amount",
  Rollover: "rollover",
} as const;
export type InvoiceDiscountType =
  | (typeof InvoiceDiscountType)[keyof typeof InvoiceDiscountType]
  | (string & {});

export const invoiceDiscountTypeSchema: EnumSchema<InvoiceDiscountType> =
  s.enumOf<InvoiceDiscountType>(InvoiceDiscountType);
