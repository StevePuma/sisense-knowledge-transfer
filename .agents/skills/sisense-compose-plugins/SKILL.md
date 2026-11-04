---
name: sisense-compose-plugins
description: Build or review React Compose SDK analytics components and reusable visualization plugins, including Ogma integrations.
---

# Sisense Compose Plugins

Read [the reference](../../../knowledge/compose-sdk.md) when applying this workflow and [root instructions](../../../AGENTS.md) for evidence standards.

Identify whether the target is an application component, registered SDK widget plugin, or Fusion add-on. Read package versions and the installed SDK type definitions before selecting a contract. Consult the linked official DevX reference for the matching version.

For a plugin, use the supported scaffold as the contract baseline. Specify data roles, styles, selection/filter events, and persistence; isolate a pure data adapter from React and renderer lifecycle. Keep customer mappings outside the reusable package. Use synthetic fixtures for development previews.

Verify registration and type-name matching in the intended host, then data changes, selection/reset, resize, empty/error states, and teardown. Record whether actual host integration was exercised. A deployment script can replace a plugin; do not run it merely to validate a build.

For an NG-inspired implementation, read the NG case and explicitly choose whether to preserve its identity and metric behavior. Do not describe NG's component as a registered widget plugin without evidence.
