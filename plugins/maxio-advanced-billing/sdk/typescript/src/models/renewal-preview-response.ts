import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { renewalPreviewSchema, type RenewalPreview } from "./renewal-preview.js";

export type RenewalPreviewResponse = {
  renewalPreview: RenewalPreview;
};

export const renewalPreviewResponseSchema: Schema<RenewalPreviewResponse> = s.object<RenewalPreviewResponse>({
  renewalPreview: renewalPreviewSchema,
  _keysMap: {
    renewalPreview: "renewal_preview",
  },
});
