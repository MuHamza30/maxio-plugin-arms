import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { price1Schema, type Price1 } from "./price1.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

/** A price point to create for the Wallet Product, in the same call that creates or updates it. */
export type WalletProductPricePointAttributes = {
  /**
   * The price point's name. Required. Omitting it fails validation with a message that reads `Name:
   * cannot be blank.`, not naming the price point.
   */
  name: string;
  handle?: string;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme?: PricingScheme;
  /** Required when `pricing_scheme` is `per_unit`. */
  unitPrice?: string | null;
  taxIncluded?: boolean;
  /** Requires Multifrequency to be enabled on the site. */
  interval?: number;
  intervalUnit?: IntervalUnit;
  useSiteExchangeRate?: boolean;
  /** Required for every `pricing_scheme` other than `per_unit`. */
  prices?: Price1[];
};

export const walletProductPricePointAttributesSchema: Schema<WalletProductPricePointAttributes> =
  s.object<WalletProductPricePointAttributes>({
    name: s.string(),
    handle: s.optional(s.string()),
    pricingScheme: s.optional(s.lazy(() => pricingSchemeSchema)),
    unitPrice: s.optionalNullable(s.string()),
    taxIncluded: s.optional(s.boolean()),
    interval: s.optional(s.int()),
    intervalUnit: s.optional(s.lazy(() => intervalUnitSchema)),
    useSiteExchangeRate: s.optional(s.boolean()),
    prices: s.optional(s.array(s.lazy(() => price1Schema))),
    _keysMap: {
      pricingScheme: "pricing_scheme",
      unitPrice: "unit_price",
      taxIncluded: "tax_included",
      intervalUnit: "interval_unit",
      useSiteExchangeRate: "use_site_exchange_rate",
    },
  });
