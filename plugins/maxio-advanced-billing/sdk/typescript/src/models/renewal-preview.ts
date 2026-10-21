import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { renewalPreviewLineItemSchema, type RenewalPreviewLineItem } from "./renewal-preview-line-item.js";

export type RenewalPreview = {
  /** The timestamp for the subscription’s next renewal */
  nextAssessmentAt?: Date;
  /**
   * An integer representing the amount of the total pre-tax, pre-discount charges that will be
   * assessed at the next renewal
   */
  subtotalInCents?: number;
  /** An integer representing the total tax charges that will be assessed at the next renewal */
  totalTaxInCents?: number;
  /**
   * An integer representing the amount of the coupon discounts that will be applied to the next
   * renewal
   */
  totalDiscountInCents?: number;
  /**
   * An integer representing the total amount owed, less any discounts, that will be assessed at the
   * next renewal
   */
  totalInCents?: number;
  /** An integer representing the amount of the subscription’s current balance */
  existingBalanceInCents?: number;
  /** An integer representing the existing_balance_in_cents plus the total_in_cents */
  totalAmountDueInCents?: number;
  /**
   * A boolean indicating whether or not additional taxes will be calculated at the time of renewal.
   * This will be true if you are using Avalara and the address of the subscription is in one of
   * your defined taxable regions.
   */
  uncalculatedTaxes?: boolean;
  /**
   * An array of objects representing the individual transactions that will be created at the next
   * renewal
   */
  lineItems?: RenewalPreviewLineItem[];
};

export const renewalPreviewSchema: Schema<RenewalPreview> = s.object<RenewalPreview>({
  nextAssessmentAt: s.optional(s.dateTime()),
  subtotalInCents: s.optional(s.int()),
  totalTaxInCents: s.optional(s.int()),
  totalDiscountInCents: s.optional(s.int()),
  totalInCents: s.optional(s.int()),
  existingBalanceInCents: s.optional(s.int()),
  totalAmountDueInCents: s.optional(s.int()),
  uncalculatedTaxes: s.optional(s.boolean()),
  lineItems: s.optional(s.array(s.lazy(() => renewalPreviewLineItemSchema))),
  _keysMap: {
    nextAssessmentAt: "next_assessment_at",
    subtotalInCents: "subtotal_in_cents",
    totalTaxInCents: "total_tax_in_cents",
    totalDiscountInCents: "total_discount_in_cents",
    totalInCents: "total_in_cents",
    existingBalanceInCents: "existing_balance_in_cents",
    totalAmountDueInCents: "total_amount_due_in_cents",
    uncalculatedTaxes: "uncalculated_taxes",
    lineItems: "line_items",
  },
});
