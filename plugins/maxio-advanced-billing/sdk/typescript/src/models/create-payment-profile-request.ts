import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createPaymentProfileSchema, type CreatePaymentProfile } from "./create-payment-profile.js";

export type CreatePaymentProfileRequest = {
  paymentProfile: CreatePaymentProfile;
};

export const createPaymentProfileRequestSchema: Schema<CreatePaymentProfileRequest> =
  s.object<CreatePaymentProfileRequest>({
    paymentProfile: createPaymentProfileSchema,
    _keysMap: {
      paymentProfile: "payment_profile",
    },
  });
