import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentPricePointItemSchema, type ComponentPricePointItem } from "./component-price-point-item.js";
import { creditTypeSchema, type CreditType } from "./credit-type.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { unitPrice3Schema, type UnitPrice3 } from "./unions/unit-price3.js";

export type OnOffComponent = {
  /**
   * A name for this component that is suitable for showing customers and displaying on billing
   * statements, e.g., "Minutes".
   */
  name: string;
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
   * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
   * site setting if one is not provided.
   */
  upgradeCharge?: CreditType | null;
  /**
   * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
   * site setting if one is not provided.
   */
  downgradeCredit?: CreditType | null;
  pricePoints?: ComponentPricePointItem[];
  /**
   * This is the amount that the customer will be charged when they turn the component on for the
   * subscription. The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065
   */
  unitPrice: UnitPrice3;
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

export const onOffComponentSchema: Schema<OnOffComponent> = s.object<OnOffComponent>({
  name: s.string(),
  description: s.optional(s.string()),
  handle: s.optional(s.string()),
  taxable: s.optional(s.boolean()),
  upgradeCharge: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  downgradeCredit: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  pricePoints: s.optional(s.array(s.lazy(() => componentPricePointItemSchema))),
  unitPrice: unitPrice3Schema,
  taxCode: s.optional(s.string()),
  hideDateRangeOnInvoice: s.optional(s.boolean()),
  displayOnHostedPage: s.optional(s.boolean()),
  allowFractionalQuantities: s.optional(s.boolean()),
  publicSignupPageIds: s.optional(s.array(s.int())),
  interval: s.optional(s.int()),
  intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  unspscCode: s.optionalNullable(s.string()),
  _keysMap: {
    upgradeCharge: "upgrade_charge",
    downgradeCredit: "downgrade_credit",
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
