import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  allocationPreviewDirectionSchema,
  type AllocationPreviewDirection,
} from "./allocation-preview-direction.js";
import {
  allocationPreviewLineItemKindSchema,
  type AllocationPreviewLineItemKind,
} from "./allocation-preview-line-item-kind.js";
import { lineItemTransactionTypeSchema, type LineItemTransactionType } from "./line-item-transaction-type.js";

export type AllocationPreviewLineItem = {
  /** A handle for the line item transaction type */
  transactionType?: LineItemTransactionType;
  /** A handle for the line item kind for allocation preview */
  kind?: AllocationPreviewLineItemKind;
  amountInCents?: number;
  memo?: string;
  discountAmountInCents?: number;
  taxableAmountInCents?: number;
  componentId?: number;
  componentHandle?: string;
  /** Visible when using Fine-grained Component Control. */
  direction?: AllocationPreviewDirection;
};

export const allocationPreviewLineItemSchema: Schema<AllocationPreviewLineItem> =
  s.object<AllocationPreviewLineItem>({
    transactionType: s.optional(s.lazy(() => lineItemTransactionTypeSchema)),
    kind: s.optional(s.lazy(() => allocationPreviewLineItemKindSchema)),
    amountInCents: s.optional(s.int()),
    memo: s.optional(s.string()),
    discountAmountInCents: s.optional(s.int()),
    taxableAmountInCents: s.optional(s.int()),
    componentId: s.optional(s.int()),
    componentHandle: s.optional(s.string()),
    direction: s.optional(s.lazy(() => allocationPreviewDirectionSchema)),
    _keysMap: {
      transactionType: "transaction_type",
      amountInCents: "amount_in_cents",
      discountAmountInCents: "discount_amount_in_cents",
      taxableAmountInCents: "taxable_amount_in_cents",
      componentId: "component_id",
      componentHandle: "component_handle",
    },
  });
