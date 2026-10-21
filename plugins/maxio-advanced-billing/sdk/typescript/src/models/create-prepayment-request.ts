import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createPrepaymentSchema, type CreatePrepayment } from "./create-prepayment.js";

export type CreatePrepaymentRequest = {
  prepayment: CreatePrepayment;
};

export const createPrepaymentRequestSchema: Schema<CreatePrepaymentRequest> =
  s.object<CreatePrepaymentRequest>({
    prepayment: createPrepaymentSchema,
  });
