# Sisense CustomJS and Fusion add-ons

CustomJS runs in a Fusion dashboard/widget context. React Compose SDK components run in an application context. Do not paste code that expects Fusion globals into a React component or assume a translated dashboard automatically executes its original script.

Sisense distinguishes per-dashboard/widget scripts from reusable add-ons, and its Dashboard API documents event handling. Pick the intended scope before changing behavior. [Customization overview](https://docs.sisense.com/main/SisenseLinux/customizing-sisense-overview.htm), [Dashboard API](https://developer.sisense.com/guides/customJs/jsApiRef/dashboardClass/).

## Diagnose and implement

Obtain the affected script, widget type, Sisense version, trigger, and a small synthetic result shape. Determine whether the issue is query transformation, result transformation, rendering, or navigation. Consult the version-specific widget/dashboard lifecycle before choosing a hook; do not infer an event name from another framework.

Keep behavior idempotent across refreshes. Register listeners once per intended lifecycle, remove them on teardown where supported, and avoid creating duplicate controls on every render. Scope DOM lookups to the widget container, escape untrusted text, and avoid global CSS when a local selector can express the change.

Treat undocumented internal properties as a compatibility dependency: identify why they are needed, prefer a documented hook when possible, and test the exact deployed version. Compare refresh, filter change, navigation away/back, and dashboard duplication. Check that the script does not trigger recursive refreshes or mutate shared data consumed by another widget.

## Migrate to React

Inventory what the script does: field mapping, calculated values, chart styling, tooltip content, filter state, and navigation. Move pure data transforms into tested adapters; move interactive state into React; map chart customization to supported SDK properties/events; isolate imperative third-party rendering in a lifecycle adapter. Preserve user-visible behavior with before/after fixtures.

No NG CustomJS script was established by this capture. The known NG implementation uses React, query hooks, Ogma, and translated dashboard props. Do not invent a customer script to fill that gap.
