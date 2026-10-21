import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { metafieldsSchema, type Metafields } from "./unions/metafields.js";

export type CreateMetafieldsRequest = {
  metafields: Metafields;
};

export const createMetafieldsRequestSchema: Schema<CreateMetafieldsRequest> =
  s.object<CreateMetafieldsRequest>({
    metafields: metafieldsSchema,
  });
