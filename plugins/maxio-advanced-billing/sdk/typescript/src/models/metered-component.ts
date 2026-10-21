import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentPricePointItemSchema, type ComponentPricePointItem } from "./component-price-point-item.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { priceSchema, type Price } from "./price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";
import { unitPrice1Schema, type UnitPrice1 } from "./unions/unit-price1.js";

export type MeteredComponent = {
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
  pricePoints?: ComponentPricePointItem[];
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
  displayOnHostedPage?: boolean;
  allowFractionalQuantities?: boolean;
  publicSignupPageIds?: number[];
  /**
   * The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would
   * mean this component's default price point would renew every 30 days. This property is only
   * available for sites with Multifrequency enabled.
   */
  interval?: number;
  /**
   * A string representing the interval unit for this component's default price point, either month
   * or day. This property is only available for sites with Multifrequency enabled.
   */
  intervalUnit?: IntervalUnit | null;
  /**
   * (Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is
   * sent as the commodity code on invoice line items for this component instead of the default
   * derived from item_category.
   */
  unspscCode?: string | null;
};

export const meteredComponentSchema: Schema<MeteredComponent> = s.object<MeteredComponent>({
  name: s.string(),
  unitName: s.string(),
  description: s.optional(s.string()),
  handle: s.optional(s.string()),
  taxable: s.optional(s.boolean()),
  pricingScheme: pricingSchemeSchema,
  prices: s.optional(s.array(s.lazy(() => priceSchema))),
  pricePoints: s.optional(s.array(s.lazy(() => componentPricePointItemSchema))),
  unitPrice: s.optional(s.lazy(() => unitPrice1Schema)),
  taxCode: s.optional(s.string()),
  hideDateRangeOnInvoice: s.optional(s.boolean()),
  displayOnHostedPage: s.optional(s.boolean()),
  allowFractionalQuantities: s.optional(s.boolean()),
  publicSignupPageIds: s.optional(s.array(s.int())),
  interval: s.optional(s.int()),
  intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  unspscCode: s.optionalNullable(s.string()),
  _keysMap: {
    unitName: "unit_name",
    pricingScheme: "pricing_scheme",
    pricePoints: "price_points",
    unitPrice: "unit_price",
    taxCode: "tax_code",
    hideDateRangeOnInvoice: "hide_date_range_on_invoice",
    displayOnHostedPage: "display_on_hosted_page",
    allowFractionalQuantities: "allow_fractional_quantities",
    publicSignupPageIds: "public_signup_page_ids",
    intervalUnit: "interval_unit",
    unspscCode: "unspsc_code",
  },
});
