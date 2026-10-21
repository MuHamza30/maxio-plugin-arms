import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ActivateSubscriptionRequest = {
  /**
   * You may choose how to handle the activation failure. `true` means do not change the
   * subscription’s state and billing period. `false` means to continue through with the activation
   * and enter an end-of-life state. If this parameter is omitted or `null` is passed it will
   * default to the value set in the site settings (default: `true`).
   */
  revertOnFailure?: boolean | null;
};

export const activateSubscriptionRequestSchema: Schema<ActivateSubscriptionRequest> =
  s.object<ActivateSubscriptionRequest>({
    revertOnFailure: s.optionalNullable(s.boolean()),
    _keysMap: {
      revertOnFailure: "revert_on_failure",
    },
  });
