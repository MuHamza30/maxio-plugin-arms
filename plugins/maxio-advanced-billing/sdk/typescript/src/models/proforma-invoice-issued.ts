import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceLineItemEventDataSchema,
  type InvoiceLineItemEventData,
} from "./invoice-line-item-event-data.js";

export type ProformaInvoiceIssued = {
  uid: string;
  number: string;
  role: string;
  deliveryDate: string;
  createdAt: Date;
  dueAmount: string;
  paidAmount: string;
  taxAmount: string;
  totalAmount: string;
  productName: string;
  lineItems: InvoiceLineItemEventData[];
};

export const proformaInvoiceIssuedSchema: Schema<ProformaInvoiceIssued> = s.object<ProformaInvoiceIssued>({
  uid: s.string(),
  number: s.string(),
  role: s.string(),
  deliveryDate: s.dateOnly(),
  createdAt: s.dateTime(),
  dueAmount: s.string(),
  paidAmount: s.string(),
  taxAmount: s.string(),
  totalAmount: s.string(),
  productName: s.string(),
  lineItems: s.array(s.lazy(() => invoiceLineItemEventDataSchema)),
  _keysMap: {
    deliveryDate: "delivery_date",
    createdAt: "created_at",
    dueAmount: "due_amount",
    paidAmount: "paid_amount",
    taxAmount: "tax_amount",
    totalAmount: "total_amount",
    productName: "product_name",
    lineItems: "line_items",
  },
});
