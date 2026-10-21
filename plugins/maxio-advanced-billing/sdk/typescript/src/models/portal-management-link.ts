import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PortalManagementLink = {
  url?: string;
  fetchCount?: number;
  createdAt?: Date;
  newLinkAvailableAt?: Date;
  expiresAt?: Date;
  lastInviteSentAt?: Date | null;
};

export const portalManagementLinkSchema: Schema<PortalManagementLink> = s.object<PortalManagementLink>({
  url: s.optional(s.string()),
  fetchCount: s.optional(s.int()),
  createdAt: s.optional(s.dateTime()),
  newLinkAvailableAt: s.optional(s.dateTime()),
  expiresAt: s.optional(s.dateTime()),
  lastInviteSentAt: s.optionalNullable(s.dateTime()),
  _keysMap: {
    fetchCount: "fetch_count",
    createdAt: "created_at",
    newLinkAvailableAt: "new_link_available_at",
    expiresAt: "expires_at",
    lastInviteSentAt: "last_invite_sent_at",
  },
});
