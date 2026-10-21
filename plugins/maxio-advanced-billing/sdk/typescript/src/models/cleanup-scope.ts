import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * all: Will clear all products, customers, and related subscriptions from the site. customers: Will
 * clear only customers and related subscriptions (leaving the products untouched) for the site.
 * Revenue will also be reset to 0.
 */
export const CleanupScope = {
  All: "all",
  Customers: "customers",
} as const;
export type CleanupScope = (typeof CleanupScope)[keyof typeof CleanupScope] | (string & {});

export const cleanupScopeSchema: EnumSchema<CleanupScope> = s.enumOf<CleanupScope>(CleanupScope);
