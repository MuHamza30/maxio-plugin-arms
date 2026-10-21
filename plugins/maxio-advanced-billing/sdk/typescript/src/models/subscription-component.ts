import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentKindSchema, type ComponentKind } from "./component-kind.js";
import { creditTypeSchema, type CreditType } from "./credit-type.js";
import { historicUsageSchema, type HistoricUsage } from "./historic-usage.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { pricePointTypeSchema, type PricePointType } from "./price-point-type.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";
import {
  subscriptionComponentSubscriptionSchema,
  type SubscriptionComponentSubscription,
} from "./subscription-component-subscription.js";
import { allocatedQuantity2Schema, type AllocatedQuantity2 } from "./unions/allocated-quantity2.js";
import { unitBalance1Schema, type UnitBalance1 } from "./unions/unit-balance1.js";

export type SubscriptionComponent = {
  id?: number;
  name?: string;
  /** A handle for the component type */
  kind?: ComponentKind;
  unitName?: string;
  /** (for on/off components) indicates if the component is enabled for the subscription. */
  enabled?: boolean;
  unitBalance?: UnitBalance1;
  currency?: string;
  /**
   * For Quantity-based components: The current allocation for the component on the given
   * subscription. For On/Off components: Use 1 for on. Use 0 for off.
   */
  allocatedQuantity?: AllocatedQuantity2;
  pricingScheme?: PricingScheme | null;
  componentId?: number;
  componentHandle?: string | null;
  subscriptionId?: number;
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
  archivedAt?: Date | null;
  pricePointId?: number | null;
  pricePointHandle?: string | null;
  pricePointType?: PricePointType | null;
  pricePointName?: string | null;
  productFamilyId?: number;
  productFamilyHandle?: string;
  createdAt?: Date;
  updatedAt?: Date;
  useSiteExchangeRate?: boolean | null;
  description?: string | null;
  allowFractionalQuantities?: boolean;
  /**
   * (Optional) Object that will be returned if the `include=subscription` query param is provided.
   */
  subscription?: SubscriptionComponentSubscription;
  historicUsages?: HistoricUsage[];
  displayOnHostedPage?: boolean;
  /**
   * The numerical interval. e.g., an interval of '30' coupled with an interval_unit of day would
   * mean this component price point would renew every 30 days. This property is only available for
   * sites with Multifrequency enabled.
   */
  interval?: number;
  /**
   * A string representing the interval unit for this component price point, either month or day.
   * This property is only available for sites with Multifrequency enabled.
   */
  intervalUnit?: IntervalUnit | null;
};

export const subscriptionComponentSchema: Schema<SubscriptionComponent> = s.object<SubscriptionComponent>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  kind: s.optional(s.lazy(() => componentKindSchema)),
  unitName: s.optional(s.string()),
  enabled: s.optional(s.boolean()),
  unitBalance: s.optional(s.lazy(() => unitBalance1Schema)),
  currency: s.optional(s.string()),
  allocatedQuantity: s.optional(s.lazy(() => allocatedQuantity2Schema)),
  pricingScheme: s.optionalNullable(s.lazy(() => pricingSchemeSchema)),
  componentId: s.optional(s.int()),
  componentHandle: s.optionalNullable(s.string()),
  subscriptionId: s.optional(s.int()),
  recurring: s.optional(s.boolean()),
  upgradeCharge: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  downgradeCredit: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  archivedAt: s.optionalNullable(s.dateTime()),
  pricePointId: s.optionalNullable(s.int()),
  pricePointHandle: s.optionalNullable(s.string()),
  pricePointType: s.optionalNullable(s.lazy(() => pricePointTypeSchema)),
  pricePointName: s.optionalNullable(s.string()),
  productFamilyId: s.optional(s.int()),
  productFamilyHandle: s.optional(s.string()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  useSiteExchangeRate: s.optionalNullable(s.boolean()),
  description: s.optionalNullable(s.string()),
  allowFractionalQuantities: s.optional(s.boolean()),
  subscription: s.optional(s.lazy(() => subscriptionComponentSubscriptionSchema)),
  historicUsages: s.optional(s.array(s.lazy(() => historicUsageSchema))),
  displayOnHostedPage: s.optional(s.boolean()),
  interval: s.optional(s.int()),
  intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  _keysMap: {
    unitName: "unit_name",
    unitBalance: "unit_balance",
    allocatedQuantity: "allocated_quantity",
    pricingScheme: "pricing_scheme",
    componentId: "component_id",
    componentHandle: "component_handle",
    subscriptionId: "subscription_id",
    upgradeCharge: "upgrade_charge",
    downgradeCredit: "downgrade_credit",
    archivedAt: "archived_at",
    pricePointId: "price_point_id",
    pricePointHandle: "price_point_handle",
    pricePointType: "price_point_type",
    pricePointName: "price_point_name",
    productFamilyId: "product_family_id",
    productFamilyHandle: "product_family_handle",
    createdAt: "created_at",
    updatedAt: "updated_at",
    useSiteExchangeRate: "use_site_exchange_rate",
    allowFractionalQuantities: "allow_fractional_quantities",
    historicUsages: "historic_usages",
    displayOnHostedPage: "display_on_hosted_page",
    intervalUnit: "interval_unit",
  },
});
