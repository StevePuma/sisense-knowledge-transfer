---
name: sisense-data-modeling
description: Design or diagnose Sisense model grain, relationships, measures, semantic attributes, and graph query projections.
---

# Sisense Data Modeling

Read [the reference](../../../knowledge/data-modeling.md) when applying this workflow and [root instructions](../../../AGENTS.md) for evidence standards.

Define the business grain, unique key, join cardinality, and aggregation for each requested measure. Inspect model relations and before/after query counts when available. Generated TypeScript attributes establish names/types, not warehouse lineage or join correctness.

For graph consumers, separate identity/path dimensions from enrichment. Check how wide projections multiply grouped rows and whether a row limit truncates coverage. Propose a bridge or pre-aggregation only after identifying the actual fan-out.

For NG, preserve the confidence-to-finalRisk mapping as an observed implementation and distinguish numeric behavior from business semantics. Report live versus extracted status only from the model declaration/configuration. Verify server-side security separately from filters.
