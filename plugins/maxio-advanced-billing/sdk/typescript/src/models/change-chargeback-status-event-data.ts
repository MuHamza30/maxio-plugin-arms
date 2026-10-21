import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { chargebackStatusSchema, type ChargebackStatus } from "./chargeback-status.js";

/** Example schema for an `change_chargeback_status` event */
export type ChangeChargebackStatusEventData = {
  chargebackStatus: ChargebackStatus;
};

export const changeChargebackStatusEventDataSchema: Schema<ChangeChargebackStatusEventData> =
  s.object<ChangeChargebackStatusEventData>({
    chargebackStatus: chargebackStatusSchema,
    _keysMap: {
      chargebackStatus: "chargeback_status",
    },
  });
