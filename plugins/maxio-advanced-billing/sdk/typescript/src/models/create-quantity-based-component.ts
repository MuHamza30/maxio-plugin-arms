import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { quantityBasedComponentSchema, type QuantityBasedComponent } from "./quantity-based-component.js";

export type CreateQuantityBasedComponent = {
  quantityBasedComponent: QuantityBasedComponent;
};

export const createQuantityBasedComponentSchema: Schema<CreateQuantityBasedComponent> =
  s.object<CreateQuantityBasedComponent>({
    quantityBasedComponent: quantityBasedComponentSchema,
    _keysMap: {
      quantityBasedComponent: "quantity_based_component",
    },
  });
