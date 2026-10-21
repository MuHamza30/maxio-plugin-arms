import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/**
 * The metering meter this wallet is paired with, or `null` for a wallet with no meter. Set on
 * create and immutable afterward.
 */
export type Meter = {
  id?: number;
  name?: string;
  handle?: string;
  /** How many wallet units one meter unit is worth, as a decimal string. Defaults to `"1.0"`. */
  conversionRate?: string;
};

export const meterSchema: Schema<Meter> = s.object<Meter>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  handle: s.optional(s.string()),
  conversionRate: s.optional(s.string()),
  _keysMap: {
    conversionRate: "conversion_rate",
  },
});
