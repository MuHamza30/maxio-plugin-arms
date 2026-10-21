import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { sendEmailSchema, type SendEmail } from "./send-email.js";

export type AvailableActions = {
  sendEmail?: SendEmail;
};

export const availableActionsSchema: Schema<AvailableActions> = s.object<AvailableActions>({
  sendEmail: s.optional(s.lazy(() => sendEmailSchema)),
  _keysMap: {
    sendEmail: "send_email",
  },
});
