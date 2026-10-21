import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentCostDataSchema, type ComponentCostData } from "./component-cost-data.js";

export type InvoiceLineItemComponentCostData = {
  rates?: ComponentCostData[];
};

export const invoiceLineItemComponentCostDataSchema: Schema<InvoiceLineItemComponentCostData> =
  s.object<InvoiceLineItemComponentCostData>({
    rates: s.optional(s.array(s.lazy(() => componentCostDataSchema))),
  });
