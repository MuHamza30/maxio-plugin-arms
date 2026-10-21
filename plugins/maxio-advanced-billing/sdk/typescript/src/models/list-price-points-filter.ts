import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { basicDateFieldSchema, type BasicDateField } from "./basic-date-field.js";
import { includeNullOrNotNullSchema, type IncludeNullOrNotNull } from "./include-null-or-not-null.js";
import { pricePointTypeSchema, type PricePointType } from "./price-point-type.js";

export type ListPricePointsFilter = {
  /**
   * The type of filter you would like to apply to your search. Use in query:
   * `filter[date_field]=created_at`.
   */
  dateField?: BasicDateField;
  /**
   * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns price points
   * with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
   * specified.
   */
  startDate?: string;
  /**
   * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns price points with
   * a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
   */
  endDate?: string;
  /**
   * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
   * Returns price points with a timestamp at or after exact time provided in query. You can specify
   * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
   * will be used instead of start_date.
   */
  startDatetime?: Date;
  /**
   * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns
   * price points with a timestamp at or before exact time provided in query. You can specify
   * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
   * will be used instead of end_date.
   */
  endDatetime?: Date;
  /**
   * Allows fetching price points with matching type. Use in query: `filter[type]=custom,catalog`.
   */
  type?: PricePointType[];
  /**
   * Allows fetching price points with matching id based on provided values. Use in query:
   * `filter[ids]=1,2,3`.
   */
  ids?: number[];
  /**
   * Allows fetching price points only if archived_at is present or not. Use in query:
   * `filter[archived_at]=not_null`.
   */
  archivedAt?: IncludeNullOrNotNull;
};

export const listPricePointsFilterSchema: Schema<ListPricePointsFilter> = s.object<ListPricePointsFilter>({
  dateField: s.optional(s.lazy(() => basicDateFieldSchema)),
  startDate: s.optional(s.dateOnly()),
  endDate: s.optional(s.dateOnly()),
  startDatetime: s.optional(s.dateTime()),
  endDatetime: s.optional(s.dateTime()),
  type: s.optional(s.array(s.lazy(() => pricePointTypeSchema))),
  ids: s.optional(s.array(s.int())),
  archivedAt: s.optional(s.lazy(() => includeNullOrNotNullSchema)),
  _keysMap: {
    dateField: "date_field",
    startDate: "start_date",
    endDate: "end_date",
    startDatetime: "start_datetime",
    endDatetime: "end_datetime",
    archivedAt: "archived_at",
  },
});
