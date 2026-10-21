import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../error-list-response1.js";
import {
  errorStringMapResponse1Schema,
  type ErrorStringMapResponse1,
} from "../error-string-map-response1.js";

export type IssueServiceCreditErrorResponse = ErrorListResponse1 | ErrorStringMapResponse1;

export const issueServiceCreditErrorResponseSchema: Schema<IssueServiceCreditErrorResponse> =
  s.of<IssueServiceCreditErrorResponse>(
    s.union([s.lazy(() => errorListResponse1Schema), s.lazy(() => errorStringMapResponse1Schema)]),
  );
