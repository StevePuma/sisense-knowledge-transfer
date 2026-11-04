---
name: ogma-react
description: Build and debug Ogma graph visualizations in React, including identity, layout, selection, filtering, and renderer lifecycle.
---

# Ogma React

Read [the reference](../../../knowledge/ogma-react.md) when applying this workflow and [root instructions](../../../AGENTS.md) for evidence standards.

Establish the graph contract and installed Ogma version. Decide how raw entity IDs, repeated tier/path occurrences, and display labels relate. Define edge direction and null metric behavior.

Separate graph replacement from style, visibility, layout, and camera updates. Inspect raw versus visible collections when a hidden node appears missing. Prevent obsolete queries/layouts from moving or replacing the current graph. Release the renderer and subscriptions on unmount.

Test duplicate labels, repeated entities, disconnected nodes, hidden-node restoration, rapid selections, resize, and StrictMode remount. Use synthetic data and licensed installation mechanisms; never copy signed package URLs into artifacts.

Linkurious vendor documentation is not evidence of a Linkurious Enterprise backend. Trace the actual data source.
