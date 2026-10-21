# Control arm: the CLI-generated Maxio plugin

`plugins/maxio-advanced-billing/` is exactly what this command wrote, unedited:

```
apimatic plugin generate --input <input> --destination <plugin>
```

- **CLI:** `apimatic/apimatic-cli` `dev` at `1bd40e52` (`@apimatic/cli` 1.5.0), built locally, run 2026-10-21 05:21 UTC, logged in as the operator. The backend generated the plugin; the CLI reported "Context plugin is preview only" (a local plugin with bundled SDKs, not a published one).
- **Spec:** `apimatic/Customer-build-files` `specs/spec-maxio.zip`, sha256 `7d521d263a968b56c35c01ea877cd34578bc512490bbd5a57011ace06b7d7df0`, unzipped into `<input>/src/spec/` (APIMATIC-META.json, openapi.yaml, components/).
- **`<input>/src/apimatic.json`:**

```json
{
  "plugin": {
    "pluginId": "maxio-advanced-billing",
    "pluginName": "Maxio Advanced Billing",
    "pluginVersion": "0.1.0"
  },
  "languages": {
    "csharp": {},
    "python": {},
    "typescript": {}
  }
}
```

The plugin carries 30 skills (dotnet 9, python 11, typescript 10) and the three SDKs under `sdk/`. Its .NET SDK code differs from the treatment's only in XML doc comments (no code line differs).
