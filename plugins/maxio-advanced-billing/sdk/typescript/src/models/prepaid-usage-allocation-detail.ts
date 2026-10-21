import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PrepaidUsageAllocationDetail = {
  allocationId?: number;
  chargeId?: number;
  usageQuantity?: number;
};

export const prepaidUsageAllocationDetailSchema: Schema<PrepaidUsageAllocationDetail> =
  s.object<PrepaidUsageAllocationDetail>({
    allocationId: s.optional(s.int()),
    chargeId: s.optional(s.int()),
    usageQuantity: s.optional(s.int()),
    _keysMap: {
      allocationId: "allocation_id",
      chargeId: "charge_id",
      usageQuantity: "usage_quantity",
    },
  });
