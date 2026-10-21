import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { itemCategorySchema, type ItemCategory } from "./item-category.js";
import {
  walletProductPricePointAttributesSchema,
  type WalletProductPricePointAttributes,
} from "./wallet-product-price-point-attributes.js";

export type WalletProduct = {
  name: string;
  /** The name of the unit the Wallet Product's usage is measured in, for example `tokens`. */
  unitName: string;
  handle?: string;
  description?: string | null;
  taxable?: boolean;
  taxCode?: string | null;
  accountingCode?: string | null;
  /**
   * One of the following: Business Software, Consumer Software, Digital Services, Physical Goods,
   * Other
   */
  itemCategory?: ItemCategory | null;
  /**
   * Creates one price point for the Wallet Product in the same call. Ignored if `price_points` is
   * also sent.
   */
  pricePoint?: WalletProductPricePointAttributes;
  /**
   * Creates several price points for the Wallet Product in the same call, winning over
   * `price_point` if both are sent. The first price point created becomes the Wallet Product's
   * default. The whole call is one transaction: if any price point in the array fails validation,
   * nothing is created, including the Wallet Product itself.
   */
  pricePoints?: WalletProductPricePointAttributes[];
};

export const walletProductSchema: Schema<WalletProduct> = s.object<WalletProduct>({
  name: s.string(),
  unitName: s.string(),
  handle: s.optional(s.string()),
  description: s.optionalNullable(s.string()),
  taxable: s.optional(s.boolean()),
  taxCode: s.optionalNullable(s.string()),
  accountingCode: s.optionalNullable(s.string()),
  itemCategory: s.optionalNullable(s.lazy(() => itemCategorySchema)),
  pricePoint: s.optional(s.lazy(() => walletProductPricePointAttributesSchema)),
  pricePoints: s.optional(s.array(s.lazy(() => walletProductPricePointAttributesSchema))),
  _keysMap: {
    unitName: "unit_name",
    taxCode: "tax_code",
    accountingCode: "accounting_code",
    itemCategory: "item_category",
    pricePoint: "price_point",
    pricePoints: "price_points",
  },
});
