import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { basicDateFieldSchema, type BasicDateField } from "./basic-date-field.js";

export type ListCouponsFilter = {
  /**
   * The type of filter you would like to apply to your search. Use in query
   * `filter[date_field]=created_at`.
   */
  dateField?: BasicDateField;
  /**
   * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns coupons with a
   * timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
   * Use in query `filter[start_date]=2011-12-17`.
   */
  startDate?: string;
  /**
   * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns coupons with a
   * timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in
   * query `filter[end_date]=2011-12-15`.
   */
  endDate?: string;
  /**
   * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
   * Returns coupons with a timestamp at or after exact time provided in query. You can specify
   * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
   * will be used instead of start_date. Use in query
   * `filter[start_datetime]=2011-12-19T10:15:30+01:00`.
   */
  startDatetime?: Date;
  /**
   * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns
   * coupons with a timestamp at or before exact time provided in query. You can specify timezone in
   * query - otherwise your site's time zone will be used. If provided, this parameter will be used
   * instead of end_date. Use in query `filter[end_datetime]=2011-12-1T10:15:30+01:00`.
   */
  endDatetime?: Date;
  /**
   * Allows fetching coupons with matching id based on provided values. Use in query
   * `filter[ids]=1,2,3`.
   */
  ids?: number[];
  /**
   * Allows fetching coupons with matching codes based on provided values. Use in query
   * `filter[codes]=free,free_trial`.
   */
  codes?: string[];
  /**
   * If true, restricts the list to coupons whose pricing is recalculated from the site’s current
   * exchange rates, so their currency_prices array contains on-the-fly conversions rather than
   * stored price records. If false, restricts the list to coupons that have manually defined
   * amounts for each currency, ensuring the response includes the saved currency_prices entries
   * instead of exchange-rate-derived values. Use in query `filter[use_site_exchange_rate]=true`.
   */
  useSiteExchangeRate?: boolean;
  /** Controls returning archived coupons. */
  includeArchived?: boolean;
};

export const listCouponsFilterSchema: Schema<ListCouponsFilter> = s.object<ListCouponsFilter>({
  dateField: s.optional(s.lazy(() => basicDateFieldSchema)),
  startDate: s.optional(s.dateOnly()),
  endDate: s.optional(s.dateOnly()),
  startDatetime: s.optional(s.dateTime()),
  endDatetime: s.optional(s.dateTime()),
  ids: s.optional(s.array(s.int())),
  codes: s.optional(s.array(s.string())),
  useSiteExchangeRate: s.optional(s.boolean()),
  includeArchived: s.optional(s.boolean()),
  _keysMap: {
    dateField: "date_field",
    startDate: "start_date",
    endDate: "end_date",
    startDatetime: "start_datetime",
    endDatetime: "end_datetime",
    useSiteExchangeRate: "use_site_exchange_rate",
    includeArchived: "include_archived",
  },
});
