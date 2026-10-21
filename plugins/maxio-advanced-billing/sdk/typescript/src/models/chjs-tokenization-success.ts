import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { tokenizedPaymentProfileSchema, type TokenizedPaymentProfile } from "./tokenized-payment-profile.js";

export type ChjsTokenizationSuccess = {
  paymentProfile: TokenizedPaymentProfile;
  gatewayCustomerId?: number | null;
};

export const chjsTokenizationSuccessSchema: Schema<ChjsTokenizationSuccess> =
  s.object<ChjsTokenizationSuccess>({
    paymentProfile: tokenizedPaymentProfileSchema,
    gatewayCustomerId: s.optionalNullable(s.int()),
    _keysMap: {
      paymentProfile: "payment_profile",
      gatewayCustomerId: "gateway_customer_id",
    },
  });
