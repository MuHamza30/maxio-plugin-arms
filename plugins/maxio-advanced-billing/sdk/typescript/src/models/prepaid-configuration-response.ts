import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { prepaidConfigurationSchema, type PrepaidConfiguration } from "./prepaid-configuration.js";

export type PrepaidConfigurationResponse = {
  prepaidConfiguration: PrepaidConfiguration;
};

export const prepaidConfigurationResponseSchema: Schema<PrepaidConfigurationResponse> =
  s.object<PrepaidConfigurationResponse>({
    prepaidConfiguration: prepaidConfigurationSchema,
    _keysMap: {
      prepaidConfiguration: "prepaid_configuration",
    },
  });
