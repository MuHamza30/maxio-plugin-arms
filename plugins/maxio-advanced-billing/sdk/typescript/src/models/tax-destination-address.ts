import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const TaxDestinationAddress = {
  ShippingThenBilling: "shipping_then_billing",
  BillingThenShipping: "billing_then_shipping",
  ShippingOnly: "shipping_only",
  BillingOnly: "billing_only",
} as const;
export type TaxDestinationAddress =
  | (typeof TaxDestinationAddress)[keyof typeof TaxDestinationAddress]
  | (string & {});

export const taxDestinationAddressSchema: EnumSchema<TaxDestinationAddress> =
  s.enumOf<TaxDestinationAddress>(TaxDestinationAddress);
