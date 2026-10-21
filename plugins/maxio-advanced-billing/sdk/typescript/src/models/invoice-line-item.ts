import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceLineItemComponentCostDataSchema,
  type InvoiceLineItemComponentCostData,
} from "./invoice-line-item-component-cost-data.js";

export type InvoiceLineItem = {
  /**
   * Unique identifier for the line item. Useful when cross-referencing the line against individual
   * discounts in the `discounts` or `taxes` lists.
   */
  uid?: string;
  /** A short descriptor for the charge or item represented by this line. */
  title?: string;
  /**
   * Detailed description for the charge or item represented by this line. May include proration
   * details in plain text.
   *
   * Note: this string may contain line breaks that are hints for the best display format on the
   * invoice.
   */
  description?: string;
  /**
   * The quantity or count of units billed by the line item.
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
   * The approximate discount applied to just this line.
   *
   * The value is approximated in cases where rounding errors make it difficult to apportion exactly
   * a total discount among many lines. Several lines may have been summed prior to applying the
   * discount to arrive at `discount_amount` for the invoice - backing that out to the discount on a
   * single line may introduce rounding or precision errors.
   */
  discountAmount?: string;
  /**
   * The approximate tax applied to just this line.
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
  /**
   * Start date for the period covered by this line. The format is `"YYYY-MM-DD"`.
   *
   * * For periodic charges paid in advance, this date will match the billing date, and the end date
   *   will be in the future.
   * * For periodic charges paid in arrears (e.g., metered charges), this date will be the date of
   *   the previous billing, and the end date will be the current billing date.
   * * For non-periodic charges, this date and the end date will match.
   */
  periodRangeStart?: string;
  /**
   * End date for the period covered by this line. The format is `"YYYY-MM-DD"`.
   *
   * * For periodic charges paid in advance, this date will match the next (future) billing date.
   * * For periodic charges paid in arrears (e.g., metered charges), this date will be the date of
   *   the current billing date.
   * * For non-periodic charges, this date and the start date will match.
   */
  periodRangeEnd?: string;
  transactionId?: number;
  /**
   * The ID of the product subscribed when the charge was made.
   *
   * This may be set even for component charges, so true product-only (non-component) charges will
   * also have a nil `component_id`.
   */
  productId?: number | null;
  /** The version of the product subscribed when the charge was made. */
  productVersion?: number | null;
  /** The ID of the component being billed. Will be `nil` for non-component charges. */
  componentId?: number | null;
  /** The price point ID of the component being billed. Will be `nil` for non-component charges. */
  pricePointId?: number | null;
  billingScheduleItemId?: number | null;
  hide?: boolean;
  componentCostData?: InvoiceLineItemComponentCostData | null;
  /** The price point ID of the line item's product */
  productPricePointId?: number | null;
  customItem?: boolean;
  kind?: string;
  /**
   * The date a prepaid allocation is set to expire. Only present on line items representing prepaid
   * component allocations. The format is `"YYYY-MM-DD"`.
   */
  prepaidAllocationExpiresAt?: string | null;
};

export const invoiceLineItemSchema: Schema<InvoiceLineItem> = s.object<InvoiceLineItem>({
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
  transactionId: s.optional(s.int()),
  productId: s.optionalNullable(s.int()),
  productVersion: s.optionalNullable(s.int()),
  componentId: s.optionalNullable(s.int()),
  pricePointId: s.optionalNullable(s.int()),
  billingScheduleItemId: s.optionalNullable(s.int()),
  hide: s.optional(s.boolean()),
  componentCostData: s.optionalNullable(s.lazy(() => invoiceLineItemComponentCostDataSchema)),
  productPricePointId: s.optionalNullable(s.int()),
  customItem: s.optional(s.boolean()),
  kind: s.optional(s.string()),
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
    transactionId: "transaction_id",
    productId: "product_id",
    productVersion: "product_version",
    componentId: "component_id",
    pricePointId: "price_point_id",
    billingScheduleItemId: "billing_schedule_item_id",
    componentCostData: "component_cost_data",
    productPricePointId: "product_price_point_id",
    customItem: "custom_item",
    prepaidAllocationExpiresAt: "prepaid_allocation_expires_at",
  },
});
