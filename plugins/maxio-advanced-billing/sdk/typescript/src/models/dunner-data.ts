import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type DunnerData = {
  state: string;
  subscriptionId: number;
  revenueAtRiskInCents: number;
  createdAt: Date;
  attempts: number;
  lastAttemptedAt: Date;
};

export const dunnerDataSchema: Schema<DunnerData> = s.object<DunnerData>({
  state: s.string(),
  subscriptionId: s.int(),
  revenueAtRiskInCents: s.int(),
  createdAt: s.dateTime(),
  attempts: s.int(),
  lastAttemptedAt: s.dateTime(),
  _keysMap: {
    subscriptionId: "subscription_id",
    revenueAtRiskInCents: "revenue_at_risk_in_cents",
    createdAt: "created_at",
    lastAttemptedAt: "last_attempted_at",
  },
});
