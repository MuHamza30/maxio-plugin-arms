import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SaleRepItemMrr = {
  mrr?: string;
  usage?: string;
  recurring?: string;
};

export const saleRepItemMrrSchema: Schema<SaleRepItemMrr> = s.object<SaleRepItemMrr>({
  mrr: s.optional(s.string()),
  usage: s.optional(s.string()),
  recurring: s.optional(s.string()),
});
