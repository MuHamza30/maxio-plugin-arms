import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  upsertPrepaidConfigurationSchema,
  type UpsertPrepaidConfiguration,
} from "./upsert-prepaid-configuration.js";

export type UpsertPrepaidConfigurationRequest = {
  prepaidConfiguration: UpsertPrepaidConfiguration;
};

export const upsertPrepaidConfigurationRequestSchema: Schema<UpsertPrepaidConfigurationRequest> =
  s.object<UpsertPrepaidConfigurationRequest>({
    prepaidConfiguration: upsertPrepaidConfigurationSchema,
    _keysMap: {
      prepaidConfiguration: "prepaid_configuration",
    },
  });
