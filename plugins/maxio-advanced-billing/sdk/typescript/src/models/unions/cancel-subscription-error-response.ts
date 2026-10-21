import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../error-list-response1.js";
import { singleErrorResponse1Schema, type SingleErrorResponse1 } from "../single-error-response1.js";

export type CancelSubscriptionErrorResponse = ErrorListResponse1 | SingleErrorResponse1;

export const cancelSubscriptionErrorResponseSchema: Schema<CancelSubscriptionErrorResponse> =
  s.of<CancelSubscriptionErrorResponse>(
    s.union([s.lazy(() => errorListResponse1Schema), s.lazy(() => singleErrorResponse1Schema)]),
  );
