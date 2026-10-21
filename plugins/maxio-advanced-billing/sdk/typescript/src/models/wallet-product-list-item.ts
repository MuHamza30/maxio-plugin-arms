import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentKindSchema, type ComponentKind } from "./component-kind.js";
import { componentPriceSchema, type ComponentPrice } from "./component-price.js";
import { creditTypeSchema, type CreditType } from "./credit-type.js";
import { featureCatalogItemSchema, type FeatureCatalogItem } from "./feature-catalog-item.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { itemCategorySchema, type ItemCategory } from "./item-category.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";
import {
  walletProductPricePointSummarySchema,
  type WalletProductPricePointSummary,
} from "./wallet-product-price-point-summary.js";
import { walletProductUsageCountSchema, type WalletProductUsageCount } from "./wallet-product-usage-count.js";

/**
 * A Wallet Product as it appears in [List Wallet
 * Products]($e/Wallet%20Products/listWalletProducts): the full Component field set, plus a usage
 * count and a price point summary that only the list response reports.
 */
export type WalletProductListItem = {
  /**
   * The unique ID assigned to the component by Chargify. This ID can be used to fetch the component
   * from the API.
   */
  id?: number;
  /** The name of the Component, suitable for display on statements. e.g., Text Messages. */
  name?: string;
  /** The component API handle */
  handle?: string | null;
  pricingScheme?: PricingScheme | null;
  /** The name of the unit that the component’s usage is measured in. e.g., message */
  unitName?: string;
  /**
   * The amount the customer will be charged per unit. This field is only populated for ‘per_unit’
   * pricing schemes, otherwise it may be null.
   */
  unitPrice?: string | null;
  /**
   * The id of the Product Family to which the Component belongs. `null` for a Wallet Product, which
   * has no Product Family.
   */
  productFamilyId?: number | null;
  /**
   * The name of the Product Family to which the Component belongs. `null` for a Wallet Product,
   * which has no Product Family.
   */
  productFamilyName?: string | null;
  /**
   * The handle of the Product Family to which the Component belongs. `null` for a Wallet Product,
   * which has no Product Family.
   */
  productFamilyHandle?: string | null;
  /** deprecated - use unit_price instead. */
  pricePerUnitInCents?: number | null;
  /** A handle for the component type */
  kind?: ComponentKind;
  /** Boolean flag describing whether a component is archived or not. */
  archived?: boolean;
  /** The description of the component. */
  description?: string | null;
  defaultPricePointId?: number | null;
  /** Applicable only to prepaid usage components. An array of overage price brackets. */
  overagePrices?: ComponentPrice[] | null;
  /**
   * An array of price brackets. If the component uses the ‘per_unit’ pricing scheme, this array
   * will be empty.
   */
  prices?: ComponentPrice[] | null;
  /** Count for the number of price points associated with the component */
  pricePointCount?: number;
  /** URL that points to the location to read the existing price points via GET request */
  pricePointsUrl?: string | null;
  defaultPricePointName?: string;
  /** Boolean flag describing whether a component is taxable or not. */
  taxable?: boolean;
  /**
   * A string representing the tax code related to the component type. This is especially important
   * when using AvaTax to tax based on locale. This attribute has a max length of 25 characters.
   */
  taxCode?: string | null;
  recurring?: boolean;
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
  /** Timestamp indicating when this component was created */
  createdAt?: Date;
  /** Timestamp indicating when this component was updated */
  updatedAt?: Date;
  /** Timestamp indicating when this component was archived */
  archivedAt?: Date | null;
  /**
   * (Only available on Relationship Invoicing sites) Boolean flag describing if the service date
   * range should show for the component on generated invoices.
   */
  hideDateRangeOnInvoice?: boolean;
  allowFractionalQuantities?: boolean;
  /**
   * One of the following: Business Software, Consumer Software, Digital Services, Physical Goods,
   * Other
   */
  itemCategory?: ItemCategory | null;
  useSiteExchangeRate?: boolean | null;
  /** E.g. Internal ID or SKU Number */
  accountingCode?: string | null;
  /**
   * (Only for Event Based Components) This is an ID of a metric attached to the component. This
   * metric is used to bill upon collected events.
   */
  eventBasedBillingMetricId?: number;
  /**
   * The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would
   * mean this component’s default price point would renew every 30 days. This property is only
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
  /**
   * The active feature catalog items attached to this component. Present only when the request
   * includes `include_features=true`.
   */
  features?: FeatureCatalogItem[] | null;
  /** A rollup of what's using this Wallet Product, for the catalog listing. */
  usedBy?: WalletProductUsageCount;
  /**
   * A summary of the Wallet Product's default price point, for rendering a catalog listing without
   * a separate price points call.
   */
  pricePointSummary?: WalletProductPricePointSummary;
};

