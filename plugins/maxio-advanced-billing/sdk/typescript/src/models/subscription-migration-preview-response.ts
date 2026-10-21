import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionMigrationPreviewSchema,
  type SubscriptionMigrationPreview,
} from "./subscription-migration-preview.js";

export type SubscriptionMigrationPreviewResponse = {
  migration: SubscriptionMigrationPreview;
};

export const subscriptionMigrationPreviewResponseSchema: Schema<SubscriptionMigrationPreviewResponse> =
  s.object<SubscriptionMigrationPreviewResponse>({
    migration: subscriptionMigrationPreviewSchema,
  });
