import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CloneComponentPricePoint = {
  name: string;
  handle?: string;
};

export const cloneComponentPricePointSchema: Schema<CloneComponentPricePoint> =
  s.object<CloneComponentPricePoint>({
    name: s.string(),
    handle: s.optional(s.string()),
  });
