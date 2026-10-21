import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ProductFamily = {
  id?: number;
  name?: string;
  handle?: string;
  accountingCode?: string | null;
  description?: string | null;
  /**
   * Whether surcharging applies to this product family. Only included on sites where surcharging is
   * enabled.
   */
  surcharging?: boolean;
  createdAt?: Date;
  updatedAt?: Date;
  /**
   * Timestamp indicating when this product family was archived. `null` if the product family is not
   * archived.
   */
  archivedAt?: Date | null;
};

export const productFamilySchema: Schema<ProductFamily> = s.object<ProductFamily>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  handle: s.optional(s.string()),
  accountingCode: s.optionalNullable(s.string()),
  description: s.optionalNullable(s.string()),
  surcharging: s.optional(s.boolean()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  archivedAt: s.optionalNullable(s.dateTime()),
  _keysMap: {
    accountingCode: "accounting_code",
    createdAt: "created_at",
    updatedAt: "updated_at",
    archivedAt: "archived_at",
  },
});
