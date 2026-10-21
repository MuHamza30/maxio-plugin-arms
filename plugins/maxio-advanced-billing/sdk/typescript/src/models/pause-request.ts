import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { autoResumeSchema, type AutoResume } from "./auto-resume.js";

/** Allows you to pause a Subscription. */
export type PauseRequest = {
  hold?: AutoResume;
};

export const pauseRequestSchema: Schema<PauseRequest> = s.object<PauseRequest>({
  hold: s.optional(s.lazy(() => autoResumeSchema)),
});
