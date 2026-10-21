import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SendInvoiceRequest = {
  recipientEmails?: string[];
  ccRecipientEmails?: string[];
  bccRecipientEmails?: string[];
  /** Array of URLs to files to attach to the invoice email. Max 10 files, 10MB each. */
  attachmentUrls?: string[];
};

export const sendInvoiceRequestSchema: Schema<SendInvoiceRequest> = s.object<SendInvoiceRequest>({
  recipientEmails: s.optional(s.array(s.string())),
  ccRecipientEmails: s.optional(s.array(s.string())),
  bccRecipientEmails: s.optional(s.array(s.string())),
  attachmentUrls: s.optional(s.array(s.string())),
  _keysMap: {
    recipientEmails: "recipient_emails",
    ccRecipientEmails: "cc_recipient_emails",
    bccRecipientEmails: "bcc_recipient_emails",
    attachmentUrls: "attachment_urls",
  },
});
