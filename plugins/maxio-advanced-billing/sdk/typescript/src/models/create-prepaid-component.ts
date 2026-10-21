import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { prepaidUsageComponentSchema, type PrepaidUsageComponent } from "./prepaid-usage-component.js";

export type CreatePrepaidComponent = {
  prepaidUsageComponent: PrepaidUsageComponent;
};

export const createPrepaidComponentSchema: Schema<CreatePrepaidComponent> = s.object<CreatePrepaidComponent>({
  prepaidUsageComponent: prepaidUsageComponentSchema,
  _keysMap: {
    prepaidUsageComponent: "prepaid_usage_component",
  },
});
