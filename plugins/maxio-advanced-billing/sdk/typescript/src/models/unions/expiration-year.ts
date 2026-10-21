import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type ExpirationYear = string | number;

export const expirationYearSchema: Schema<ExpirationYear> = s.of<ExpirationYear>(
  s.union([s.string(), s.int()]),
);
