import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  scheduledRenewalConfigurationItemSchema,
  type ScheduledRenewalConfigurationItem,
} from "./scheduled-renewal-configuration-item.js";

export type ScheduledRenewalConfigurationItemResponse = {
  scheduledRenewalConfigurationItem?: ScheduledRenewalConfigurationItem;
};

export const scheduledRenewalConfigurationItemResponseSchema: Schema<ScheduledRenewalConfigurationItemResponse> =
  s.object<ScheduledRenewalConfigurationItemResponse>({
    scheduledRenewalConfigurationItem: s.optional(s.lazy(() => scheduledRenewalConfigurationItemSchema)),
    _keysMap: {
      scheduledRenewalConfigurationItem: "scheduled_renewal_configuration_item",
    },
  });
