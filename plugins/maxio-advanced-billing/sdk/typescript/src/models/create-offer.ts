import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createOfferComponentSchema, type CreateOfferComponent } from "./create-offer-component.js";

export type CreateOffer = {
  name: string;
  handle: string;
  description?: string;
  productId: number;
  productPricePointId?: number;
  components?: CreateOfferComponent[];
  coupons?: string[];
};

export const createOfferSchema: Schema<CreateOffer> = s.object<CreateOffer>({
  name: s.string(),
  handle: s.string(),
  description: s.optional(s.string()),
  productId: s.int(),
  productPricePointId: s.optional(s.int()),
  components: s.optional(s.array(s.lazy(() => createOfferComponentSchema))),
  coupons: s.optional(s.array(s.string())),
  _keysMap: {
    productId: "product_id",
    productPricePointId: "product_price_point_id",
  },
});
