import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import {
  subscriptionGroupMembersArrayErrorSchema,
  type SubscriptionGroupMembersArrayError,
} from "../subscription-group-members-array-error.js";
import {
  subscriptionGroupSingleErrorSchema,
  type SubscriptionGroupSingleError,
} from "../subscription-group-single-error.js";

export type Errors11 = SubscriptionGroupMembersArrayError | SubscriptionGroupSingleError | string;

export const errors11Schema: Schema<Errors11> = s.of<Errors11>(
  s.union([
    s.lazy(() => subscriptionGroupMembersArrayErrorSchema),
    s.lazy(() => subscriptionGroupSingleErrorSchema),
    s.string(),
  ]),
);
