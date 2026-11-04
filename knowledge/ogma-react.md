# Ogma and React graph engineering

Ogma renders graphs; React owns application state and translates analytical results into the graph contract. Linkurious is the vendor. A use of Ogma does not establish a Linkurious Enterprise server or graph database connection.

The official React guidance supports a wrapper package or a direct integration. Choose based on the target app and installed Ogma version; avoid replacing a functioning direct adapter just to adopt the latest wrapper. [React integration](https://doc.linkurious.com/ogma/latest/tutorials/react/).

## Contract and lifecycle

Keep canonical IDs, display labels, raw lookup keys, tiers, and metric values distinct. Define edge orientation once and use it consistently in traversal, arrows, and labels. NG’s generic hierarchy creates parent→child edges; a separate relationship network can use a different direction.

Own one Ogma instance per mounted canvas. Keep it in a ref and release resources on teardown. Separate raw graph updates from layout, visibility, style, and camera changes. On asynchronous layouts or queries, ignore obsolete results after selection or mount generation changes. Test React StrictMode’s remount cycle and a resize after the container was hidden.

[SCRM’s existing Ogma skill](../customers/northrop-grumman/evidence/ogma-guidance.md) warns that visible counts are not raw graph counts. In a version where `getNodes('raw')`/`getEdges('raw')` provide raw collections, use those for synchronization and hidden-node updates; use visible collections for display counts. Verify the signature against the installed version. A visibility-only change should not automatically rebuild the graph and restart layout.

## NG identity and semantics

Supplier nodes normally use tier-plus-name identities. Part child IDs include their parent path, so the same part label under different parents can remain distinct. The root supplier is synthetic. Risk maps, however, are keyed by tier/name, which can pool observations across repeated labels even when display nodes are separate. See [builder](../customers/northrop-grumman/evidence/hierarchy-builder.md) and [metrics](../customers/northrop-grumman/evidence/metrics.md).

For new work, favor stable domain IDs when supplied. Test two entities sharing a label and one entity occurring at several tiers. Decide whether repeated entities are one node with multiple memberships or distinct path occurrences; neither representation is universally correct.

## Diagnose graph defects by layer

| Symptom | First checks |
| --- | --- |
| Missing branches | Query cap, projected dimensions, null break in row traversal, current client |
| Duplicate company | Identity policy, aliasing, tier/path occurrence |
| Wrong risk color | Source field, scale, averaging, inherited maximum, missing values |
| Jitter after filtering | Unnecessary graph rebuild, repeated layout/fit, stale async camera work |
| Node focus miss | Raw versus visible collection, lookup keys, filtered query not yet complete |
| Incorrect detail | Display label versus raw key, selected mode/tier, stale query rows |

Use synthetic fixtures and verify node IDs, edge endpoints, orientation, hidden-node restoration, selection, and cleanup. Do not copy licensed Ogma binaries or signed download URLs into shared examples.
