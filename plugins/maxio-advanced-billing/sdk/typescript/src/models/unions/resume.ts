import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { resumeOptionsSchema, type ResumeOptions } from "../resume-options.js";

/**
 * If `true`, Advanced Billing will attempt to resume the subscription's billing period. If not
 * resumable, the subscription will be reactivated with a new billing period. If `false` or omitted,
 * Advanced Billing will only attempt to reactivate the subscription with a new billing period,
 * regardless of whether or not the subscription is resumable.
 */
export type Resume = boolean | ResumeOptions;

export const resumeSchema: Schema<Resume> = s.of<Resume>(
  s.union([s.boolean(), s.lazy(() => resumeOptionsSchema)]),
);
