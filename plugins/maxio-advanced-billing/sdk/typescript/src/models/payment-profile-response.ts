import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { paymentProfileSchema, type PaymentProfile } from "./unions/payment-profile.js";

export type PaymentProfileResponse = {
  paymentProfile: PaymentProfile;
};

export const paymentProfileResponseSchema: Schema<PaymentProfileResponse> = s.object<PaymentProfileResponse>({
  paymentProfile: paymentProfileSchema,
  _keysMap: {
    paymentProfile: "payment_profile",
  },
});
