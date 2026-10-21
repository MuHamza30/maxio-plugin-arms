import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type TokenizedPaymentProfile = {
  id: number;
  vaultToken?: string;
  gatewayHandle?: string | null;
  customerVaultToken?: string | null;
};

export const tokenizedPaymentProfileSchema: Schema<TokenizedPaymentProfile> =
  s.object<TokenizedPaymentProfile>({
    id: s.int(),
    vaultToken: s.optional(s.string()),
    gatewayHandle: s.optionalNullable(s.string()),
    customerVaultToken: s.optionalNullable(s.string()),
    _keysMap: {
      vaultToken: "vault_token",
      gatewayHandle: "gateway_handle",
      customerVaultToken: "customer_vault_token",
    },
  });
