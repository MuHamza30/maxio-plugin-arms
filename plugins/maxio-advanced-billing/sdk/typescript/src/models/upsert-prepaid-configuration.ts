import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type UpsertPrepaidConfiguration = {
  initialFundingAmountInCents?: number;
  replenishToAmountInCents?: number;
  autoReplenish?: boolean;
  replenishThresholdAmountInCents?: number;
};

export const upsertPrepaidConfigurationSchema: Schema<UpsertPrepaidConfiguration> =
  s.object<UpsertPrepaidConfiguration>({
    initialFundingAmountInCents: s.optional(s.int()),
    replenishToAmountInCents: s.optional(s.int()),
    autoReplenish: s.optional(s.boolean()),
    replenishThresholdAmountInCents: s.optional(s.int()),
    _keysMap: {
      initialFundingAmountInCents: "initial_funding_amount_in_cents",
      replenishToAmountInCents: "replenish_to_amount_in_cents",
      autoReplenish: "auto_replenish",
      replenishThresholdAmountInCents: "replenish_threshold_amount_in_cents",
    },
  });
