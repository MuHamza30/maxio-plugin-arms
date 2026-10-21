import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type OkResponse = {
  ok?: string;
};

export const okResponseSchema: Schema<OkResponse> = s.object<OkResponse>({
  ok: s.optional(s.string()),
});
