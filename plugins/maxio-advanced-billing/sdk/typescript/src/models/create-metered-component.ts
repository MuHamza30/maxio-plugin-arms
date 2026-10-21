import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { meteredComponentSchema, type MeteredComponent } from "./metered-component.js";

export type CreateMeteredComponent = {
  meteredComponent: MeteredComponent;
};

export const createMeteredComponentSchema: Schema<CreateMeteredComponent> = s.object<CreateMeteredComponent>({
  meteredComponent: meteredComponentSchema,
  _keysMap: {
    meteredComponent: "metered_component",
  },
});
