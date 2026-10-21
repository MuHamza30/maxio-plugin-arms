import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type ExpirationMonth = string | number;

export const expirationMonthSchema: Schema<ExpirationMonth> = s.of<ExpirationMonth>(
  s.union([s.string(), s.int()]),
);
