import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { TaxConfigurationKind, taxConfigurationKindSchema } from "./tax-configuration-kind.js";
import { taxDestinationAddressSchema, type TaxDestinationAddress } from "./tax-destination-address.js";

export type TaxConfiguration = {
  /** @default TaxConfigurationKind.Custom */
  kind?: TaxConfigurationKind;
  destinationAddress?: TaxDestinationAddress;
  /**
   * Returns `true` when Chargify has been properly configured to charge tax using the specified tax
   * system. More details about taxes:
   * https://maxio.zendesk.com/hc/en-us/articles/24287012608909-Taxes-Overview
   *
   * @default false
   */
  fullyConfigured?: boolean;
};

export const taxConfigurationSchema: Schema<TaxConfiguration> = s.object<TaxConfiguration>({
  kind: s.defaulted(taxConfigurationKindSchema, TaxConfigurationKind.Custom),
  destinationAddress: s.optional(s.lazy(() => taxDestinationAddressSchema)),
  fullyConfigured: s.defaulted(s.boolean(), false),
  _keysMap: {
    destinationAddress: "destination_address",
    fullyConfigured: "fully_configured",
  },
});
