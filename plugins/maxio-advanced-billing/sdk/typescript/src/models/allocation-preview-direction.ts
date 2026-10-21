import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const AllocationPreviewDirection = {
  Upgrade: "upgrade",
  Downgrade: "downgrade",
} as const;
export type AllocationPreviewDirection =
  | (typeof AllocationPreviewDirection)[keyof typeof AllocationPreviewDirection]
  | (string & {});

export const allocationPreviewDirectionSchema: EnumSchema<AllocationPreviewDirection> =
  s.enumOf<AllocationPreviewDirection>(AllocationPreviewDirection);
