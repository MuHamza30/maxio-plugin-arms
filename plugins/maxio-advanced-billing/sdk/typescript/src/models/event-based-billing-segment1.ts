import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  eventBasedBillingSegmentErrorSchema,
  type EventBasedBillingSegmentError,
} from "./event-based-billing-segment-error.js";

export type EventBasedBillingSegment1 = {
  errors: EventBasedBillingSegmentError;
};

export const eventBasedBillingSegment1Schema: Schema<EventBasedBillingSegment1> =
  s.object<EventBasedBillingSegment1>({
    errors: eventBasedBillingSegmentErrorSchema,
  });
