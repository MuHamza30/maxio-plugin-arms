import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  componentAllocationErrorItemSchema,
  type ComponentAllocationErrorItem,
} from "./component-allocation-error-item.js";

export type ComponentAllocationError1 = {
  errors?: ComponentAllocationErrorItem[];
};

export const componentAllocationError1Schema: Schema<ComponentAllocationError1> =
  s.object<ComponentAllocationError1>({
    errors: s.optional(s.array(s.lazy(() => componentAllocationErrorItemSchema))),
  });
