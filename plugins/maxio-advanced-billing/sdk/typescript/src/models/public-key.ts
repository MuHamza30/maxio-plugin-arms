import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PublicKey = {
  publicKey?: string;
  requiresSecurityToken?: boolean;
  createdAt?: Date;
};

export const publicKeySchema: Schema<PublicKey> = s.object<PublicKey>({
  publicKey: s.optional(s.string()),
  requiresSecurityToken: s.optional(s.boolean()),
  createdAt: s.optional(s.dateTime()),
  _keysMap: {
    publicKey: "public_key",
    requiresSecurityToken: "requires_security_token",
    createdAt: "created_at",
  },
});
