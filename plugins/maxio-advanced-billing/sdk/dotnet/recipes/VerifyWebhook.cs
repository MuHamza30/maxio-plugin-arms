// VerifyWebhook.cs
//
// Checks that a webhook came from Maxio. It computes the hex HMAC-SHA256 of the raw request body,
// keyed with the site's shared key, and compares it in constant time with the signature Maxio
// sent. A missing or malformed signature is false, never an exception. SignatureFrom reads the
// signature out of a request's headers whatever the case of the header name.
//
// Implements: knowledge/rules.md R19 (the signature step).
//
// What it does not do:
// - It does not read the body. Pass the bytes exactly as they were received, before anything
//   parses them as a form or as JSON or decodes them to a string. A body that was parsed and
//   written out again never matches.
// - It does not answer the webhook. Answer 200 quickly, also for events you do not handle, and do
//   the work afterwards.
// - It does not skip a webhook id you have already processed, and it does not re-read the resource
//   before you act on it (knowledge/rules.md R20).
// - It does not read a signature that Maxio put in the query string of your endpoint URL. Pass
//   that value to IsFromMaxio yourself.
//
// Copy into your project and adapt. Not part of the SDK's API.

#nullable enable

using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Security.Cryptography;
using System.Text;

namespace MaxioRecipes;

/// <summary>Verifies the signature of a Maxio webhook (knowledge/rules.md R19).</summary>
public static class VerifyWebhook
{
    /// <summary>The request header that carries the signature.</summary>
    public const string SignatureHeader = "X-Chargify-Webhook-Signature-Hmac-Sha-256";

    /// <summary>
    /// True when <paramref name="signature"/> is the hex HMAC-SHA256 of <paramref name="rawBody"/>
    /// under <paramref name="sharedKey"/>. False when the signature is null, is not 64 hex digits,
    /// or does not match. Throws only for a null body or a missing shared key, which are faults in
    /// your own setup and must not look like a forged webhook.
    /// </summary>
    /// <param name="rawBody">The request body exactly as received.</param>
    /// <param name="signature">The signature Maxio sent, or null when it sent none.</param>
    /// <param name="sharedKey">The site's shared key, from secret storage.</param>
    public static bool IsFromMaxio(byte[] rawBody, string? signature, string sharedKey)
    {
        _ = rawBody ?? throw new ArgumentNullException(nameof(rawBody));

        // An empty key still produces a signature, and anyone can compute that one. A missing
        // secret has to stop the endpoint, not turn the check into one every forger passes.
        if (string.IsNullOrEmpty(sharedKey))
            throw new ArgumentException("The site's shared key is not configured.", nameof(sharedKey));

        var sent = DecodeHex(signature);
        if (sent is null)
            return false;

        using (var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(sharedKey)))
        {
            return FixedTimeEquals(hmac.ComputeHash(rawBody), sent);
        }
    }

    /// <summary>
    /// The signature from headers that carry several values per name: ASP.NET Core's
    /// <c>Request.Headers</c>, the <c>Headers</c> of an <c>HttpRequestMessage</c> and of an Azure
    /// Functions <c>HttpRequestData</c>, or a dictionary of string arrays. The name is matched in
    /// any case. Null when the header is absent or has more than one value.
    /// </summary>
    public static string? SignatureFrom<TValues>(IEnumerable<KeyValuePair<string, TValues>>? headers)
        where TValues : IEnumerable<string?>
    {
        if (headers is null)
            return null;

        string? signature = null;
        var seen = 0;
        foreach (var header in headers)
        {
            if (!IsSignatureHeader(header.Key) || header.Value == null)
                continue;

            foreach (var value in header.Value)
            {
                signature = value;
                seen++;
            }
        }

        // Two signatures cannot both be the one Maxio sent, so more than one is treated as none.
        return seen == 1 ? signature : null;
    }

    /// <summary>
    /// The signature from headers that carry one string per name, such as the dictionary an AWS
    /// Lambda proxy event delivers. The name is matched in any case. Null when the header is
    /// absent or appears under two spellings.
    /// </summary>
    public static string? SignatureFrom(IEnumerable<KeyValuePair<string, string>>? headers)
    {
        if (headers is null)
            return null;

        string? signature = null;
        var seen = 0;
        foreach (var header in headers)
        {
            if (!IsSignatureHeader(header.Key))
                continue;

            signature = header.Value;
            seen++;
        }

        return seen == 1 ? signature : null;
    }

    /// <summary>
    /// The signature from a <see cref="NameValueCollection"/>: the <c>Headers</c> of an
    /// <c>HttpListenerRequest</c> or of an ASP.NET (System.Web) <c>HttpRequest</c>. The name is
    /// matched in any case. Null when the header is absent or has more than one value.
    /// </summary>
    public static string? SignatureFrom(NameValueCollection? headers)
    {
        if (headers is null)
            return null;

        string? signature = null;
        var seen = 0;
        for (var i = 0; i < headers.Count; i++)
        {
            if (!IsSignatureHeader(headers.GetKey(i)))
                continue;

            var values = headers.GetValues(i);
            if (values is null)
                continue;

            foreach (var value in values)
            {
                signature = value;
                seen++;
            }
        }

        return seen == 1 ? signature : null;
    }

    private static bool IsSignatureHeader(string? name) =>
        string.Equals(name, SignatureHeader, StringComparison.OrdinalIgnoreCase);

    // Comparing the 32 decoded bytes, not two strings, makes upper and lower case hex equal.
    private static byte[]? DecodeHex(string? hex)
    {
        if (hex is null || hex.Length != 64)
            return null;

        var bytes = new byte[32];
        for (var i = 0; i < bytes.Length; i++)
        {
            int high = HexValue(hex[2 * i]), low = HexValue(hex[(2 * i) + 1]);
            if (high < 0 || low < 0)
                return null;
            bytes[i] = (byte)((high << 4) | low);
        }

        return bytes;
    }

    private static int HexValue(char c) =>
        c >= '0' && c <= '9' ? c - '0'
        : c >= 'a' && c <= 'f' ? c - 'a' + 10
        : c >= 'A' && c <= 'F' ? c - 'A' + 10
        : -1;

    // `==` or SequenceEqual stops at the first byte that differs, and that timing tells a forger
    // how much of a guess was right. Both arrays are 32 bytes here; the lengths are not secret.
#if NETCOREAPP2_1_OR_GREATER || NETSTANDARD2_1_OR_GREATER
    private static bool FixedTimeEquals(byte[] computed, byte[] sent) =>
        CryptographicOperations.FixedTimeEquals(computed, sent);
#else
    // netstandard2.0 and .NET Framework have no CryptographicOperations.FixedTimeEquals. This is
    // the same loop: it reads every byte and has no branch that depends on the data.
    [System.Runtime.CompilerServices.MethodImpl(
        System.Runtime.CompilerServices.MethodImplOptions.NoInlining |
        System.Runtime.CompilerServices.MethodImplOptions.NoOptimization)]
    private static bool FixedTimeEquals(byte[] computed, byte[] sent)
    {
        if (computed.Length != sent.Length)
            return false;

        var difference = 0;
        for (var i = 0; i < computed.Length; i++)
            difference |= computed[i] ^ sent[i];
        return difference == 0;
    }
#endif
}
