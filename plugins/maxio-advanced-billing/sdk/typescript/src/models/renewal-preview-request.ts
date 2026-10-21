import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { renewalPreviewComponentSchema, type RenewalPreviewComponent } from "./renewal-preview-component.js";

export type RenewalPreviewRequest = {
  /**
   * (Optional) Array of component definitions to preview. Providing any component definitions here
   * will override the actual components on the subscription (and their quantities), and the billing
   * preview will contain only these components (in addition to any product base fees).
   */
  components?: RenewalPreviewComponent[];
};

export const renewalPreviewRequestSchema: Schema<RenewalPreviewRequest> = s.object<RenewalPreviewRequest>({
  components: s.optional(s.array(s.lazy(() => renewalPreviewComponentSchema))),
});
