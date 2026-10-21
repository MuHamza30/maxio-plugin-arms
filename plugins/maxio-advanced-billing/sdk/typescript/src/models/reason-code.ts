import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ReasonCode = {
  id?: number;
  siteId?: number;
  code?: string;
  description?: string;
  position?: number;
  createdAt?: Date;
  updatedAt?: Date;
};

export const reasonCodeSchema: Schema<ReasonCode> = s.object<ReasonCode>({
  id: s.optional(s.int()),
  siteId: s.optional(s.int()),
  code: s.optional(s.string()),
  description: s.optional(s.string()),
  position: s.optional(s.int()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  _keysMap: {
    siteId: "site_id",
    createdAt: "created_at",
    updatedAt: "updated_at",
  },
});
