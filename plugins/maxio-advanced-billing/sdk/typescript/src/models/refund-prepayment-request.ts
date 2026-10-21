import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { refundPrepaymentSchema, type RefundPrepayment } from "./refund-prepayment.js";

export type RefundPrepaymentRequest = {
  refund: RefundPrepayment;
};

export const refundPrepaymentRequestSchema: Schema<RefundPrepaymentRequest> =
  s.object<RefundPrepaymentRequest>({
    refund: refundPrepaymentSchema,
  });
