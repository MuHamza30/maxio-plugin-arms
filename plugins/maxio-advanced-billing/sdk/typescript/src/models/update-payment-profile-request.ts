import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updatePaymentProfileSchema, type UpdatePaymentProfile } from "./update-payment-profile.js";

export type UpdatePaymentProfileRequest = {
  paymentProfile: UpdatePaymentProfile;
};

export const updatePaymentProfileRequestSchema: Schema<UpdatePaymentProfileRequest> =
  s.object<UpdatePaymentProfileRequest>({
    paymentProfile: updatePaymentProfileSchema,
    _keysMap: {
      paymentProfile: "payment_profile",
    },
  });
