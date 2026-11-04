# Dashboards and contextual analytics

Treat dashboard identity, query filters, visual state, and server-side access rules as separate concerns. For each navigation path, specify which entity key and tier select the dashboard, how the filter is formed, and what happens when there is no mapping.

## NG’s implemented flow

A clicked node produces a `{tier, name}` analytics target. The tier indexes `analyticsDashboard.byTier`, with an optional default fallback. `useGetDashboardModel` retrieves widgets and filters, and `dashboardModelTranslator.toDashboardProps` prepares a Compose SDK `Dashboard`. [Evidence](../customers/northrop-grumman/evidence/analytics.md).

NG has IDs for tiers 1–3, no default, and only part-specific analytics filter fields. A part target becomes an equality filter against the corresponding BOM text attribute. A supplied target filter replaces the translated filter array. Supplier targets have no configured supplier filter. Original dashboard filters can therefore survive where no target filter is available, and be replaced where one exists. Verify the desired business behavior before changing it.

Part levels start at zero; supplier levels start at one. Do not automatically add or subtract one when routing dashboards. NG’s current code uses the stored node tier directly. Display labels can be changed by shared label logic, so trace the exact selected key/name before debugging a seemingly empty dashboard.

## Building another customer dashboard flow

Write a mapping table: node type, tier, dashboard ID, semantic filter attribute, raw value, and fallback. Keep author-provided filters when required by composing a deliberate policy rather than accidentally spreading or replacing an array. Missing dashboard should yield a clear unavailable state. Empty results, denied access, and a failed dashboard load need distinct UI states.

Verify target identity, date grain, units, null display, tooltip formatting, reset behavior, theme, and narrow viewport behavior. Test multiple users where access rules differ; a hidden component or an application filter is not row-level security.

Fusion dashboard compatibility with Compose SDK is a separate check. Use the platform’s Compose SDK mode to assess support, then exercise the actual widget types and interactions in the target React application. [Official compatibility guidance](https://docs.sisense.com/main/SisenseLinux/compose-SDK-mode.htm).
