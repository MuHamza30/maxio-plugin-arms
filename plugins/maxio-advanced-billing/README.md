# Maxio Advanced Billing SDK Plugin

A plugin for integrating Maxio Advanced Billing with the APIMatic-generated SDK, in C#/.NET, Python and
TypeScript. Everything of substance ships inside each SDK folder, beside the SDK's code: the contract map,
Maxio's business rules, usage docs and recipes. The plugin adds the parts that make sure they are read.

## What's inside

| Path | What it is |
| --- | --- |
| `sdk/dotnet/`, `sdk/python/`, `sdk/typescript/` | The SDK for each language, with everything an agent needs beside its code (below) |
| `skills/maxio-advanced-billing/` | The one skill: a router that sends the agent to the SDK folder for the project's language |
| `hooks/` | One hook script and a hooks file per host: `hooks.json` (Claude Code), `hooks.codex.json`, `hooks.cursor.json` |
| `rules/` | The ten rules as an always-applied rule for Cursor |

Each SDK folder holds:

| Path | Holds |
| --- | --- |
| `AGENTS.md` | The entry point for a coding agent: the reading order, the ten rules agents most often get wrong, and where everything else is |
| `sdk-map.md`, `map/operations/` | The contract: every operation's signature, types and error cases. `sdk-map.md` opens with the ten rules, and an operation block carries Maxio's must-follow rules for that operation, or a pointer to its notes |
| `knowledge/` | Maxio's business rules: 20 API-wide rules, 20 decision tables, 9 lifecycles, 15 go-live checks, notes for 114 operations, and 147 documented rejections by status and message with cause and fix |
| `docs/` | How to use this SDK: the plan-first workflow, and a page each for authentication, calling endpoints, models, errors, configuration and testing, with Maxio's site, retry, timeout and rejection specifics marked |
| `recipes/` | Code to copy for what the SDK does not do for you: paging a list to the end, a safe signup, subscription-state checks, webhook verification, a request limit. Their tests are in `recipe-tests/` in the sample repository |

## How the rules reach the agent

| Host | The ten rules | Rules for the operation being called | A rejection's cause and fix |
| --- | --- | --- | --- |
| Any, with or without this plugin | In `AGENTS.md` and at the top of `sdk-map.md`; in the project's own `AGENTS.md` once the block from `knowledge/AGENTS.block.md` is added there (this plugin's skill and hook make that a plan step; without the plugin the agent only offers it) | On the operation's block in the map | `knowledge/failures.md` |
| Claude Code (run live) | Also injected at session start in a project that uses the SDK, on the first prompt that names Maxio, and again after compaction | Also injected right after an edit that calls the operation | Also injected when a command's output, failing or not, shows a request to Maxio that was rejected |
| Codex (built from its documentation, not run) | The same hooks, once you review and trust them in `/hooks` | The same | The same |
| Cursor (built from its documentation, not run) | Also `rules/maxio-advanced-billing.mdc`, always applied, and the session-start hook | Also after an edit, through Cursor's `postToolUse` hook | Also through Cursor's `postToolUse` and `postToolUseFailure` hooks |

The hooks hold no knowledge of their own: they read the SDK folder, preferring the project's own installed
copy when it carries `AGENTS.md`. They need Node.js, show each piece once until the context is compacted,
skip the ten rules when the project's own always-on file already carries them, and never block a tool call.

The SDK folder they read is the copy the project's code compiles against when it carries `AGENTS.md`: for
TypeScript `node_modules/maxio-advanced-billing/`; for Python the installed `maxio_advanced_billing/` package
in the project's environment, or the folder it was installed from; for C# the package's folder in the NuGet
cache (from the project's `obj/project.assets.json`), or the folder a `<ProjectReference>` points into.
Otherwise they use the copy this plugin bundles under `sdk/`.

In Claude Code one more hook approves `Read`, `Glob` and `Grep`, and only for paths inside this plugin's
own `sdk/` folder and inside the project's installed MaxioAdvancedBilling package in the NuGet cache. Both
are outside the project, so without it those reads ask for permission, or are refused in a headless run.
Nothing else is approved.

## Install

This plugin is a proof of concept, **not published to a shared plugin marketplace**. The repository that holds
it is the marketplace: its root carries `.claude-plugin/marketplace.json` (Claude Code) and
`.agents/plugins/marketplace.json` (Codex), both listing this folder as `maxio-advanced-billing`.

**Claude Code.** Add the repository as a marketplace, then install the plugin from it:

```
/plugin marketplace add <path to the repository>
/plugin install maxio-advanced-billing@maxio-plugin-sample
```

Once the repository is pushed, one line does both:

```
/plugin install maxio-advanced-billing --marketplace <owner>/<repo>
```

For a one-off session, `claude --plugin-dir <path to this folder>` loads it without installing.

**Codex** (built from its documentation and from other providers' marketplace files, never run). Add the
repository as a marketplace and install `maxio-advanced-billing` from it. Codex runs a plugin's hooks only
after you review and trust them in `/hooks`, and its IDE extension does not run plugins. Without the plugin,
Codex still reads the project's `AGENTS.md`, so the block, once added there, carries the ten rules.

**Cursor** (built from its documentation, never run). Copy or link this folder to
`~/.cursor/plugins/local/maxio-advanced-billing` and reload Cursor. Local plugins can be switched off by an
Enterprise policy.

**The SDK.** Install the SDK package as the project would install a published one; `packaging/pack.mjs` in the
repository builds the three packages with the agent files inside. Without a package that carries them, the
plugin falls back to the SDK folders it bundles under `sdk/`.

Then ask the agent to add a Maxio feature to your project: it reads the SDK folder's `AGENTS.md` and follows
the workflow from there.