export const walletProductListItemSchema: Schema<WalletProductListItem> = s.object<WalletProductListItem>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  handle: s.optionalNullable(s.string()),
  pricingScheme: s.optionalNullable(s.lazy(() => pricingSchemeSchema)),
  unitName: s.optional(s.string()),
  unitPrice: s.optionalNullable(s.string()),
  productFamilyId: s.optionalNullable(s.int()),
  productFamilyName: s.optionalNullable(s.string()),
  productFamilyHandle: s.optionalNullable(s.string()),
  pricePerUnitInCents: s.optionalNullable(s.int()),
  kind: s.optional(s.lazy(() => componentKindSchema)),
  archived: s.optional(s.boolean()),
  description: s.optionalNullable(s.string()),
  defaultPricePointId: s.optionalNullable(s.int()),
  overagePrices: s.optionalNullable(s.array(s.lazy(() => componentPriceSchema))),
  prices: s.optionalNullable(s.array(s.lazy(() => componentPriceSchema))),
  pricePointCount: s.optional(s.int()),
  pricePointsUrl: s.optionalNullable(s.string()),
  defaultPricePointName: s.optional(s.string()),
  taxable: s.optional(s.boolean()),
  taxCode: s.optionalNullable(s.string()),
  recurring: s.optional(s.boolean()),
  upgradeCharge: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  downgradeCredit: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  archivedAt: s.optionalNullable(s.dateTime()),
  hideDateRangeOnInvoice: s.optional(s.boolean()),
  allowFractionalQuantities: s.optional(s.boolean()),
  itemCategory: s.optionalNullable(s.lazy(() => itemCategorySchema)),
  useSiteExchangeRate: s.optionalNullable(s.boolean()),
  accountingCode: s.optionalNullable(s.string()),
  eventBasedBillingMetricId: s.optional(s.int()),
  interval: s.optional(s.int()),
  intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  unspscCode: s.optionalNullable(s.string()),
  features: s.optionalNullable(s.array(s.lazy(() => featureCatalogItemSchema))),
  usedBy: s.optional(s.lazy(() => walletProductUsageCountSchema)),
  pricePointSummary: s.optional(s.lazy(() => walletProductPricePointSummarySchema)),
  _keysMap: {
    pricingScheme: "pricing_scheme",
    unitName: "unit_name",
    unitPrice: "unit_price",
    productFamilyId: "product_family_id",
    productFamilyName: "product_family_name",
    productFamilyHandle: "product_family_handle",
    pricePerUnitInCents: "price_per_unit_in_cents",
    defaultPricePointId: "default_price_point_id",
    overagePrices: "overage_prices",
    pricePointCount: "price_point_count",
    pricePointsUrl: "price_points_url",
    defaultPricePointName: "default_price_point_name",
    taxCode: "tax_code",
    upgradeCharge: "upgrade_charge",
    downgradeCredit: "downgrade_credit",
    createdAt: "created_at",
    updatedAt: "updated_at",
    archivedAt: "archived_at",
    hideDateRangeOnInvoice: "hide_date_range_on_invoice",
    allowFractionalQuantities: "allow_fractional_quantities",
    itemCategory: "item_category",
    useSiteExchangeRate: "use_site_exchange_rate",
    accountingCode: "accounting_code",
    eventBasedBillingMetricId: "event_based_billing_metric_id",
    intervalUnit: "interval_unit",
    unspscCode: "unspsc_code",
    usedBy: "used_by",
    pricePointSummary: "price_point_summary",
  },
});
