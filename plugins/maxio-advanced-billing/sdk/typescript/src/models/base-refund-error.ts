import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type BaseRefundError = {
  base?: Record<string, unknown>[];
};

export const baseRefundErrorSchema: Schema<BaseRefundError> = s.object<BaseRefundError>({
  base: s.optional(s.array(s.record(s.string(), s.unknown()))),
});
