# Config And Queries

Source: `src/features/supply-chain/components/HierarchicalViz/HierarchicalViz.tsx`. Working-tree snapshot on 2026-11-04; original line numbers retained.

## Lines 1878 to 1978

```text
1878:   dataModel,
1879:   viewMode,
1880:   onViewModeChange,
1881:   enabledViewModes,
1882: }) => {
1883:   const { mode } = useThemeMode();
1884:   const sisenseThemeSettings = useMemo(() => getSisenseAppThemeSettings(mode), [mode]);
1885:   const clientConfig = getClientConfig();
1886:   const isRivianAiV2HierarchicalClient =
1887:     clientConfig.clientId === 'rivian_ai_mappingv2' || clientConfig.clientId === 'rivian_ai_v2';
1888:   const isDellHierarchicalClient = clientConfig.clientId === 'dell';
1889:   const isEdgeTraversalHierarchicalClient =
1890:     isRivianAiV2HierarchicalClient || isDellHierarchicalClient;
1891:   const adminEnabledFromConfig = Boolean(clientConfig.admin?.enabled);
1892:   const partsEnabled = clientConfig.hierarchicalViz?.partsEnabled ?? true;
1893:   const supplierLevels = clientConfig.hierarchicalViz?.hierarchy?.suppliers?.levels ?? [];
1894:   const partsLevels = partsEnabled
1895:     ? clientConfig.hierarchicalViz?.hierarchy?.parts?.levels ?? []
1896:     : [];
1897:   const riskFieldRoles = clientConfig.hierarchicalViz?.riskFieldRoles ?? {};
1898:   const riskMetrics = clientConfig.risk?.metrics ?? [];
1899:   const riskMetricById = useMemo(
1900:     () => new Map(riskMetrics.map((metric) => [metric.id, metric])),
1901:     [riskMetrics]
1902:   );
1903:   const metricIds = riskMetrics.map((metric) => metric.id);
1904:   const supplierQueryMode =
1905:     clientConfig.hierarchicalViz?.supplierQueryMode ?? 'fullDepth';
1906:   const maxSupplierDepth = clientConfig.hierarchicalViz?.maxSupplierDepth ?? 10;
1907:   const expandOnClick = Boolean(clientConfig.hierarchicalViz?.expandOnClick);
1908:   // Wide full-depth grouping can truncate large path sets before all tier-1 suppliers appear.
1909:   // For Rivian AI mapping data, prefer prefix queries when more than two supplier levels are
1910:   // configured so distinct direct suppliers are not dropped by the grouped row cap.
1911:   const usePrefixSupplierQueries =
1912:     supplierQueryMode === 'prefix' ||
1913:     (isRivianAiV2HierarchicalClient &&
1914:       supplierQueryMode === 'fullDepth' &&
1915:       supplierLevels.length > 2);
1916:   if (!supplierLevels.length || (partsEnabled && !partsLevels.length)) {
1917:     throw new Error('Missing hierarchical levels configuration.');
1918:   }
1919:   if (!metricIds.length) {
1920:     throw new Error('Missing risk metric configuration.');
1921:   }
1922:   const dimensionKey =
1923:     clientConfig.dataModels?.hierarchical?.dimension ?? 'VALIDATION_PART_ENRICHED';
1924:   const dimension = (dataModel as Record<string, any>)[dimensionKey];
1925:   if (!dimension) {
1926:     throw new Error(`Missing hierarchical dimension "${dimensionKey}" in data model.`);
1927:   }
1928:   const fieldRoles = clientConfig.dataModels?.hierarchical?.fieldRoles ?? {};
1929:   const getField = (role: string) => {
1930:     const fieldKey = fieldRoles[role];
1931:     if (!fieldKey) {
1932:       throw new Error(`Missing hierarchical field role mapping for "${role}".`);
1933:     }
1934:     if (fieldKey.includes('.')) {
1935:       const [dimensionName, attributeName] = fieldKey.split('.');
1936:       const resolvedDimension = (dataModel as Record<string, any>)[dimensionName];
1937:       const resolvedField = (resolvedDimension as Record<string, any> | undefined)?.[
1938:         attributeName
1939:       ];
1940:       if (resolvedField) return resolvedField;
1941:     }
1942:     return (dimension as Record<string, any>)[fieldKey];
1943:   };
1944:   const requiredRoles = new Set<string>();
1945:   supplierLevels.forEach((level) => {
1946:     requiredRoles.add(level.nameRole);
1947:   });
1948:   if (partsEnabled) {
1949:     partsLevels.forEach((level) => {
1950:       requiredRoles.add(level.nameRole);
1951:       if (level.imageRole) {
1952:         requiredRoles.add(level.imageRole);
1953:       }
1954:     });
1955:   }
1956:   Object.values(riskFieldRoles.suppliers ?? {}).forEach((metricMap) => {
1957:     Object.values(metricMap ?? {}).forEach((role) => requiredRoles.add(role));
1958:   });
1959:   if (partsEnabled) {
1960:     Object.values(riskFieldRoles.parts ?? {}).forEach((metricMap) => {
1961:       Object.values(metricMap ?? {}).forEach((role) => requiredRoles.add(role));
1962:     });
1963:   }
1964:   requiredRoles.forEach((role) => {
1965:     if (!fieldRoles[role]) {
1966:       throw new Error(`Missing hierarchical field role mapping for "${role}".`);
1967:     }
1968:   });
1969:   const riskThresholdControl = clientConfig.risk?.thresholdControl;
1970:   const analyticsDashboardConfig = clientConfig.hierarchicalViz?.analyticsDashboard;
1971:   const analyticsDashboardDefault = analyticsDashboardConfig?.default ?? null;
1972:   const analyticsDashboardByTier = analyticsDashboardConfig?.byTier ?? {};
1973:   const analyticsFilterFields = analyticsDashboardConfig?.analyticsFilterFields;
1974:   const rootSupplierName = clientConfig.hierarchicalViz?.rootSupplier ?? '';
1975:   const partsRootLabel = clientConfig.hierarchicalViz?.partsRootLabel ?? '';
1976:   const hierarchicalPopoverConfig = clientConfig.popovers?.hierarchical ?? null;
1977:   const hierarchicalPopoverTabs = useMemo(
1978:     () => hierarchicalPopoverConfig?.tabs ?? [],
```

