import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateComponentSchema, type UpdateComponent } from "./update-component.js";

export type UpdateComponentRequest = {
  component: UpdateComponent;
};

export const updateComponentRequestSchema: Schema<UpdateComponentRequest> = s.object<UpdateComponentRequest>({
  component: updateComponentSchema,
});
