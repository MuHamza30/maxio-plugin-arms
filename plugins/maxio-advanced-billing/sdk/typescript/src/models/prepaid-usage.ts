import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  prepaidUsageAllocationDetailSchema,
  type PrepaidUsageAllocationDetail,
} from "./prepaid-usage-allocation-detail.js";
import {
  newOverageUnitBalanceSchema,
  type NewOverageUnitBalance,
} from "./unions/new-overage-unit-balance.js";
import { newUnitBalanceSchema, type NewUnitBalance } from "./unions/new-unit-balance.js";

export type PrepaidUsage = {
  previousUnitBalance: string;
  previousOverageUnitBalance: string;
  newUnitBalance: NewUnitBalance;
  newOverageUnitBalance: NewOverageUnitBalance;
  usageQuantity: number;
  overageUsageQuantity: number;
  componentId: number;
  componentHandle: string;
  memo: string;
  allocationDetails: PrepaidUsageAllocationDetail[];
};

export const prepaidUsageSchema: Schema<PrepaidUsage> = s.object<PrepaidUsage>({
  previousUnitBalance: s.string(),
  previousOverageUnitBalance: s.string(),
  newUnitBalance: newUnitBalanceSchema,
  newOverageUnitBalance: newOverageUnitBalanceSchema,
  usageQuantity: s.int(),
  overageUsageQuantity: s.int(),
  componentId: s.int(),
  componentHandle: s.string(),
  memo: s.string(),
  allocationDetails: s.array(s.lazy(() => prepaidUsageAllocationDetailSchema)),
  _keysMap: {
    previousUnitBalance: "previous_unit_balance",
    previousOverageUnitBalance: "previous_overage_unit_balance",
    newUnitBalance: "new_unit_balance",
    newOverageUnitBalance: "new_overage_unit_balance",
    usageQuantity: "usage_quantity",
    overageUsageQuantity: "overage_usage_quantity",
    componentId: "component_id",
    componentHandle: "component_handle",
    allocationDetails: "allocation_details",
  },
});
