import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  scheduledRenewalConfigurationSchema,
  type ScheduledRenewalConfiguration,
} from "./scheduled-renewal-configuration.js";

export type ScheduledRenewalConfigurationResponse = {
  scheduledRenewalConfiguration?: ScheduledRenewalConfiguration;
};

export const scheduledRenewalConfigurationResponseSchema: Schema<ScheduledRenewalConfigurationResponse> =
  s.object<ScheduledRenewalConfigurationResponse>({
    scheduledRenewalConfiguration: s.optional(s.lazy(() => scheduledRenewalConfigurationSchema)),
    _keysMap: {
      scheduledRenewalConfiguration: "scheduled_renewal_configuration",
    },
  });
