import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type DunningStepData = {
  dayThreshold: number;
  action: string;
  emailBody?: string | null;
  emailSubject?: string | null;
  sendEmail: boolean;
  sendBccEmail: boolean;
  sendSms: boolean;
  smsBody?: string | null;
};

export const dunningStepDataSchema: Schema<DunningStepData> = s.object<DunningStepData>({
  dayThreshold: s.int(),
  action: s.string(),
  emailBody: s.optionalNullable(s.string()),
  emailSubject: s.optionalNullable(s.string()),
  sendEmail: s.boolean(),
  sendBccEmail: s.boolean(),
  sendSms: s.boolean(),
  smsBody: s.optionalNullable(s.string()),
  _keysMap: {
    dayThreshold: "day_threshold",
    emailBody: "email_body",
    emailSubject: "email_subject",
    sendEmail: "send_email",
    sendBccEmail: "send_bcc_email",
    sendSms: "send_sms",
    smsBody: "sms_body",
  },
});
