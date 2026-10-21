import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { cancellationOptionsSchema, type CancellationOptions } from "./cancellation-options.js";

export type CancellationRequest = {
  subscription: CancellationOptions;
};

export const cancellationRequestSchema: Schema<CancellationRequest> = s.object<CancellationRequest>({
  subscription: cancellationOptionsSchema,
});
