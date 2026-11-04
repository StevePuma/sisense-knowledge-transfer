# Sources and version boundaries

Reviewed November 4, 2026. These are authoritative entry points, not vendored manuals. Recheck version-specific signatures when implementing. The SCRM package declarations are React `^19.2.0`, Compose SDK packages `^2.16.1`, TypeScript `^4.9.5`, and Ogma download version `5.3.6`; ranges do not prove an installed version. Current Ogma documentation displayed 6.0.9 when inspected. Do not apply newer APIs to the older application without checking types.

| Area | Official reference | Use |
| --- | --- | --- |
| Integration choice | [Sisense integration methods](https://developer.sisense.com/guides/choosing-an-integration.html) | Distinguish Compose SDK, Embed SDK, and platform APIs |
| React charts and explicit queries | [Compose SDK charts](https://developer.sisense.com/guides/sdk/guides/charts/guide-compose-sdk-charts.html) | Chart-driven queries versus explicit query results |
| Semantic attributes | [Compose data model](https://developer.sisense.com/guides/sdk/guides/data-model.html) | Generated model representation |
| Plugin authoring | [Plugin DevX reference](https://developer.sisense.com/guides/sdk/guides/plugins/plugin-devx-reference.html) | Scaffold, plugin contracts, registration, build, deployment |
| Modeling | [Model building practices](https://docs.sisense.com/main/SisenseLinux/data-model-building-practices.htm) | Grain, join cardinality, modeling decisions |
| CustomJS | [Dashboard API](https://developer.sisense.com/guides/customJs/jsApiRef/dashboardClass/) | Fusion dashboard events and object API |
| Customization surfaces | [Embedded Sisense customization](https://docs.sisense.com/main/SisenseLinux/customizing-sisense-overview.htm) | Scripts and add-ons |
| Dashboard compatibility | [Compose SDK mode](https://docs.sisense.com/main/SisenseLinux/compose-SDK-mode.htm) | Evaluate dashboard compatibility |
| React and Ogma | [Official React integration](https://doc.linkurious.com/ogma/latest/tutorials/react/) | Wrapper or direct integration |

The customer-specific material comes from the inspected local SCRM tree. [NG provenance](../customers/northrop-grumman/provenance.json) identifies hashes and excerpts. No claim is made that the generic model-building advice describes the physical NG warehouse.
