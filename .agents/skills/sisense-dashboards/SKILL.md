---
name: sisense-dashboards
description: Build and debug Sisense dashboards, Compose SDK dashboard rendering, filter propagation, contextual analytics, and drilldown.
---

# Sisense Dashboards

Read [the reference](../../../knowledge/dashboards.md) when applying this workflow and [root instructions](../../../AGENTS.md) for evidence standards.

Map the selected raw entity key, node type/tier, dashboard ID, semantic filter attribute, and fallback. Inspect how translated dashboard filters combine with target filters. Verify exact equality values rather than trusting a displayed label.

For NG, use the node tier directly: no implicit one-based conversion. Dashboard IDs exist only for tiers 1–3; supplier filters are absent. Read evidence before diagnosing an empty or unfiltered result.

Validate widget compatibility, loading/empty/error behavior, reset, theme, and access under relevant user roles. Treat UI filters as presentation/query intent, not an access boundary. Preserve customer dashboard IDs in config rather than reusable component code.
