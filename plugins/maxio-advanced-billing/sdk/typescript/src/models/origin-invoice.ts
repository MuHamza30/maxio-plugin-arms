import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type OriginInvoice = {
  /** The UID of the invoice serving as an origin invoice. */
  uid?: string;
  /** The number of the invoice serving as an origin invoice. */
  number?: string;
};

export const originInvoiceSchema: Schema<OriginInvoice> = s.object<OriginInvoice>({
  uid: s.optional(s.string()),
  number: s.optional(s.string()),
});
