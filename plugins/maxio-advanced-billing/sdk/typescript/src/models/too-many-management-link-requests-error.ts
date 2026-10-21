import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  tooManyManagementLinkRequestsSchema,
  type TooManyManagementLinkRequests,
} from "./too-many-management-link-requests.js";

export type TooManyManagementLinkRequestsError = {
  errors: TooManyManagementLinkRequests;
};

export const tooManyManagementLinkRequestsErrorSchema: Schema<TooManyManagementLinkRequestsError> =
  s.object<TooManyManagementLinkRequestsError>({
    errors: tooManyManagementLinkRequestsSchema,
  });
