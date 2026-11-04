# React analytics implementation patterns

The captured SCRM application uses React StrictMode, a Sisense provider, and a theme provider. React is the boundary between analytical query results and the imperative Ogma renderer. See [provider evidence](../customers/northrop-grumman/evidence/react-provider.md).

Keep query construction, row normalization, graph-domain logic, and rendering in separate modules when changing or extracting the existing implementation. Positional rows must be interpreted with the dimensions that produced them. Use named descriptors or an index map next to the query definition; do not scatter numeric offsets through unrelated components.

Model loading, empty, error, and ready states explicitly. When dimensions or filters change, retained old rows may still exist while a new query is in progress. Associate completed data with a query key or generation before committing a graph. Never show an old result as the new selection just because the rows array is nonempty.

Keep hook order stable. Conditional behavior belongs in supported `enabled` flags or in separate mounted components, not conditional hook calls. Memoize costly normalization using the inputs that actually change. Avoid making render effects depend on freshly created objects or functions unless reexecution is intended.

Keep the selected domain key in React state and Ogma instance handles in refs. Do not use rendered labels as database identifiers. Clear or reconcile dependent state when the client, hierarchy mode, or dataset changes. Cancel subscriptions, timers, animation frames, and renderer resources on teardown.

For tests, prioritize changes that cross boundaries: dimension order, null/zero handling, duplicate IDs, quick selection switches, background query completion, theme changes, and StrictMode remount. Component snapshots alone cannot validate analytical correctness. Use the existing application’s test/build toolchain; do not silently replace it while extracting knowledge.
