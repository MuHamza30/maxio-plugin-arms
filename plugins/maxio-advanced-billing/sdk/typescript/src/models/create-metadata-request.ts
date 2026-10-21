import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createMetadataSchema, type CreateMetadata } from "./create-metadata.js";

export type CreateMetadataRequest = {
  metadata: CreateMetadata[];
};

export const createMetadataRequestSchema: Schema<CreateMetadataRequest> = s.object<CreateMetadataRequest>({
  metadata: s.array(s.lazy(() => createMetadataSchema)),
});
