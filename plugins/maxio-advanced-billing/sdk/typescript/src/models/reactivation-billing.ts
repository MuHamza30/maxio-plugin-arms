import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { ReactivationCharge, reactivationChargeSchema } from "./reactivation-charge.js";

/** These values are only applicable to subscriptions using calendar billing. */
export type ReactivationBilling = {
  /**
   * You may choose how to handle the reactivation charge for that subscription: 1) `prorated` A
   * prorated charge for the product price will be attempted to complete the period 2) `immediate` A
   * full-price charge for the product price will be attempted immediately 3) `delayed` A full-price
   * charge for the product price will be attempted at the next renewal.
   *
   * @default ReactivationCharge.Prorated
   */
  reactivationCharge?: ReactivationCharge;
};

export const reactivationBillingSchema: Schema<ReactivationBilling> = s.object<ReactivationBilling>({
  reactivationCharge: s.defaulted(reactivationChargeSchema, ReactivationCharge.Prorated),
  _keysMap: {
    reactivationCharge: "reactivation_charge",
  },
});
