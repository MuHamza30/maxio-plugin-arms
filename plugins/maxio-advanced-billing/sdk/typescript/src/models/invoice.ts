import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { collectionMethodSchema, type CollectionMethod } from "./collection-method.js";
import { invoiceAddressSchema, type InvoiceAddress } from "./invoice-address.js";
import { invoiceAvataxDetailsSchema, type InvoiceAvataxDetails } from "./invoice-avatax-details.js";
import {
  invoiceConsolidationLevelSchema,
  type InvoiceConsolidationLevel,
} from "./invoice-consolidation-level.js";
import { invoiceCreditSchema, type InvoiceCredit } from "./invoice-credit.js";
import { invoiceCustomFieldSchema, type InvoiceCustomField } from "./invoice-custom-field.js";
import { invoiceCustomerSchema, type InvoiceCustomer } from "./invoice-customer.js";
import { invoiceDebitSchema, type InvoiceDebit } from "./invoice-debit.js";
import { invoiceDiscountSchema, type InvoiceDiscount } from "./invoice-discount.js";
import { invoiceDisplaySettingsSchema, type InvoiceDisplaySettings } from "./invoice-display-settings.js";
import { invoiceLineItemSchema, type InvoiceLineItem } from "./invoice-line-item.js";
import { invoicePayerSchema, type InvoicePayer } from "./invoice-payer.js";
import { invoicePaymentSchema, type InvoicePayment } from "./invoice-payment.js";
import { invoicePreviousBalanceSchema, type InvoicePreviousBalance } from "./invoice-previous-balance.js";
import { invoiceRefundSchema, type InvoiceRefund } from "./invoice-refund.js";
import { invoiceRoleSchema, type InvoiceRole } from "./invoice-role.js";
import { invoiceSellerSchema, type InvoiceSeller } from "./invoice-seller.js";
import { invoiceStatusSchema, type InvoiceStatus } from "./invoice-status.js";
import { invoiceTaxSchema, type InvoiceTax } from "./invoice-tax.js";

