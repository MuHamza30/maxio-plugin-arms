import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CancelGroupedSubscriptionsRequest = {
  chargeUnbilledUsage?: boolean;
};

export const cancelGroupedSubscriptionsRequestSchema: Schema<CancelGroupedSubscriptionsRequest> =
  s.object<CancelGroupedSubscriptionsRequest>({
    chargeUnbilledUsage: s.optional(s.boolean()),
    _keysMap: {
      chargeUnbilledUsage: "charge_unbilled_usage",
    },
  });
