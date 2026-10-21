import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createAllocationSchema, type CreateAllocation } from "./create-allocation.js";

export type CreateAllocationRequest = {
  allocation: CreateAllocation;
};

export const createAllocationRequestSchema: Schema<CreateAllocationRequest> =
  s.object<CreateAllocationRequest>({
    allocation: createAllocationSchema,
  });
