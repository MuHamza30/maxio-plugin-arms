import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type DelayedCancellationResponse = {
  message?: string;
};

export const delayedCancellationResponseSchema: Schema<DelayedCancellationResponse> =
  s.object<DelayedCancellationResponse>({
    message: s.optional(s.string()),
  });
