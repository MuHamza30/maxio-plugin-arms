import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoiceTaxComponentBreakout = {
  taxRuleId?: number;
  percentage?: string;
  countryCode?: string;
  subdivisionCode?: string;
  taxAmount?: string;
  taxableAmount?: string;
  taxExemptAmount?: string;
  nonTaxableAmount?: string;
  taxName?: string;
  taxType?: string;
  rateType?: string;
  taxAuthorityType?: number;
  stateAssignedNo?: string;
  taxSubType?: string;
};

export const invoiceTaxComponentBreakoutSchema: Schema<InvoiceTaxComponentBreakout> =
  s.object<InvoiceTaxComponentBreakout>({
    taxRuleId: s.optional(s.int()),
    percentage: s.optional(s.string()),
    countryCode: s.optional(s.string()),
    subdivisionCode: s.optional(s.string()),
    taxAmount: s.optional(s.string()),
    taxableAmount: s.optional(s.string()),
    taxExemptAmount: s.optional(s.string()),
    nonTaxableAmount: s.optional(s.string()),
    taxName: s.optional(s.string()),
    taxType: s.optional(s.string()),
    rateType: s.optional(s.string()),
    taxAuthorityType: s.optional(s.int()),
    stateAssignedNo: s.optional(s.string()),
    taxSubType: s.optional(s.string()),
    _keysMap: {
      taxRuleId: "tax_rule_id",
      countryCode: "country_code",
      subdivisionCode: "subdivision_code",
      taxAmount: "tax_amount",
      taxableAmount: "taxable_amount",
      taxExemptAmount: "tax_exempt_amount",
      nonTaxableAmount: "non_taxable_amount",
      taxName: "tax_name",
      taxType: "tax_type",
      rateType: "rate_type",
      taxAuthorityType: "tax_authority_type",
      stateAssignedNo: "state_assigned_no",
      taxSubType: "tax_sub_type",
    },
  });
