import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { groupSettingsSchema, type GroupSettings } from "./group-settings.js";

export type AddSubscriptionToAGroup = {
  group?: GroupSettings;
};

export const addSubscriptionToAGroupSchema: Schema<AddSubscriptionToAGroup> =
  s.object<AddSubscriptionToAGroup>({
    group: s.optional(s.lazy(() => groupSettingsSchema)),
  });
