import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type SubscriptionIdOrReference = number | string;

export const subscriptionIdOrReferenceSchema: Schema<SubscriptionIdOrReference> =
  s.of<SubscriptionIdOrReference>(s.union([s.int(), s.string()]));
