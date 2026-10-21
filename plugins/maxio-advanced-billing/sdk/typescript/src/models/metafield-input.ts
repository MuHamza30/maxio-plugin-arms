import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * Indicates the type of metafield. A text metafield allows any string value. Dropdown and radio
 * metafields have a set of values that can be selected. Defaults to 'text'.
 */
export const MetafieldInput = {
  BalanceTracker: "balance_tracker",
  Text: "text",
  Radio: "radio",
  Dropdown: "dropdown",
} as const;
export type MetafieldInput = (typeof MetafieldInput)[keyof typeof MetafieldInput] | (string & {});

export const metafieldInputSchema: EnumSchema<MetafieldInput> = s.enumOf<MetafieldInput>(MetafieldInput);
