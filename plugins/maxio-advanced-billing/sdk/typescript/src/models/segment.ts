import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";
import { segmentPriceSchema, type SegmentPrice } from "./segment-price.js";
import {
  segmentProperty1Value1Schema,
  type SegmentProperty1Value1,
} from "./unions/segment-property1-value1.js";
import {
  segmentProperty2Value1Schema,
  type SegmentProperty2Value1,
} from "./unions/segment-property2-value1.js";
import {
  segmentProperty3Value1Schema,
  type SegmentProperty3Value1,
} from "./unions/segment-property3-value1.js";
import {
  segmentProperty4Value1Schema,
  type SegmentProperty4Value1,
} from "./unions/segment-property4-value1.js";

export type Segment = {
  id?: number;
  componentId?: number;
  pricePointId?: number;
  eventBasedBillingMetricId?: number;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme?: PricingScheme;
  segmentProperty1Value?: SegmentProperty1Value1;
  segmentProperty2Value?: SegmentProperty2Value1;
  segmentProperty3Value?: SegmentProperty3Value1;
  segmentProperty4Value?: SegmentProperty4Value1;
  createdAt?: Date;
  updatedAt?: Date;
  prices?: SegmentPrice[];
};

export const segmentSchema: Schema<Segment> = s.object<Segment>({
  id: s.optional(s.int()),
  componentId: s.optional(s.int()),
  pricePointId: s.optional(s.int()),
  eventBasedBillingMetricId: s.optional(s.int()),
  pricingScheme: s.optional(s.lazy(() => pricingSchemeSchema)),
  segmentProperty1Value: s.optional(s.lazy(() => segmentProperty1Value1Schema)),
  segmentProperty2Value: s.optional(s.lazy(() => segmentProperty2Value1Schema)),
  segmentProperty3Value: s.optional(s.lazy(() => segmentProperty3Value1Schema)),
  segmentProperty4Value: s.optional(s.lazy(() => segmentProperty4Value1Schema)),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  prices: s.optional(s.array(s.lazy(() => segmentPriceSchema))),
  _keysMap: {
    componentId: "component_id",
    pricePointId: "price_point_id",
    eventBasedBillingMetricId: "event_based_billing_metric_id",
    pricingScheme: "pricing_scheme",
    segmentProperty1Value: "segment_property_1_value",
    segmentProperty2Value: "segment_property_2_value",
    segmentProperty3Value: "segment_property_3_value",
    segmentProperty4Value: "segment_property_4_value",
    createdAt: "created_at",
    updatedAt: "updated_at",
  },
});
