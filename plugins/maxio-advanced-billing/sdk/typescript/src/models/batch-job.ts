import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type BatchJob = {
  id?: number;
  finishedAt?: Date | null;
  rowCount?: number | null;
  createdAt?: Date | null;
  completed?: string;
};

export const batchJobSchema: Schema<BatchJob> = s.object<BatchJob>({
  id: s.optional(s.int()),
  finishedAt: s.optionalNullable(s.dateTime()),
  rowCount: s.optionalNullable(s.int()),
  createdAt: s.optionalNullable(s.dateTime()),
  completed: s.optional(s.string()),
  _keysMap: {
    finishedAt: "finished_at",
    rowCount: "row_count",
    createdAt: "created_at",
  },
});
