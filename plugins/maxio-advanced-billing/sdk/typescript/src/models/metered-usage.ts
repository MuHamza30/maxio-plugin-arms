import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { newUnitBalanceSchema, type NewUnitBalance } from "./unions/new-unit-balance.js";

export type MeteredUsage = {
  previousUnitBalance: string;
  newUnitBalance: NewUnitBalance;
  usageQuantity: number;
  componentId: number;
  componentHandle: string;
  memo: string;
};

export const meteredUsageSchema: Schema<MeteredUsage> = s.object<MeteredUsage>({
  previousUnitBalance: s.string(),
  newUnitBalance: newUnitBalanceSchema,
  usageQuantity: s.int(),
  componentId: s.int(),
  componentHandle: s.string(),
  memo: s.string(),
  _keysMap: {
    previousUnitBalance: "previous_unit_balance",
    newUnitBalance: "new_unit_balance",
    usageQuantity: "usage_quantity",
    componentId: "component_id",
    componentHandle: "component_handle",
  },
});
