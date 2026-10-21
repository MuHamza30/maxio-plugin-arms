import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * Indicates how a trial is handled when the trial period ends and there is no credit card on file.
 * For `no_obligation`, the subscription transitions to a Trial Ended state. Maxio will not send any
 * emails or statements. For `payment_expected`, the subscription transitions to a Past Due state.
 * Maxio will send normal dunning emails and statements according to your other settings.
 */
export const TrialType = {
  NoObligation: "no_obligation",
  PaymentExpected: "payment_expected",
} as const;
export type TrialType = (typeof TrialType)[keyof typeof TrialType] | (string & {});

export const trialTypeSchema: EnumSchema<TrialType> = s.enumOf<TrialType>(TrialType);
