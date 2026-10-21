import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  listSubscriptionGroupPrepaymentSchema,
  type ListSubscriptionGroupPrepayment,
} from "./list-subscription-group-prepayment.js";

export type ListSubscriptionGroupPrepaymentResponse = {
  prepayments: ListSubscriptionGroupPrepayment[];
};

export const listSubscriptionGroupPrepaymentResponseSchema: Schema<ListSubscriptionGroupPrepaymentResponse> =
  s.object<ListSubscriptionGroupPrepaymentResponse>({
    prepayments: s.array(s.lazy(() => listSubscriptionGroupPrepaymentSchema)),
  });
