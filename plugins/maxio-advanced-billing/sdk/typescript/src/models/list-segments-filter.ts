import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ListSegmentsFilter = {
  /**
   * The value passed here would be used to filter segments. Pass a value related to
   * `segment_property_1` on attached Metric. If empty string is passed, this filter would be
   * rejected. Use in query `filter[segment_property_1_value]=EU`.
   */
  segmentProperty1Value?: string;
  /**
   * The value passed here would be used to filter segments. Pass a value related to
   * `segment_property_2` on attached Metric. If empty string is passed, this filter would be
   * rejected.
   */
  segmentProperty2Value?: string;
  /**
   * The value passed here would be used to filter segments. Pass a value related to
   * `segment_property_3` on attached Metric. If empty string is passed, this filter would be
   * rejected.
   */
  segmentProperty3Value?: string;
  /**
   * The value passed here would be used to filter segments. Pass a value related to
   * `segment_property_4` on attached Metric. If empty string is passed, this filter would be
   * rejected.
   */
  segmentProperty4Value?: string;
};

export const listSegmentsFilterSchema: Schema<ListSegmentsFilter> = s.object<ListSegmentsFilter>({
  segmentProperty1Value: s.optional(s.string()),
  segmentProperty2Value: s.optional(s.string()),
  segmentProperty3Value: s.optional(s.string()),
  segmentProperty4Value: s.optional(s.string()),
  _keysMap: {
    segmentProperty1Value: "segment_property_1_value",
    segmentProperty2Value: "segment_property_2_value",
    segmentProperty3Value: "segment_property_3_value",
    segmentProperty4Value: "segment_property_4_value",
  },
});
