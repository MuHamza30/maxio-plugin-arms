import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CustomFieldValueChange = {
  eventType: string;
  metafieldName: string;
  metafieldId: number;
  oldValue: string | null;
  newValue: string | null;
  resourceType: string;
  resourceId: number;
};

export const customFieldValueChangeSchema: Schema<CustomFieldValueChange> = s.object<CustomFieldValueChange>({
  eventType: s.string(),
  metafieldName: s.string(),
  metafieldId: s.int(),
  oldValue: s.nullable(s.string()),
  newValue: s.nullable(s.string()),
  resourceType: s.string(),
  resourceId: s.int(),
  _keysMap: {
    eventType: "event_type",
    metafieldName: "metafield_name",
    metafieldId: "metafield_id",
    oldValue: "old_value",
    newValue: "new_value",
    resourceType: "resource_type",
    resourceId: "resource_id",
  },
});
