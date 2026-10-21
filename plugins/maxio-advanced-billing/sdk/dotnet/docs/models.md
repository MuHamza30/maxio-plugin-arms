# Working with models in an APIMatic .NET SDK

**Read when:** you are about to construct request payloads or map SDK models onto your own domain types.
It covers working with models in an APIMatic-generated .NET SDK in C#: building request models, required
members and nullability, enums, union/AnyOf accessors, and JSON wire names versus C# property names.

Most request/response data are immutable `record`s built with object-initializers (covered in
`docs/calling-endpoints.md`). This doc covers the **non-obvious model shapes** that trip integrations up.
The patterns are generic across APIMatic .NET SDKs; take the real type names from the contract sheet (grounded from the SDK map/source) — never a decompiled or reflected view of the
installed package.

> Throughout this doc, `{...}` is a placeholder for a name you take from your SDK (e.g. `{Union}`,
> `{Variant}`, `{EnumType}`, `{RequestType}`) — replace it with the concrete identifier from the source.

## Polymorphic union types: `OneOf` and `AnyOf`

When a field can be one of several types, APIMatic generates a union `record` (under
`{RootNamespace}.Models.OneOf` or `.Models.AnyOf`). Build these with the generated **static factory
methods** (one per variant) and read them back with **`TryGet…` methods** — a union has no
object-initializer. JSON (de)serialization is automatic.

- `OneOf` — the value is exactly one variant, selected on the wire by a **discriminator property** (e.g.
  `type`). The generated converter reads that property and switches on it.
- `AnyOf` — no discriminator; the converter **tries each variant's schema in declaration order** and takes
  the first that deserializes.

⚠ **A payload matching no variant throws.** Both converters end in
`throw new JsonException("JSON does not match … schemas: …")`, raised mid-deserialization of the response —
you do not get a null union or an unset variant. A provider that adds a variant your SDK predates turns
into a `JsonException` on a call that was previously fine, so a union field is a place to expect
regeneration pressure. See `docs/error-handling.md` for where that surfaces in a catch ladder.

### Construct

```csharp
// One static factory per variant: {Union}.{Variant}(value)
var u1 = {Union}.String("...");
var u2 = {Union}.{Variant}(new {Variant} { /* ... */ });

// Implicit conversions: every OneOf variant has one; on AnyOf, primitives and models do.
{Union} u3 = "...";                          // AnyOf only — same as {Union}.String("...")
{Union} u4 = new {Variant} { /* ... */ };    // same as {Union}.{Variant}(...)
```

**A `OneOf`'s variants are always model or enum references** — the generator builds them from the schema's
discriminator mappings, so a `OneOf` has no primitive, list or map variant at all, and every variant it does
have gets an implicit conversion. An `AnyOf` is the open one: primitives and models get a conversion, while
list, map and untyped-object variants do not, and neither do two variants that share one CLR type (the
operators would collide). The factory is the form that always exists — reach for the implicit conversion
only where you can see one.

### Read / unwrap

```csharp
// Each variant has a bool TryGet{Variant}(out var value). The member name comes from the
// variant's SCHEMA type, not its CLR type — a `decimal` variant reads TryGetBigDecimal:
if (u1.TryGetString(out var s))            { /* use s (string)  */ }
else if (u1.TryGetBigDecimal(out var d))   { /* use d (decimal) */ }

// OneOf: branch over the variants you expect
if (resp.{Field}.TryGet{Variant}(out var v))           { /* ... */ }
else if (resp.{Field}.TryGet{OtherVariant}(out var w)) { /* ... */ }
```

The factory and `TryGet` names are built from the **variant's schema type name, which is often not its
CLR type name** — this is the single easiest thing to get wrong when writing a union branch from memory:

| Variant | Factory method | Reader |
| --- | --- | --- |
| a model `{Variant}` | `.{Variant}({Variant})` | `TryGet{Variant}(out {Variant})` |
| a big-decimal (CLR `decimal`) | `.BigDecimal(decimal)` | `TryGetBigDecimal(out decimal)` |
| a UUID (CLR `Guid`) | `.Guid(Guid)` | `TryGetGuid(out Guid)` |
| a date-time (CLR `DateTimeOffset`) | `.DateTime(DateTimeOffset)` | `TryGetDateTime(out DateTimeOffset)` |
| a date (**also** CLR `DateTimeOffset`) | `.Date(DateTimeOffset)` | `TryGetDate(out DateTimeOffset)` |
| an email / uri / ip (all CLR `string`) | `.EmailString(...)` / `.UriString(...)` / `.IpString(...)` | `TryGetEmailString(...)`, … |
| a list of `{Variant}` | `.ListOf{Variant}(IReadOnlyList<{Variant}>)` | `TryGetListOf{Variant}(out IReadOnlyList<{Variant}>)` |
| a map of `{Variant}` | `.MapOf{Variant}(...)` | `TryGetMapOf{Variant}(out …)` |

