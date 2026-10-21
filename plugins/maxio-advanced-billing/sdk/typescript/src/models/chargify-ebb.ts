import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ChargifyEbb = {
  /**
   * This timestamp determines what billing period the event will be billed in. If your request
   * payload does not include it, Chargify will add `chargify.timestamp` to the event payload and
   * set the value to `now`.
   */
  timestamp?: Date;
  /**
   * A unique ID set by Chargify. This field is reserved. If `chargify.id` is present in the request
   * payload, it will be overwritten.
   */
  id?: string;
  /**
   * An ISO-8601 timestamp, set by Chargify at the time each event is recorded. This field is
   * reserved. If `chargify.created_at` is present in the request payload, it will be overwritten.
   */
  createdAt?: Date;
  /**
   * User-defined string scoped per-stream. Duplicate events within a stream will be silently
   * ignored. Tokens expire after 31 days.
   */
  uniquenessToken?: string;
  /**
   * Id of Maxio Advanced Billing Subscription which is connected to this event. Provide
   * `subscription_id` if you configured `chargify.subscription_id` as Subscription Identifier in
   * your Event Stream.
   */
  subscriptionId?: number;
  /**
   * Reference of Maxio Advanced Billing Subscription which is connected to this event. Provide
   * `subscription_reference` if you configured `chargify.subscription_reference` as Subscription
   * Identifier in your Event Stream.
   */
  subscriptionReference?: string;
};

export const chargifyEbbSchema: Schema<ChargifyEbb> = s.object<ChargifyEbb>({
  timestamp: s.optional(s.dateTime()),
  id: s.optional(s.string()),
  createdAt: s.optional(s.dateTime()),
  uniquenessToken: s.optional(s.string()),
  subscriptionId: s.optional(s.int()),
  subscriptionReference: s.optional(s.string()),
  _keysMap: {
    createdAt: "created_at",
    uniquenessToken: "uniqueness_token",
    subscriptionId: "subscription_id",
    subscriptionReference: "subscription_reference",
  },
});
