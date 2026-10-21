---
name: maxio-advanced-billing
description: MANDATORY FIRST STEP for Maxio Advanced Billing (Chargify) work with the APIMatic-generated SDK in C#/.NET, Python or TypeScript. Load this BEFORE opening an SDK file or touching a project file. Applies when asked to integrate, change or debug Maxio code (subscriptions, signups, customers, payment profiles, plan changes, components and usage, coupons, invoices, webhooks, entitlements), or when a Maxio call errors or behaves unexpectedly. It names the one folder that holds this SDK's contract map, Maxio's business rules (what no signature can tell you, such as the optional field that decides whether a signup is accepted) and the plan-first workflow, and the order to read them in. Three rules hold whatever the task: (1) the workflow doc is read and followed before any project file is edited, (2) every SDK name and signature comes from the map and every Maxio rule from the knowledge files, never from memory, (3) a rejection is looked up before code is changed.
---

# Maxio Advanced Billing SDK

This skill is a router. Everything of substance ships in the SDK folder for your language: its
`AGENTS.md` carries the same three rules as below, the ten rules agents most often get wrong, and the
workflow. This page tells you which folder that is, how to read it, and how to keep the ten rules in the
project.

## 1. Find the SDK folder

Use the copy the project's code compiles against, because it matches the SDK version in use:

| Language | The SDK folder |
|---|---|
| TypeScript or JavaScript | `node_modules/maxio-advanced-billing/` once the package is installed |
| Python | the installed package, `maxio_advanced_billing/` in the project's environment's `site-packages`: `python -c "import maxio_advanced_billing, os; print(os.path.dirname(maxio_advanced_billing.__file__))"` prints it. If the SDK was installed from a folder with `pip install <folder>`, that folder instead: `pip freeze` prints it as `maxio-advanced-billing @ file:///<folder>` |
| C#/.NET | the package's folder in the NuGet cache. The project's `obj/project.assets.json` names it: one of the `packageFolders`, joined with the `path` of the `MaxioAdvancedBilling/<version>` entry under `libraries`. `dotnet build` also prints it, on a line that starts "Maxio Advanced Billing SDK:". If the project has a `<ProjectReference>` to `MaxioAdvancedBilling.csproj` instead, the nearest folder above that `.csproj` that holds `AGENTS.md` |

That folder's root holds `AGENTS.md`. For C#, the package also carries the SDK's source under
`src/`: start at the root, not there.

If that copy does not exist yet, or does not hold `AGENTS.md`, use the copy this plugin bundles:
`${CLAUDE_PLUGIN_ROOT}/sdk/<language>/`, where `<language>` is `dotnet`, `python` or `typescript`.
That is the `sdk/` folder two levels above this skill's own folder. It is outside the project.

A project with a `.csproj` or `.fsproj` is C#/.NET, one with `pyproject.toml` or `requirements*.txt` is
Python, and one with `package.json` is TypeScript. If it matches more than one, or none, ask which language
the Maxio code is to be written in.

## 2. Read in this order

1. The SDK folder's `AGENTS.md`. It holds the ten rules (read them once; `sdk-map.md` repeats them) and
   says where everything else is.
2. `docs/integrate.md`, the workflow, and follow it.
3. Then only what your task touches:
   - for each operation in scope, the "Provider rules" (or "Provider notes") line on its block in the map
     and the section of the notes it links under `knowledge/operations/`, not the whole notes file;
   - the sections of `knowledge/rules.md`, `knowledge/decisions.md` and `knowledge/lifecycles.md` that
     those lines cite, or that the flow you are building needs;
   - the one recipe under `recipes/` you copy, if any.

Do not read whole files you only need one section of.

## 3. Three rules that hold whatever the task

1. **Workflow first.** Read `docs/integrate.md` and follow it before you create or edit any project file.
   For implementation work that means a plan file before code.
2. **Look it up.** Every SDK name, signature, model and error comes from the map. Every Maxio business
   rule comes from `knowledge/`. Never from memory: this SDK's names are not in your training data, and
   agents get Maxio's rules wrong far more often than they get signatures wrong.
3. **A rejection is information.** When Maxio rejects a call, find its status and message in
   `knowledge/failures.md` before you change code. A 4xx is never evidence that a call works.

## 4. Keep the rules in the project

The user installed this plugin to keep Maxio's rules in front of every coding agent, so this step is part
of the work. It is the request that the SDK folder's `AGENTS.md`, section "The project block", says to
follow: that section and this one agree. If the project's `AGENTS.md` has no block marked
`maxio-advanced-billing:rules:start`, make adding it a step of your plan, so the user can approve or
decline it with the plan:

- Add the block from the SDK folder's `knowledge/AGENTS.block.md` to the project's `AGENTS.md`, exactly as
  it is: it has nothing to fill in. Create `AGENTS.md` if the project has none.
- If the project also has a `CLAUDE.md`, the block must reach it once. When `CLAUDE.md` already imports
  `AGENTS.md` (a line `@AGENTS.md`), do nothing more; otherwise add the same block to `CLAUDE.md` too.

Say in your report whether you added it. If you write no plan, do not add it: offer it in your report.
It keeps the ten rules in context for every later session and every coding tool, with or without this
plugin.
