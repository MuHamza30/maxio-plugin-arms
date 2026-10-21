import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  listSubscriptionGroupPrepaymentItemSchema,
  type ListSubscriptionGroupPrepaymentItem,
} from "./list-subscription-group-prepayment-item.js";

export type ListSubscriptionGroupPrepayment = {
  prepayment: ListSubscriptionGroupPrepaymentItem;
};

export const listSubscriptionGroupPrepaymentSchema: Schema<ListSubscriptionGroupPrepayment> =
  s.object<ListSubscriptionGroupPrepayment>({
    prepayment: listSubscriptionGroupPrepaymentItemSchema,
  });
