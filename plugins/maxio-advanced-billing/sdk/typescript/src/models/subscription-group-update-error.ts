import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionGroupUpdateError = {
  members?: string[];
};

export const subscriptionGroupUpdateErrorSchema: Schema<SubscriptionGroupUpdateError> =
  s.object<SubscriptionGroupUpdateError>({
    members: s.optional(s.array(s.string())),
  });
