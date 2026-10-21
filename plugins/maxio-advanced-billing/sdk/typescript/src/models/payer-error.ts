import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PayerError = {
  lastName?: string[];
  firstName?: string[];
  email?: string[];
};

export const payerErrorSchema: Schema<PayerError> = s.object<PayerError>({
  lastName: s.optional(s.array(s.string())),
  firstName: s.optional(s.array(s.string())),
  email: s.optional(s.array(s.string())),
  _keysMap: {
    lastName: "last_name",
    firstName: "first_name",
  },
});
