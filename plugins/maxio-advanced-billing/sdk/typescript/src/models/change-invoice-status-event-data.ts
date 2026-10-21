import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceConsolidationLevelSchema,
  type InvoiceConsolidationLevel,
} from "./invoice-consolidation-level.js";
import { invoiceStatusSchema, type InvoiceStatus } from "./invoice-status.js";

/** Example schema for an `change_invoice_status` event */
export type ChangeInvoiceStatusEventData = {
  /** Identifier for the transaction within the payment gateway. */
  gatewayTransId?: string;
  /** The monetary value associated with the linked payment, expressed in dollars. */
  amount?: string;
  /**
   * The status of the invoice before any changes occurred. See [Invoice
   * Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses)
   * for more.
   */
  fromStatus: InvoiceStatus;
  /**
   * The updated status of the invoice after changes have been made. See [Invoice
   * Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses)
   * for more.
   */
  toStatus: InvoiceStatus;
  consolidationLevel?: InvoiceConsolidationLevel;
};

export const changeInvoiceStatusEventDataSchema: Schema<ChangeInvoiceStatusEventData> =
  s.object<ChangeInvoiceStatusEventData>({
    gatewayTransId: s.optional(s.string()),
    amount: s.optional(s.string()),
    fromStatus: invoiceStatusSchema,
    toStatus: invoiceStatusSchema,
    consolidationLevel: s.optional(s.lazy(() => invoiceConsolidationLevelSchema)),
    _keysMap: {
      gatewayTransId: "gateway_trans_id",
      fromStatus: "from_status",
      toStatus: "to_status",
      consolidationLevel: "consolidation_level",
    },
  });
