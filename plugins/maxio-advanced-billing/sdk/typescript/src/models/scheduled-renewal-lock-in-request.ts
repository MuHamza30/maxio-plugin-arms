import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ScheduledRenewalLockInRequest = {
  /** Date to lock in the renewal. */
  lockInAt: string;
};

export const scheduledRenewalLockInRequestSchema: Schema<ScheduledRenewalLockInRequest> =
  s.object<ScheduledRenewalLockInRequest>({
    lockInAt: s.dateOnly(),
    _keysMap: {
      lockInAt: "lock_in_at",
    },
  });
