import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PendingCancellationChange = {
  cancellationState: string;
  cancelsAt: Date;
};

export const pendingCancellationChangeSchema: Schema<PendingCancellationChange> =
  s.object<PendingCancellationChange>({
    cancellationState: s.string(),
    cancelsAt: s.dateTime(),
    _keysMap: {
      cancellationState: "cancellation_state",
      cancelsAt: "cancels_at",
    },
  });
