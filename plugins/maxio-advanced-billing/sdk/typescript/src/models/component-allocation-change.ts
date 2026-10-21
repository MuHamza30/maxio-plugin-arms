import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { allocatedQuantitySchema, type AllocatedQuantity } from "./unions/allocated-quantity.js";

export type ComponentAllocationChange = {
  previousAllocation: number;
  newAllocation: number;
  componentId: number;
  componentHandle: string;
  memo: string;
  allocationId: number;
  allocatedQuantity?: AllocatedQuantity;
};

export const componentAllocationChangeSchema: Schema<ComponentAllocationChange> =
  s.object<ComponentAllocationChange>({
    previousAllocation: s.int(),
    newAllocation: s.int(),
    componentId: s.int(),
    componentHandle: s.string(),
    memo: s.string(),
    allocationId: s.int(),
    allocatedQuantity: s.optional(s.lazy(() => allocatedQuantitySchema)),
    _keysMap: {
      previousAllocation: "previous_allocation",
      newAllocation: "new_allocation",
      componentId: "component_id",
      componentHandle: "component_handle",
      allocationId: "allocation_id",
      allocatedQuantity: "allocated_quantity",
    },
  });
