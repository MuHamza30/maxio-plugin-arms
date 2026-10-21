import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/**
 * Event data for both `subscription_product_change` and `subscription_product_change_scheduled`.
 * The price point and `effective_at` fields are only populated for scheduled changes.
 */
export type SubscriptionProductChange = {
  previousProductId: number;
  newProductId: number;
  previousProductPricePointId?: number | null;
  newProductPricePointId?: number | null;
  /**
   * When the scheduled product change takes effect (the subscription's next renewal). Only sent for
   * `subscription_product_change_scheduled`.
   */
  effectiveAt?: Date | null;
};

export const subscriptionProductChangeSchema: Schema<SubscriptionProductChange> =
  s.object<SubscriptionProductChange>({
    previousProductId: s.int(),
    newProductId: s.int(),
    previousProductPricePointId: s.optionalNullable(s.int()),
    newProductPricePointId: s.optionalNullable(s.int()),
    effectiveAt: s.optionalNullable(s.dateTime()),
    _keysMap: {
      previousProductId: "previous_product_id",
      newProductId: "new_product_id",
      previousProductPricePointId: "previous_product_price_point_id",
      newProductPricePointId: "new_product_price_point_id",
      effectiveAt: "effective_at",
    },
  });
