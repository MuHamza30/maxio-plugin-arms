import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { usageSchema, type Usage } from "./usage.js";

export type UsageResponse = {
  usage: Usage;
};

export const usageResponseSchema: Schema<UsageResponse> = s.object<UsageResponse>({
  usage: usageSchema,
});
