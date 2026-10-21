import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceLineItemPricingDetailSchema,
  type InvoiceLineItemPricingDetail,
} from "./invoice-line-item-pricing-detail.js";

export type InvoiceLineItemEventData = {
  uid?: string;
  title?: string;
  description?: string;
  quantity?: number;
  quantityDelta?: number | null;
  unitPrice?: string;
  periodRangeStart?: string;
  periodRangeEnd?: string;
  amount?: string;
  lineReferences?: string;
  pricingDetailsIndex?: number | null;
  pricingDetails?: InvoiceLineItemPricingDetail[];
  taxCode?: string | null;
  taxAmount?: string;
  productId?: number;
  productPricePointId?: number | null;
  pricePointId?: number | null;
  componentId?: number | null;
  billingScheduleItemId?: number | null;
  customItem?: boolean | null;
};

export const invoiceLineItemEventDataSchema: Schema<InvoiceLineItemEventData> =
  s.object<InvoiceLineItemEventData>({
    uid: s.optional(s.string()),
    title: s.optional(s.string()),
    description: s.optional(s.string()),
    quantity: s.optional(s.int()),
    quantityDelta: s.optionalNullable(s.int()),
    unitPrice: s.optional(s.string()),
    periodRangeStart: s.optional(s.string()),
    periodRangeEnd: s.optional(s.string()),
    amount: s.optional(s.string()),
    lineReferences: s.optional(s.string()),
    pricingDetailsIndex: s.optionalNullable(s.int()),
    pricingDetails: s.optional(s.array(s.lazy(() => invoiceLineItemPricingDetailSchema))),
    taxCode: s.optionalNullable(s.string()),
    taxAmount: s.optional(s.string()),
    productId: s.optional(s.int()),
    productPricePointId: s.optionalNullable(s.int()),
    pricePointId: s.optionalNullable(s.int()),
    componentId: s.optionalNullable(s.int()),
    billingScheduleItemId: s.optionalNullable(s.int()),
    customItem: s.optionalNullable(s.boolean()),
    _keysMap: {
      quantityDelta: "quantity_delta",
      unitPrice: "unit_price",
      periodRangeStart: "period_range_start",
      periodRangeEnd: "period_range_end",
      lineReferences: "line_references",
      pricingDetailsIndex: "pricing_details_index",
      pricingDetails: "pricing_details",
      taxCode: "tax_code",
      taxAmount: "tax_amount",
      productId: "product_id",
      productPricePointId: "product_price_point_id",
      pricePointId: "price_point_id",
      componentId: "component_id",
      billingScheduleItemId: "billing_schedule_item_id",
      customItem: "custom_item",
    },
  });
