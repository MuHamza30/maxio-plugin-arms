import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateCustomerSchema, type UpdateCustomer } from "./update-customer.js";

export type UpdateCustomerRequest = {
  customer: UpdateCustomer;
};

export const updateCustomerRequestSchema: Schema<UpdateCustomerRequest> = s.object<UpdateCustomerRequest>({
  customer: updateCustomerSchema,
});
