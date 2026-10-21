import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createPaymentSchema, type CreatePayment } from "./create-payment.js";

export type RecordPaymentRequest = {
  payment: CreatePayment;
};

export const recordPaymentRequestSchema: Schema<RecordPaymentRequest> = s.object<RecordPaymentRequest>({
  payment: createPaymentSchema,
});
