import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { billingManifestSchema, type BillingManifest } from "./billing-manifest.js";

export type SubscriptionPreview = {
  currentBillingManifest?: BillingManifest;
  nextBillingManifest?: BillingManifest;
};

export const subscriptionPreviewSchema: Schema<SubscriptionPreview> = s.object<SubscriptionPreview>({
  currentBillingManifest: s.optional(s.lazy(() => billingManifestSchema)),
  nextBillingManifest: s.optional(s.lazy(() => billingManifestSchema)),
  _keysMap: {
    currentBillingManifest: "current_billing_manifest",
    nextBillingManifest: "next_billing_manifest",
  },
});
