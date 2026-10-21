import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { eventSchema, type Event } from "./event.js";

export type EventResponse = {
  event: Event;
};

export const eventResponseSchema: Schema<EventResponse> = s.object<EventResponse>({
  event: eventSchema,
});
