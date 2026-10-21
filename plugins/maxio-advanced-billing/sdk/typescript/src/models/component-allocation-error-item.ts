import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ComponentAllocationErrorItem = {
  componentId?: number;
  message?: string;
  kind?: string;
  on?: string;
};

export const componentAllocationErrorItemSchema: Schema<ComponentAllocationErrorItem> =
  s.object<ComponentAllocationErrorItem>({
    componentId: s.optional(s.int()),
    message: s.optional(s.string()),
    kind: s.optional(s.string()),
    on: s.optional(s.string()),
    _keysMap: {
      componentId: "component_id",
    },
  });
