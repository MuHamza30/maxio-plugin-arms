import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ResumeOptions = {
  /**
   * Chargify will only attempt to resume the subscription's billing period. If not resumable, the
   * subscription will be left in its current state.
   */
  requireResume?: boolean;
  /**
   * Indicates whether or not Chargify should clear the subscription's existing balance before
   * attempting to resume the subscription. If subscription cannot be resumed, the balance will
   * remain as it was before the attempt to resume was made.
   */
  forgiveBalance?: boolean;
};

export const resumeOptionsSchema: Schema<ResumeOptions> = s.object<ResumeOptions>({
  requireResume: s.optional(s.boolean()),
  forgiveBalance: s.optional(s.boolean()),
  _keysMap: {
    requireResume: "require_resume",
    forgiveBalance: "forgive_balance",
  },
});
