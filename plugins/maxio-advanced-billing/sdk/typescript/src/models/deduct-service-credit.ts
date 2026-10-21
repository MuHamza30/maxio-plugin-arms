import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { amount2Schema, type Amount2 } from "./unions/amount2.js";

export type DeductServiceCredit = {
  amount: Amount2;
  memo?: string;
};

export const deductServiceCreditSchema: Schema<DeductServiceCredit> = s.object<DeductServiceCredit>({
  amount: amount2Schema,
  memo: s.optional(s.string()),
});
