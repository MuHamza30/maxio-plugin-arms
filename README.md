# maxio-plugin-arms

Two arms of a plugin-experiments cell (task 1, Maxio subscriptions in eShopOnWeb), each on its own branch:

| Branch | Arm | What it holds |
|---|---|---|
| `control-codegen-e210fc8` | control | The Maxio Advanced Billing context plugin codegen-v2 generates at `e210fc8` (main, with the Claude Code planner agent at `plugins/maxio-advanced-billing/scoped/agents/maxio-advanced-billing-planner.md`), from `apimatic/Customer-build-files` `specs/spec-maxio.zip`, for C#, Python and TypeScript, with the SDKs bundled. Pinned at `085367a0`. |
| `treatment-sample-sdk-e210fc8` | treatment | `plugin/` of `saeedjamshaid/maxio-plugin-sample` at `cb278e4`, moved onto the control's SDK: its SDK code and build files (.NET, Python, TypeScript) are byte-identical to the control's, and Saeed's maps, docs, knowledge, recipes, router skill and hooks are kept (adapted where the newer SDK changed a fact). The commit message says how. Pinned at `46bb9a89`. |
| `treatment-sample` | replaced, not used | `plugin/` of `saeedjamshaid/maxio-plugin-sample` at `cb278e4`, byte for byte (git tree `63e7b7bf`), on its own older SDK. Replaced before any run so both arms carry one SDK. Kept as a record. |
| `control-cli-gen` | replaced, not used | The first control: the plugin the deployed APIMatic backend gave through the CLI (`apimatic plugin generate`, `dev`). It has no planner agent, so it was replaced by `control-codegen-e210fc8` before any run. Kept as a record. |

Each branch is a Claude Code marketplace (`maxio-plugin-arms`) with the plugin under `plugins/maxio-advanced-billing/`. Experiments pin a commit, never a branch.
