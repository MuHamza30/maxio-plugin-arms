import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** The current chargeback status. */
export const ChargebackStatus = {
  Open: "open",
  Lost: "lost",
  Won: "won",
  Closed: "closed",
} as const;
export type ChargebackStatus = (typeof ChargebackStatus)[keyof typeof ChargebackStatus] | (string & {});

export const chargebackStatusSchema: EnumSchema<ChargebackStatus> =
  s.enumOf<ChargebackStatus>(ChargebackStatus);
