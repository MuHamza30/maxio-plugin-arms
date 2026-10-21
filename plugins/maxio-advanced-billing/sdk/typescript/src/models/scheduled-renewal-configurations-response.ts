import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  scheduledRenewalConfigurationSchema,
  type ScheduledRenewalConfiguration,
} from "./scheduled-renewal-configuration.js";

export type ScheduledRenewalConfigurationsResponse = {
  scheduledRenewalConfigurations?: ScheduledRenewalConfiguration[];
};

export const scheduledRenewalConfigurationsResponseSchema: Schema<ScheduledRenewalConfigurationsResponse> =
  s.object<ScheduledRenewalConfigurationsResponse>({
    scheduledRenewalConfigurations: s.optional(s.array(s.lazy(() => scheduledRenewalConfigurationSchema))),
    _keysMap: {
      scheduledRenewalConfigurations: "scheduled_renewal_configurations",
    },
  });
