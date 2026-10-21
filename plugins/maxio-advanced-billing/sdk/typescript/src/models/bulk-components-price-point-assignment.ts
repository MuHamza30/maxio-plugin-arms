import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  componentPricePointAssignmentSchema,
  type ComponentPricePointAssignment,
} from "./component-price-point-assignment.js";

export type BulkComponentsPricePointAssignment = {
  components?: ComponentPricePointAssignment[];
};

export const bulkComponentsPricePointAssignmentSchema: Schema<BulkComponentsPricePointAssignment> =
  s.object<BulkComponentsPricePointAssignment>({
    components: s.optional(s.array(s.lazy(() => componentPricePointAssignmentSchema))),
  });
