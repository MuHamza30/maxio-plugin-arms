import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditTypeSchema, type CreditType } from "./credit-type.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { paymentForAllocationSchema, type PaymentForAllocation } from "./payment-for-allocation.js";
import { previousQuantitySchema, type PreviousQuantity } from "./unions/previous-quantity.js";
import { quantitySchema, type Quantity } from "./unions/quantity.js";

export type Allocation = {
  /** The allocation unique ID */
  allocationId?: number;
  /**
   * The integer component ID for the allocation. This references a component that you have created
   * in your Product setup.
   */
  componentId?: number;
  /**
   * The handle of the component. This references a component that you have created in your Product
   * setup.
   */
  componentHandle?: string | null;
  /**
   * The integer subscription ID for the allocation. This references a unique subscription in your
   * Site.
   */
  subscriptionId?: number;
  /**
   * The allocated quantity set into effect by the allocation. String for components supporting
   * fractional quantities
   */
  quantity?: Quantity;
  /**
   * The allocated quantity that was in effect before this allocation was created. String for
   * components supporting fractional quantities
   */
  previousQuantity?: PreviousQuantity;
  /** The memo passed when the allocation was created */
  memo?: string | null;
  /**
   * The time that the allocation was recorded, in ISO 8601 format and UTC timezone, e.g.,
   * 2012-11-20T22:00:37Z
   */
  timestamp?: Date;
  /** Timestamp indicating when this allocation was created */
  createdAt?: Date;
  /**
   * The scheme used if the proration was an upgrade. This is only present when the allocation was
   * created mid-period.
   *
   * @deprecated
   */
  prorationUpgradeScheme?: string;
  /**
   * The scheme used if the proration was a downgrade. This is only present when the allocation was
   * created mid-period.
   *
   * @deprecated
   */
  prorationDowngradeScheme?: string;
  pricePointId?: number;
  pricePointName?: string;
  pricePointHandle?: string;
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
  /**
   * If the change in cost is an upgrade, this determines if the charge should accrue to the next
   * renewal or if capture should be attempted immediately.
   */
  accrueCharge?: boolean;
  /**
   * If true, if the immediate component payment fails, initiate dunning for the subscription.
   * Otherwise, leave the charges on the subscription to pay for at renewal.
   */
  initiateDunning?: boolean;
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
  payment?: PaymentForAllocation | null;
  expiresAt?: Date;
  usedQuantity?: number;
  chargeId?: number;
};

export const allocationSchema: Schema<Allocation> = s.object<Allocation>({
  allocationId: s.optional(s.int()),
  componentId: s.optional(s.int()),
  componentHandle: s.optionalNullable(s.string()),
  subscriptionId: s.optional(s.int()),
  quantity: s.optional(s.lazy(() => quantitySchema)),
  previousQuantity: s.optional(s.lazy(() => previousQuantitySchema)),
  memo: s.optionalNullable(s.string()),
  timestamp: s.optional(s.dateTime()),
  createdAt: s.optional(s.dateTime()),
  prorationUpgradeScheme: s.optional(s.string()),
  prorationDowngradeScheme: s.optional(s.string()),
  pricePointId: s.optional(s.int()),
  pricePointName: s.optional(s.string()),
  pricePointHandle: s.optional(s.string()),
  interval: s.optional(s.int()),
  intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  previousPricePointId: s.optional(s.int()),
  accrueCharge: s.optional(s.boolean()),
  initiateDunning: s.optional(s.boolean()),
  upgradeCharge: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  downgradeCredit: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  payment: s.optionalNullable(s.lazy(() => paymentForAllocationSchema)),
  expiresAt: s.optional(s.dateTime()),
  usedQuantity: s.optional(s.int()),
  chargeId: s.optional(s.int()),
  _keysMap: {
    allocationId: "allocation_id",
    componentId: "component_id",
    componentHandle: "component_handle",
    subscriptionId: "subscription_id",
    previousQuantity: "previous_quantity",
    createdAt: "created_at",
    prorationUpgradeScheme: "proration_upgrade_scheme",
    prorationDowngradeScheme: "proration_downgrade_scheme",
    pricePointId: "price_point_id",
    pricePointName: "price_point_name",
    pricePointHandle: "price_point_handle",
    intervalUnit: "interval_unit",
    previousPricePointId: "previous_price_point_id",
    accrueCharge: "accrue_charge",
    initiateDunning: "initiate_dunning",
    upgradeCharge: "upgrade_charge",
    downgradeCredit: "downgrade_credit",
    expiresAt: "expires_at",
    usedQuantity: "used_quantity",
    chargeId: "charge_id",
  },
});
