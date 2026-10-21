import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditNoteApplicationSchema, type CreditNoteApplication } from "./credit-note-application.js";
import { creditNoteLineItemSchema, type CreditNoteLineItem } from "./credit-note-line-item.js";
import { creditNoteStatusSchema, type CreditNoteStatus } from "./credit-note-status.js";
import { invoiceAddressSchema, type InvoiceAddress } from "./invoice-address.js";
import { invoiceCustomerSchema, type InvoiceCustomer } from "./invoice-customer.js";
import { invoiceDiscountSchema, type InvoiceDiscount } from "./invoice-discount.js";
import { invoiceRefundSchema, type InvoiceRefund } from "./invoice-refund.js";
import { invoiceSellerSchema, type InvoiceSeller } from "./invoice-seller.js";
import { invoiceTaxSchema, type InvoiceTax } from "./invoice-tax.js";
import { originInvoiceSchema, type OriginInvoice } from "./origin-invoice.js";

export type CreditNote = {
  /**
   * Unique identifier for the credit note. It is generated automatically by Chargify and has the
   * prefix "cn_" followed by alphanumeric characters.
   */
  uid?: string;
  /** ID of the site to which the credit note belongs. */
  siteId?: number;
  /** ID of the customer to which the credit note belongs. */
  customerId?: number;
  /** ID of the subscription that generated the credit note. */
  subscriptionId?: number;
  /**
   * A unique, identifying string that appears on the credit note and in places it is referenced.
   *
   * While the UID is long and not appropriate to show to customers, the number is usually shorter
   * and consumable by the customer and the merchant alike.
   */
  number?: string;
  /**
   * A monotonically increasing number assigned to credit notes as they are created. This number is
   * unique within a site and can be used to sort and order credit notes.
   */
  sequenceNumber?: number;
  /**
   * Date the credit note was issued to the customer. This is the date that the credit was made
   * available for application, and may come before it is fully applied.
   *
   * The format is `"YYYY-MM-DD"`.
   */
  issueDate?: string;
  /**
   * Credit notes are applied to invoices to offset invoiced amounts - they reduce the amount due.
   * This field is the date the credit note became fully applied to invoices.
   *
   * If the credit note has been partially applied, this field will not have a value until it has
   * been fully applied.
   *
   * The format is `"YYYY-MM-DD"`.
   */
  appliedDate?: string;
  /** Current status of the credit note. */
  status?: CreditNoteStatus;
  /**
   * The ISO 4217 currency code (3 character string) representing the currency of the credit note
   * amount fields.
   */
  currency?: string;
  /** The memo printed on credit note, which is a description of the reason for the credit. */
  memo?: string;
  /** Information about the seller (merchant) listed on the masthead of the credit note. */
  seller?: InvoiceSeller;
  /** Information about the customer who is owner or recipient of the credited subscription. */
  customer?: InvoiceCustomer;
  /** The billing address of the credit subscription. */
  billingAddress?: InvoiceAddress;
  /** The shipping address of the credited subscription. */
  shippingAddress?: InvoiceAddress;
  /**
   * Subtotal of the credit note, which is the sum of all line items before discounts or taxes. Note
   * that this is a positive amount representing the credit back to the customer.
   */
  subtotalAmount?: string;
  /**
   * Total discount applied to the credit note. Note that this is a positive amount representing the
   * discount amount being credited back to the customer (i.e., a credit on an earlier discount).
   * For example, if the original purchase was $1.00 and the original discount was $0.10, a credit
   * of $0.50 of the original purchase (half) would have a discount credit of $0.05 (also half).
   */
  discountAmount?: string;
  /**
   * Total tax of the credit note. Note that this is a positive amount representing a previously
   * taxed amount being credited back to the customer (i.e., a credit of an earlier tax). For
   * example, if the original purchase was $1.00 and the original tax was $0.10, a credit of $0.50
   * of the original purchase (half) would also have a tax credit of $0.05 (also half).
   */
  taxAmount?: string;
  /** The credit note total, which is `subtotal_amount - discount_amount + tax_amount`. */
  totalAmount?: string;
  /** The amount of the credit note that has already been applied to invoices. */
  appliedAmount?: string;
  /**
   * The amount of the credit note remaining to be applied to invoices, which is `total_amount -
   * applied_amount`.
   */
  remainingAmount?: string;
  /** Line items on the credit note. */
  lineItems?: CreditNoteLineItem[];
  discounts?: InvoiceDiscount[];
  taxes?: InvoiceTax[];
  applications?: CreditNoteApplication[];
  refunds?: InvoiceRefund[];
  /**
   * An array of origin invoices for the credit note. Learn more about [Origin Invoice from our
   * docs](https://maxio.zendesk.com/hc/en-us/articles/24252261284749-Credit-Notes-Proration#origin-invoices).
   */
  originInvoices?: OriginInvoice[];
};

export const creditNoteSchema: Schema<CreditNote> = s.object<CreditNote>({
  uid: s.optional(s.string()),
  siteId: s.optional(s.int()),
  customerId: s.optional(s.int()),
  subscriptionId: s.optional(s.int()),
  number: s.optional(s.string()),
  sequenceNumber: s.optional(s.int()),
  issueDate: s.optional(s.dateOnly()),
  appliedDate: s.optional(s.dateOnly()),
  status: s.optional(s.lazy(() => creditNoteStatusSchema)),
  currency: s.optional(s.string()),
  memo: s.optional(s.string()),
  seller: s.optional(s.lazy(() => invoiceSellerSchema)),
  customer: s.optional(s.lazy(() => invoiceCustomerSchema)),
  billingAddress: s.optional(s.lazy(() => invoiceAddressSchema)),
  shippingAddress: s.optional(s.lazy(() => invoiceAddressSchema)),
  subtotalAmount: s.optional(s.string()),
  discountAmount: s.optional(s.string()),
  taxAmount: s.optional(s.string()),
  totalAmount: s.optional(s.string()),
  appliedAmount: s.optional(s.string()),
  remainingAmount: s.optional(s.string()),
  lineItems: s.optional(s.array(s.lazy(() => creditNoteLineItemSchema))),
  discounts: s.optional(s.array(s.lazy(() => invoiceDiscountSchema))),
  taxes: s.optional(s.array(s.lazy(() => invoiceTaxSchema))),
  applications: s.optional(s.array(s.lazy(() => creditNoteApplicationSchema))),
  refunds: s.optional(s.array(s.lazy(() => invoiceRefundSchema))),
  originInvoices: s.optional(s.array(s.lazy(() => originInvoiceSchema))),
  _keysMap: {
    siteId: "site_id",
    customerId: "customer_id",
    subscriptionId: "subscription_id",
    sequenceNumber: "sequence_number",
    issueDate: "issue_date",
    appliedDate: "applied_date",
    billingAddress: "billing_address",
    shippingAddress: "shipping_address",
    subtotalAmount: "subtotal_amount",
    discountAmount: "discount_amount",
    taxAmount: "tax_amount",
    totalAmount: "total_amount",
    appliedAmount: "applied_amount",
    remainingAmount: "remaining_amount",
    lineItems: "line_items",
    originInvoices: "origin_invoices",
  },
});
