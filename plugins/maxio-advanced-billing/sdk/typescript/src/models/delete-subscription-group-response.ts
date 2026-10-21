import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type DeleteSubscriptionGroupResponse = {
  uid?: string;
  deleted?: boolean;
};

export const deleteSubscriptionGroupResponseSchema: Schema<DeleteSubscriptionGroupResponse> =
  s.object<DeleteSubscriptionGroupResponse>({
    uid: s.optional(s.string()),
    deleted: s.optional(s.boolean()),
  });
