import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  renewalConfigurationItemSchema,
  type RenewalConfigurationItem,
} from "./unions/renewal-configuration-item.js";

export type ScheduledRenewalConfigurationItemRequest = {
  renewalConfigurationItem: RenewalConfigurationItem;
};

export const scheduledRenewalConfigurationItemRequestSchema: Schema<ScheduledRenewalConfigurationItemRequest> =
  s.object<ScheduledRenewalConfigurationItemRequest>({
    renewalConfigurationItem: renewalConfigurationItemSchema,
    _keysMap: {
      renewalConfigurationItem: "renewal_configuration_item",
    },
  });
