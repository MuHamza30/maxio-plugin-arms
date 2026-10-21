import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { errorsSchema, type Errors } from "./errors.js";

export type EventBasedBillingListSegmentsErrors1 = {
  errors?: Errors;
};

export const eventBasedBillingListSegmentsErrors1Schema: Schema<EventBasedBillingListSegmentsErrors1> =
  s.object<EventBasedBillingListSegmentsErrors1>({
    errors: s.optional(s.lazy(() => errorsSchema)),
  });
