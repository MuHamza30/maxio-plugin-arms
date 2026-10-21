import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const CreditScheme = {
  None: "none",
  Credit: "credit",
  Refund: "refund",
} as const;
export type CreditScheme = (typeof CreditScheme)[keyof typeof CreditScheme] | (string & {});

export const creditSchemeSchema: EnumSchema<CreditScheme> = s.enumOf<CreditScheme>(CreditScheme);
