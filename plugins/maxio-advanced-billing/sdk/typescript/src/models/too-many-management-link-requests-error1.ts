import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  tooManyManagementLinkRequestsSchema,
  type TooManyManagementLinkRequests,
} from "./too-many-management-link-requests.js";

export type TooManyManagementLinkRequestsError1 = {
  errors: TooManyManagementLinkRequests;
};

export const tooManyManagementLinkRequestsError1Schema: Schema<TooManyManagementLinkRequestsError1> =
  s.object<TooManyManagementLinkRequestsError1>({
    errors: tooManyManagementLinkRequestsSchema,
  });
