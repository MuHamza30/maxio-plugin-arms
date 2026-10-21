import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type Proration = {
  /** The alternative to sending preserve_period as a direct attribute to migration */
  preservePeriod?: boolean;
};

export const prorationSchema: Schema<Proration> = s.object<Proration>({
  preservePeriod: s.optional(s.boolean()),
  _keysMap: {
    preservePeriod: "preserve_period",
  },
});
