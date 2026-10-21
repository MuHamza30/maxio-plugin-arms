import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type Webhook = {
  /** A string describing which event type produced the given webhook */
  event?: string;
  /**
   * The unique identifier for the webhook (unique across all of Chargify). This is not changed on a
   * retry/replay of the same webhook, so it may be used to avoid duplicate action for the same
   * event.
   */
  id?: number;
  /** Timestamp indicating when the webhook was created */
  createdAt?: Date;
  /**
   * Text describing the status code and/or error from the last failed attempt to send the Webhook.
   * When a webhook is retried and accepted, this field will be cleared.
   */
  lastError?: string;
  /**
   * Timestamp indicating when the last non-acceptance occurred. If a webhook is later resent and
   * accepted, this field will be cleared.
   */
  lastErrorAt?: Date;
  /**
   * Timestamp indicating when the webhook was accepted by the merchant endpoint. When a webhook is
   * explicitly replayed by the merchant, this value will be cleared until it is accepted again.
   */
  acceptedAt?: Date | null;
  /** Timestamp indicating when the most recent attempt was made to send the webhook */
  lastSentAt?: Date;
  /** The url that the endpoint was last sent to. */
  lastSentUrl?: string;
  /**
   * “A boolean flag describing whether the webhook was accepted by the webhook endpoint for the
   * most recent attempt. (Acceptance is defined by receiving a “200 OK” HTTP response within a
   * reasonable timeframe, e.g., 15 seconds.)”
   */
  successful?: boolean;
  /** The data sent within the webhook post */
  body?: string;
  /** The calculated webhook signature */
  signature?: string;
  /** The calculated HMAC-SHA-256 webhook signature */
  signatureHmacSha256?: string;
};

export const webhookSchema: Schema<Webhook> = s.object<Webhook>({
  event: s.optional(s.string()),
  id: s.optional(s.int()),
  createdAt: s.optional(s.dateTime()),
  lastError: s.optional(s.string()),
  lastErrorAt: s.optional(s.dateTime()),
  acceptedAt: s.optionalNullable(s.dateTime()),
  lastSentAt: s.optional(s.dateTime()),
  lastSentUrl: s.optional(s.string()),
  successful: s.optional(s.boolean()),
  body: s.optional(s.string()),
  signature: s.optional(s.string()),
  signatureHmacSha256: s.optional(s.string()),
  _keysMap: {
    createdAt: "created_at",
    lastError: "last_error",
    lastErrorAt: "last_error_at",
    acceptedAt: "accepted_at",
    lastSentAt: "last_sent_at",
    lastSentUrl: "last_sent_url",
    signatureHmacSha256: "signature_hmac_sha_256",
  },
});
