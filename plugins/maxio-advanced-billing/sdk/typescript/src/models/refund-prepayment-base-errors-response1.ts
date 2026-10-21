import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  refundPrepaymentBaseRefundErrorSchema,
  type RefundPrepaymentBaseRefundError,
} from "./refund-prepayment-base-refund-error.js";

/** Errors returned on creating a refund prepayment when bad request */
export type RefundPrepaymentBaseErrorsResponse1 = {
  errors?: RefundPrepaymentBaseRefundError;
};

export const refundPrepaymentBaseErrorsResponse1Schema: Schema<RefundPrepaymentBaseErrorsResponse1> =
  s.object<RefundPrepaymentBaseErrorsResponse1>({
    errors: s.optional(s.lazy(() => refundPrepaymentBaseRefundErrorSchema)),
  });
