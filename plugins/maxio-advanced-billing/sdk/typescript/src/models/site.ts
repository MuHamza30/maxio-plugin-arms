import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { allocationSettingsSchema, type AllocationSettings } from "./allocation-settings.js";
import { netTermsSchema, type NetTerms } from "./net-terms.js";
import { organizationAddressSchema, type OrganizationAddress } from "./organization-address.js";
import { taxConfigurationSchema, type TaxConfiguration } from "./tax-configuration.js";

export type Site = {
  id?: number;
  name?: string;
  subdomain?: string;
  currency?: string;
  sellerId?: number;
  nonPrimaryCurrencies?: string[];
  relationshipInvoicingEnabled?: boolean;
  scheduleSubscriptionCancellationEnabled?: boolean;
  customerHierarchyEnabled?: boolean;
  whopaysEnabled?: boolean;
  whopaysDefaultPayer?: string;
  allocationSettings?: AllocationSettings;
  defaultPaymentCollectionMethod?: string;
  organizationAddress?: OrganizationAddress;
  taxConfiguration?: TaxConfiguration;
  netTerms?: NetTerms;
  /**
   * Whether the site has the multi-frequency billing feature enabled. Only present when
   * relationship invoicing is active.
   */
  multiFrequencyEnabled?: boolean;
  /** Whether the auto-renewals feature is enabled for this site. */
  autoRenewalsEnabled?: boolean;
  /** Whether the Billing Portal is enabled for this site. */
  portalEnabled?: boolean;
  test?: boolean;
};

export const siteSchema: Schema<Site> = s.object<Site>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  subdomain: s.optional(s.string()),
  currency: s.optional(s.string()),
  sellerId: s.optional(s.int()),
  nonPrimaryCurrencies: s.optional(s.array(s.string())),
  relationshipInvoicingEnabled: s.optional(s.boolean()),
  scheduleSubscriptionCancellationEnabled: s.optional(s.boolean()),
  customerHierarchyEnabled: s.optional(s.boolean()),
  whopaysEnabled: s.optional(s.boolean()),
  whopaysDefaultPayer: s.optional(s.string()),
  allocationSettings: s.optional(s.lazy(() => allocationSettingsSchema)),
  defaultPaymentCollectionMethod: s.optional(s.string()),
  organizationAddress: s.optional(s.lazy(() => organizationAddressSchema)),
  taxConfiguration: s.optional(s.lazy(() => taxConfigurationSchema)),
  netTerms: s.optional(s.lazy(() => netTermsSchema)),
  multiFrequencyEnabled: s.optional(s.boolean()),
  autoRenewalsEnabled: s.optional(s.boolean()),
  portalEnabled: s.optional(s.boolean()),
  test: s.optional(s.boolean()),
  _keysMap: {
    sellerId: "seller_id",
    nonPrimaryCurrencies: "non_primary_currencies",
    relationshipInvoicingEnabled: "relationship_invoicing_enabled",
    scheduleSubscriptionCancellationEnabled: "schedule_subscription_cancellation_enabled",
    customerHierarchyEnabled: "customer_hierarchy_enabled",
    whopaysEnabled: "whopays_enabled",
    whopaysDefaultPayer: "whopays_default_payer",
    allocationSettings: "allocation_settings",
    defaultPaymentCollectionMethod: "default_payment_collection_method",
    organizationAddress: "organization_address",
    taxConfiguration: "tax_configuration",
    netTerms: "net_terms",
    multiFrequencyEnabled: "multi_frequency_enabled",
    autoRenewalsEnabled: "auto_renewals_enabled",
    portalEnabled: "portal_enabled",
  },
});
