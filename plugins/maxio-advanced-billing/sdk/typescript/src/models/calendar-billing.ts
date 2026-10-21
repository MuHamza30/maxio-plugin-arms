import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { firstChargeTypeSchema, type FirstChargeType } from "./first-charge-type.js";
import { snapDaySchema, type SnapDay } from "./unions/snap-day.js";

/** (Optional). Cannot be used when also specifying next_billing_at. */
export type CalendarBilling = {
  /** A day of month that subscription will be processed on. Can be 1 up to 28 or 'end'. */
  snapDay?: SnapDay;
  calendarBillingFirstCharge?: FirstChargeType;
};

export const calendarBillingSchema: Schema<CalendarBilling> = s.object<CalendarBilling>({
  snapDay: s.optional(s.lazy(() => snapDaySchema)),
  calendarBillingFirstCharge: s.optional(s.lazy(() => firstChargeTypeSchema)),
  _keysMap: {
    snapDay: "snap_day",
    calendarBillingFirstCharge: "calendar_billing_first_charge",
  },
});
