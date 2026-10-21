import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The process used to cancel the subscription, if the subscription has been canceled. It is nil if
 * the subscription's state is not canceled.
 */
export const CancellationMethod = {
  MerchantUi: "merchant_ui",
  MerchantApi: "merchant_api",
  Dunning: "dunning",
  BillingPortal: "billing_portal",
  Unknown: "unknown",
  Imported: "imported",
} as const;
export type CancellationMethod = (typeof CancellationMethod)[keyof typeof CancellationMethod] | (string & {});

export const cancellationMethodSchema: EnumSchema<CancellationMethod> =
  s.enumOf<CancellationMethod>(CancellationMethod);
