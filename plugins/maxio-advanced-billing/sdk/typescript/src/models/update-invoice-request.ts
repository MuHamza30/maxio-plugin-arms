import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateInvoiceSchema, type UpdateInvoice } from "./update-invoice.js";

/** Request payload for updating a draft ad hoc invoice. */
export type UpdateInvoiceRequest = {
  /**
   * Attributes of a draft ad hoc invoice which can be updated. Only the submitted attributes are
   * changed.
   */
  invoice: UpdateInvoice;
};

export const updateInvoiceRequestSchema: Schema<UpdateInvoiceRequest> = s.object<UpdateInvoiceRequest>({
  invoice: updateInvoiceSchema,
});
