import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ScheduledRenewalConfigurationRequestBody = {
  /** (Optional) Start of the renewal term. */
  startsAt?: Date;
  /** (Optional) End of the renewal term. */
  endsAt?: Date;
  /** (Optional) Lock-in date for the renewal. */
  lockInAt?: Date;
  /**
   * (Optional) Existing contract to associate with the scheduled renewal. Contracts must be enabled
   * for your site.
   */
  contractId?: number;
  /**
   * (Optional) Set to true to create a new contract when contracts are enabled. Contracts must be
   * enabled for your site.
   */
  createNewContract?: boolean;
};

export const scheduledRenewalConfigurationRequestBodySchema: Schema<ScheduledRenewalConfigurationRequestBody> =
  s.object<ScheduledRenewalConfigurationRequestBody>({
    startsAt: s.optional(s.dateTime()),
    endsAt: s.optional(s.dateTime()),
    lockInAt: s.optional(s.dateTime()),
    contractId: s.optional(s.int()),
    createNewContract: s.optional(s.boolean()),
    _keysMap: {
      startsAt: "starts_at",
      endsAt: "ends_at",
      lockInAt: "lock_in_at",
      contractId: "contract_id",
      createNewContract: "create_new_contract",
    },
  });