## Lines 2116 to 2140

```text
2116:   const requiresPartSelectionBeforeLoad =
2117:     clientConfig.hierarchicalViz?.partsSelectionRequired ?? isRivianAiV2HierarchicalClient;
2118:   const isDellPartsHierarchyClient = isDellHierarchicalClient && hierarchyMode === 'parts';
2119:   const dellPartsOnlyMode = isDellHierarchicalClient;
2120:   const hasAppliedPartSelection =
2121:     appliedBomIdFilter.trim().length > 0 || appliedBomTextFilter.trim().length > 0;
2122:   // Keep parts queries warm in background unless this client requires selecting a part first.
2123:   const partsQueryEnabled =
2124:     partsEnabled &&
2125:     !isDellPartsHierarchyClient &&
2126:     (!requiresPartSelectionBeforeLoad || hasAppliedPartSelection);
2127:   const supplierNameFields = supplierLevels.map((level) => getField(level.nameRole));
2128:   const partsNameFields = partsEnabled
2129:     ? partsLevels.map((level) => getField(level.nameRole))
2130:     : [];
2131:   const isTraversalSupplierHierarchyClient =
2132:     hierarchyMode === 'suppliers' && isEdgeTraversalHierarchicalClient;
2133:   const getOptionalField = (role?: string) => {
2134:     if (!role || !fieldRoles[role]) return null;
2135:     return getField(role);
2136:   };
2137:   const dellEdgesDimension = isDellHierarchicalClient
2138:     ? ((dataModel as Record<string, any>).GRAPH_MODEL_DELL_EDGES as Record<string, any> | undefined)
2139:     : undefined;
2140:   const dellMapDimension = isDellHierarchicalClient
```

## Lines 2269 to 2408