So a `decimal` variant is `TryGetBigDecimal`, never `TryGetDecimal`; three variants that are all CLR
`string` get three different names; and a `DateTimeOffset` variant is `TryGetDateTime` **or** `TryGetDate`
depending on which the definition declared — two members, one CLR type, and the C# signature cannot tell
them apart. Where two variants would collide outright the generator suffixes them (`String`, `String2`).
The primitive rows apply to `AnyOf` only, since a `OneOf` has no primitive variants. **Take the exact member
name from the contract sheet** (grounded from the SDK map/source) rather than deriving it from
the C# type you see. (Unions use the per-variant factories and `TryGet…` readers shown above;
`TryGetKnownValue` belongs to enums.) The `Optional<T>` backing a union is internal — interact only through the factories and
`TryGet…`.

## Collections

List/array properties are `IReadOnlyList<T>?`; maps are `IReadOnlyDictionary<TKey, TValue>?`. Assign a
`List<>`/array/`Dictionary<>` directly (each implements the read-only interface), or use collection
expressions:

```csharp
var body = new {RequestType}
{
    {ListProp} = ["A", "B"],                                    // IReadOnlyList<string>
    {MapProp}  = new Dictionary<string, string> { ["k"] = "v" } // IReadOnlyDictionary<string,string>
};
```

A null collection is omitted from the JSON; an **empty** collection is serialized.

**An untyped field holds a `JsonElement`.** A property typed `object` or `JsonElement` (nullable or not) holds a
`JsonElement` after a read, when it is not `null`. Read it with the `JsonElement` API,
never a cast to `Dictionary`.

## Dates & numbers

- **A date/time field is not necessarily a `DateTimeOffset?` — check the property type.** The generator
  emits `DateTimeOffset?` only where the API definition marks the field as a date/time. Where it does not,
  the field is a plain `string?`, frequently carrying a `[RegularExpression]` attribute that *documents* an
  RFC-3339 shape without enforcing it (see below). Both are common in the same SDK, and one of the sampled
  SDKs has **no** `DateTimeOffset` in its models at all. Take the type from the contract sheet; a
  `DateTimeOffset.Parse` written against a field that is already a `DateTimeOffset` will not compile, and a
  hand-built string written into a `DateTimeOffset?` field will not either.
- **A `DateTimeOffset` model property carries no converter** — it round-trips as `System.Text.Json`'s
  default, ISO-8601 with an offset (`"2024-06-17T15:30:45+00:00"`), *even where the API documents a
  date-only shape*. The generator does ship four date converters (ISO-8601, RFC-1123, Unix epoch seconds,
  date-only), but it attaches them to **whole-response payloads** — an operation whose response body is a
  date scalar, or a list or map of them — not to properties inside a model. So if a field's documented wire shape is `YYYY-MM-DD` and
  the property is a `DateTimeOffset?`, what the SDK sends is the full ISO-8601 form, and reconciling that
  with the provider is your problem, not the SDK's. Do not hand-format anyway; for your own formatting use
  the BCL (`DateTimeOffset.Parse`, `.ToString("O")`), never the SDK's internal converters.
- Money/quantities may be `string`, `decimal`, or a string-or-number `AnyOf` union; the model's property
  type is the source of truth. Numeric types vary per SDK (`int`, `long`, `double`, …) — take the exact
  type from the contract sheet; don't assume `double`.

<!-- maxio:start -->
**Maxio money in this SDK.** No model has a `decimal` member, so `knowledge/rules.md` R4 ("never a float")
is met by choosing the arm or the type, field by field. The member's type in the model's own file decides:

