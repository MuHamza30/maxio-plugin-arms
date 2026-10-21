import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  renewalConfigurationItemSchema,
  type RenewalConfigurationItem,
} from "./unions/renewal-configuration-item.js";

export type ScheduledRenewalUpdateRequest = {
  renewalConfigurationItem: RenewalConfigurationItem;
};

export const scheduledRenewalUpdateRequestSchema: Schema<ScheduledRenewalUpdateRequest> =
  s.object<ScheduledRenewalUpdateRequest>({
    renewalConfigurationItem: renewalConfigurationItemSchema,
    _keysMap: {
      renewalConfigurationItem: "renewal_configuration_item",
    },
  });
