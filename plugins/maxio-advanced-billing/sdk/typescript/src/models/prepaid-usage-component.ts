import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  createPrepaidUsageComponentPricePointSchema,
  type CreatePrepaidUsageComponentPricePoint,
} from "./create-prepaid-usage-component-price-point.js";
import { creditTypeSchema, type CreditType } from "./credit-type.js";
import { expirationIntervalUnitSchema, type ExpirationIntervalUnit } from "./expiration-interval-unit.js";
import { overagePricingSchema, type OveragePricing } from "./overage-pricing.js";
import { priceSchema, type Price } from "./price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";
import { unitPrice1Schema, type UnitPrice1 } from "./unions/unit-price1.js";

export type PrepaidUsageComponent = {
  /**
   * A name for this component that is suitable for showing customers and displaying on billing
   * statements, e.g., "Minutes".
   */
  name: string;
  /**
   * The name of the unit of measurement for the component. It should be singular since it will be
   * automatically pluralized when necessary. e.g., “message”, which may then be shown as “5
   * messages” on a subscription’s component line-item
   */
  unitName: string;
  /**
   * A description for the component that will be displayed to the user on the hosted signup page.
   */
  description?: string;
  /**
   * A unique identifier for your use that can be used to retrieve this component in subsequent
   * requests. Must start with a letter or number and may only contain lowercase letters, numbers,
   * or the characters '.', ':', '-', or '_'.
   */
  handle?: string;
  /** Boolean flag describing whether a component is taxable or not. */
  taxable?: boolean;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme: PricingScheme;
  /**
   * (Not required for ‘per_unit’ pricing schemes) One or more price brackets. See [Price Bracket
   * Rules](https://maxio.zendesk.com/hc/en-us/articles/24261149166733-Component-Pricing-Schemes#price-bracket-rules)
   * for an overview of how price brackets work for different pricing schemes.
   */
  prices?: Price[];
  /**
   * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
   * site setting if one is not provided.
   */
  upgradeCharge?: CreditType | null;
  /**
   * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
   * site setting if one is not provided.
   */
  downgradeCredit?: CreditType | null;
  pricePoints?: CreatePrepaidUsageComponentPricePoint[];
  /**
   * The amount the customer will be charged per unit when the pricing scheme is “per_unit”. For
   * On/Off Components, this is the amount that the customer will be charged when they turn the
   * component on for the subscription. The price can contain up to 8 decimal places. e.g., 1.00 or
   * 0.0012 or 0.00000065
   */
  unitPrice?: UnitPrice1;
  /**
   * A string representing the tax code related to the component type. This is especially important
   * when using AvaTax to tax based on locale. This attribute has a max length of 25 characters.
   */
  taxCode?: string;
  /**
   * (Only available on Relationship Invoicing sites) Boolean flag describing if the service date
   * range should show for the component on generated invoices.
   */
  hideDateRangeOnInvoice?: boolean;
  overagePricing: OveragePricing;
  /**
   * Boolean which controls whether or not remaining units should be rolled over to the next period.
   */
  rolloverPrepaidRemainder?: boolean;
  /**
   * Boolean which controls whether or not the allocated quantity should be renewed at the beginning
   * of each period.
   */
  renewPrepaidAllocation?: boolean;
  /**
   * (only for prepaid usage components where rollover_prepaid_remainder is true) The number of
   * `expiration_interval_unit`s after which rollover amounts should expire
   */
  expirationInterval?: number;
  expirationIntervalUnit?: ExpirationIntervalUnit | null;
  displayOnHostedPage?: boolean;
  allowFractionalQuantities?: boolean;
  publicSignupPageIds?: number[];
  /**
   * (Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is
   * sent as the commodity code on invoice line items for this component instead of the default
   * derived from item_category.
   */
  unspscCode?: string | null;
};

export const prepaidUsageComponentSchema: Schema<PrepaidUsageComponent> = s.object<PrepaidUsageComponent>({
  name: s.string(),
  unitName: s.string(),
  description: s.optional(s.string()),
  handle: s.optional(s.string()),
  taxable: s.optional(s.boolean()),
  pricingScheme: pricingSchemeSchema,
  prices: s.optional(s.array(s.lazy(() => priceSchema))),
  upgradeCharge: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  downgradeCredit: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  pricePoints: s.optional(s.array(s.lazy(() => createPrepaidUsageComponentPricePointSchema))),
  unitPrice: s.optional(s.lazy(() => unitPrice1Schema)),
  taxCode: s.optional(s.string()),
  hideDateRangeOnInvoice: s.optional(s.boolean()),
  overagePricing: overagePricingSchema,
  rolloverPrepaidRemainder: s.optional(s.boolean()),
  renewPrepaidAllocation: s.optional(s.boolean()),
  expirationInterval: s.optional(s.float64()),
  expirationIntervalUnit: s.optionalNullable(s.lazy(() => expirationIntervalUnitSchema)),
  displayOnHostedPage: s.optional(s.boolean()),
  allowFractionalQuantities: s.optional(s.boolean()),
  publicSignupPageIds: s.optional(s.array(s.int())),
  unspscCode: s.optionalNullable(s.string()),
  _keysMap: {
    unitName: "unit_name",
    pricingScheme: "pricing_scheme",
    upgradeCharge: "upgrade_charge",
    downgradeCredit: "downgrade_credit",
    pricePoints: "price_points",
    unitPrice: "unit_price",
    taxCode: "tax_code",
    hideDateRangeOnInvoice: "hide_date_range_on_invoice",
    overagePricing: "overage_pricing",
    rolloverPrepaidRemainder: "rollover_prepaid_remainder",
    renewPrepaidAllocation: "renew_prepaid_allocation",
    expirationInterval: "expiration_interval",
    expirationIntervalUnit: "expiration_interval_unit",
    displayOnHostedPage: "display_on_hosted_page",
    allowFractionalQuantities: "allow_fractional_quantities",
    publicSignupPageIds: "public_signup_page_ids",
    unspscCode: "unspsc_code",
  },
});