| The member's type | Examples | Do |
| --- | --- | --- |
| `long`, `long?`, or a `string`-or-`long` union | The `*_in_cents` fields | Integer cents, exact. Never divide into a `double` |
| `string` or `string?` | Most invoice amounts, `Component.UnitPrice` | `decimal.Parse(text, NumberStyles.Number, CultureInfo.InvariantCulture)` |
| A `string`-or-`double` union | Component and bracket `unit_price` (`UnitPrice1`, `UnitPrice`), payment and credit `amount` (`Amount`, `Amount2`), coupon `percentage` | Write the `String` arm. Read `TryGetString` first |
| `double` or `double?` | `Coupon.Amount`, `CurrencyPrice.Price`, `CouponCurrency.Price`, `CreateCurrencyPrice.Price`, `UpdateCurrencyPrice.Price`, `CreatePrepayment.Amount` | No exact form exists. See below |

```csharp
// Write: the String arm carries the decimal's own digits.
UnitPrice price = UnitPrice.String(amount.ToString(CultureInfo.InvariantCulture));

// Read: text when Maxio sent text.
decimal value =
    unitPrice.TryGetString(out var text) ? decimal.Parse(text, NumberStyles.Number, CultureInfo.InvariantCulture)
    : unitPrice.TryGetDouble(out var number) ? (decimal)number   // Maxio sent a JSON number: already a double
    : throw new InvalidOperationException("unit_price holds no value.");
```

Where these types do not let you keep a value out of `double`:

- **A JSON number always arrives as a `double`**, in every one of these unions.
- **A union whose first factory is `Double` reads a quoted number as a `double` too.** `UnitPrice` (the
  bracket price on `Price`) and the request-only `UnitPrice7`, `Quantity3` and `Amount3` try `Double` first,
  and the serializer accepts a number in quotes. So `"unit_price": "0.00000065"` arrives in the `Double` arm
  and `TryGetString` is false. A union whose first factory is `String` keeps the text.
- **The six `double` members have no other form.** Convert at the edge, `(decimal)value` on a read and
  `(double)amount` on a write, and keep your own arithmetic in `decimal`. Where a cents sibling exists
  (`Coupon.AmountInCents`), use it.
<!-- maxio:end -->

## Validation attributes are documentation, not enforcement

Generated models carry validation attributes transcribed from the API definition — hundreds, sometimes
thousands, in a large SDK. They come from two places:

- the BCL: `[StringLength]`, `[MaxLength]`, `[MinLength]`, `[RegularExpression]`, `[Range]`;
- the SDK's own `{RootNamespace}.Core.Validation.Attributes`, for the constraints DataAnnotations has no
  equivalent for: `[Minimum]`, `[Maximum]`, `[ExclusiveMinimum]`, `[ExclusiveMaximum]`, `[MultipleOf]`,
  `[Format]`, `[UniqueItems]`, `[MinProperties]`, `[MaxProperties]`. `[Format]` in particular is easy to
  miss and can be the most common attribute in the tree.

**Nothing in the SDK evaluates any of them.** No validation is invoked anywhere on the request path, so a
value that violates the attribute right next to it is serialized and sent, and the constraint is enforced
only by the provider, as a `400` you then have to interpret.

Read them as the API's documented contract — they are an accurate, machine-transcribed statement of what
the provider will accept, and far cheaper to consult than the API docs. Just do not mistake their presence
for a client-side guard. Where you want one, opt in explicitly at your own boundary:

```csharp
Validator.ValidateObject(body, new ValidationContext(body), validateAllProperties: true);
```

The SDK's own attributes derive from `ValidationAttribute`, so that one call covers both families — you do
not need to handle `[Format]` or `[Minimum]` separately.

That is worth doing on user-supplied input before a write, where a rejected request costs a round-trip and
an error path; it is usually not worth it on values your own code produced.

## Enums

Enums are type-safe records — `OpenStringEnum<T>` over `string` or `OpenIntEnum<T>` over `long` — never C#
enums. Use the static constants; they convert implicitly to their underlying value. Reading back: `.Value`
(or the implicit conversion) yields the raw wire value — but **not** `ToString()`, see the warning below —
and `==` compares by value, so two instances read from the same wire value are equal.

There is **no public factory**: `{EnumType}.FromValue(...)` does not exist, and a value the spec does not
declare cannot be constructed in code. Resolve a raw value with `{EnumType}.TryGetKnownValue(value, out var
known)` — exact, case-sensitive — and guard a received value with `instance.IsKnownValue()`. A server value
the SDK does not declare still deserializes (enums are open on reads), round-trips unchanged with the
server's own casing, and compares without constructing one: `instance.Is("raw")` or `instance == "raw"`.

