import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type UpdateSubscriptionGroup = {
  memberIds?: number[];
};

export const updateSubscriptionGroupSchema: Schema<UpdateSubscriptionGroup> =
  s.object<UpdateSubscriptionGroup>({
    memberIds: s.optional(s.array(s.int())),
    _keysMap: {
      memberIds: "member_ids",
    },
  });
