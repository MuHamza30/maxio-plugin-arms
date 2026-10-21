import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ResentInvitation = {
  /**
   * @deprecated
   */
  lastSentAt?: string;
  /**
   * @deprecated
   */
  lastAcceptedAt?: string;
  sendInviteLinkText?: string;
  uninvitedCount?: number;
  lastInviteSentAt?: Date;
  lastInviteAcceptedAt?: Date;
};

export const resentInvitationSchema: Schema<ResentInvitation> = s.object<ResentInvitation>({
  lastSentAt: s.optional(s.string()),
  lastAcceptedAt: s.optional(s.string()),
  sendInviteLinkText: s.optional(s.string()),
  uninvitedCount: s.optional(s.int()),
  lastInviteSentAt: s.optional(s.dateTime()),
  lastInviteAcceptedAt: s.optional(s.dateTime()),
  _keysMap: {
    lastSentAt: "last_sent_at",
    lastAcceptedAt: "last_accepted_at",
    sendInviteLinkText: "send_invite_link_text",
    uninvitedCount: "uninvited_count",
    lastInviteSentAt: "last_invite_sent_at",
    lastInviteAcceptedAt: "last_invite_accepted_at",
  },
});
