import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreditNoteLineItem = {
  /**
   * Unique identifier for the line item. Useful when cross-referencing the line against individual
   * discounts in the `discounts` or `taxes` lists.
   */
  uid?: string;
  /** A short descriptor for the credit given by this line. */
  title?: string;
  /**
   * Detailed description for the credit given by this line. May include proration details in plain
   * text.
   *
   * Note: this string may contain line breaks that are hints for the best display format on the
   * credit note.
   */
  description?: string;
  /**
   * The quantity or count of units credited by the line item.
   *
   * This is a decimal number represented as a string. (See "About Decimal Numbers".)
   */
  quantity?: string;
  /**
   * The price per unit for the line item.
   *
   * When tiered pricing was used (i.e., not every unit was actually priced at the same price) this
   * will be the blended average cost per unit and the `tiered_unit_price` field will be set to
   * `true`.
   */
  unitPrice?: string;
  /**
   * The line subtotal, generally calculated as `quantity * unit_price`. This is the canonical
   * amount of record for the line - when rounding differences are in play, `subtotal_amount` takes
   * precedence over the value derived from `quantity * unit_price` (which may not have the proper
   * precision to exactly equal this amount).
   */
  subtotalAmount?: string;
  /**
   * The approximate discount of just this line.
   *
   * The value is approximated in cases where rounding errors make it difficult to apportion exactly
   * a total discount among many lines. Several lines may have been summed prior to applying the
   * discount to arrive at `discount_amount` for the invoice - backing that out to the discount on a
   * single line may introduce rounding or precision errors.
   */
  discountAmount?: string;
  /**
   * The approximate tax of just this line.
   *
   * The value is approximated in cases where rounding errors make it difficult to apportion exactly
   * a total tax among many lines. Several lines may have been summed prior to applying the tax rate
   * to arrive at `tax_amount` for the invoice - backing that out to the tax on a single line may
   * introduce rounding or precision errors.
   */
  taxAmount?: string;
  /**
   * Whether the unit price for this line item is tax-inclusive.
   *
   * When `true`, `unit_price` already includes tax and `tax_amount` represents the portion of the
   * price attributable to tax. When `false`, any applicable tax is added on top of the price.
   *
   * The value is inherited from the source price point's `tax_included` setting. Custom or ad-hoc
   * line items (which have no associated price point) always return `false`.
   */
  taxIncluded?: boolean;
  /**
   * The non-canonical total amount for the line.
   *
   * `subtotal_amount` is the canonical amount for a line. The invoice `total_amount` is derived
   * from the sum of the line `subtotal_amount`s and discounts or taxes applied thereafter.
   * Therefore, due to rounding or precision errors, the sum of line `total_amount`s may not equal
   * the invoice `total_amount`.
   */
  totalAmount?: string;
  /**
   * When `true`, indicates that the actual pricing scheme for the line was tiered, so the
   * `unit_price` shown is the blended average for all units.
   */
  tieredUnitPrice?: boolean;
  /** Start date for the period credited by this line. The format is `"YYYY-MM-DD"`. */
  periodRangeStart?: string;
  /** End date for the period credited by this line. The format is `"YYYY-MM-DD"`. */
  periodRangeEnd?: string;
  /**
   * The ID of the product being credited.
   *
   * This may be set even for component credits, so true product-only (non-component) credits will
   * also have a nil `component_id`.
   */
  productId?: number;
  /** The version of the product being credited. */
  productVersion?: number;
  /** The ID of the component being credited. Will be `nil` for non-component credits. */
  componentId?: number | null;
  /**
   * The price point ID of the component being credited. Will be `nil` for non-component credits.
   */
  pricePointId?: number | null;
  billingScheduleItemId?: number | null;
  customItem?: boolean;
  /**
   * The date a prepaid allocation is set to expire. Only present on line items representing prepaid
   * component allocations. The format is `"YYYY-MM-DD"`.
   */
  prepaidAllocationExpiresAt?: string | null;
};

export const creditNoteLineItemSchema: Schema<CreditNoteLineItem> = s.object<CreditNoteLineItem>({
  uid: s.optional(s.string()),
  title: s.optional(s.string()),
  description: s.optional(s.string()),
  quantity: s.optional(s.string()),
  unitPrice: s.optional(s.string()),
  subtotalAmount: s.optional(s.string()),
  discountAmount: s.optional(s.string()),
  taxAmount: s.optional(s.string()),
  taxIncluded: s.optional(s.boolean()),
  totalAmount: s.optional(s.string()),
  tieredUnitPrice: s.optional(s.boolean()),
  periodRangeStart: s.optional(s.dateOnly()),
  periodRangeEnd: s.optional(s.dateOnly()),
  productId: s.optional(s.int()),
  productVersion: s.optional(s.int()),
  componentId: s.optionalNullable(s.int()),
  pricePointId: s.optionalNullable(s.int()),
  billingScheduleItemId: s.optionalNullable(s.int()),
  customItem: s.optional(s.boolean()),
  prepaidAllocationExpiresAt: s.optionalNullable(s.dateOnly()),
  _keysMap: {
    unitPrice: "unit_price",
    subtotalAmount: "subtotal_amount",
    discountAmount: "discount_amount",
    taxAmount: "tax_amount",
    taxIncluded: "tax_included",
    totalAmount: "total_amount",
    tieredUnitPrice: "tiered_unit_price",
    periodRangeStart: "period_range_start",
    periodRangeEnd: "period_range_end",
    productId: "product_id",
    productVersion: "product_version",
    componentId: "component_id",
    pricePointId: "price_point_id",
    billingScheduleItemId: "billing_schedule_item_id",
    customItem: "custom_item",
    prepaidAllocationExpiresAt: "prepaid_allocation_expires_at",
  },
});
