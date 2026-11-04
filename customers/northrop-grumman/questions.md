# Worked NG questions

## What data is used in NG’s SCRM?

A live Sisense source named `NG_SUBTIER_DEMO`. Supplier names and part text come from `BOM_TIER_1` through `BOM_TIER_10`; BOM searches use the spine; configured part `finalRisk` uses confidence fields from `BOM_RISK_TIERS`. Read [field roles](field-roles.md) for exact paths and types. This describes configured consumption, not upstream warehouse systems or actual customer records.

## Is the graph queried from Linkurious?

The inspected NG hierarchy uses Compose SDK queries against Sisense and renders the converted rows with Ogma. There is no evidence here of a Linkurious Enterprise backend serving that hierarchy. Linkurious is the vendor; Ogma is the visualization library. See [query evidence](evidence/config-and-queries.md).

## Why do I only see a hierarchy?

The NG entry enables only `hierarchical`, although other clients use network or geo views. See [feature routing](evidence/feature-routing.md), original lines 77–79.

## Why can a parent’s Final Risk be higher than its own confidence?

The generic metric builder averages row values by name and tier, then the part hierarchy propagates descendant maxima upward. That explains the numeric behavior without validating the business semantics of confidence-as-risk. See [metrics](evidence/metrics.md) and [hierarchy builder](evidence/hierarchy-builder.md).

## Does Capacity appear as a risk metric?

It is configured and projected in the part metric query, but is not among NG’s registered risk metric IDs. The configuration alone does not make it a rendered overlay. See `/risk/metrics` in [config](config.snapshot.json) and the `metricIds` loop in [metrics](evidence/metrics.md).

## Why is a dashboard missing or apparently unfiltered?

Dashboard keys cover node tiers 1–3 only. Part level zero has no mapped dashboard. Supplier-specific analytics filter fields are not configured. For parts, compare the clicked display name with the mapped BOM text before blaming the dashboard query. See [analytics](evidence/analytics.md) and [part labels](evidence/part-labels.md).

## Are these findings reproducible from the base commit?

Not solely: the inspected tree had uncommitted changes. Selected source excerpts, the config snapshot, the extracted schema, original line numbers, and file hashes preserve the evidence used here. See [provenance](provenance.json).
