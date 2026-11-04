---
name: sisense-custom-js
description: Create, debug, or migrate Sisense Fusion dashboard and widget JavaScript scripts or add-ons.
---

# Sisense Custom Js

Read [the reference](../../../knowledge/custom-js.md) when applying this workflow and [root instructions](../../../AGENTS.md) for evidence standards.

Determine Fusion version, widget type, script scope, trigger, and expected result. Read the matching documented lifecycle API before selecting a hook. Keep repeated refreshes idempotent and local DOM changes scoped to the widget.

For migration, inventory transformations, styling, interactions, and navigation; implement each in the appropriate React/SDK layer instead of copying Fusion globals. Validate refresh, filter change, navigation away/back, and duplicate listener/DOM behavior.

Do not claim a customer uses CustomJS without a captured script. NG's known integration is React/Compose SDK/Ogma. When an API is internal, name the compatibility dependency and test the exact target version.
