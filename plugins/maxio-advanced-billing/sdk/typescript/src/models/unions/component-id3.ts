import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Component handle or component id. */
export type ComponentId3 = string | number;

export const componentId3Schema: Schema<ComponentId3> = s.of<ComponentId3>(s.union([s.string(), s.int()]));
