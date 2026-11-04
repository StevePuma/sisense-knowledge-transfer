---
name: react-analytics
description: Implement and debug React analytics state, query normalization, effects, and imperative visualization integrations.
---

# React Analytics

Read [the reference](../../../knowledge/react-analytics.md) when applying this workflow and [root instructions](../../../AGENTS.md) for evidence standards.

Trace state from query inputs through dimension descriptors and completed rows to the graph and selected detail. Keep hook order stable and use supported enable flags for conditional queries.

Do not normalize retained rows using a new query's column order. Track query completion/generation, and clear or reconcile selected IDs when datasets or modes change. Keep domain state in React and imperative renderer handles in refs.

Separate pure adapters from effects. Clean up timers, listeners, animation frames, and renderer resources. Test null versus zero, duplicate labels, rapid query changes, resize, and remount. Use the target repository's toolchain and avoid unrelated framework migrations.
