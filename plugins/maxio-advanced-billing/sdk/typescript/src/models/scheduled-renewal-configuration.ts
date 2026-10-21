import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { contractSchema, type Contract } from "./contract.js";
import {
  scheduledRenewalConfigurationItemSchema,
  type ScheduledRenewalConfigurationItem,
} from "./scheduled-renewal-configuration-item.js";

export type ScheduledRenewalConfiguration = {
  /** ID of the renewal. */
  id?: number;
  /** ID of the site to which the renewal belongs. */
  siteId?: number;
  /** The id of the subscription. */
  subscriptionId?: number;
  startsAt?: Date;
  endsAt?: Date;
  lockInAt?: Date;
  createdAt?: Date;
  status?: string;
  scheduledRenewalConfigurationItems?: ScheduledRenewalConfigurationItem[];
  /** Contract linked to the scheduled renewal configuration. */
  contract?: Contract;
};

export const scheduledRenewalConfigurationSchema: Schema<ScheduledRenewalConfiguration> =
  s.object<ScheduledRenewalConfiguration>({
    id: s.optional(s.int()),
    siteId: s.optional(s.int()),
    subscriptionId: s.optional(s.int()),
    startsAt: s.optional(s.dateTime()),
    endsAt: s.optional(s.dateTime()),
    lockInAt: s.optional(s.dateTime()),
    createdAt: s.optional(s.dateTime()),
    status: s.optional(s.string()),
    scheduledRenewalConfigurationItems: s.optional(
      s.array(s.lazy(() => scheduledRenewalConfigurationItemSchema)),
    ),
    contract: s.optional(s.lazy(() => contractSchema)),
    _keysMap: {
      siteId: "site_id",
      subscriptionId: "subscription_id",
      startsAt: "starts_at",
      endsAt: "ends_at",
      lockInAt: "lock_in_at",
      createdAt: "created_at",
      scheduledRenewalConfigurationItems: "scheduled_renewal_configuration_items",
    },
  });
