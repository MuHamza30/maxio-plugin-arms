import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditNoteLineItemSchema, type CreditNoteLineItem } from "./credit-note-line-item.js";
import { debitNoteRoleSchema, type DebitNoteRole } from "./debit-note-role.js";
import { debitNoteStatusSchema, type DebitNoteStatus } from "./debit-note-status.js";
import { invoiceAddressSchema, type InvoiceAddress } from "./invoice-address.js";
import { invoiceCustomerSchema, type InvoiceCustomer } from "./invoice-customer.js";
import { invoiceDiscountSchema, type InvoiceDiscount } from "./invoice-discount.js";
import { invoiceRefundSchema, type InvoiceRefund } from "./invoice-refund.js";
import { invoiceSellerSchema, type InvoiceSeller } from "./invoice-seller.js";
import { invoiceTaxSchema, type InvoiceTax } from "./invoice-tax.js";

export type DebitNote = {
  /**
   * Unique identifier for the debit note. It is generated automatically by Chargify and has the
   * prefix "db_" followed by alphanumeric characters.
   */
  uid?: string;
  /** ID of the site to which the debit note belongs. */
  siteId?: number;
  /** ID of the customer to which the debit note belongs. */
  customerId?: number;
  /** ID of the subscription that generated the debit note. */
  subscriptionId?: number;
  /** A unique identifier that appears on the debit note and in places it is referenced. */
  number?: number;
  /** A monotonically increasing number assigned to debit notes as they are created. */
  sequenceNumber?: number;
  /**
   * Unique identifier for the connected credit note. It is generated automatically by Chargify and
   * has the prefix "cn_" followed by alphanumeric characters.
   *
   * While the UID is long and not appropriate to show to customers, the number is usually shorter
   * and consumable by the customer and the merchant alike.
   */
  originCreditNoteUid?: string;
  /** A unique identifying string of the connected credit note. */
  originCreditNoteNumber?: string;
  /**
   * Date the document was issued to the customer. This is the date that the document was made
   * available for payment.
   *
   * The format is "YYYY-MM-DD".
   */
  issueDate?: string;
  /**
   * Debit notes are applied to invoices to offset invoiced amounts - they adjust the amount due.
   * This field is the date the debit note document became fully applied to the invoice.
   *
   * The format is "YYYY-MM-DD".
   */
  appliedDate?: string;
  /** Date the document is due for payment. The format is "YYYY-MM-DD". */
  dueDate?: string;
  /** Current status of the debit note. */
  status?: DebitNoteStatus;
  /** The memo printed on debit note, which is a description of the reason for the debit. */
  memo?: string;
  /** The role of the debit note. */
  role?: DebitNoteRole;
  /**
   * The ISO 4217 currency code (3 character string) representing the currency of the credit note
   * amount fields.
   */
  currency?: string;
  /** Information about the seller (merchant) listed on the masthead of the debit note. */
  seller?: InvoiceSeller;
  /** Information about the customer who is the owner or recipient of the debited subscription. */
  customer?: InvoiceCustomer;
  /** The billing address of the debited subscription. */
  billingAddress?: InvoiceAddress;
  /** The shipping address of the debited subscription. */
  shippingAddress?: InvoiceAddress;
  /** Line items on the debit note. */
  lineItems?: CreditNoteLineItem[];
  discounts?: InvoiceDiscount[];
  taxes?: InvoiceTax[];
  refunds?: InvoiceRefund[];
};

export const debitNoteSchema: Schema<DebitNote> = s.object<DebitNote>({
  uid: s.optional(s.string()),
  siteId: s.optional(s.int()),
  customerId: s.optional(s.int()),
  subscriptionId: s.optional(s.int()),
  number: s.optional(s.int()),
  sequenceNumber: s.optional(s.int()),
  originCreditNoteUid: s.optional(s.string()),
  originCreditNoteNumber: s.optional(s.string()),
  issueDate: s.optional(s.dateOnly()),
  appliedDate: s.optional(s.dateOnly()),
  dueDate: s.optional(s.dateOnly()),
  status: s.optional(s.lazy(() => debitNoteStatusSchema)),
  memo: s.optional(s.string()),
  role: s.optional(s.lazy(() => debitNoteRoleSchema)),
  currency: s.optional(s.string()),
  seller: s.optional(s.lazy(() => invoiceSellerSchema)),
  customer: s.optional(s.lazy(() => invoiceCustomerSchema)),
  billingAddress: s.optional(s.lazy(() => invoiceAddressSchema)),
  shippingAddress: s.optional(s.lazy(() => invoiceAddressSchema)),
  lineItems: s.optional(s.array(s.lazy(() => creditNoteLineItemSchema))),
  discounts: s.optional(s.array(s.lazy(() => invoiceDiscountSchema))),
  taxes: s.optional(s.array(s.lazy(() => invoiceTaxSchema))),
  refunds: s.optional(s.array(s.lazy(() => invoiceRefundSchema))),
  _keysMap: {
    siteId: "site_id",
    customerId: "customer_id",
    subscriptionId: "subscription_id",
    sequenceNumber: "sequence_number",
    originCreditNoteUid: "origin_credit_note_uid",
    originCreditNoteNumber: "origin_credit_note_number",
    issueDate: "issue_date",
    appliedDate: "applied_date",
    dueDate: "due_date",
    billingAddress: "billing_address",
    shippingAddress: "shipping_address",
    lineItems: "line_items",
  },
});
