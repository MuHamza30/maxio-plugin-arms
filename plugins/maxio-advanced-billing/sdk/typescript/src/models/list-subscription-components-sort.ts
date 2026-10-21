import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ListSubscriptionComponentsSort = {
  Id: "id",
  UpdatedAt: "updated_at",
} as const;
export type ListSubscriptionComponentsSort =
  | (typeof ListSubscriptionComponentsSort)[keyof typeof ListSubscriptionComponentsSort]
  | (string & {});

export const listSubscriptionComponentsSortSchema: EnumSchema<ListSubscriptionComponentsSort> =
  s.enumOf<ListSubscriptionComponentsSort>(ListSubscriptionComponentsSort);
