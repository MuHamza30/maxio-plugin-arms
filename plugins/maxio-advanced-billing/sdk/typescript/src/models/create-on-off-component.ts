import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { onOffComponentSchema, type OnOffComponent } from "./on-off-component.js";

export type CreateOnOffComponent = {
  onOffComponent: OnOffComponent;
};

export const createOnOffComponentSchema: Schema<CreateOnOffComponent> = s.object<CreateOnOffComponent>({
  onOffComponent: onOffComponentSchema,
  _keysMap: {
    onOffComponent: "on_off_component",
  },
});
