import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** (Optional) If passed, the proof of the authorized ACH agreement terms will be persisted. */
export type AchAgreement = {
  /** (Required when providing ACH agreement params) The ACH authorization agreement terms. */
  agreementTerms?: string;
  /**
   * (Required when providing ACH agreement params) The first name of the person authorizing the ACH
   * agreement.
   */
  authorizerFirstName?: string;
  /**
   * (Required when providing ACH agreement params) The last name of the person authorizing the ACH
   * agreement.
   */
  authorizerLastName?: string;
  /**
   * (Required when providing ACH agreement params) The IP address of the person authorizing the ACH
   * agreement.
   */
  ipAddress?: string;
};

export const achAgreementSchema: Schema<AchAgreement> = s.object<AchAgreement>({
  agreementTerms: s.optional(s.string()),
  authorizerFirstName: s.optional(s.string()),
  authorizerLastName: s.optional(s.string()),
  ipAddress: s.optional(s.string()),
  _keysMap: {
    agreementTerms: "agreement_terms",
    authorizerFirstName: "authorizer_first_name",
    authorizerLastName: "authorizer_last_name",
    ipAddress: "ip_address",
  },
});
