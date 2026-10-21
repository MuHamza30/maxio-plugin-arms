import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditSchemeSchema, type CreditScheme } from "./credit-scheme.js";

export type CreditSchemeRequest = {
  creditScheme: CreditScheme;
};

export const creditSchemeRequestSchema: Schema<CreditSchemeRequest> = s.object<CreditSchemeRequest>({
  creditScheme: creditSchemeSchema,
  _keysMap: {
    creditScheme: "credit_scheme",
  },
});