Branch with the generated `Match`, not a `switch`: one `on{Member}` arm per declared value in spec order,
then `otherwise`, which receives the raw wire value of anything undeclared. Pass the arms by name — the
parameters are positional, and a regenerated SDK that adds or reorders a value changes the signature (a
source break, and `MissingMethodException` for an assembly compiled against the old shape).

```csharp
{request}.{EnumProp} = {EnumType}.SomeConstant;
string wire = {response}.{EnumProp}.Value;                          // raw wire value back out
if ({EnumType}.TryGetKnownValue(value, out var known)) { /* known constant */ }
var text = {response}.{EnumProp}.Match(
    onSomeConstant: () => "some",
    onOtherConstant: () => "other",
    otherwise: raw => $"undeclared: {raw}");
```

⚠ **`ToString()` does not give you the wire value — it gives the record's debug form.** The base class
overrides `ToString()` to return the value, but each generated enum is itself a `record`, so the compiler
synthesises its own `ToString()` that shadows the override:

```csharp
string a = {EnumType}.SomeConstant.Value;      // "SOME_CONSTANT"  ← the wire value
string b = {EnumType}.SomeConstant;            // "SOME_CONSTANT"  ← implicit conversion, also fine
string c = $"{ {EnumType}.SomeConstant }";     // "{EnumType} { Value = SOME_CONSTANT }"  ← NOT the wire value
string d = {EnumType}.SomeConstant.ToString(); // same debug form
```

String interpolation picks `ToString()`, so an enum interpolated into a URL, a log line, or a hand-built
query string silently carries the debug form — and so does `string.Format`. Concatenation with `+` is safe
on a **string** enum (the implicit conversion to `string` wins overload resolution) but **not** on an int
enum: there is no `string + int` operator, so it binds `string + object` and you get the debug form again.
Use `.Value` explicitly whenever the string leaves your process, and the distinction stops mattering.

A member whose name would collide with the enum's own name, with the inherited or generated surface
(such as `Value`, `Match` or `IsKnownValue`), or with a member of `object` carries a `Member` suffix — a
value `value` becomes `ValueMember`; its siblings keep their plain names.

See [docs/models-reference.md](models-reference.md) for full string- and int-enum declarations and union-member discovery.

<!-- maxio:start -->
**Maxio: where a note and these types do not line up.** Maxio's notes name wire fields. Where a note
allows a value that a member's type does not, the note cannot be followed as written. Check the member's
type in its file first.

- **A filter is one value of its own enum.** `ListSubscriptionsRequest.State` is a single
  `SubscriptionStateFilter`. That is not `SubscriptionState`, it is not a list, and enums have no public
  factory, so several states cannot be sent in one call. List without the filter and classify each row's
  `State` (`recipes/SubscriptionState.cs`).
- **A path id typed `int` takes no handle.** A path member that accepts `handle:<handle>` is typed
  `string`. `ReadProductFamilyRequest.Id` is `required int`, so `ReadProductFamily` cannot be called with a
  handle. `ListProductsForProductFamilyRequest.ProductFamilyId` is a `string` and can. To turn a family
  handle into an id, call `ListProductFamilies` and match `ProductFamily.Handle`.
- **"The same body" on two operations is two types.** `MigrateSubscriptionProduct` takes a
  `SubscriptionProductMigration` and `PreviewSubscriptionProductMigration` takes a
  `SubscriptionMigrationPreviewOptions`. Neither can be passed to the other: set the same members on both.
- **A wire name may have no member on the model you hold.** `Subscription` has no `next_billing_at`. Its
  nearest members are `NextAssessmentAt` and `CurrentPeriodEndsAt`. Which one a note means is Maxio's to
  say: read the member docs in the model's file and put the choice on the sheet as `UNVERIFIED`.
<!-- maxio:end -->

## Fields the spec does not declare

Models declare their wire properties explicitly. An object or allOf model also carries a
`[JsonExtensionData]` bag — `public AdditionalProperties AdditionalProperties { get; init; } = [];`
(`{RootNamespace}.Core.Models`) — so unknown JSON fields are **kept**, not dropped: a field the provider
added after this SDK was generated survives deserialization and round-trips back out on serialize. A
schema with `additionalProperties: false` has no bag, a `OneOf`/`AnyOf` union has none of its own, and the
bag is named `AdditionalProperties2` when a spec property's C# name is already `AdditionalProperties`.
Take the bag's name and type from the contract sheet.

