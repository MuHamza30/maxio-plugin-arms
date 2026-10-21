import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { prorationSchema, type Proration } from "./proration.js";

export type SubscriptionMigrationPreviewOptions = {
  /**
   * The ID of the target Product. Either a product_id or product_handle must be present. A
   * Subscription can be migrated to another product for both the current Product Family and another
   * Product Family. Note: Going to another Product Family, components will not be migrated as well.
   */
  productId?: number;
  /**
   * The ID of the specified product's price point. This can be passed to migrate to a non-default
   * price point.
   */
  productPricePointId?: number;
  /**
   * Whether to include the trial period configured for the product price point when starting a new
   * billing period. Note that if preserve_period is set, then include_trial will be ignored.
   *
   * @default false
   */
  includeTrial?: boolean;
  /** If `true` is sent initial charges will be assessed. @default false */
  includeInitialCharge?: boolean;
  /**
   * If `true` is sent, any coupons associated with the subscription will be applied to the
   * migration. If `false` is sent, coupons will not be applied. Note: When migrating to a new
   * product family, the coupon cannot migrate.
   *
   * @default true
   */
  includeCoupons?: boolean;
  /**
   * If `false` is sent, the subscription's billing period will be reset to today and the full price
   * of the new product will be charged. If `true` is sent, the billing period will not change and a
   * prorated charge will be issued for the new product.
   *
   * @default false
   */
  preservePeriod?: boolean;
  /**
   * The handle of the target Product. Either a product_id or product_handle must be present. A
   * Subscription can be migrated to another product for both the current Product Family and another
   * Product Family. Note: Going to another Product Family, components will not be migrated as well.
   */
  productHandle?: string;
  /**
   * The ID or handle of the specified product's price point. This can be passed to migrate to a
   * non-default price point.
   */
  productPricePointHandle?: string;
  proration?: Proration;
  /** The date that the proration is calculated from for the preview */
  prorationDate?: Date;
};

export const subscriptionMigrationPreviewOptionsSchema: Schema<SubscriptionMigrationPreviewOptions> =
  s.object<SubscriptionMigrationPreviewOptions>({
    productId: s.optional(s.int()),
    productPricePointId: s.optional(s.int()),
    includeTrial: s.defaulted(s.boolean(), false),
    includeInitialCharge: s.defaulted(s.boolean(), false),
    includeCoupons: s.defaulted(s.boolean(), true),
    preservePeriod: s.defaulted(s.boolean(), false),
    productHandle: s.optional(s.string()),
    productPricePointHandle: s.optional(s.string()),
    proration: s.optional(s.lazy(() => prorationSchema)),
    prorationDate: s.optional(s.dateTime()),
    _keysMap: {
      productId: "product_id",
      productPricePointId: "product_price_point_id",
      includeTrial: "include_trial",
      includeInitialCharge: "include_initial_charge",
      includeCoupons: "include_coupons",
      preservePeriod: "preserve_period",
      productHandle: "product_handle",
      productPricePointHandle: "product_price_point_handle",
      prorationDate: "proration_date",
    },
  });
