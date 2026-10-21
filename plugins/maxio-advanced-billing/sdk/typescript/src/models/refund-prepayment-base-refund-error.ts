import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { baseRefundErrorSchema, type BaseRefundError } from "./base-refund-error.js";

export type RefundPrepaymentBaseRefundError = {
  refund?: BaseRefundError;
};

export const refundPrepaymentBaseRefundErrorSchema: Schema<RefundPrepaymentBaseRefundError> =
  s.object<RefundPrepaymentBaseRefundError>({
    refund: s.optional(s.lazy(() => baseRefundErrorSchema)),
  });