Read one with `response.AdditionalProperties.TryGetValue<T>("field_name", out var value)` (deserializes
the captured `JsonElement` to `T`), or `TryGetElement` for the raw `JsonElement`; `Set(key, value)` adds
one to a request. When the schema types its extra fields, the bag is `AdditionalProperties<T>`, whose
`TryGetValue("field_name", out var value)` takes no type argument.
Two cautions: the keys are **wire names** (there is no C# property, so nothing maps the
casing for you), and a field appearing here rather than as a typed property is a regeneration signal —
prefer regenerating the SDK over building program logic on stringly-typed lookups. The
bag itself has no `[JsonPropertyName]` and no wire name — its contents merge
into the model's own JSON object.

<!-- maxio:start -->
### Maxio: `uniqueness_token` and `action_link`

Maxio uses two fields the spec declares on no request and no error model. The map's contract cannot show
them and no typed property exists, so both go through the bag.

**Send `uniqueness_token` beside the resource object.** It is Maxio's duplicate key (`knowledge/rules.md`
R12): one per write, minted once for that write, kept with your own record of it, and sent again
unchanged on every resend of it. It belongs at the top level of the body, so set it on the root body model
(the type of the request record's `Body`), not on the resource model inside it:

```csharp
var body = new CreateSubscriptionRequest { Subscription = subscription };   // the root model
body.AdditionalProperties.Set("uniqueness_token", uniquenessToken);         // beside "subscription"

var created = await client.Subscriptions.CreateSubscription(
    new CreateSubscriptionOperationRequest { Body = body }, cancellationToken: ct);
```

That sends `{"subscription":{...},"uniqueness_token":"..."}`.

- **A misspelt key is sent silently.** The key is a string, so `uniqeness_token` compiles, goes out, and
  Maxio ignores it. So does a token set on `body.Subscription.AdditionalProperties`, which lands inside
  `"subscription"`. Only a test that captures the request proves the key is where Maxio reads it
  (`docs/testing.md`, *Assert the outgoing request*). Assert on the root of the parsed body,
  `JsonDocument.Parse(handler.LastBody!).RootElement.GetProperty("uniqueness_token")`: a substring check
  also passes on a nested key. `recipes/SafeSignup.cs` sends the token this way and was checked on the wire
  (`recipes/README.md`).
- **Which writes can carry it.** Every operation that has a `Body` takes a root model with this bag, except
  `BulkRecordEvents`, whose body is a list. A write whose request record has no `Body` member cannot carry
  the token with this SDK: `RetrySubscriptionRequest` is one. Its only guards are no automatic resend and a
  read-back (`docs/configuration-resilience.md`, "Maxio: retries, timeouts and paging").
- **Events are different.** `RecordEvent` and `BulkRecordEvents` take the token inside each event, as the
  declared member `ChargifyEbb.UniquenessToken` (reached through `EbbEvent.Chargify`). Set that property.
- The `Idempotency-Key` header the SDK adds to every non-GET call is not this key. Maxio does not read it.

**Read `action_link` from a 422.** A 422 can be a 3-D Secure challenge carrying an `action_link` to send the
customer to (R13). No error model declares it. On `CreateSubscription` the typed 422 body is
`ErrorListResponse1`, whose bag keeps it:

```csharp
catch (ApiException<CreateSubscriptionError> ex)
    when (ex.Error.TryGetErrorListResponse1(out var rejection) &&
          rejection.AdditionalProperties.TryGetValue<string>("action_link", out var actionLink))
{
    // 3-D Secure: send the customer to actionLink. Not a validation error, so do not change the request.
}
```

For another operation, take the error type, the accessor and the body model from its map row. The link is
read this way only when the 422 body fits the typed model: for `ErrorListResponse1`, an `errors` list of
strings. A 422 that does not fit arrives as `ResponseDeserializationException`, which carries no body. The
spec names the field and shows no example body, so its place at the top level of the body is
*(unconfirmed)*. If a real challenge shows no link, print the raw body (`docs/error-handling.md`, "Maxio:
reading a rejection") and report it.
<!-- maxio:end -->
