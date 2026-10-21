import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  prepaymentAggregatedErrorSchema,
  type PrepaymentAggregatedError,
} from "./prepayment-aggregated-error.js";

export type RefundPrepaymentAggregatedError = {
  refund?: PrepaymentAggregatedError;
};

export const refundPrepaymentAggregatedErrorSchema: Schema<RefundPrepaymentAggregatedError> =
  s.object<RefundPrepaymentAggregatedError>({
    refund: s.optional(s.lazy(() => prepaymentAggregatedErrorSchema)),
  });
