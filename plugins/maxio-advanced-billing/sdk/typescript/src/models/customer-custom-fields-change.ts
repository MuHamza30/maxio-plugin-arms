import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceCustomFieldSchema, type InvoiceCustomField } from "./invoice-custom-field.js";

export type CustomerCustomFieldsChange = {
  before: InvoiceCustomField[];
  after: InvoiceCustomField[];
};

export const customerCustomFieldsChangeSchema: Schema<CustomerCustomFieldsChange> =
  s.object<CustomerCustomFieldsChange>({
    before: s.array(s.lazy(() => invoiceCustomFieldSchema)),
    after: s.array(s.lazy(() => invoiceCustomFieldSchema)),
  });
