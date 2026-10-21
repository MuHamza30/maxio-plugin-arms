import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { batchJobSchema, type BatchJob } from "./batch-job.js";

export type BatchJobResponse = {
  batchjob: BatchJob;
};

export const batchJobResponseSchema: Schema<BatchJobResponse> = s.object<BatchJobResponse>({
  batchjob: batchJobSchema,
});
