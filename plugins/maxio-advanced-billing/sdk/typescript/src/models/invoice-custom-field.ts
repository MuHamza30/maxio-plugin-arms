import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { customFieldOwnerSchema, type CustomFieldOwner } from "./custom-field-owner.js";

export type InvoiceCustomField = {
  ownerId?: number;
  ownerType?: CustomFieldOwner;
  name?: string;
  value?: string;
  metadatumId?: number;
};

export const invoiceCustomFieldSchema: Schema<InvoiceCustomField> = s.object<InvoiceCustomField>({
  ownerId: s.optional(s.int()),
  ownerType: s.optional(s.lazy(() => customFieldOwnerSchema)),
  name: s.optional(s.string()),
  value: s.optional(s.string()),
  metadatumId: s.optional(s.int()),
  _keysMap: {
    ownerId: "owner_id",
    ownerType: "owner_type",
    metadatumId: "metadatum_id",
  },
});
