import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../error-list-response1.js";
import {
  errorStringMapResponse1Schema,
  type ErrorStringMapResponse1,
} from "../error-string-map-response1.js";

export type PrepaidConfigurationErrorResponse = ErrorStringMapResponse1 | ErrorListResponse1;

export const prepaidConfigurationErrorResponseSchema: Schema<PrepaidConfigurationErrorResponse> =
  s.of<PrepaidConfigurationErrorResponse>(
    s.union([s.lazy(() => errorStringMapResponse1Schema), s.lazy(() => errorListResponse1Schema)]),
  );
