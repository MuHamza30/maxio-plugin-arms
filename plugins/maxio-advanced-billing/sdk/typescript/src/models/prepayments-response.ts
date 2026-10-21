import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { prepaymentSchema, type Prepayment } from "./prepayment.js";

export type PrepaymentsResponse = {
  prepayments?: Prepayment[];
};

export const prepaymentsResponseSchema: Schema<PrepaymentsResponse> = s.object<PrepaymentsResponse>({
  prepayments: s.optional(s.array(s.lazy(() => prepaymentSchema))),
});
