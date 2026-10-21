import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type TooManyManagementLinkRequests = {
  error: string;
  newLinkAvailableAt: Date;
};

export const tooManyManagementLinkRequestsSchema: Schema<TooManyManagementLinkRequests> =
  s.object<TooManyManagementLinkRequests>({
    error: s.string(),
    newLinkAvailableAt: s.dateTime(),
    _keysMap: {
      newLinkAvailableAt: "new_link_available_at",
    },
  });
