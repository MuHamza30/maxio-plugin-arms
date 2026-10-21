import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ExpirationIntervalUnit = {
  Day: "day",
  Month: "month",
  Never: "never",
} as const;
export type ExpirationIntervalUnit =
  | (typeof ExpirationIntervalUnit)[keyof typeof ExpirationIntervalUnit]
  | (string & {});

export const expirationIntervalUnitSchema: EnumSchema<ExpirationIntervalUnit> =
  s.enumOf<ExpirationIntervalUnit>(ExpirationIntervalUnit);
