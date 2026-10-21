import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  billingManifestLineItemKindSchema,
  type BillingManifestLineItemKind,
} from "./billing-manifest-line-item-kind.js";
import { lineItemTransactionTypeSchema, type LineItemTransactionType } from "./line-item-transaction-type.js";

export type BillingManifestItem = {
  /** A handle for the line item transaction type */
  transactionType?: LineItemTransactionType;
  /** A handle for the billing manifest line item kind */
  kind?: BillingManifestLineItemKind;
  amountInCents?: number;
  memo?: string;
  discountAmountInCents?: number;
  taxableAmountInCents?: number;
  componentId?: number;
  componentHandle?: string;
  componentName?: string;
  productId?: number;
  productHandle?: string;
  productName?: string;
  periodRangeStart?: string;
  periodRangeEnd?: string;
};

export const billingManifestItemSchema: Schema<BillingManifestItem> = s.object<BillingManifestItem>({
  transactionType: s.optional(s.lazy(() => lineItemTransactionTypeSchema)),
  kind: s.optional(s.lazy(() => billingManifestLineItemKindSchema)),
  amountInCents: s.optional(s.int()),
  memo: s.optional(s.string()),
  discountAmountInCents: s.optional(s.int()),
  taxableAmountInCents: s.optional(s.int()),
  componentId: s.optional(s.int()),
  componentHandle: s.optional(s.string()),
  componentName: s.optional(s.string()),
  productId: s.optional(s.int()),
  productHandle: s.optional(s.string()),
  productName: s.optional(s.string()),
  periodRangeStart: s.optional(s.string()),
  periodRangeEnd: s.optional(s.string()),
  _keysMap: {
    transactionType: "transaction_type",
    amountInCents: "amount_in_cents",
    discountAmountInCents: "discount_amount_in_cents",
    taxableAmountInCents: "taxable_amount_in_cents",
    componentId: "component_id",
    componentHandle: "component_handle",
    componentName: "component_name",
    productId: "product_id",
    productHandle: "product_handle",
    productName: "product_name",
    periodRangeStart: "period_range_start",
    periodRangeEnd: "period_range_end",
  },
});
