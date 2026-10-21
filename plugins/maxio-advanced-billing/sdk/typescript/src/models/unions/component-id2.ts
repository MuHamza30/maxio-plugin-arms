import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Either the component's Chargify id or its handle prefixed with `handle:` */
export type ComponentId2 = string | number;

export const componentId2Schema: Schema<ComponentId2> = s.of<ComponentId2>(s.union([s.string(), s.int()]));
