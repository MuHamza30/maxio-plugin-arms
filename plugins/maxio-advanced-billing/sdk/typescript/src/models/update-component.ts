import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditTypeSchema, type CreditType } from "./credit-type.js";
import { itemCategorySchema, type ItemCategory } from "./item-category.js";

export type UpdateComponent = {
  handle?: string;
  /** The name of the Component, suitable for display on statements. e.g., Text Messages. */
  name?: string;
  /** The description of the component. */
  description?: string | null;
  accountingCode?: string | null;
  /** Boolean flag describing whether a component is taxable or not. */
  taxable?: boolean;
  /**
   * A string representing the tax code related to the component type. This is especially important
   * when using AvaTax to tax based on locale. This attribute has a max length of 25 characters.
   */
  taxCode?: string | null;
  /**
   * One of the following: Business Software, Consumer Software, Digital Services, Physical Goods,
   * Other
   */
  itemCategory?: ItemCategory | null;
  displayOnHostedPage?: boolean;
  /**
   * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
   * site setting if one is not provided.
   */
  upgradeCharge?: CreditType | null;
  /**
   * (Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is
   * sent as the commodity code on invoice line items for this component instead of the default
   * derived from item_category.
   */
  unspscCode?: string | null;
};

export const updateComponentSchema: Schema<UpdateComponent> = s.object<UpdateComponent>({
  handle: s.optional(s.string()),
  name: s.optional(s.string()),
  description: s.optionalNullable(s.string()),
  accountingCode: s.optionalNullable(s.string()),
  taxable: s.optional(s.boolean()),
  taxCode: s.optionalNullable(s.string()),
  itemCategory: s.optionalNullable(s.lazy(() => itemCategorySchema)),
  displayOnHostedPage: s.optional(s.boolean()),
  upgradeCharge: s.optionalNullable(s.lazy(() => creditTypeSchema)),
  unspscCode: s.optionalNullable(s.string()),
  _keysMap: {
    accountingCode: "accounting_code",
    taxCode: "tax_code",
    itemCategory: "item_category",
    displayOnHostedPage: "display_on_hosted_page",
    upgradeCharge: "upgrade_charge",
    unspscCode: "unspsc_code",
  },
});
