import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  eventBasedBillingSegmentErrorSchema,
  type EventBasedBillingSegmentError,
} from "./event-based-billing-segment-error.js";

export type EventBasedBillingSegment = {
  errors: EventBasedBillingSegmentError;
};

export const eventBasedBillingSegmentSchema: Schema<EventBasedBillingSegment> =
  s.object<EventBasedBillingSegment>({
    errors: eventBasedBillingSegmentErrorSchema,
  });
