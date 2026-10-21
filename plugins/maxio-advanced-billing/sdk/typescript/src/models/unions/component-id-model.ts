import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type ComponentIdModel = number | string;

export const componentIdModelSchema: Schema<ComponentIdModel> = s.of<ComponentIdModel>(
  s.union([s.int(), s.string()]),
);
