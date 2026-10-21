import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { issueServiceCreditSchema, type IssueServiceCredit } from "./issue-service-credit.js";

export type IssueServiceCreditRequest = {
  serviceCredit: IssueServiceCredit;
};

export const issueServiceCreditRequestSchema: Schema<IssueServiceCreditRequest> =
  s.object<IssueServiceCreditRequest>({
    serviceCredit: issueServiceCreditSchema,
    _keysMap: {
      serviceCredit: "service_credit",
    },
  });
