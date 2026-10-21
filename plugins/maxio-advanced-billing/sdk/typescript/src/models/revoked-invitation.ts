import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type RevokedInvitation = {
  lastSentAt?: string;
  lastAcceptedAt?: string;
  uninvitedCount?: number;
};

export const revokedInvitationSchema: Schema<RevokedInvitation> = s.object<RevokedInvitation>({
  lastSentAt: s.optional(s.string()),
  lastAcceptedAt: s.optional(s.string()),
  uninvitedCount: s.optional(s.int()),
  _keysMap: {
    lastSentAt: "last_sent_at",
    lastAcceptedAt: "last_accepted_at",
    uninvitedCount: "uninvited_count",
  },
});
