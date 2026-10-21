import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { allocationPreviewSchema, type AllocationPreview } from "./allocation-preview.js";

export type AllocationPreviewResponse = {
  allocationPreview: AllocationPreview;
};

export const allocationPreviewResponseSchema: Schema<AllocationPreviewResponse> =
  s.object<AllocationPreviewResponse>({
    allocationPreview: allocationPreviewSchema,
    _keysMap: {
      allocationPreview: "allocation_preview",
    },
  });
