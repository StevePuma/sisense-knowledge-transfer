---
name: ng-scrm
description: Explain and investigate Northrop Grumman SCRM data, field mappings, hierarchy, metrics, and contextual dashboards from captured source evidence.
---

# Ng Scrm

Read [the reference](../../../customers/northrop-grumman/README.md) when applying this workflow and [root instructions](../../../AGENTS.md) for evidence standards.

Read the case study, config snapshot, role dictionary, and provenance. Use the specific evidence file for the question; do not load all 952 attributes unless needed.

Trace the requested role to its attribute, query projection, normalization, and UI consumer. Preserve the zero-based part levels versus one-based suppliers. Recognize that prefix queries project successively deeper tier columns. Check whether a metric is registered as well as mapped: capacity is mapped/projected but not a registered risk metric.

For confidence/risk questions, describe numeric averaging and descendant maximum propagation without endorsing the business interpretation. For dashboards, inspect direct tier lookup, absent default, absent supplier filters, and label/key differences. Never substitute another client's geo/network logic.

Cite config JSON pointers or original line numbers in the evidence. For live row counts, warehouse lineage, or deployment claims, identify the missing artifact instead of guessing.
