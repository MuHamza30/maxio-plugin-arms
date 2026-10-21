import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { offerSchema, type Offer } from "./offer.js";

export type ListOffersResponse = {
  offers?: Offer[];
};

export const listOffersResponseSchema: Schema<ListOffersResponse> = s.object<ListOffersResponse>({
  offers: s.optional(s.array(s.lazy(() => offerSchema))),
});
