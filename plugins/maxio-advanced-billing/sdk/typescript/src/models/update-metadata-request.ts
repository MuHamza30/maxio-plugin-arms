import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateMetadataSchema, type UpdateMetadata } from "./update-metadata.js";

export type UpdateMetadataRequest = {
  metadata?: UpdateMetadata;
};

export const updateMetadataRequestSchema: Schema<UpdateMetadataRequest> = s.object<UpdateMetadataRequest>({
  metadata: s.optional(s.lazy(() => updateMetadataSchema)),
});
