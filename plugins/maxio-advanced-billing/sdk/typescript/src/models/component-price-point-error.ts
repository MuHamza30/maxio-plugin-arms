import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  componentPricePointErrorItemSchema,
  type ComponentPricePointErrorItem,
} from "./component-price-point-error-item.js";

export type ComponentPricePointError = {
  errors?: ComponentPricePointErrorItem[];
};

export const componentPricePointErrorSchema: Schema<ComponentPricePointError> =
  s.object<ComponentPricePointError>({
    errors: s.optional(s.array(s.lazy(() => componentPricePointErrorItemSchema))),
  });
