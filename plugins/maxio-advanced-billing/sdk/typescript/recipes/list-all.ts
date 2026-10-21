/*
 * list-all: read every page of a Maxio list operation.
 *
 * Which operations it fits
 *   A list operation that takes `page` and `perPage` and returns an array. The SDK has no paging
 *   helper: each call returns one page, and a call that leaves `perPage` out gets the spec default
 *   (20 on most lists), so it returns part of the data with no error.
 *
 *     const rows = await listAll(
 *       (page, perPage) => client.subscriptions.listSubscriptions({ page, perPage }),
 *       { maxPages: 50, key: (row) => row.subscription?.id },
 *     );
 *
 *   A list that returns a wrapper object: unwrap the array inside the function you pass.
 *
 *     const invoices = await listAll(
 *       (page, perPage) => client.invoices.listInvoices({ page, perPage }).then((r) => r.invoices),
 *       { maxPages: 50, key: (invoice) => invoice.uid },
 *     );
 *
 *   A list operation with no `page` field must not be passed here. Its Fields table on the SDK map
 *   has no `page` row (`listSubscriptionComponents` is one), and one call returns everything. It
 *   would hand back the same rows for every page until the ceiling throws. TypeScript refuses
 *   `{ page, perPage }` in the request of such an operation, so the mistake does not compile.
 *
 * What it does
 *   - Asks for 200 rows a page, Maxio's maximum. A larger value is cut to 200 with no error. Pass
 *     `perPage` for an operation whose own maximum is lower (`listMrrMovements` stops at 50).
 *   - Starts at page 1 and stops only when a page comes back empty. A short page is not the end:
 *     where the operation's maximum is below what was asked, every page is short.
 *   - Never returns part of a list. `maxPages` is the most requests it makes, the final empty page
 *     included. Reaching it throws `PageCeilingReached`.
 *   - With a `key` function, drops a row whose key was already seen. Pages are cut by position, so
 *     when a row is added or removed while you read, the rows after it shift: without a key the
 *     same row can come back on the next page.
 *
 * What a key cannot fix
 *   A shift can also move a row you have not read yet onto a page you have already passed. That
 *   row is missed, and nothing reports it. To make it unlikely, sort by something that does not
 *   change, oldest first, where the operation offers it: for subscriptions
 *   `{ sort: "id", direction: "asc" }`. The spec declares both values. They were not tried against
 *   a live site.
 *
 * Implements knowledge/rules.md R8.
 *
 * Leaves to the caller: the filters (knowledge/rules.md R9 names the ones that fail open), the
 * ceiling and what to do when it is hit, the sort order, and the request limit
 * (recipes/request-limit.ts: a walk makes its calls one after another, so wrapping the whole walk
 * takes one slot).
 *
 * Needs only the SDK. Copy into your project and adapt. Not part of the SDK's API.
 */
import type {
  MaxioAdvancedBillingClient,
  RequestOptions,
  SubscriptionResponse,
  Subscriptions,
} from "maxio-advanced-billing";

/** Maxio's maximum for `per_page`. A larger value returns 200 rows and no error. */
export const MAX_PER_PAGE = 200;

export type ListAllOptions<T> = {
  /**
   * The most requests to make, the final empty page included. A list of N full pages needs at
   * least N + 1.
   */
  maxPages: number;
  /** Rows to ask for per page, from 1 to 200. Default 200. */
  perPage?: number | undefined;
  /**
   * What makes a row the same row, usually its id. When given, a row whose key was already seen
   * is dropped. A row whose key is `undefined` is always kept.
   */
  key?: ((row: T) => string | number | undefined) | undefined;
};

/** The walk used up its ceiling before Maxio returned an empty page. Nothing was returned. */
export class PageCeilingReached extends Error {
  readonly maxPages: number;
  /** Rows read before the walk stopped, after duplicates were dropped. */
  readonly rowsRead: number;

  constructor(maxPages: number, rowsRead: number) {
    super(
      `Read ${rowsRead} rows in ${maxPages} pages without reaching an empty page. ` +
        "The list is longer than maxPages allows, or the operation ignores `page`.",
    );
    this.name = "PageCeilingReached";
    this.maxPages = maxPages;
    this.rowsRead = rowsRead;
  }
}

/**
 * Reads every page of one list. `fetchPage` makes the SDK call for the page it is handed and
 * returns that page's rows.
 *
 * @throws PageCeilingReached when `maxPages` requests did not reach an empty page.
 * @throws RangeError before any request when `maxPages` or `perPage` is out of range.
 */
export async function listAll<T>(
  fetchPage: (page: number, perPage: number) => Promise<readonly T[]>,
  options: ListAllOptions<T>,
): Promise<T[]> {
  const { maxPages, key } = options;
  const perPage = options.perPage ?? MAX_PER_PAGE;
  // An unbounded ceiling would leave Maxio's cooperation as the only way the loop ends.
  if (!Number.isInteger(maxPages) || maxPages < 1) {
    throw new RangeError("maxPages must be an integer of 1 or more");
  }
  if (!Number.isInteger(perPage) || perPage < 1 || perPage > MAX_PER_PAGE) {
    throw new RangeError(`perPage must be an integer from 1 to ${MAX_PER_PAGE}`);
  }

  const rows: T[] = [];
  const seen = new Set<string | number>();
  for (let page = 1; page <= maxPages; page++) {
    const batch = await fetchPage(page, perPage);
    if (batch.length === 0) return rows; // the only end signal
    for (const row of batch) {
      const id = key?.(row);
      if (id !== undefined) {
        if (seen.has(id)) continue;
        seen.add(id);
      }
      rows.push(row);
    }
  }
  throw new PageCeilingReached(maxPages, rows.length);
}

/**
 * Every subscription that matches `filters`, each as the `{ subscription }` wrapper Maxio sends.
 * Rows are told apart by `subscription.id`, so a subscription is returned once.
 */
export function listAllSubscriptions(
  client: MaxioAdvancedBillingClient,
  filters: Omit<Subscriptions.ListSubscriptionsRequest, "page" | "perPage">,
  options: Pick<ListAllOptions<SubscriptionResponse>, "maxPages" | "perPage">,
  requestOptions?: RequestOptions,
): Promise<SubscriptionResponse[]> {
  return listAll(
    (page, perPage) => client.subscriptions.listSubscriptions({ ...filters, page, perPage }, requestOptions),
    { ...options, key: (row) => row.subscription?.id },
  );
}
