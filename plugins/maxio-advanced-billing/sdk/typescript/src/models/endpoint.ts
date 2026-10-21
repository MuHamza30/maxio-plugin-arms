import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type Endpoint = {
  id?: number;
  url?: string;
  siteId?: number;
  status?: string;
  webhookSubscriptions?: string[];
};

export const endpointSchema: Schema<Endpoint> = s.object<Endpoint>({
  id: s.optional(s.int()),
  url: s.optional(s.string()),
  siteId: s.optional(s.int()),
  status: s.optional(s.string()),
  webhookSubscriptions: s.optional(s.array(s.string())),
  _keysMap: {
    siteId: "site_id",
    webhookSubscriptions: "webhook_subscriptions",
  },
});
