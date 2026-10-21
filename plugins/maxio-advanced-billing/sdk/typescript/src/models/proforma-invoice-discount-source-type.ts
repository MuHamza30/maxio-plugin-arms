import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ProformaInvoiceDiscountSourceType = {
  Coupon: "Coupon",
  Referral: "Referral",
} as const;
export type ProformaInvoiceDiscountSourceType =
  | (typeof ProformaInvoiceDiscountSourceType)[keyof typeof ProformaInvoiceDiscountSourceType]
  | (string & {});

export const proformaInvoiceDiscountSourceTypeSchema: EnumSchema<ProformaInvoiceDiscountSourceType> =
  s.enumOf<ProformaInvoiceDiscountSourceType>(ProformaInvoiceDiscountSourceType);
