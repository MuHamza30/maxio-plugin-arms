import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { collectionMethodSchema, type CollectionMethod } from "./collection-method.js";
import { createAllocationSchema, type CreateAllocation } from "./create-allocation.js";
import { creditTypeSchema, type CreditType } from "./credit-type.js";

export type AllocateComponents = {
  /**
   * @deprecated
   */
  prorationUpgradeScheme?: string;
  /**
   * @deprecated
   */
  prorationDowngradeScheme?: string;
  allocations?: CreateAllocation[];
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
  /**
   * (Optional) If not passed, the allocation(s) will use the payment collection method on the
   * subscription.
   */
  paymentCollectionMethod?: CollectionMethod;
  /**
   * If true, if the immediate component payment fails, initiate dunning for the subscription.
   * Otherwise, leave the charges on the subscription to pay for at renewal.
   */
  initiateDunning?: boolean;
};

export const allocateComponentsSchema: Schema<AllocateComponents> = s.object<AllocateComponents>({
  prorationUpgradeScheme: s.optional(s.string()),
  prorationDowngradeScheme: s.optional(s.string()),
  allocations: s.optional(s.array(s.lazy(() => createAllocationSchema))),
  accrueCharge: s.optional(s.boolean()),
  upgradeCharge: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  downgradeCredit: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  paymentCollectionMethod: s.optional(s.lazy(() => collectionMethodSchema)),
  initiateDunning: s.optional(s.boolean()),
  _keysMap: {
    prorationUpgradeScheme: "proration_upgrade_scheme",
    prorationDowngradeScheme: "proration_downgrade_scheme",
    accrueCharge: "accrue_charge",
    upgradeCharge: "upgrade_charge",
    downgradeCredit: "downgrade_credit",
    paymentCollectionMethod: "payment_collection_method",
    initiateDunning: "initiate_dunning",
  },
});