```text
2269:   const { data: supplierData, isLoading: supplierLoading } = useExecuteQuery({
2270:     dataSource: dataModel.DataSource,
2271:     dimensions: supplierNameFields,
2272:     count: 100000,
2273:     enabled: hierarchyMode === 'suppliers' && !usePrefixSupplierQueries,
2274:   });
2275:   const { data: supplierTraversalData } = useExecuteQuery({
2276:     dataSource: dataModel.DataSource,
2277:     dimensions: supplierTraversalDimensions,
2278:     count: 100000,
2279:     enabled: isTraversalSupplierHierarchyClient && supplierTraversalDimensions.length >= 5,
2280:   });
2281:
2282:   const MAX_SUPPLIER_DEPTH = maxSupplierDepth;
2283:   const getSupplierDepthDimensions = (depth: number) =>
2284:     supplierNameFields.slice(0, Math.min(depth, supplierNameFields.length));
2285:
2286:   const supplierDepth1 = getSupplierDepthDimensions(1);
2287:   const supplierDepth2 = getSupplierDepthDimensions(2);
2288:   const supplierDepth3 = getSupplierDepthDimensions(3);
2289:   const supplierDepth4 = getSupplierDepthDimensions(4);
2290:   const supplierDepth5 = getSupplierDepthDimensions(5);
2291:   const supplierDepth6 = getSupplierDepthDimensions(6);
2292:   const supplierDepth7 = getSupplierDepthDimensions(7);
2293:   const supplierDepth8 = getSupplierDepthDimensions(8);
2294:   const supplierDepth9 = getSupplierDepthDimensions(9);
2295:   const supplierDepth10 = getSupplierDepthDimensions(10);
2296:
2297:   const supplierQuery1 = useExecuteQuery({
2298:     dataSource: dataModel.DataSource,
2299:     dimensions: supplierDepth1,
2300:     count: 100000,
2301:     enabled:
2302:       hierarchyMode === 'suppliers' &&
2303:       usePrefixSupplierQueries &&
2304:       supplierNameFields.length >= 1,
2305:   });
2306:   const supplierQuery2 = useExecuteQuery({
2307:     dataSource: dataModel.DataSource,
2308:     dimensions: supplierDepth2,
2309:     count: 100000,
2310:     enabled:
2311:       hierarchyMode === 'suppliers' &&
2312:       usePrefixSupplierQueries &&
2313:       supplierNameFields.length >= 2,
2314:   });
2315:   const supplierQuery3 = useExecuteQuery({
2316:     dataSource: dataModel.DataSource,
2317:     dimensions: supplierDepth3,
2318:     count: 100000,
2319:     enabled:
2320:       hierarchyMode === 'suppliers' &&
2321:       usePrefixSupplierQueries &&
2322:       supplierNameFields.length >= 3,
2323:   });
2324:   const supplierQuery4 = useExecuteQuery({
2325:     dataSource: dataModel.DataSource,
2326:     dimensions: supplierDepth4,
2327:     count: 100000,
2328:     enabled:
2329:       hierarchyMode === 'suppliers' &&
2330:       usePrefixSupplierQueries &&
2331:       supplierNameFields.length >= 4,
2332:   });
2333:   const supplierQuery5 = useExecuteQuery({
2334:     dataSource: dataModel.DataSource,
2335:     dimensions: supplierDepth5,
2336:     count: 100000,
2337:     enabled:
2338:       hierarchyMode === 'suppliers' &&
2339:       usePrefixSupplierQueries &&
2340:       supplierNameFields.length >= 5,
2341:   });
2342:   const supplierQuery6 = useExecuteQuery({
2343:     dataSource: dataModel.DataSource,
2344:     dimensions: supplierDepth6,
2345:     count: 100000,
2346:     enabled:
2347:       hierarchyMode === 'suppliers' &&
2348:       usePrefixSupplierQueries &&
2349:       supplierNameFields.length >= 6,
2350:   });
2351:   const supplierQuery7 = useExecuteQuery({
2352:     dataSource: dataModel.DataSource,
2353:     dimensions: supplierDepth7,
2354:     count: 100000,
2355:     enabled:
2356:       hierarchyMode === 'suppliers' &&
2357:       usePrefixSupplierQueries &&
2358:       supplierNameFields.length >= 7,
2359:   });
2360:   const supplierQuery8 = useExecuteQuery({
2361:     dataSource: dataModel.DataSource,
2362:     dimensions: supplierDepth8,
2363:     count: 100000,
2364:     enabled:
2365:       hierarchyMode === 'suppliers' &&
2366:       usePrefixSupplierQueries &&
2367:       supplierNameFields.length >= 8,
2368:   });
2369:   const supplierQuery9 = useExecuteQuery({
2370:     dataSource: dataModel.DataSource,
2371:     dimensions: supplierDepth9,
2372:     count: 100000,
2373:     enabled:
2374:       hierarchyMode === 'suppliers' &&
2375:       usePrefixSupplierQueries &&
2376:       supplierNameFields.length >= 9,
2377:   });
2378:   const supplierQuery10 = useExecuteQuery({
2379:     dataSource: dataModel.DataSource,
2380:     dimensions: supplierDepth10,
2381:     count: 100000,
2382:     enabled:
2383:       hierarchyMode === 'suppliers' &&
2384:       usePrefixSupplierQueries &&
2385:       supplierNameFields.length >= 10,
2386:   });
2387:
2388:   const supplierHierarchyResults = useMemo(
2389:     () =>
2390:       [
2391:         supplierQuery1,
2392:         supplierQuery2,
2393:         supplierQuery3,
2394:         supplierQuery4,
2395:         supplierQuery5,
2396:         supplierQuery6,
2397:         supplierQuery7,
2398:         supplierQuery8,
2399:         supplierQuery9,
2400:         supplierQuery10,
2401:       ].slice(0, Math.min(MAX_SUPPLIER_DEPTH, supplierNameFields.length)),
2402:     [
2403:       supplierQuery1,
2404:       supplierQuery2,
2405:       supplierQuery3,
2406:       supplierQuery4,
2407:       supplierQuery5,
2408:       supplierQuery6,
```

