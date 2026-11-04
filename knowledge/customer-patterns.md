# Customer implementation patterns

This catalog separates a grounded customer example from patterns that can be reused. NG is the detailed case study in this first capture. Other customer names in the SCRM registry indicate configuration entries, not completed case studies or proof of production deployments.

| Pattern | Observed NG evidence | Reusable lesson |
| --- | --- | --- |
| Client-configured semantic model | File path and field roles select the generated model | Keep customer mappings outside renderer logic |
| Multiple query projections | Supplier prefixes; parts, metrics, labels, associations | Match query shape to its consumer and track row order |
| Imperative graph inside React | Hierarchy builder plus Ogma canvas | Keep a stable domain contract across the boundary |
| Contextual analytics | Node tier selects dashboard; part name supplies filter | Preserve raw identity and define absent-mapping behavior |
| Shared metric engine | Confidence mapped to `finalRisk`, averaged and propagated | Document field semantics separately from UI labels |
| Shared component defaults | NG omits some mappings that other customers use | Missing overrides can inherit behavior; trace defaults |

For source details, start at [NG](../customers/northrop-grumman/README.md). To add another customer, capture their configuration and actual consumer branches using the [template](../templates/customer-capture.md). Do not apply NG’s ten-tier BOM structure to a relationship-edge model without inspecting it.
