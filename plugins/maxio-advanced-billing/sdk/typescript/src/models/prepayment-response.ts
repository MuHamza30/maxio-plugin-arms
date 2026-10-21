import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { prepaymentSchema, type Prepayment } from "./prepayment.js";

export type PrepaymentResponse = {
  prepayment: Prepayment;
};

export const prepaymentResponseSchema: Schema<PrepaymentResponse> = s.object<PrepaymentResponse>({
  prepayment: prepaymentSchema,
});
