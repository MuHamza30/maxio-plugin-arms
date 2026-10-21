import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type IssueAdvanceInvoiceRequest = {
  force?: boolean;
};

export const issueAdvanceInvoiceRequestSchema: Schema<IssueAdvanceInvoiceRequest> =
  s.object<IssueAdvanceInvoiceRequest>({
    force: s.optional(s.boolean()),
  });
