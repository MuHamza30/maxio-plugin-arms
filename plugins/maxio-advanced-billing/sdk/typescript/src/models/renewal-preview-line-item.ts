import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { lineItemKindSchema, type LineItemKind } from "./line-item-kind.js";
import { lineItemTransactionTypeSchema, type LineItemTransactionType } from "./line-item-transaction-type.js";

export type RenewalPreviewLineItem = {
  /** A handle for the line item transaction type */
  transactionType?: LineItemTransactionType;
  /** A handle for the line item kind */
  kind?: LineItemKind;
  amountInCents?: number;
  memo?: string;
  discountAmountInCents?: number;
  taxableAmountInCents?: number;
  productId?: number;
  productName?: string;
  componentId?: number;
  componentHandle?: string;
  componentName?: string;
  productHandle?: string;
  periodRangeStart?: string;
  periodRangeEnd?: string;
};

export const renewalPreviewLineItemSchema: Schema<RenewalPreviewLineItem> = s.object<RenewalPreviewLineItem>({
  transactionType: s.optional(s.lazy(() => lineItemTransactionTypeSchema)),
  kind: s.optional(s.lazy(() => lineItemKindSchema)),
  amountInCents: s.optional(s.int()),
  memo: s.optional(s.string()),
  discountAmountInCents: s.optional(s.int()),
  taxableAmountInCents: s.optional(s.int()),
  productId: s.optional(s.int()),
  productName: s.optional(s.string()),
  componentId: s.optional(s.int()),
  componentHandle: s.optional(s.string()),
  componentName: s.optional(s.string()),
  productHandle: s.optional(s.string()),
  periodRangeStart: s.optional(s.string()),
  periodRangeEnd: s.optional(s.string()),
  _keysMap: {
    transactionType: "transaction_type",
    amountInCents: "amount_in_cents",
    discountAmountInCents: "discount_amount_in_cents",
    taxableAmountInCents: "taxable_amount_in_cents",
    productId: "product_id",
    productName: "product_name",
    componentId: "component_id",
    componentHandle: "component_handle",
    componentName: "component_name",
    productHandle: "product_handle",
    periodRangeStart: "period_range_start",
    periodRangeEnd: "period_range_end",
  },
});
