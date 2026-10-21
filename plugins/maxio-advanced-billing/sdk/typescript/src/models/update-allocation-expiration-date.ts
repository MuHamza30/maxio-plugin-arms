import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  allocationExpirationDateSchema,
  type AllocationExpirationDate,
} from "./allocation-expiration-date.js";

export type UpdateAllocationExpirationDate = {
  allocation?: AllocationExpirationDate;
};

export const updateAllocationExpirationDateSchema: Schema<UpdateAllocationExpirationDate> =
  s.object<UpdateAllocationExpirationDate>({
    allocation: s.optional(s.lazy(() => allocationExpirationDateSchema)),
  });
