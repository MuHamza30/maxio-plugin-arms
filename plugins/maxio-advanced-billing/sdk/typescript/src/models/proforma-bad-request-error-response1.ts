import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { proformaErrorSchema, type ProformaError } from "./proforma-error.js";

export type ProformaBadRequestErrorResponse1 = {
  errors?: ProformaError;
};

export const proformaBadRequestErrorResponse1Schema: Schema<ProformaBadRequestErrorResponse1> =
  s.object<ProformaBadRequestErrorResponse1>({
    errors: s.optional(s.lazy(() => proformaErrorSchema)),
  });
