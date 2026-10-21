import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type EventBasedBillingSegmentError = {
  /**
   * The key of the object would be a number (an index in the request array) where the error
   * occurred. In the value object, the key represents the field and the value is an array with
   * error messages. In most cases, this object would contain just one key.
   */
  segments: Record<string, Record<string, unknown>>;
};

export const eventBasedBillingSegmentErrorSchema: Schema<EventBasedBillingSegmentError> =
  s.object<EventBasedBillingSegmentError>({
    segments: s.record(s.string(), s.record(s.string(), s.unknown())),
  });
