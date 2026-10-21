import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type ComponentId1 = number | string;

export const componentId1Schema: Schema<ComponentId1> = s.of<ComponentId1>(s.union([s.int(), s.string()]));
