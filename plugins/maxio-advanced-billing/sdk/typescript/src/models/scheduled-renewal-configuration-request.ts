import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  scheduledRenewalConfigurationRequestBodySchema,
  type ScheduledRenewalConfigurationRequestBody,
} from "./scheduled-renewal-configuration-request-body.js";

export type ScheduledRenewalConfigurationRequest = {
  renewalConfiguration: ScheduledRenewalConfigurationRequestBody;
};

export const scheduledRenewalConfigurationRequestSchema: Schema<ScheduledRenewalConfigurationRequest> =
  s.object<ScheduledRenewalConfigurationRequest>({
    renewalConfiguration: scheduledRenewalConfigurationRequestBodySchema,
    _keysMap: {
      renewalConfiguration: "renewal_configuration",
    },
  });
