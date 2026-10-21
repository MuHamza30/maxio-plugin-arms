import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ReferralCode = {
  id?: number;
  siteId?: number;
  subscriptionId?: number;
  code?: string;
};

export const referralCodeSchema: Schema<ReferralCode> = s.object<ReferralCode>({
  id: s.optional(s.int()),
  siteId: s.optional(s.int()),
  subscriptionId: s.optional(s.int()),
  code: s.optional(s.string()),
  _keysMap: {
    siteId: "site_id",
    subscriptionId: "subscription_id",
  },
});
