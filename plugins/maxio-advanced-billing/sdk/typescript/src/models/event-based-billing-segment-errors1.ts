import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type EventBasedBillingSegmentErrors1 = {
  /**
   * The key of the object would be a number (an index in the request array) where the error
   * occurred. In the value object, the key represents the field and the value is an array with
   * error messages. In most cases, this object would contain just one key.
   */
  errors?: Record<string, Record<string, unknown>>;
};

export const eventBasedBillingSegmentErrors1Schema: Schema<EventBasedBillingSegmentErrors1> =
  s.object<EventBasedBillingSegmentErrors1>({
    errors: s.optional(s.record(s.string(), s.record(s.string(), s.unknown()))),
  });
