import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreateProductFamily = {
  name: string;
  handle?: string | null;
  description?: string | null;
  /**
   * Whether surcharging applies to this product family. Defaults to `true` when omitted. Only
   * applied on sites where surcharging is enabled.
   */
  surcharging?: boolean;
};

export const createProductFamilySchema: Schema<CreateProductFamily> = s.object<CreateProductFamily>({
  name: s.string(),
  handle: s.optionalNullable(s.string()),
  description: s.optionalNullable(s.string()),
  surcharging: s.optional(s.boolean()),
});
