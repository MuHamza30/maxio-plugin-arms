import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { paymentProfileModelSchema, type PaymentProfileModel } from "./unions/payment-profile-model.js";

export type GetOneTimeTokenRequest = {
  paymentProfile: PaymentProfileModel;
};

export const getOneTimeTokenRequestSchema: Schema<GetOneTimeTokenRequest> = s.object<GetOneTimeTokenRequest>({
  paymentProfile: paymentProfileModelSchema,
  _keysMap: {
    paymentProfile: "payment_profile",
  },
});
