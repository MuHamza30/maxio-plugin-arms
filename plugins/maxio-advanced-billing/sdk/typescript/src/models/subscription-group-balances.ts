import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { accountBalanceSchema, type AccountBalance } from "./account-balance.js";

export type SubscriptionGroupBalances = {
  prepayments?: AccountBalance;
  serviceCredits?: AccountBalance;
  openInvoices?: AccountBalance;
  pendingDiscounts?: AccountBalance;
};

export const subscriptionGroupBalancesSchema: Schema<SubscriptionGroupBalances> =
  s.object<SubscriptionGroupBalances>({
    prepayments: s.optional(s.lazy(() => accountBalanceSchema)),
    serviceCredits: s.optional(s.lazy(() => accountBalanceSchema)),
    openInvoices: s.optional(s.lazy(() => accountBalanceSchema)),
    pendingDiscounts: s.optional(s.lazy(() => accountBalanceSchema)),
    _keysMap: {
      serviceCredits: "service_credits",
      openInvoices: "open_invoices",
      pendingDiscounts: "pending_discounts",
    },
  });
