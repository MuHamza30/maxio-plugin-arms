import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Example schema for an `change_invoice_collection_method` event */
export type ChangeInvoiceCollectionMethodEventData = {
  /** The previous collection method of the invoice. */
  fromCollectionMethod: string;
  /** The new collection method of the invoice. */
  toCollectionMethod: string;
};

export const changeInvoiceCollectionMethodEventDataSchema: Schema<ChangeInvoiceCollectionMethodEventData> =
  s.object<ChangeInvoiceCollectionMethodEventData>({
    fromCollectionMethod: s.string(),
    toCollectionMethod: s.string(),
    _keysMap: {
      fromCollectionMethod: "from_collection_method",
      toCollectionMethod: "to_collection_method",
    },
  });
