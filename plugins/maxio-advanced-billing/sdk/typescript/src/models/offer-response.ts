import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { offerSchema, type Offer } from "./offer.js";

export type OfferResponse = {
  offer?: Offer;
};

export const offerResponseSchema: Schema<OfferResponse> = s.object<OfferResponse>({
  offer: s.optional(s.lazy(() => offerSchema)),
});
