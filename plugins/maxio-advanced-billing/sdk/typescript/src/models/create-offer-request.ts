import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createOfferSchema, type CreateOffer } from "./create-offer.js";

export type CreateOfferRequest = {
  offer: CreateOffer;
};

export const createOfferRequestSchema: Schema<CreateOfferRequest> = s.object<CreateOfferRequest>({
  offer: createOfferSchema,
});
