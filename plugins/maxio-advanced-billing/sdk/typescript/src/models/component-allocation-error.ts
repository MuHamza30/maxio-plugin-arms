import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  componentAllocationErrorItemSchema,
  type ComponentAllocationErrorItem,
} from "./component-allocation-error-item.js";

export type ComponentAllocationError = {
  errors?: ComponentAllocationErrorItem[];
};

export const componentAllocationErrorSchema: Schema<ComponentAllocationError> =
  s.object<ComponentAllocationError>({
    errors: s.optional(s.array(s.lazy(() => componentAllocationErrorItemSchema))),
  });
