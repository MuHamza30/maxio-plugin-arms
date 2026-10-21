import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { amount3Schema, type Amount3 } from "./unions/amount3.js";

export type IssueServiceCredit = {
  amount: Amount3;
  memo?: string;
};

export const issueServiceCreditSchema: Schema<IssueServiceCredit> = s.object<IssueServiceCredit>({
  amount: amount3Schema,
  memo: s.optional(s.string()),
});
