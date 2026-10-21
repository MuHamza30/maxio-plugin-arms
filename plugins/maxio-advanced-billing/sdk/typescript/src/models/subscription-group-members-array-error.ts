import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionGroupMembersArrayError = {
  members: string[];
};

export const subscriptionGroupMembersArrayErrorSchema: Schema<SubscriptionGroupMembersArrayError> =
  s.object<SubscriptionGroupMembersArrayError>({
    members: s.array(s.string()),
  });
