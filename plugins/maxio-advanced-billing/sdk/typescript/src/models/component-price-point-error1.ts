import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  componentPricePointErrorItemSchema,
  type ComponentPricePointErrorItem,
} from "./component-price-point-error-item.js";

export type ComponentPricePointError1 = {
  errors?: ComponentPricePointErrorItem[];
};

export const componentPricePointError1Schema: Schema<ComponentPricePointError1> =
  s.object<ComponentPricePointError1>({
    errors: s.optional(s.array(s.lazy(() => componentPricePointErrorItemSchema))),
  });
