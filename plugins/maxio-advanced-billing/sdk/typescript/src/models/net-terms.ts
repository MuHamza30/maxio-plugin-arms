import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type NetTerms = {
  /** @default 0 */
  defaultNetTerms?: number;
  /** @default 0 */
  automaticNetTerms?: number;
  /** @default 0 */
  remittanceNetTerms?: number;
  /** @default false */
  netTermsOnRemittanceSignupsEnabled?: boolean;
  /** @default false */
  customNetTermsEnabled?: boolean;
};

export const netTermsSchema: Schema<NetTerms> = s.object<NetTerms>({
  defaultNetTerms: s.defaulted(s.int(), 0),
  automaticNetTerms: s.defaulted(s.int(), 0),
  remittanceNetTerms: s.defaulted(s.int(), 0),
  netTermsOnRemittanceSignupsEnabled: s.defaulted(s.boolean(), false),
  customNetTermsEnabled: s.defaulted(s.boolean(), false),
  _keysMap: {
    defaultNetTerms: "default_net_terms",
    automaticNetTerms: "automatic_net_terms",
    remittanceNetTerms: "remittance_net_terms",
    netTermsOnRemittanceSignupsEnabled: "net_terms_on_remittance_signups_enabled",
    customNetTermsEnabled: "custom_net_terms_enabled",
  },
});