export type Invoice = {
  id?: number;
  /**
   * Unique identifier for the invoice. It is generated automatically by Chargify and has the prefix
   * "inv_" followed by alphanumeric characters.
   */
  uid?: string;
  /** ID of the site to which the invoice belongs. */
  siteId?: number;
  /** ID of the customer to which the invoice belongs. */
  customerId?: number;
  /** ID of the subscription that generated the invoice. */
  subscriptionId?: number;
  /**
   * A unique, identifying string that appears on the invoice and in places the invoice is
   * referenced.
   *
   * While the UID is long and not appropriate to show to customers, the number is usually shorter
   * and consumable by the customer and the merchant alike.
   */
  number?: string;
  /**
   * A monotonically increasing number assigned to invoices as they are created. This number is
   * unique within a site and can be used to sort and order invoices.
   */
  sequenceNumber?: number;
  transactionTime?: Date;
  createdAt?: Date;
  updatedAt?: Date;
  /**
   * Date the invoice was issued to the customer. This is the date that the invoice was made
   * available for payment.
   *
   * The format is `"YYYY-MM-DD"`.
   */
  issueDate?: string;
  /**
   * Date the invoice is due.
   *
   * The format is `"YYYY-MM-DD"`.
   */
  dueDate?: string;
  /**
   * Date the invoice became fully paid.
   *
   * If partial payments are applied to the invoice, this date will not be present until payment has
   * been made in full.
   *
   * The format is `"YYYY-MM-DD"`.
   */
  paidDate?: string | null;
  /**
   * The current status of the invoice. See [Invoice
   * Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses)
   * for more.
   */
  status?: InvoiceStatus;
  role?: InvoiceRole;
  parentInvoiceId?: number | null;
  /**
   * The type of payment collection to be used in the subscription. For legacy Statements
   * Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing
   * Architecture valid options are - `remittance`, `automatic`, `prepaid`.
   */
  collectionMethod?: CollectionMethod;
  /**
   * A message that is printed on the invoice when it is marked for remittance collection. It is
   * intended to describe to the customer how they may make payment, and is configured by the
   * merchant.
   */
  paymentInstructions?: string;
  /**
   * The ISO 4217 currency code (3 character string) representing the currency of invoice
   * transaction.
   */
  currency?: string;
  /**
   * Consolidation level of the invoice, which is applicable to invoice consolidation. It will hold
   * one of the following values:
   *
   * * "none": A normal invoice with no consolidation.
   * * "child": An invoice segment which has been combined into a consolidated invoice.
   * * "parent": A consolidated invoice, whose contents are composed of invoice segments.
   *
   * "Parent" invoices do not have lines of their own, but they have subtotals and totals which
   * aggregate the member invoice segments.
   *
   * See also the [invoice consolidation
   * documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation).
   */
  consolidationLevel?: InvoiceConsolidationLevel;
  /**
   * For invoices with `consolidation_level` of `child`, this specifies the UID of the parent
   * (consolidated) invoice.
   */
  parentInvoiceUid?: string | null;
  subscriptionGroupId?: number | null;
  /**
   * For invoices with `consolidation_level` of `child`, this specifies the number of the parent
   * (consolidated) invoice.
   */
  parentInvoiceNumber?: number | null;
  /**
   * For invoices with `consolidation_level` of `parent`, this specifies the ID of the subscription
   * which was the primary subscription of the subscription group that generated the invoice.
   */
  groupPrimarySubscriptionId?: number | null;
  /** The name of the product subscribed when the invoice was generated. */
  productName?: string;
  /** The name of the product family subscribed when the invoice was generated. */
  productFamilyName?: string;
  /** Information about the seller (merchant) listed on the masthead of the invoice. */
  seller?: InvoiceSeller;
  /** Information about the customer who is owner or recipient of the invoiced subscription. */
  customer?: InvoiceCustomer;
  payer?: InvoicePayer;
  recipientEmails?: string[];
  netTerms?: number;
  /**
   * The memo printed on invoices of any collection type. This message is in control of the
   * merchant.
   */
  memo?: string;
  /** The invoice billing address. */
  billingAddress?: InvoiceAddress;
  /** The invoice shipping address. */
  shippingAddress?: InvoiceAddress;
  /** Subtotal of the invoice, which is the sum of all line items before discounts or taxes. */
  subtotalAmount?: string;
  /** Total discount applied to the invoice. */
  discountAmount?: string;
  /** Total tax on the invoice. */
  taxAmount?: string;
  /** The invoice total, which is `subtotal_amount - discount_amount + tax_amount`. */
  totalAmount?: string;
  /**
   * The amount of credit (from credit notes) applied to this invoice.
   *
   * Credits offset the amount due from the customer.
   */
  creditAmount?: string;
  debitAmount?: string;
  refundAmount?: string;
  /** The amount paid on the invoice by the customer. */
  paidAmount?: string;
  /** Amount due on the invoice, which is `total_amount - credit_amount - paid_amount`. */
  dueAmount?: string;
  /** Line items on the invoice. */
  lineItems?: InvoiceLineItem[];
  discounts?: InvoiceDiscount[];
  taxes?: InvoiceTax[];
  credits?: InvoiceCredit[];
  debits?: InvoiceDebit[];
  refunds?: InvoiceRefund[];
  payments?: InvoicePayment[];
  customFields?: InvoiceCustomField[];
  displaySettings?: InvoiceDisplaySettings;
  avataxDetails?: InvoiceAvataxDetails;
  /** The public URL of the invoice */
  publicUrl?: string;
  previousBalanceData?: InvoicePreviousBalance;
  /** The format is `"YYYY-MM-DD"`. */
  publicUrlExpiresOn?: string;
  /**
   * The ID of the Branding Theme associated with this invoice. This value represents the Branding
   * Theme used for invoice theming, such as themed invoice rendering. Available only when Branding
   * Themes are enabled for the site.
   */
  brandingThemeId?: number | null;
};

