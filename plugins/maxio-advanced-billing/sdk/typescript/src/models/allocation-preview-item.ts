import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditTypeSchema, type CreditType } from "./credit-type.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { previousQuantity1Schema, type PreviousQuantity1 } from "./unions/previous-quantity1.js";
import { quantity1Schema, type Quantity1 } from "./unions/quantity1.js";

export type AllocationPreviewItem = {
  componentId?: number;
  subscriptionId?: number;
  quantity?: Quantity1;
  previousQuantity?: PreviousQuantity1;
  memo?: string | null;
  timestamp?: string | null;
  /**
   * @deprecated
   */
  prorationUpgradeScheme?: string;
  /**
   * @deprecated
   */
  prorationDowngradeScheme?: string;
  accrueCharge?: boolean;
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
  pricePointId?: number;
  /**
   * The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would
   * mean this component price point would renew every 30 days. This property is only available for
   * sites with Multifrequency enabled.
   */
  interval?: number;
  /**
   * A string representing the interval unit for this component price point, either month or day.
   * This property is only available for sites with Multifrequency enabled.
   */
  intervalUnit?: IntervalUnit | null;
  previousPricePointId?: number;
  pricePointHandle?: string;
  pricePointName?: string;
  componentHandle?: string | null;
};

export const allocationPreviewItemSchema: Schema<AllocationPreviewItem> = s.object<AllocationPreviewItem>({
  componentId: s.optional(s.int()),
  subscriptionId: s.optional(s.int()),
  quantity: s.optional(s.lazy(() => quantity1Schema)),
  previousQuantity: s.optional(s.lazy(() => previousQuantity1Schema)),
  memo: s.optionalNullable(s.string()),
  timestamp: s.optionalNullable(s.string()),
  prorationUpgradeScheme: s.optional(s.string()),
  prorationDowngradeScheme: s.optional(s.string()),
  accrueCharge: s.optional(s.boolean()),
  upgradeCharge: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  downgradeCredit: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  pricePointId: s.optional(s.int()),
  interval: s.optional(s.int()),
  intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  previousPricePointId: s.optional(s.int()),
  pricePointHandle: s.optional(s.string()),
  pricePointName: s.optional(s.string()),
  componentHandle: s.optionalNullable(s.string()),
  _keysMap: {
    componentId: "component_id",
    subscriptionId: "subscription_id",
    previousQuantity: "previous_quantity",
    prorationUpgradeScheme: "proration_upgrade_scheme",
    prorationDowngradeScheme: "proration_downgrade_scheme",
    accrueCharge: "accrue_charge",
    upgradeCharge: "upgrade_charge",
    downgradeCredit: "downgrade_credit",
    pricePointId: "price_point_id",
    intervalUnit: "interval_unit",
    previousPricePointId: "previous_price_point_id",
    pricePointHandle: "price_point_handle",
    pricePointName: "price_point_name",
    componentHandle: "component_handle",
  },
});
