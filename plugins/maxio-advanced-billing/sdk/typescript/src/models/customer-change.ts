import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { addressChangeSchema, type AddressChange } from "./address-change.js";
import {
  customerCustomFieldsChangeSchema,
  type CustomerCustomFieldsChange,
} from "./customer-custom-fields-change.js";
import { customerPayerChangeSchema, type CustomerPayerChange } from "./customer-payer-change.js";

export type CustomerChange = {
  payer?: CustomerPayerChange | null;
  shippingAddress?: AddressChange | null;
  billingAddress?: AddressChange | null;
  customFields?: CustomerCustomFieldsChange | null;
};

export const customerChangeSchema: Schema<CustomerChange> = s.object<CustomerChange>({
  payer: s.optionalNullable(s.lazy(() => customerPayerChangeSchema)),
  shippingAddress: s.optionalNullable(s.lazy(() => addressChangeSchema)),
  billingAddress: s.optionalNullable(s.lazy(() => addressChangeSchema)),
  customFields: s.optionalNullable(s.lazy(() => customerCustomFieldsChangeSchema)),
  _keysMap: {
    shippingAddress: "shipping_address",
    billingAddress: "billing_address",
    customFields: "custom_fields",
  },
});
