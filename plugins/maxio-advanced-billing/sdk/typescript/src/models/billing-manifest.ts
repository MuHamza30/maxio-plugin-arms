import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { billingManifestItemSchema, type BillingManifestItem } from "./billing-manifest-item.js";

export type BillingManifest = {
  lineItems?: BillingManifestItem[];
  totalInCents?: number;
  totalDiscountInCents?: number;
  totalTaxInCents?: number;
  subtotalInCents?: number;
  startDate?: Date | null;
  endDate?: Date | null;
  periodType?: string | null;
  existingBalanceInCents?: number;
};

export const billingManifestSchema: Schema<BillingManifest> = s.object<BillingManifest>({
  lineItems: s.optional(s.array(s.lazy(() => billingManifestItemSchema))),
  totalInCents: s.optional(s.int()),
  totalDiscountInCents: s.optional(s.int()),
  totalTaxInCents: s.optional(s.int()),
  subtotalInCents: s.optional(s.int()),
  startDate: s.optionalNullable(s.dateTime()),
  endDate: s.optionalNullable(s.dateTime()),
  periodType: s.optionalNullable(s.string()),
  existingBalanceInCents: s.optional(s.int()),
  _keysMap: {
    lineItems: "line_items",
    totalInCents: "total_in_cents",
    totalDiscountInCents: "total_discount_in_cents",
    totalTaxInCents: "total_tax_in_cents",
    subtotalInCents: "subtotal_in_cents",
    startDate: "start_date",
    endDate: "end_date",
    periodType: "period_type",
    existingBalanceInCents: "existing_balance_in_cents",
  },
});
