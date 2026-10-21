import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { customerChangeSchema, type CustomerChange } from "./customer-change.js";

export type CustomerChangesPreviewResponse = {
  changes: CustomerChange;
};

export const customerChangesPreviewResponseSchema: Schema<CustomerChangesPreviewResponse> =
  s.object<CustomerChangesPreviewResponse>({
    changes: customerChangeSchema,
  });
