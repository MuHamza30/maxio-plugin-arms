import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { billingScheduleSchema, type BillingSchedule } from "./billing-schedule.js";
import { componentCustomPriceSchema, type ComponentCustomPrice } from "./component-custom-price.js";
import {
  downgradeCreditCreditTypeSchema,
  type DowngradeCreditCreditType,
} from "./downgrade-credit-credit-type.js";
import { pricePointId1Schema, type PricePointId1 } from "./unions/price-point-id1.js";
import { upgradeChargeCreditTypeSchema, type UpgradeChargeCreditType } from "./upgrade-charge-credit-type.js";

export type CreateAllocation = {
  /**
   * The allocated quantity to which to set the line-items allocated quantity. By default, this is
   * an integer. If decimal allocations are enabled for the component, it will be a decimal number.
   * For On/Off components, use 1 for on and 0 for off.
   */
  quantity: number;
  /**
   * Decimal representation of the allocated quantity. Only valid when decimal allocations are
   * enabled for the component.
   */
  decimalQuantity?: string;
  /**
   * The quantity that was in effect before this allocation. Responses always include this value; it
   * may be supplied on preview requests to ensure the expected change is evaluated.
   */
  previousQuantity?: number;
  /**
   * Decimal representation of `previous_quantity`. Only valid when decimal allocations are enabled
   * for the component.
   */
  decimalPreviousQuantity?: string;
  /**
   * (required for the multiple allocations endpoint) The id associated with the component for which
   * the allocation is being made.
   */
  componentId?: number;
  /** A memo to record along with the allocation. */
  memo?: string;
  /**
   * The scheme used if the proration is a downgrade. Defaults to the site setting if one is not
   * provided.
   *
   * @deprecated
   */
  prorationDowngradeScheme?: string;
  /**
   * The scheme used if the proration is an upgrade. Defaults to the site setting if one is not
   * provided.
   *
   * @deprecated
   */
  prorationUpgradeScheme?: string;
  /**
   * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
   * site setting if one is not provided. Values are:
   *
   * `full` - A full price credit is added for the amount owed.
   *
   * `prorated` - A prorated credit is added for the amount owed.
   *
   * `none` - No charge is added.
   */
  downgradeCredit?: DowngradeCreditCreditType | null;
  /**
   * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
   * site setting if one is not provided. Values are:
   *
   * `full` - A charge is added for the full price of the component.
   *
   * `prorated` - A charge is added for the prorated price of the component change.
   *
   * `none` - No charge is added.
   */
  upgradeCharge?: UpgradeChargeCreditType | null;
  /**
   * "If the change in cost is an upgrade, this determines if the charge should accrue to the next
   * renewal or if capture should be attempted immediately.
   *
   * `true` - Attempt to charge the customer at the next renewal.
   *
   * `false` - Attempt to charge the customer right away. If it fails, the charge will be accrued
   * until the next renewal.
   *
   * Defaults to the site setting if unspecified in the request.
   */
  accrueCharge?: boolean;
  /**
   * If set to true, if the immediate component payment fails, initiate dunning for the
   * subscription. Otherwise, leave the charges on the subscription to pay for at renewal. Defaults
   * to false.
   */
  initiateDunning?: boolean;
  /**
   * Price point that the allocation should be charged at. Accepts either the price point's id
   * (integer) or handle (string). When not specified, the default price point will be used.
   */
  pricePointId?: PricePointId1 | null;
  /**
   * Billing schedule settings for component allocations or usages on multi-frequency subscriptions.
   * Use this to start a component's billing period on a custom date instead of aligning with the
   * product charge schedule.
   */
  billingSchedule?: BillingSchedule;
  /**
   * Create or update custom pricing unique to the subscription. Used in place of `price_point_id`.
   */
  customPrice?: ComponentCustomPrice;
};

export const createAllocationSchema: Schema<CreateAllocation> = s.object<CreateAllocation>({
  quantity: s.float64(),
  decimalQuantity: s.optional(s.string()),
  previousQuantity: s.optional(s.float64()),
  decimalPreviousQuantity: s.optional(s.string()),
  componentId: s.optional(s.int()),
  memo: s.optional(s.string()),
  prorationDowngradeScheme: s.optional(s.string()),
  prorationUpgradeScheme: s.optional(s.string()),
  downgradeCredit: s.optionalNullable(s.lazy(() => downgradeCreditCreditTypeSchema)),
  upgradeCharge: s.optionalNullable(s.lazy(() => upgradeChargeCreditTypeSchema)),
  accrueCharge: s.optional(s.boolean()),
  initiateDunning: s.optional(s.boolean()),
  pricePointId: s.optionalNullable(s.lazy(() => pricePointId1Schema)),
  billingSchedule: s.optional(s.lazy(() => billingScheduleSchema)),
  customPrice: s.optional(s.lazy(() => componentCustomPriceSchema)),
  _keysMap: {
    decimalQuantity: "decimal_quantity",
    previousQuantity: "previous_quantity",
    decimalPreviousQuantity: "decimal_previous_quantity",
    componentId: "component_id",
    prorationDowngradeScheme: "proration_downgrade_scheme",
    prorationUpgradeScheme: "proration_upgrade_scheme",
    downgradeCredit: "downgrade_credit",
    upgradeCharge: "upgrade_charge",
    accrueCharge: "accrue_charge",
    initiateDunning: "initiate_dunning",
    pricePointId: "price_point_id",
    billingSchedule: "billing_schedule",
    customPrice: "custom_price",
  },
});
