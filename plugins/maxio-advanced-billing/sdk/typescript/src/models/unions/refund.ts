import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import {
  refundConsolidatedInvoiceSchema,
  type RefundConsolidatedInvoice,
} from "../refund-consolidated-invoice.js";
import { refundInvoiceSchema, type RefundInvoice } from "../refund-invoice.js";

export type Refund = RefundInvoice | RefundConsolidatedInvoice;

export const refundSchema: Schema<Refund> = s.of<Refund>(
  s.union([s.lazy(() => refundInvoiceSchema), s.lazy(() => refundConsolidatedInvoiceSchema)]),
);
