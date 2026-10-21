import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type OrganizationAddress = {
  street?: string | null;
  line2?: string | null;
  city?: string | null;
  state?: string | null;
  zip?: string | null;
  country?: string | null;
  name?: string | null;
  phone?: string | null;
};

export const organizationAddressSchema: Schema<OrganizationAddress> = s.object<OrganizationAddress>({
  street: s.optionalNullable(s.string()),
  line2: s.optionalNullable(s.string()),
  city: s.optionalNullable(s.string()),
  state: s.optionalNullable(s.string()),
  zip: s.optionalNullable(s.string()),
  country: s.optionalNullable(s.string()),
  name: s.optionalNullable(s.string()),
  phone: s.optionalNullable(s.string()),
});
