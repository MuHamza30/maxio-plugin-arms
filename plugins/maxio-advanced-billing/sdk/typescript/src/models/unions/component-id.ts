import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Required if passing any component to `components` attribute. */
export type ComponentId = string | number;

export const componentIdSchema: Schema<ComponentId> = s.of<ComponentId>(s.union([s.string(), s.int()]));
