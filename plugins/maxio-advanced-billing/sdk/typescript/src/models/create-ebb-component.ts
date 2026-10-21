import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { ebbComponentSchema, type EbbComponent } from "./ebb-component.js";

export type CreateEbbComponent = {
  eventBasedComponent: EbbComponent;
};

export const createEbbComponentSchema: Schema<CreateEbbComponent> = s.object<CreateEbbComponent>({
  eventBasedComponent: ebbComponentSchema,
  _keysMap: {
    eventBasedComponent: "event_based_component",
  },
});
