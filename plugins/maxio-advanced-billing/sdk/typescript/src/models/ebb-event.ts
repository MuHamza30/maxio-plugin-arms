import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { chargifyEbbSchema, type ChargifyEbb } from "./chargify-ebb.js";

export type EbbEvent = {
  chargify?: ChargifyEbb;
};

export const ebbEventSchema: Schema<EbbEvent> = s.object<EbbEvent>({
  chargify: s.optional(s.lazy(() => chargifyEbbSchema)),
});
