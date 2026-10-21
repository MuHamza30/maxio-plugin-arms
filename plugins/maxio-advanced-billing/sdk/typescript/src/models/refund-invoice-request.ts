import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { refundSchema, type Refund } from "./unions/refund.js";

export type RefundInvoiceRequest = {
  refund: Refund;
};

export const refundInvoiceRequestSchema: Schema<RefundInvoiceRequest> = s.object<RefundInvoiceRequest>({
  refund: refundSchema,
});