## Lines 2416 to 2468

```text
2416:
2417:   const supplierRiskRolesByTier = riskFieldRoles.suppliers ?? {};
2418:   const supplierRiskRoleSet = new Set<string>();
2419:   Object.values(supplierRiskRolesByTier).forEach((metricMap) => {
2420:     Object.values(metricMap ?? {}).forEach((role) => supplierRiskRoleSet.add(role));
2421:   });
2422:   const supplierRiskRoles = Array.from(supplierRiskRoleSet.values());
2423:   const supplierRiskFields = supplierRiskRoles.map((role) => getField(role));
2424:   const supplierRiskFieldIndexByRole = new Map<string, number>();
2425:   supplierRiskRoles.forEach((role, index) => supplierRiskFieldIndexByRole.set(role, index));
2426:   const supplierNameIndexByTier = new Map<number, number>();
2427:   supplierLevels.forEach((level, index) => supplierNameIndexByTier.set(level.tier, index));
2428:   const supplierLinkRoleByTier = useMemo<Record<number, string>>(() => {
2429:     const links: Record<number, string> = {};
2430:     const tier1Role = fieldRoles.tier1ExigerLinkName;
2431:     const tier2Role = fieldRoles.tier2ExigerLinkName;
2432:     if (tier1Role) links[1] = 'tier1ExigerLinkName';
2433:     if (tier2Role) links[2] = 'tier2ExigerLinkName';
2434:     return links;
2435:   }, [fieldRoles]);
2436:   const supplierLinkRoles = useMemo(
2437:     () => Array.from(new Set(Object.values(supplierLinkRoleByTier))),
2438:     [supplierLinkRoleByTier]
2439:   );
2440:   const supplierLinkFields = useMemo(
2441:     () => supplierLinkRoles.map((role) => getField(role)),
2442:     [getField, supplierLinkRoles]
2443:   );
2444:   const supplierLinkFieldIndexByRole = useMemo(() => {
2445:     const map = new Map<string, number>();
2446:     supplierLinkRoles.forEach((role, index) => map.set(role, index));
2447:     return map;
2448:   }, [supplierLinkRoles]);
2449:
2450:   const { data: supplierRiskData, isLoading: supplierRiskLoading } = useExecuteQuery({
2451:     dataSource: dataModel.DataSource,
2452:     dimensions: [...supplierNameFields, ...supplierRiskFields],
2453:     count: 100000,
2454:     enabled: hierarchyMode === 'suppliers' && supplierRiskFields.length > 0,
2455:   });
2456:   const { data: supplierLinkData } = useExecuteQuery({
2457:     dataSource: dataModel.DataSource,
2458:     dimensions: [...supplierNameFields, ...supplierLinkFields],
2459:     count: 100000,
2460:     enabled: hierarchyMode === 'suppliers' && supplierLinkFields.length > 0,
2461:   });
2462:
2463:   const partsUnifiedQuery = useExecuteQuery({
2464:     dataSource: dataModel.DataSource,
2465:     dimensions: partsNameFields,
2466:     count: 100000,
2467:     enabled: partsQueryEnabled && partsNameFields.length > 0 && partsNameFields.every(Boolean),
2468:   });
```

## Lines 3486 to 3584

