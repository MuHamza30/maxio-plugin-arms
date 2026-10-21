import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const InvoiceDiscountSourceType = {
  Coupon: "Coupon",
  Referral: "Referral",
  AdHocCoupon: "Ad Hoc Coupon",
} as const;
export type InvoiceDiscountSourceType =
  | (typeof InvoiceDiscountSourceType)[keyof typeof InvoiceDiscountSourceType]
  | (string & {});

export const invoiceDiscountSourceTypeSchema: EnumSchema<InvoiceDiscountSourceType> =
  s.enumOf<InvoiceDiscountSourceType>(InvoiceDiscountSourceType);
