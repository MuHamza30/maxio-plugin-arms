import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CountResponse = {
  count?: number;
};

export const countResponseSchema: Schema<CountResponse> = s.object<CountResponse>({
  count: s.optional(s.int()),
});
