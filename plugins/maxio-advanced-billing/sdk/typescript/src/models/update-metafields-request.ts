import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { metafields1Schema, type Metafields1 } from "./unions/metafields1.js";

export type UpdateMetafieldsRequest = {
  metafields?: Metafields1;
};

export const updateMetafieldsRequestSchema: Schema<UpdateMetafieldsRequest> =
  s.object<UpdateMetafieldsRequest>({
    metafields: s.optional(s.lazy(() => metafields1Schema)),
  });