```text
3486:   const partsHierarchyResults = useMemo(
3487:     () => [partsUnifiedQuery],
3488:     [partsUnifiedQuery]
3489:   );
3490:
3491:   const { data: partsPlatformImageData, isLoading: partsPlatformImageLoading } =
3492:     useExecuteQuery({
3493:       dataSource: dataModel.DataSource,
3494:       dimensions:
3495:         partsImageNameField && partsImageField
3496:           ? [partsImageNameField, partsImageField]
3497:           : [partsNameFields[0]],
3498:       count: 100000,
3499:       enabled: Boolean(partsImageNameField && partsImageField),
3500:     });
3501:
3502:   const partsRiskRolesByTier = partsEnabled ? riskFieldRoles.parts ?? {} : {};
3503:   const partsRiskRoleSet = new Set<string>();
3504:   Object.values(partsRiskRolesByTier).forEach((metricMap) => {
3505:     Object.values(metricMap ?? {}).forEach((role) => partsRiskRoleSet.add(role));
3506:   });
3507:   const partsRiskRoles = Array.from(partsRiskRoleSet.values());
3508:   const partsRiskFields = partsEnabled ? partsRiskRoles.map((role) => getField(role)) : [];
3509:   const partsRiskFieldIndexByRole = new Map<string, number>();
3510:   partsRiskRoles.forEach((role, index) => partsRiskFieldIndexByRole.set(role, index));
3511:   const partsNameIndexByTier = new Map<number, number>();
3512:   if (partsEnabled) {
3513:     partsLevels.forEach((level, index) => partsNameIndexByTier.set(level.tier, index));
3514:   }
3515:
3516:   const { data: partsRiskData, isLoading: partsRiskLoading } = useExecuteQuery({
3517:     dataSource: dataModel.DataSource,
3518:     dimensions: [...partsNameFields, ...partsRiskFields],
3519:     count: 100000,
3520:     enabled: partsQueryEnabled && partsRiskFields.length > 0,
3521:   });
3522:   const { data: partsLabelLookupData } = useExecuteQuery({
3523:     dataSource: dataModel.DataSource,
3524:     dimensions: [...partsNameFields, ...partsLabelLookupFields],
3525:     count: 100000,
3526:     enabled: partsQueryEnabled && partsLabelLookupFields.length > 0,
3527:   });
3528:
3529:   const partsSupplierDimensions = useMemo(
3530:     () =>
3531:       partsEnabled && partsNameFields.length > 0 && supplierNameFields.length > 0
3532:         ? [...partsNameFields, ...supplierNameFields]
3533:         : [],
3534:     [partsEnabled, partsNameFields, supplierNameFields]
3535:   );
3536:
3537:   const { data: partsSupplierData } = useExecuteQuery({
3538:     dataSource: dataModel.DataSource,
3539:     dimensions: partsSupplierDimensions,
3540:     count: 100000,
3541:     enabled: partsQueryEnabled && partsSupplierDimensions.length > partsNameFields.length,
3542:   });
3543:
3544:   const partSuppliersByTier = useMemo<Record<number, Map<string, string[]>>>(() => {
3545:     if (!partsEnabled || partsLevels.length === 0) return {};
3546:     const supplierSetsByTier: Record<number, Map<string, Set<string>>> = {};
3547:     partsLevels.forEach((level) => {
3548:       supplierSetsByTier[level.tier] = new Map<string, Set<string>>();
3549:     });
3550:     const pairedDepth = Math.min(partsLevels.length, supplierLevels.length);
3551:     const partOffset = partsNameFields.length;
3552:     (partsSupplierData?.rows ?? []).forEach((row: any[]) => {
3553:       for (let index = 0; index < pairedDepth; index += 1) {
3554:         const partName = normalizeCellValue(row?.[index]?.data).trim();
3555:         const supplierName = normalizeCellValue(row?.[partOffset + index]?.data).trim();
3556:         if (!partName || !supplierName) continue;
3557:         const tier = partsLevels[index]?.tier;
3558:         if (tier === undefined) continue;
3559:         const tierMap = supplierSetsByTier[tier];
3560:         if (!tierMap.has(partName)) {
3561:           tierMap.set(partName, new Set<string>());
3562:         }
3563:         tierMap.get(partName)?.add(supplierName);
3564:       }
3565:     });
3566:
3567:     const normalized: Record<number, Map<string, string[]>> = {};
3568:     Object.entries(supplierSetsByTier).forEach(([tierKey, supplierSets]) => {
3569:       const tier = Number(tierKey);
3570:       const tierMap = new Map<string, string[]>();
3571:       supplierSets.forEach((supplierSet, partName) => {
3572:         tierMap.set(partName, Array.from(supplierSet.values()).sort());
3573:       });
3574:       normalized[tier] = tierMap;
3575:     });
3576:     return normalized;
3577:   }, [
3578:     partsEnabled,
3579:     partsLevels,
3580:     partsNameFields.length,
3581:     partsSupplierData?.rows,
3582:     supplierLevels.length,
3583:   ]);
3584:   const partsDisplayNamesByTier = useMemo<Record<number, Map<string, string>>>(
```
