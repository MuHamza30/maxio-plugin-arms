import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createInvoiceAddressSchema, type CreateInvoiceAddress } from "./create-invoice-address.js";
import { createInvoiceCouponSchema, type CreateInvoiceCoupon } from "./create-invoice-coupon.js";
import { createInvoiceItemSchema, type CreateInvoiceItem } from "./create-invoice-item.js";
import { CreateInvoiceStatus, createInvoiceStatusSchema } from "./create-invoice-status.js";

export type CreateInvoice = {
  lineItems?: CreateInvoiceItem[];
  /**
   * Date on which the invoice will be issued (format YYYY-MM-DD). This date is interpreted and
   * validated in your site's time zone. It must be today or a date in the past — future dates are
   * not accepted. If omitted, defaults to today in your site's time zone.
   */
  issueDate?: string;
  /**
   * By default, invoices will be created with a due date matching the date of invoice creation. If
   * a different due date is desired, the net_terms parameter can be sent indicating the number of
   * days in advance the due date should be.
   */
  netTerms?: number;
  paymentInstructions?: string;
  /** A custom memo can be sent to override the site's default. */
  memo?: string;
  /** Overrides the defaults for the site. */
  sellerAddress?: CreateInvoiceAddress;
  /** Overrides the default for the customer. */
  billingAddress?: CreateInvoiceAddress;
  /** Overrides the default for the customer. */
  shippingAddress?: CreateInvoiceAddress;
  coupons?: CreateInvoiceCoupon[];
  /** @default CreateInvoiceStatus.Open */
  status?: CreateInvoiceStatus;
};

export const createInvoiceSchema: Schema<CreateInvoice> = s.object<CreateInvoice>({
  lineItems: s.optional(s.array(s.lazy(() => createInvoiceItemSchema))),
  issueDate: s.optional(s.dateOnly()),
  netTerms: s.optional(s.int()),
  paymentInstructions: s.optional(s.string()),
  memo: s.optional(s.string()),
  sellerAddress: s.optional(s.lazy(() => createInvoiceAddressSchema)),
  billingAddress: s.optional(s.lazy(() => createInvoiceAddressSchema)),
  shippingAddress: s.optional(s.lazy(() => createInvoiceAddressSchema)),
  coupons: s.optional(s.array(s.lazy(() => createInvoiceCouponSchema))),
  status: s.defaulted(createInvoiceStatusSchema, CreateInvoiceStatus.Open),
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
