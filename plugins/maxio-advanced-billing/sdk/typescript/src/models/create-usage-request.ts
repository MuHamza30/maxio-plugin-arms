import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createUsageSchema, type CreateUsage } from "./create-usage.js";

export type CreateUsageRequest = {
  usage: CreateUsage;
};

export const createUsageRequestSchema: Schema<CreateUsageRequest> = s.object<CreateUsageRequest>({
  usage: createUsageSchema,
});
