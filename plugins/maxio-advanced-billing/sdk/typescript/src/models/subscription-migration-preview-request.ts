import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionMigrationPreviewOptionsSchema,
  type SubscriptionMigrationPreviewOptions,
} from "./subscription-migration-preview-options.js";

export type SubscriptionMigrationPreviewRequest = {
  migration: SubscriptionMigrationPreviewOptions;
};

export const subscriptionMigrationPreviewRequestSchema: Schema<SubscriptionMigrationPreviewRequest> =
  s.object<SubscriptionMigrationPreviewRequest>({
    migration: subscriptionMigrationPreviewOptionsSchema,
  });
