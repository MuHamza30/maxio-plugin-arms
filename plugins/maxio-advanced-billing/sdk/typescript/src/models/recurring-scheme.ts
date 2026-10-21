import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const RecurringScheme = {
  DoNotRecur: "do_not_recur",
  RecurIndefinitely: "recur_indefinitely",
  RecurWithDuration: "recur_with_duration",
} as const;
export type RecurringScheme = (typeof RecurringScheme)[keyof typeof RecurringScheme] | (string & {});

export const recurringSchemeSchema: EnumSchema<RecurringScheme> = s.enumOf<RecurringScheme>(RecurringScheme);
