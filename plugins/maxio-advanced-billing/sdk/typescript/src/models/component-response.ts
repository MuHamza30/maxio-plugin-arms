import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentSchema, type Component } from "./component.js";

export type ComponentResponse = {
  component: Component;
};

export const componentResponseSchema: Schema<ComponentResponse> = s.object<ComponentResponse>({
  component: componentSchema,
});
