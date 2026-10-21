import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type AllocationExpirationDate = {
  expiresAt?: Date;
};

export const allocationExpirationDateSchema: Schema<AllocationExpirationDate> =
  s.object<AllocationExpirationDate>({
    expiresAt: s.optional(s.dateTime()),
    _keysMap: {
      expiresAt: "expires_at",
    },
  });
