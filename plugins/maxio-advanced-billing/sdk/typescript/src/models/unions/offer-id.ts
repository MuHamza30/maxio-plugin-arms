import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * Use in place of passing product and component information to set up the subscription with an
 * existing offer. May be either the Chargify id of the offer or its handle prefixed with `handle:`.
 */
export type OfferId = string | number;

export const offerIdSchema: Schema<OfferId> = s.of<OfferId>(s.union([s.string(), s.int()]));
