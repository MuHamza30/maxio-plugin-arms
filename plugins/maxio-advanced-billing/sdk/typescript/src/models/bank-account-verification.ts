import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type BankAccountVerification = {
  deposit1InCents?: number;
  deposit2InCents?: number;
};

export const bankAccountVerificationSchema: Schema<BankAccountVerification> =
  s.object<BankAccountVerification>({
    deposit1InCents: s.optional(s.int()),
    deposit2InCents: s.optional(s.int()),
    _keysMap: {
      deposit1InCents: "deposit_1_in_cents",
      deposit2InCents: "deposit_2_in_cents",
    },
  });
