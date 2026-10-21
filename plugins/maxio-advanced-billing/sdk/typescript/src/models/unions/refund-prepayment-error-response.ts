import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import {
  errorStringMapResponse1Schema,
  type ErrorStringMapResponse1,
} from "../error-string-map-response1.js";
import {
  refundPrepaymentAggregatedErrorsResponseSchema,
  type RefundPrepaymentAggregatedErrorsResponse,
} from "../refund-prepayment-aggregated-errors-response.js";

export type RefundPrepaymentErrorResponse =
  | RefundPrepaymentAggregatedErrorsResponse
  | ErrorStringMapResponse1;

export const refundPrepaymentErrorResponseSchema: Schema<RefundPrepaymentErrorResponse> =
  s.of<RefundPrepaymentErrorResponse>(
    s.union([
      s.lazy(() => refundPrepaymentAggregatedErrorsResponseSchema),
      s.lazy(() => errorStringMapResponse1Schema),
    ]),
  );
