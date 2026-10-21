import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { priceSchema, type Price } from "./price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

/** Custom pricing for a component within a scheduled renewal. */
export type ScheduledRenewalComponentCustomPrice = {
  /** Whether or not the price point includes tax */
  taxIncluded?: boolean;
  /** Omit for On/Off components. */
  pricingScheme: PricingScheme;
  /** On/off components only need one price bracket starting at 1. */
  prices: Price[];
};

export const scheduledRenewalComponentCustomPriceSchema: Schema<ScheduledRenewalComponentCustomPrice> =
  s.object<ScheduledRenewalComponentCustomPrice>({
    taxIncluded: s.optional(s.boolean()),
    pricingScheme: pricingSchemeSchema,
    prices: s.array(s.lazy(() => priceSchema)),
    _keysMap: {
      taxIncluded: "tax_included",
      pricingScheme: "pricing_scheme",
    },
  });
