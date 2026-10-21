import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { updateMetafieldSchema, type UpdateMetafield } from "../update-metafield.js";

export type Metafields1 = UpdateMetafield | UpdateMetafield[];

export const metafields1Schema: Schema<Metafields1> = s.of<Metafields1>(
  s.union([s.lazy(() => updateMetafieldSchema), s.array(s.lazy(() => updateMetafieldSchema))]),
);
