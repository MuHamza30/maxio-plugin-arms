import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type Errors = {
  perPage?: string[];
  pricePoint?: string[];
};

export const errorsSchema: Schema<Errors> = s.object<Errors>({
  perPage: s.optional(s.array(s.string())),
  pricePoint: s.optional(s.array(s.string())),
  _keysMap: {
    perPage: "per_page",
    pricePoint: "price_point",
  },
});
