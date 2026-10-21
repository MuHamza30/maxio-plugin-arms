import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Required when creating a subscription with Maxio Payments. */
export type AgreementAcceptance = {
  /** Required when providing agreement acceptance params. */
  ipAddress?: string;
  /**
   * Required when creating a subscription with Maxio Payments. Either terms_url or
   * privacy_policy_url is required when providing agreement_acceptance params.
   */
  termsUrl?: string;
  privacyPolicyUrl?: string;
  returnRefundPolicyUrl?: string;
  deliveryPolicyUrl?: string;
  secureCheckoutPolicyUrl?: string;
};

export const agreementAcceptanceSchema: Schema<AgreementAcceptance> = s.object<AgreementAcceptance>({
  ipAddress: s.optional(s.string()),
  termsUrl: s.optional(s.string()),
  privacyPolicyUrl: s.optional(s.string()),
  returnRefundPolicyUrl: s.optional(s.string()),
  deliveryPolicyUrl: s.optional(s.string()),
  secureCheckoutPolicyUrl: s.optional(s.string()),
  _keysMap: {
    ipAddress: "ip_address",
    termsUrl: "terms_url",
    privacyPolicyUrl: "privacy_policy_url",
    returnRefundPolicyUrl: "return_refund_policy_url",
    deliveryPolicyUrl: "delivery_policy_url",
    secureCheckoutPolicyUrl: "secure_checkout_policy_url",
  },
});
