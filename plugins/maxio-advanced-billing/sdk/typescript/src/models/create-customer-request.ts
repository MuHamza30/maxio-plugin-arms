import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createCustomerSchema, type CreateCustomer } from "./create-customer.js";

export type CreateCustomerRequest = {
  customer: CreateCustomer;
};

export const createCustomerRequestSchema: Schema<CreateCustomerRequest> = s.object<CreateCustomerRequest>({
  customer: createCustomerSchema,
});
