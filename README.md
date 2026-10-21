# Treatment arm: the Maxio plugin proof of concept, on the control's SDK

`plugins/maxio-advanced-billing/` is `plugin/` of `saeedjamshaid/maxio-plugin-sample` at commit `cb278e4`
("feat: add the maxio plugin proof of concept", 2026-10-20), moved onto the newer SDK that the control
(branch `control-codegen-e210fc8`, codegen-v2 `e210fc8`) ships, so both arms carry one SDK. Saeed's repo is
not changed.

- **SDK code and build files** (.NET, Python, TypeScript): byte-identical to the control's. Saeed never edited
  them; they matched his generator baseline (`plugin-generated/`) exactly. `sdk/typescript/package.json` keeps
  his additions to its `files` list.
- **Generated files he did not edit** (`api-reference.md`, 6 TypeScript map pages): the newer generator's.
- **Maps and READMEs he edited:** kept where the newer generator left them alone, three-way merged where it
  changed them too.
- **His own layer** (router skill, hooks, `knowledge/`, `recipes/`, `AGENTS.md`, `docs/`): kept, with 27
  statements corrected that are false for the newer SDK. Nothing outside `sdk/` differs from `cb278e4:plugin`.
- **Checked:** his recipe tests pass on this SDK (.NET, TypeScript, Python).

The previous treatment, `plugin/` at `cb278e4` byte for byte on its own older SDK, is branch `treatment-sample`.

Only the plugin folder is here. The sample repository's design notes, reviews, curation notes, earlier versions
and experiment rubrics are deliberately left out, so a run sees what a user installing the plugin gets.
The hooks need Node.js on the PATH; they fire on Claude Code 2.1.295 (probed 2026-10-21).
