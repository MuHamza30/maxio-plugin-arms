import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type UpdateMetadata = {
  currentName?: string;
  name?: string;
  value?: string;
};

export const updateMetadataSchema: Schema<UpdateMetadata> = s.object<UpdateMetadata>({
  currentName: s.optional(s.string()),
  name: s.optional(s.string()),
  value: s.optional(s.string()),
  _keysMap: {
    currentName: "current_name",
  },
});
