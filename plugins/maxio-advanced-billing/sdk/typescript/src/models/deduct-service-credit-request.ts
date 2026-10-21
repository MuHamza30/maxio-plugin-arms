import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { deductServiceCreditSchema, type DeductServiceCredit } from "./deduct-service-credit.js";

export type DeductServiceCreditRequest = {
  deduction: DeductServiceCredit;
};

export const deductServiceCreditRequestSchema: Schema<DeductServiceCreditRequest> =
  s.object<DeductServiceCreditRequest>({
    deduction: deductServiceCreditSchema,
  });
