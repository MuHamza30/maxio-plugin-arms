import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionMigrationPreview = {
  /** The amount of the prorated adjustment that would be issued for the current subscription. */
  proratedAdjustmentInCents?: number;
  /** The amount of the charge that would be created for the new product. */
  chargeInCents?: number;
  /** The amount of the payment due in the case of an upgrade. */
  paymentDueInCents?: number;
  /**
   * Represents a credit in cents that is applied to your subscription as part of a migration
   * process for a specific product, which reduces the amount owed for the subscription.
   */
  creditAppliedInCents?: number;
};

export const subscriptionMigrationPreviewSchema: Schema<SubscriptionMigrationPreview> =
  s.object<SubscriptionMigrationPreview>({
    proratedAdjustmentInCents: s.optional(s.int()),
    chargeInCents: s.optional(s.int()),
    paymentDueInCents: s.optional(s.int()),
    creditAppliedInCents: s.optional(s.int()),
    _keysMap: {
      proratedAdjustmentInCents: "prorated_adjustment_in_cents",
      chargeInCents: "charge_in_cents",
      paymentDueInCents: "payment_due_in_cents",
      creditAppliedInCents: "credit_applied_in_cents",
    },
  });
