import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createInvoiceAddressSchema, type CreateInvoiceAddress } from "./create-invoice-address.js";
import { createInvoiceCouponSchema, type CreateInvoiceCoupon } from "./create-invoice-coupon.js";
import { updateInvoiceItemSchema, type UpdateInvoiceItem } from "./update-invoice-item.js";

/**
 * Attributes of a draft ad hoc invoice which can be updated. Only the submitted attributes are
 * changed.
 */
export type UpdateInvoice = {
  /**
   * Line item changes to apply. Line items without a `uid` are added, line items with a `uid` are
   * updated, and line items with a `uid` and `_destroy` set to `true` are removed. Existing line
   * items not referenced in the array remain unchanged.
   */
  lineItems?: UpdateInvoiceItem[];
  /**
   * New issue date for the invoice (format YYYY-MM-DD). This date is interpreted and validated in
   * your site's time zone. It must be today or a date in the past — future dates are not accepted.
   * The due date is recalculated from the issue date and net terms.
   */
  issueDate?: string;
  /**
   * Number of days after the issue date on which the invoice is due. The due date is recalculated
   * when net terms or the issue date change.
   */
  netTerms?: number;
  /** Custom payment instructions displayed on the invoice. */
  paymentInstructions?: string;
  /** A custom memo displayed on the invoice. */
  memo?: string;
  /** Replaces the seller address on the invoice */
  sellerAddress?: CreateInvoiceAddress;
  /** Replaces the billing address on the invoice */
  billingAddress?: CreateInvoiceAddress;
  /** Replaces the shipping address on the invoice */
  shippingAddress?: CreateInvoiceAddress;
  /**
   * When present, replaces all discounts currently applied to the invoice. Send an empty array to
   * remove all discounts.
   */
  coupons?: CreateInvoiceCoupon[];
};

export const updateInvoiceSchema: Schema<UpdateInvoice> = s.object<UpdateInvoice>({
  lineItems: s.optional(s.array(s.lazy(() => updateInvoiceItemSchema))),
  issueDate: s.optional(s.dateOnly()),
  netTerms: s.optional(s.int()),
  paymentInstructions: s.optional(s.string()),
  memo: s.optional(s.string()),
  sellerAddress: s.optional(s.lazy(() => createInvoiceAddressSchema)),
  billingAddress: s.optional(s.lazy(() => createInvoiceAddressSchema)),
  shippingAddress: s.optional(s.lazy(() => createInvoiceAddressSchema)),
  coupons: s.optional(s.array(s.lazy(() => createInvoiceCouponSchema))),
  _keysMap: {
    lineItems: "line_items",
    issueDate: "issue_date",
    netTerms: "net_terms",
    paymentInstructions: "payment_instructions",
    sellerAddress: "seller_address",
    billingAddress: "billing_address",
    shippingAddress: "shipping_address",
  },
});
