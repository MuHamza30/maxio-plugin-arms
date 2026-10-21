import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type DeliverProformaInvoiceRequest = {
  recipientEmails?: string[];
  ccRecipientEmails?: string[];
  bccRecipientEmails?: string[];
};

export const deliverProformaInvoiceRequestSchema: Schema<DeliverProformaInvoiceRequest> =
  s.object<DeliverProformaInvoiceRequest>({
    recipientEmails: s.optional(s.array(s.string())),
    ccRecipientEmails: s.optional(s.array(s.string())),
    bccRecipientEmails: s.optional(s.array(s.string())),
    _keysMap: {
      recipientEmails: "recipient_emails",
      ccRecipientEmails: "cc_recipient_emails",
      bccRecipientEmails: "bcc_recipient_emails",
    },
  });
