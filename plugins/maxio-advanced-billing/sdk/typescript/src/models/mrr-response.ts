import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { mrrSchema, type Mrr } from "./mrr.js";

export type MrrResponse = {
  mrr: Mrr;
};

export const mrrResponseSchema: Schema<MrrResponse> = s.object<MrrResponse>({
  mrr: mrrSchema,
});
