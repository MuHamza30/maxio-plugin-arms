import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const GroupType = {
  SingleCustomer: "single_customer",
  MultipleCustomers: "multiple_customers",
} as const;
export type GroupType = (typeof GroupType)[keyof typeof GroupType] | (string & {});

export const groupTypeSchema: EnumSchema<GroupType> = s.enumOf<GroupType>(GroupType);
