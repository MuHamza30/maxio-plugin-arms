import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { listPrepaymentDateFieldSchema, type ListPrepaymentDateField } from "./list-prepayment-date-field.js";

export type ListPrepaymentsFilter = {
  /**
   * The type of filter you would like to apply to your search. `created_at` - Time when prepayment
   * was created. `application_at` - Time when prepayment was applied to invoice. Use in query
   * `filter[date_field]=created_at`.
   */
  dateField?: ListPrepaymentDateField;
  /**
   * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns prepayments
   * with a timestamp at or after midnight (12:00:00 AM) in your site's time zone on the date
   * specified. Use in query: `filter[start_date]=2011-12-15`.
   */
  startDate?: string;
  /**
   * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns prepayments with
   * a timestamp up to and including 11:59:59PM in your site's time zone on the date specified. Use
   * in query: `filter[end_date]=2011-12-15`.
   */
  endDate?: string;
};

export const listPrepaymentsFilterSchema: Schema<ListPrepaymentsFilter> = s.object<ListPrepaymentsFilter>({
  dateField: s.optional(s.lazy(() => listPrepaymentDateFieldSchema)),
  startDate: s.optional(s.dateOnly()),
  endDate: s.optional(s.dateOnly()),
  _keysMap: {
    dateField: "date_field",
    startDate: "start_date",
    endDate: "end_date",
  },
});
