import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { customerSchema, type Customer } from "./customer.js";

export type CustomerResponse = {
  customer: Customer;
};

export const customerResponseSchema: Schema<CustomerResponse> = s.object<CustomerResponse>({
  customer: customerSchema,
});
