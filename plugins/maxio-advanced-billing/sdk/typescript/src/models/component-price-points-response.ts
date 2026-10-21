import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentPricePointSchema, type ComponentPricePoint } from "./component-price-point.js";
import { listPublicKeysMetaSchema, type ListPublicKeysMeta } from "./list-public-keys-meta.js";

export type ComponentPricePointsResponse = {
  pricePoints?: ComponentPricePoint[];
  meta?: ListPublicKeysMeta;
};

export const componentPricePointsResponseSchema: Schema<ComponentPricePointsResponse> =
  s.object<ComponentPricePointsResponse>({
    pricePoints: s.optional(s.array(s.lazy(() => componentPricePointSchema))),
    meta: s.optional(s.lazy(() => listPublicKeysMetaSchema)),
    _keysMap: {
      pricePoints: "price_points",
    },
  });
