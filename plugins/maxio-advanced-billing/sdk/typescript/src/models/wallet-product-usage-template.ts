import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/**
 * One wallet template billing through this Wallet Product, joined to the Feature and plan/component
 * that assigns it, when there is one.
 */
export type WalletProductUsageTemplate = {
  /**
   * The name of the product or component the Feature is assigned to. `null` when the wallet
   * template has no assigning Feature.
   */
  planName?: string | null;
  /**
   * The label set in `wallet_behavior.name` on the Feature, or the standalone wallet's own `name`.
   */
  walletTemplateName?: string | null;
  unitName?: string;
  /**
   * A best-effort label for how this wallet is expected to be replenished. Currently reports
   * `"Overage"` when the wallet template allows a negative balance, and `null` otherwise; there's
   * no persisted field yet distinguishing, for example, an intended "Auto top-up" from "Purchase
   * more" setup. Treat this as informational, not a stable enum.
   */
  purchaseMechanism?: string | null;
  pricePointName?: string | null;
  currency?: string;
  /** `false` when the assigning Feature is archived. */
  active?: boolean;
  featureTemplateId?: number | null;
  featureTemplateName?: string | null;
  /**
   * `true` when this wallet template is priced at a price point other than the Wallet Product's
   * default.
   */
  pricePointOverride?: boolean;
};

export const walletProductUsageTemplateSchema: Schema<WalletProductUsageTemplate> =
  s.object<WalletProductUsageTemplate>({
    planName: s.optionalNullable(s.string()),
    walletTemplateName: s.optionalNullable(s.string()),
    unitName: s.optional(s.string()),
    purchaseMechanism: s.optionalNullable(s.string()),
    pricePointName: s.optionalNullable(s.string()),
    currency: s.optional(s.string()),
    active: s.optional(s.boolean()),
    featureTemplateId: s.optionalNullable(s.int()),
    featureTemplateName: s.optionalNullable(s.string()),
    pricePointOverride: s.optional(s.boolean()),
    _keysMap: {
      planName: "plan_name",
      walletTemplateName: "wallet_template_name",
      unitName: "unit_name",
      purchaseMechanism: "purchase_mechanism",
      pricePointName: "price_point_name",
      featureTemplateId: "feature_template_id",
      featureTemplateName: "feature_template_name",
      pricePointOverride: "price_point_override",
    },
  });
