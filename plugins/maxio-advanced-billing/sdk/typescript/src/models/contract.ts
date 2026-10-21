import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { registerSchema, type Register } from "./register.js";

/** Contract linked to the scheduled renewal configuration. */
export type Contract = {
  id?: number;
  maxioId?: string;
  number?: string | null;
  register?: Register;
};

export const contractSchema: Schema<Contract> = s.object<Contract>({
  id: s.optional(s.int()),
  maxioId: s.optional(s.string()),
  number: s.optionalNullable(s.string()),
  register: s.optional(s.lazy(() => registerSchema)),
  _keysMap: {
    maxioId: "maxio_id",
  },
});
