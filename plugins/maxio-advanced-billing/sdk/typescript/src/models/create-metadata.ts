import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreateMetadata = {
  name?: string;
  value?: string;
};

export const createMetadataSchema: Schema<CreateMetadata> = s.object<CreateMetadata>({
  name: s.optional(s.string()),
  value: s.optional(s.string()),
});
