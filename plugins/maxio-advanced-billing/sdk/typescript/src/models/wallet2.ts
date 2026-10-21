import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type Wallet2 = {
  /**
   * A merchant-facing label for the wallet. Surrounding spaces are stripped; a blank or `null`
   * value clears it.
   */
  name?: string | null;
};

export const wallet2Schema: Schema<Wallet2> = s.object<Wallet2>({
  name: s.optionalNullable(s.string()),
});
