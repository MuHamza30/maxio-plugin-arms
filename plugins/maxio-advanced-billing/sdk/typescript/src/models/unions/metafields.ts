import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { createMetafieldSchema, type CreateMetafield } from "../create-metafield.js";

export type Metafields = CreateMetafield | CreateMetafield[];

export const metafieldsSchema: Schema<Metafields> = s.of<Metafields>(
  s.union([s.lazy(() => createMetafieldSchema), s.array(s.lazy(() => createMetafieldSchema))]),
);