export const invoiceSchema: Schema<Invoice> = s.object<Invoice>({
  id: s.optional(s.int()),
  uid: s.optional(s.string()),
  siteId: s.optional(s.int()),
  customerId: s.optional(s.int()),
  subscriptionId: s.optional(s.int()),
  number: s.optional(s.string()),
  sequenceNumber: s.optional(s.int()),
  transactionTime: s.optional(s.dateTime()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  issueDate: s.optional(s.dateOnly()),
  dueDate: s.optional(s.dateOnly()),
  paidDate: s.optionalNullable(s.dateOnly()),
  status: s.optional(s.lazy(() => invoiceStatusSchema)),
  role: s.optional(s.lazy(() => invoiceRoleSchema)),
  parentInvoiceId: s.optionalNullable(s.int()),
  collectionMethod: s.optional(s.lazy(() => collectionMethodSchema)),
  paymentInstructions: s.optional(s.string()),
  currency: s.optional(s.string()),
  consolidationLevel: s.optional(s.lazy(() => invoiceConsolidationLevelSchema)),
  parentInvoiceUid: s.optionalNullable(s.string()),
  subscriptionGroupId: s.optionalNullable(s.int()),
  parentInvoiceNumber: s.optionalNullable(s.int()),
  groupPrimarySubscriptionId: s.optionalNullable(s.int()),
  productName: s.optional(s.string()),
  productFamilyName: s.optional(s.string()),
  seller: s.optional(s.lazy(() => invoiceSellerSchema)),
  customer: s.optional(s.lazy(() => invoiceCustomerSchema)),
  payer: s.optional(s.lazy(() => invoicePayerSchema)),
  recipientEmails: s.optional(s.array(s.string())),
  netTerms: s.optional(s.int()),
  memo: s.optional(s.string()),
  billingAddress: s.optional(s.lazy(() => invoiceAddressSchema)),
  shippingAddress: s.optional(s.lazy(() => invoiceAddressSchema)),
  subtotalAmount: s.optional(s.string()),
  discountAmount: s.optional(s.string()),
  taxAmount: s.optional(s.string()),
  totalAmount: s.optional(s.string()),
  creditAmount: s.optional(s.string()),
  debitAmount: s.optional(s.string()),
  refundAmount: s.optional(s.string()),
  paidAmount: s.optional(s.string()),
  dueAmount: s.optional(s.string()),
  lineItems: s.optional(s.array(s.lazy(() => invoiceLineItemSchema))),
  discounts: s.optional(s.array(s.lazy(() => invoiceDiscountSchema))),
  taxes: s.optional(s.array(s.lazy(() => invoiceTaxSchema))),
  credits: s.optional(s.array(s.lazy(() => invoiceCreditSchema))),
  debits: s.optional(s.array(s.lazy(() => invoiceDebitSchema))),
  refunds: s.optional(s.array(s.lazy(() => invoiceRefundSchema))),
  payments: s.optional(s.array(s.lazy(() => invoicePaymentSchema))),
  customFields: s.optional(s.array(s.lazy(() => invoiceCustomFieldSchema))),
  displaySettings: s.optional(s.lazy(() => invoiceDisplaySettingsSchema)),
  avataxDetails: s.optional(s.lazy(() => invoiceAvataxDetailsSchema)),
  publicUrl: s.optional(s.string()),
  previousBalanceData: s.optional(s.lazy(() => invoicePreviousBalanceSchema)),
  publicUrlExpiresOn: s.optional(s.dateOnly()),
  brandingThemeId: s.optionalNullable(s.int()),
  _keysMap: {
    siteId: "site_id",
    customerId: "customer_id",
    subscriptionId: "subscription_id",
    sequenceNumber: "sequence_number",
    transactionTime: "transaction_time",
    createdAt: "created_at",
    updatedAt: "updated_at",
    issueDate: "issue_date",
    dueDate: "due_date",
    paidDate: "paid_date",
    parentInvoiceId: "parent_invoice_id",
    collectionMethod: "collection_method",
    paymentInstructions: "payment_instructions",
    consolidationLevel: "consolidation_level",
    parentInvoiceUid: "parent_invoice_uid",
    subscriptionGroupId: "subscription_group_id",
    parentInvoiceNumber: "parent_invoice_number",
    groupPrimarySubscriptionId: "group_primary_subscription_id",
    productName: "product_name",
    productFamilyName: "product_family_name",
    recipientEmails: "recipient_emails",
    netTerms: "net_terms",
    billingAddress: "billing_address",
    shippingAddress: "shipping_address",
    subtotalAmount: "subtotal_amount",
    discountAmount: "discount_amount",
    taxAmount: "tax_amount",
    totalAmount: "total_amount",
    creditAmount: "credit_amount",
    debitAmount: "debit_amount",
    refundAmount: "refund_amount",
    paidAmount: "paid_amount",
    dueAmount: "due_amount",
    lineItems: "line_items",
    customFields: "custom_fields",
    displaySettings: "display_settings",
    avataxDetails: "avatax_details",
    publicUrl: "public_url",
    previousBalanceData: "previous_balance_data",
    publicUrlExpiresOn: "public_url_expires_on",
    brandingThemeId: "branding_theme_id",
  },
});
