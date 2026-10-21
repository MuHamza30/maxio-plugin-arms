import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  createOrUpdateSegmentPriceSchema,
  type CreateOrUpdateSegmentPrice,
} from "./create-or-update-segment-price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";
import { segmentProperty1ValueSchema, type SegmentProperty1Value } from "./unions/segment-property1-value.js";
import { segmentProperty2ValueSchema, type SegmentProperty2Value } from "./unions/segment-property2-value.js";
import { segmentProperty3ValueSchema, type SegmentProperty3Value } from "./unions/segment-property3-value.js";
import { segmentProperty4ValueSchema, type SegmentProperty4Value } from "./unions/segment-property4-value.js";

export type CreateSegment = {
  /**
   * A value that will occur in your events that you want to bill upon. The type of the value
   * depends on the property type in the related event based billing metric.
   */
  segmentProperty1Value?: SegmentProperty1Value;
  /**
   * A value that will occur in your events that you want to bill upon. The type of the value
   * depends on the property type in the related event based billing metric.
   */
  segmentProperty2Value?: SegmentProperty2Value;
  /**
   * A value that will occur in your events that you want to bill upon. The type of the value
   * depends on the property type in the related event based billing metric.
   */
  segmentProperty3Value?: SegmentProperty3Value;
  /**
   * A value that will occur in your events that you want to bill upon. The type of the value
   * depends on the property type in the related event based billing metric.
   */
  segmentProperty4Value?: SegmentProperty4Value;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme: PricingScheme;
  prices?: CreateOrUpdateSegmentPrice[];
};

export const createSegmentSchema: Schema<CreateSegment> = s.object<CreateSegment>({
  segmentProperty1Value: s.optional(s.lazy(() => segmentProperty1ValueSchema)),
  segmentProperty2Value: s.optional(s.lazy(() => segmentProperty2ValueSchema)),
  segmentProperty3Value: s.optional(s.lazy(() => segmentProperty3ValueSchema)),
  segmentProperty4Value: s.optional(s.lazy(() => segmentProperty4ValueSchema)),
  pricingScheme: pricingSchemeSchema,
  prices: s.optional(s.array(s.lazy(() => createOrUpdateSegmentPriceSchema))),
  _keysMap: {
    segmentProperty1Value: "segment_property_1_value",
    segmentProperty2Value: "segment_property_2_value",
    segmentProperty3Value: "segment_property_3_value",
    segmentProperty4Value: "segment_property_4_value",
    pricingScheme: "pricing_scheme",
  },
});
