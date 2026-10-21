import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionListDateFieldSchema,
  type SubscriptionListDateField,
} from "./subscription-list-date-field.js";
import { subscriptionStateFilterSchema, type SubscriptionStateFilter } from "./subscription-state-filter.js";

/** Nested filter used for List Subscription Components For Site Filter */
export type SubscriptionFilter = {
  /**
   * Allows fetching components allocations that belong to the subscription with matching states
   * based on provided values. To use this filter you also have to include the following param in
   * the request `include=subscription`. Use in query
   * `filter[subscription][states]=active,canceled&include=subscription`.
   */
  states?: SubscriptionStateFilter[];
  /**
   * The type of filter you'd like to apply to your search. To use this filter you also have to
   * include the following param in the request `include=subscription`.
   */
  dateField?: SubscriptionListDateField;
  /**
   * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components that
   * belong to the subscription with a timestamp at or after midnight (12:00:00 AM) in your site’s
   * time zone on the date specified. To use this filter you also have to include the following
   * param in the request `include=subscription`.
   */
  startDate?: string;
  /**
   * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components that
   * belong to the subscription with a timestamp up to and including 11:59:59PM in your site’s time
   * zone on the date specified. To use this filter you also have to include the following param in
   * the request `include=subscription`.
   */
  endDate?: string;
  /**
   * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
   * Returns components that belong to the subscription with a timestamp at or after exact time
   * provided in query. You can specify timezone in query - otherwise your site''s time zone will be
   * used. If provided, this parameter will be used instead of start_date. To use this filter you
   * also have to include the following param in the request `include=subscription`.
   */
  startDatetime?: Date;
  /**
   * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns
   * components that belong to the subscription with a timestamp at or before exact time provided in
   * query. You can specify timezone in query - otherwise your site''s time zone will be used. If
   * provided, this parameter will be used instead of end_date. To use this filter you also have to
   * include the following param in the request `include=subscription`.
   */
  endDatetime?: Date;
};

export const subscriptionFilterSchema: Schema<SubscriptionFilter> = s.object<SubscriptionFilter>({
  states: s.optional(s.array(s.lazy(() => subscriptionStateFilterSchema))),
  dateField: s.optional(s.lazy(() => subscriptionListDateFieldSchema)),
  startDate: s.optional(s.dateOnly()),
  endDate: s.optional(s.dateOnly()),
  startDatetime: s.optional(s.dateTime()),
  endDatetime: s.optional(s.dateTime()),
  _keysMap: {
    dateField: "date_field",
    startDate: "start_date",
    endDate: "end_date",
    startDatetime: "start_datetime",
    endDatetime: "end_datetime",
  },
});
