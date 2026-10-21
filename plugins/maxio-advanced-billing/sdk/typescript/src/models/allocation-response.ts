import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { allocationSchema, type Allocation } from "./allocation.js";

export type AllocationResponse = {
  allocation?: Allocation;
};

export const allocationResponseSchema: Schema<AllocationResponse> = s.object<AllocationResponse>({
  allocation: s.optional(s.lazy(() => allocationSchema)),
});
