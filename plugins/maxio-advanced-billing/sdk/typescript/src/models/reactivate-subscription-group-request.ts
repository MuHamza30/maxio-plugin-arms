import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ReactivateSubscriptionGroupRequest = {
  resume?: boolean;
  resumeMembers?: boolean;
};

export const reactivateSubscriptionGroupRequestSchema: Schema<ReactivateSubscriptionGroupRequest> =
  s.object<ReactivateSubscriptionGroupRequest>({
    resume: s.optional(s.boolean()),
    resumeMembers: s.optional(s.boolean()),
    _keysMap: {
      resumeMembers: "resume_members",
    },
  });
