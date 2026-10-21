import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionProductMigrationSchema,
  type SubscriptionProductMigration,
} from "./subscription-product-migration.js";

export type SubscriptionProductMigrationRequest = {
  migration: SubscriptionProductMigration;
};

export const subscriptionProductMigrationRequestSchema: Schema<SubscriptionProductMigrationRequest> =
  s.object<SubscriptionProductMigrationRequest>({
    migration: subscriptionProductMigrationSchema,
  });
