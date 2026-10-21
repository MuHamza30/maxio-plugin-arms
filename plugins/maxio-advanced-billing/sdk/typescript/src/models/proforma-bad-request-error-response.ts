import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { proformaErrorSchema, type ProformaError } from "./proforma-error.js";

export type ProformaBadRequestErrorResponse = {
  errors?: ProformaError;
};

export const proformaBadRequestErrorResponseSchema: Schema<ProformaBadRequestErrorResponse> =
  s.object<ProformaBadRequestErrorResponse>({
    errors: s.optional(s.lazy(() => proformaErrorSchema)),
  });
