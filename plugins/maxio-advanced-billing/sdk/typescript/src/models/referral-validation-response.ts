import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { referralCodeSchema, type ReferralCode } from "./referral-code.js";

export type ReferralValidationResponse = {
  referralCode?: ReferralCode;
};

export const referralValidationResponseSchema: Schema<ReferralValidationResponse> =
  s.object<ReferralValidationResponse>({
    referralCode: s.optional(s.lazy(() => referralCodeSchema)),
    _keysMap: {
      referralCode: "referral_code",
    },
  });
