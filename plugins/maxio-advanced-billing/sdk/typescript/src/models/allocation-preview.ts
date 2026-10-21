import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  allocationPreviewDirectionSchema,
  type AllocationPreviewDirection,
} from "./allocation-preview-direction.js";
import { allocationPreviewItemSchema, type AllocationPreviewItem } from "./allocation-preview-item.js";
import {
  allocationPreviewLineItemSchema,
  type AllocationPreviewLineItem,
} from "./allocation-preview-line-item.js";

export type AllocationPreview = {
  startDate?: Date;
  endDate?: Date;
  subtotalInCents?: number;
  totalTaxInCents?: number;
  totalDiscountInCents?: number;
  totalInCents?: number;
  direction?: AllocationPreviewDirection;
  prorationScheme?: string;
  lineItems?: AllocationPreviewLineItem[];
  accrueCharge?: boolean;
  allocations?: AllocationPreviewItem[];
  periodType?: string;
  /** An integer representing the amount of the subscription's current balance */
  existingBalanceInCents?: number;
};

export const allocationPreviewSchema: Schema<AllocationPreview> = s.object<AllocationPreview>({
  startDate: s.optional(s.dateTime()),
  endDate: s.optional(s.dateTime()),
  subtotalInCents: s.optional(s.int()),
  totalTaxInCents: s.optional(s.int()),
  totalDiscountInCents: s.optional(s.int()),
  totalInCents: s.optional(s.int()),
  direction: s.optional(s.lazy(() => allocationPreviewDirectionSchema)),
  prorationScheme: s.optional(s.string()),
  lineItems: s.optional(s.array(s.lazy(() => allocationPreviewLineItemSchema))),
  accrueCharge: s.optional(s.boolean()),
  allocations: s.optional(s.array(s.lazy(() => allocationPreviewItemSchema))),
  periodType: s.optional(s.string()),
  existingBalanceInCents: s.optional(s.int()),
  _keysMap: {
    startDate: "start_date",
    endDate: "end_date",
    subtotalInCents: "subtotal_in_cents",
    totalTaxInCents: "total_tax_in_cents",
    totalDiscountInCents: "total_discount_in_cents",
    totalInCents: "total_in_cents",
    prorationScheme: "proration_scheme",
    lineItems: "line_items",
    accrueCharge: "accrue_charge",
    periodType: "period_type",
    existingBalanceInCents: "existing_balance_in_cents",
  },
});
