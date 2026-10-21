import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type NestedSubscriptionGroup = {
  /** The UID for the group */
  uid?: string;
  /**
   * Whether the group is configured to rely on a primary subscription for billing. At this time, it
   * will always be 1.
   */
  scheme?: number;
  /** The subscription ID of the primary within the group. Applicable to scheme 1. */
  primarySubscriptionId?: number;
  /**
   * A boolean indicating whether the subscription is the primary in the group. Applicable to scheme
   * 1.
   */
  primary?: boolean;
};

export const nestedSubscriptionGroupSchema: Schema<NestedSubscriptionGroup> =
  s.object<NestedSubscriptionGroup>({
    uid: s.optional(s.string()),
    scheme: s.optional(s.int()),
    primarySubscriptionId: s.optional(s.int()),
    primary: s.optional(s.boolean()),
    _keysMap: {
      primarySubscriptionId: "primary_subscription_id",
    },
  });
