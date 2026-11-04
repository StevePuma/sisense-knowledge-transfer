# Sisense data modeling

Start with the business question and define the row grain before selecting fields. A supplier, part, supplier-part association, risk observation, and hierarchy path are different grains. Document the key and expected cardinality for each, then test whether joining them changes counts or weights an average.

Sisense’s modeling guidance covers flat and fact/dimension approaches and the risk of unintended many-to-many joins. Establish the required cardinality with actual key counts before choosing a bridge, deduplication, or pre-aggregation strategy. [Model building practices](https://docs.sisense.com/main/SisenseLinux/data-model-building-practices.htm).

## Work from semantic model to consumption

A generated Compose SDK model identifies dimensions, attributes, expressions, and data-source references. It is not a complete physical schema or warehouse lineage export. [Data model guide](https://developer.sisense.com/guides/sdk/guides/data-model.html).

For a customer model review, collect:

| Question | Evidence needed |
| --- | --- |
| What is one row? | Grain statement plus key uniqueness checks |
| Which paths connect tables? | Model relations/export and key cardinalities |
| Why does a metric change after adding a dimension? | Query before/after, row count, grouping, and join fan-out |
| Is the measure additive? | Business definition and intended aggregation |
| What does null mean? | Source definition and transformation rules |
| Is the model live or extracted? | Actual data-source configuration |
| Who can see a row? | Server-side security configuration and role-specific query results |
| How fresh is it? | Source timestamps and pipeline/build evidence |

## NG example

NG exposes 952 attributes but configures 60 field roles. Ten BOM tier tables supply names and parts; the spine provides search keys; the risk dimension provides confidence. These fields resolve in the generated model, but the physical joins are unverified. Read [field roles](../customers/northrop-grumman/field-roles.md) and [schema](../customers/northrop-grumman/schema.json).

The generic metric transformation averages numeric values per tier/name before graph-level maximum propagation. Repeated association rows can affect the average. A corrective model design must specify whether confidence belongs to a part, supplier-part pair, observation, or path; source code cannot decide the intended grain. Inspect [metric evidence](../customers/northrop-grumman/evidence/metrics.md).

A 100,000-row request is a limit, not completeness evidence. Compare returned size to the limit, reduce projection width, and validate coverage using an independent count/query at the intended grain. Avoid adding all available dimensions to a graph query simply because the generated schema exposes them.
