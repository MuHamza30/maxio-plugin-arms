import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Used for metered and events based components. */
export type UnitBalance2 = number | string;

export const unitBalance2Schema: Schema<UnitBalance2> = s.of<UnitBalance2>(s.union([s.int(), s.string()]));
