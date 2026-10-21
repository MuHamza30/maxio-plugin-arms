import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { baseStringErrorSchema, type BaseStringError } from "./base-string-error.js";

export type ProformaError = {
  /** The error is base if it is not directly associated with a single attribute. */
  subscription?: BaseStringError;
};

export const proformaErrorSchema: Schema<ProformaError> = s.object<ProformaError>({
  subscription: s.optional(s.lazy(() => baseStringErrorSchema)),
});
