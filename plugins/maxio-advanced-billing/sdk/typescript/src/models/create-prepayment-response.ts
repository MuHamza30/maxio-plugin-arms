import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createdPrepaymentSchema, type CreatedPrepayment } from "./created-prepayment.js";

export type CreatePrepaymentResponse = {
  prepayment: CreatedPrepayment;
};

export const createPrepaymentResponseSchema: Schema<CreatePrepaymentResponse> =
  s.object<CreatePrepaymentResponse>({
    prepayment: createdPrepaymentSchema,
  });
