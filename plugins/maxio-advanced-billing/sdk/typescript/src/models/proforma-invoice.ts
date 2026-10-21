import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { availableActionsSchema, type AvailableActions } from "./available-actions.js";
import { collectionMethodSchema, type CollectionMethod } from "./collection-method.js";
import { invoiceAddressSchema, type InvoiceAddress } from "./invoice-address.js";
import {
  invoiceConsolidationLevelSchema,
  type InvoiceConsolidationLevel,
} from "./invoice-consolidation-level.js";
import { invoiceCustomFieldSchema, type InvoiceCustomField } from "./invoice-custom-field.js";
import { invoiceCustomerSchema, type InvoiceCustomer } from "./invoice-customer.js";
import { invoiceLineItemSchema, type InvoiceLineItem } from "./invoice-line-item.js";
import { invoiceSellerSchema, type InvoiceSeller } from "./invoice-seller.js";
import { proformaInvoiceCreditSchema, type ProformaInvoiceCredit } from "./proforma-invoice-credit.js";
import { proformaInvoiceDiscountSchema, type ProformaInvoiceDiscount } from "./proforma-invoice-discount.js";
import { proformaInvoicePaymentSchema, type ProformaInvoicePayment } from "./proforma-invoice-payment.js";
import { proformaInvoiceRoleSchema, type ProformaInvoiceRole } from "./proforma-invoice-role.js";
import { proformaInvoiceStatusSchema, type ProformaInvoiceStatus } from "./proforma-invoice-status.js";
import { proformaInvoiceTaxSchema, type ProformaInvoiceTax } from "./proforma-invoice-tax.js";

export type ProformaInvoice = {
  uid?: string;
  siteId?: number;
  customerId?: number | null;
  subscriptionId?: number | null;
  number?: number | null;
  sequenceNumber?: number | null;
  createdAt?: Date;
  deliveryDate?: string;
  status?: ProformaInvoiceStatus;
  /**
   * The type of payment collection to be used in the subscription. For legacy Statements
   * Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing
   * Architecture valid options are - `remittance`, `automatic`, `prepaid`.
   */
  collectionMethod?: CollectionMethod;
  paymentInstructions?: string;
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
  productName?: string;
  productFamilyName?: string;
  /** 'proforma' value is deprecated in favor of proforma_adhoc and proforma_automatic. */
  role?: ProformaInvoiceRole;
  /** Information about the seller (merchant) listed on the masthead of the invoice. */
  seller?: InvoiceSeller;
  /** Information about the customer who is owner or recipient of the invoiced subscription. */
  customer?: InvoiceCustomer;
  memo?: string;
  billingAddress?: InvoiceAddress;
  shippingAddress?: InvoiceAddress;
  subtotalAmount?: string;
  discountAmount?: string;
  taxAmount?: string;
  totalAmount?: string;
  creditAmount?: string;
  paidAmount?: string;
  refundAmount?: string;
  dueAmount?: string;
  lineItems?: InvoiceLineItem[];
  discounts?: ProformaInvoiceDiscount[];
  taxes?: ProformaInvoiceTax[];
  credits?: ProformaInvoiceCredit[];
  payments?: ProformaInvoicePayment[];
  customFields?: InvoiceCustomField[];
  publicUrl?: string | null;
  availableActions?: AvailableActions;
};

export const proformaInvoiceSchema: Schema<ProformaInvoice> = s.object<ProformaInvoice>({
  uid: s.optional(s.string()),
  siteId: s.optional(s.int()),
  customerId: s.optionalNullable(s.int()),
  subscriptionId: s.optionalNullable(s.int()),
  number: s.optionalNullable(s.int()),
  sequenceNumber: s.optionalNullable(s.int()),
  createdAt: s.optional(s.dateTime()),
  deliveryDate: s.optional(s.dateOnly()),
  status: s.optional(s.lazy(() => proformaInvoiceStatusSchema)),
  collectionMethod: s.optional(s.lazy(() => collectionMethodSchema)),
  paymentInstructions: s.optional(s.string()),
  currency: s.optional(s.string()),
  consolidationLevel: s.optional(s.lazy(() => invoiceConsolidationLevelSchema)),
  productName: s.optional(s.string()),
  productFamilyName: s.optional(s.string()),
  role: s.optional(s.lazy(() => proformaInvoiceRoleSchema)),
  seller: s.optional(s.lazy(() => invoiceSellerSchema)),
  customer: s.optional(s.lazy(() => invoiceCustomerSchema)),
  memo: s.optional(s.string()),
  billingAddress: s.optional(s.lazy(() => invoiceAddressSchema)),
  shippingAddress: s.optional(s.lazy(() => invoiceAddressSchema)),
  subtotalAmount: s.optional(s.string()),
  discountAmount: s.optional(s.string()),
  taxAmount: s.optional(s.string()),
  totalAmount: s.optional(s.string()),
  creditAmount: s.optional(s.string()),
  paidAmount: s.optional(s.string()),
  refundAmount: s.optional(s.string()),
  dueAmount: s.optional(s.string()),
  lineItems: s.optional(s.array(s.lazy(() => invoiceLineItemSchema))),
  discounts: s.optional(s.array(s.lazy(() => proformaInvoiceDiscountSchema))),
  taxes: s.optional(s.array(s.lazy(() => proformaInvoiceTaxSchema))),
  credits: s.optional(s.array(s.lazy(() => proformaInvoiceCreditSchema))),
  payments: s.optional(s.array(s.lazy(() => proformaInvoicePaymentSchema))),
  customFields: s.optional(s.array(s.lazy(() => invoiceCustomFieldSchema))),
  publicUrl: s.optionalNullable(s.string()),
  availableActions: s.optional(s.lazy(() => availableActionsSchema)),
  _keysMap: {
    siteId: "site_id",
    customerId: "customer_id",
    subscriptionId: "subscription_id",
    sequenceNumber: "sequence_number",
    createdAt: "created_at",
    deliveryDate: "delivery_date",
    collectionMethod: "collection_method",
    paymentInstructions: "payment_instructions",
    consolidationLevel: "consolidation_level",
    productName: "product_name",
    productFamilyName: "product_family_name",
    billingAddress: "billing_address",
    shippingAddress: "shipping_address",
    subtotalAmount: "subtotal_amount",
    discountAmount: "discount_amount",
    taxAmount: "tax_amount",
    totalAmount: "total_amount",
    creditAmount: "credit_amount",
    paidAmount: "paid_amount",
    refundAmount: "refund_amount",
    dueAmount: "due_amount",
    lineItems: "line_items",
    customFields: "custom_fields",
    publicUrl: "public_url",
    availableActions: "available_actions",
  },
});
