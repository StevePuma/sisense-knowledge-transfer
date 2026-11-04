# Compose SDK and React plugin development

The reusable customer pattern is a React application that queries Sisense, transforms the rows, and renders Ogma. SCRM’s NG implementation is a component integration; the inspected path does not prove it is packaged as a registered Compose SDK widget plugin. See [NG architecture](../customers/northrop-grumman/README.md).

## Choose the artifact before coding

| Artifact | Suitable request | Boundary |
| --- | --- | --- |
| React feature/component | A custom analytics page or graph | Application owns query state and layout |
| Compose SDK widget plugin | A reusable visualization hosted by the SDK dashboard system | SDK plugin contract owns host integration |
| Fusion CustomJS/add-on | Modify an existing Fusion dashboard/widget | Fusion lifecycle and deployment apply |

Compose SDK charts can execute queries from semantic attributes, or consume explicitly queried datasets. Use the explicit path when multiple visual components need the same normalized result. [Official chart guide](https://developer.sisense.com/guides/sdk/guides/charts/guide-compose-sdk-charts.html).

## Build a plugin

First inspect the consuming app’s installed `@sisense/sdk-ui`, `sdk-data`, React, and TypeScript versions. Preserve its lockfile and compile against its actual types. Do not silently migrate SCRM while creating a reusable plugin.

The current DevX toolkit scaffolds plugins with `create-plugin`; its generated `WidgetPlugin`, visualization, data/design panels, and preview provide the authoritative starting contract. Register the plugin through the provider and match the widget’s custom type to the plugin’s declared name. Deployment can delete an existing plugin before uploading its replacement. Use the exact pinned CLI’s help and generated scripts; deployment requires an explicit target and authorization. [DevX reference](https://developer.sisense.com/guides/sdk/guides/plugins/plugin-devx-reference.html).

For an Ogma hierarchy plugin, define these decisions before wiring the host:

- Data roles: stable node ID, parent ID or path, display label, tier, and nullable metrics. NG’s name-based paths are a case-study constraint, not a requirement for new schemas.
- Metric contract: scale, direction, aggregation, missing values, and whether ancestors inherit descendant values.
- Interaction contract: selection versus filtering, reset behavior, and host events. Keep raw keys alongside display labels so a cross-filter never relies accidentally on presentation text.
- Styling contract: graph direction, legend, risk thresholds, theme, empty state, and dense-graph behavior.
- Persistence contract: which selections/settings survive a query or host remount, and how outdated state is discarded.

Keep the pure row-to-graph adapter separate from the host component. A plugin should accept its declared data contract rather than directly importing a customer model. Keep customer field roles and dashboard IDs in customer configuration.

## React integration and verification

SCRM places the provider above the app with SSO and query caching. Its hierarchy has distinct queries for topology, metrics, labels, and supplier associations. See [provider](../customers/northrop-grumman/evidence/react-provider.md) and [queries](../customers/northrop-grumman/evidence/config-and-queries.md).

For a new implementation, test a synthetic graph with duplicate labels, distinct IDs, a missing parent, null metrics, a zero-valued metric, and a deep branch. Check rapid query changes, mount/unmount/remount, container resize, host selection/reset, and a dataset at the configured row cap. Assert the adapter’s IDs and edge endpoints; use browser interaction checks for rendering and host behavior. A successful TypeScript build alone does not verify host interoperability.

Before calling a plugin complete, compile against the intended host, run the synthetic preview, and verify registration plus a filter event in that host. Record unavailable checks honestly. Never include an Ogma license download URL or a production authentication token in a package or browser example.
