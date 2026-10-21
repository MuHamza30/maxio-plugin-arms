/*
 * verify-webhook: check a Maxio webhook's signature before you read what it says.
 *
 * What it does
 *   `verifyWebhookSignature(rawBody, signature, sharedKey)` computes HMAC-SHA256 over the body
 *   bytes with the site's shared key, as a hex digest, and compares it with the signature in
 *   constant time. It returns `false`, and never throws, for a missing or malformed signature.
 *   `signatureFrom(headers)` reads the signature from the request's headers whatever the case of
 *   the header name.
 *
 * The body must be the bytes exactly as they arrived
 *   Verify before any body parser runs. Maxio signs the form-encoded bytes it sent
 *   (`payload[subscription][id]=...`). A body that was parsed, as a form or as JSON, and written
 *   out again has different bytes and never matches. That is why `rawBody` is a `Uint8Array` (a
 *   `Buffer` is one) and not a string or an object. With a fetch-style `Request`, pass
 *   `new Uint8Array(await request.arrayBuffer())`.
 *
 * The header name is lower case
 *   Node lower-cases the names of incoming headers, so `SIGNATURE_HEADER` is exported in lower
 *   case and `req.headers[SIGNATURE_HEADER]` finds the value. `signatureFrom` also takes a
 *   fetch-style `Headers` object and a plain object whose keys kept their case.
 *
 * An empty shared key throws. A secret that was never loaded must stop the handler loudly: read as
 * "", it would otherwise accept a signature anyone can compute.
 *
 * Implements the signature check of knowledge/rules.md R19.
 *
 * Leaves to the caller (knowledge/rules.md R19 and R20): keeping the raw body bytes; answering 200
 * for every event within about 15 seconds and doing the work afterwards; skipping a webhook `id`
 * already processed; and reading the resource again before acting on what an event says.
 *
 * Needs only Node's standard library (`node:crypto`). Copy into your project and adapt. Not part
 * of the SDK's API.
 */
import { createHmac, timingSafeEqual } from "node:crypto";

/** The request header that carries the signature, in the lower case Node delivers it in. */
export const SIGNATURE_HEADER = "x-chargify-webhook-signature-hmac-sha-256";

/**
 * Request headers in the forms HTTP servers hand them over: a fetch-style `Headers` object, or a
 * plain object of names to values such as Node's `req.headers`.
 */
export type WebhookHeaders =
  | { get(name: string): string | null }
  | Readonly<Record<string, string | readonly string[] | undefined>>;

const SHA256_HEX = /^[0-9a-f]{64}$/i;

/**
 * The signature header's value, or `undefined` when the header is absent or was sent more than
 * once. The name is matched in any case.
 */
export function signatureFrom(headers: WebhookHeaders): string | undefined {
  const get = headers["get"];
  if (typeof get === "function") {
    // A fetch-style Headers object matches names in any case itself.
    const value: unknown = get.call(headers, SIGNATURE_HEADER);
    return typeof value === "string" ? value : undefined;
  }

  const values: string[] = [];
  for (const [name, value] of Object.entries(headers)) {
    if (name.toLowerCase() !== SIGNATURE_HEADER) continue;
    if (typeof value === "string") values.push(value);
    else if (Array.isArray(value)) values.push(...value.filter((item) => typeof item === "string"));
  }
  // Two values cannot both be the signature, so neither is trusted.
  return values.length === 1 ? values[0] : undefined;
}

/**
 * @param rawBody The request body exactly as received, before any parsing.
 * @param signature The value of the signature header: pass `signatureFrom(req.headers)` or
 *   `req.headers[SIGNATURE_HEADER]`. When the endpoint URL was registered with the
 *   `{signature_hmac_sha_256}` variable, pass that query-string value instead. Anything but one
 *   string of 64 hex digits is rejected.
 * @param sharedKey The site's shared key.
 * @returns `true` only when the signature is the one Maxio computes for these bytes.
 * @throws Error when `sharedKey` is empty.
 */
export function verifyWebhookSignature(
  rawBody: Uint8Array,
  signature: string | readonly string[] | null | undefined,
  sharedKey: string,
): boolean {
  if (typeof sharedKey !== "string" || sharedKey.length === 0) {
    throw new Error("The Maxio webhook shared key is empty.");
  }

  // Shape first: timingSafeEqual throws when the lengths differ, and a hex decode silently drops
  // everything after the first character that is not hex.
  if (typeof signature !== "string" || !SHA256_HEX.test(signature)) return false;

  const expected = createHmac("sha256", sharedKey).update(rawBody).digest();
  const received = Buffer.from(signature, "hex");
  // `===` on the hex strings stops at the first character that differs, which lets a sender learn
  // a valid signature one character at a time. This comparison takes the same time wherever the
  // two differ.
  return timingSafeEqual(expected, received);
}
