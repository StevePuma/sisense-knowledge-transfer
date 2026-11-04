# Existing SCRM Ogma guidance

Source: `docs/skills/sisense-ogma/SKILL.md`. Working-tree capture on 2026-11-04. This is implementation guidance, not a live runtime test.

```text
31: ## Ogma Guidelines
32:
33: - Ogma `getNodes()` and `getEdges()` default to visible items. Use `getNodes('raw')` and `getEdges('raw')` when checking whether the graph is already rendered, updating hidden nodes, syncing data, or focusing a node.
34: - Do not call `setGraph` as a response to a visibility-only change. Keep a stable graph signature from incoming raw nodes/edges and skip rebuilds when the raw graph is already present.
35: - For single-entity focus, hide non-target raw nodes and raw edges, open the intended popover tab, set popover data from the target node, then locate the node.
36: - Increment or cancel pending view/fit operations when a user zooms, fits, clears filters, or starts a command-tower focus. Stale map operations are a common source of jitter.
37: - Keep visible counts diagnostic. They should not decide whether the raw graph needs to be rebuilt.
38:
```
