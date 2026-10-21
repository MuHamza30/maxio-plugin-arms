import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const Status = {
  Draft: "draft",
  Scheduled: "scheduled",
  Pending: "pending",
  Canceled: "canceled",
  Active: "active",
  Fulfilled: "fulfilled",
} as const;
export type Status = (typeof Status)[keyof typeof Status] | (string & {});

export const statusSchema: EnumSchema<Status> = s.enumOf<Status>(Status);
