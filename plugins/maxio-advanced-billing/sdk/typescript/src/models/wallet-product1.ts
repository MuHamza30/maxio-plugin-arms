import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { itemCategorySchema, type ItemCategory } from "./item-category.js";

export type WalletProduct1 = {
  name?: string;
  description?: string | null;
  taxable?: boolean;
  taxCode?: string | null;
  accountingCode?: string | null;
  /**
   * One of the following: Business Software, Consumer Software, Digital Services, Physical Goods,
   * Other
   */
  itemCategory?: ItemCategory | null;
};

export const walletProduct1Schema: Schema<WalletProduct1> = s.object<WalletProduct1>({
  name: s.optional(s.string()),
  description: s.optionalNullable(s.string()),
  taxable: s.optional(s.boolean()),
  taxCode: s.optionalNullable(s.string()),
  accountingCode: s.optionalNullable(s.string()),
  itemCategory: s.optionalNullable(s.lazy(() => itemCategorySchema)),
  _keysMap: {
    taxCode: "tax_code",
    accountingCode: "accounting_code",
    itemCategory: "item_category",
  },
});
