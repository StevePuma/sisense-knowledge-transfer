# Analytics

Source: `src/features/supply-chain/components/HierarchicalViz/HierarchicalViz.tsx`. Working-tree snapshot on 2026-11-04; original line numbers retained.

## Lines 5435 to 5500

```text
5435:   const fallbackDashboardOid = analyticsDashboardDefault ?? '';
5436:   const selectedDashboardOid = analyticsTarget
5437:     ? analyticsDashboardByTier[String(analyticsTarget.tier)] ?? fallbackDashboardOid
5438:     : fallbackDashboardOid;
5439:   const dashboardEnabled = Boolean(selectedDashboardOid);
5440:   const isPlaceholderDashboard =
5441:     analyticsTarget?.tier !== undefined &&
5442:     analyticsDashboardByTier[String(analyticsTarget.tier)] === null;
5443:
5444:   useEffect(() => {
5445:     if (!watchlistSelectedIds.length) return;
5446:     const allowed = new Set(watchlistItems.map((item) => item.id));
5447:     setWatchlistSelectedIds((prev) => prev.filter((item) => allowed.has(item)));
5448:   }, [watchlistItems, watchlistSelectedIds.length]);
5449:
5450:   const { dashboard } = useGetDashboardModel({
5451:     dashboardOid: selectedDashboardOid,
5452:     includeFilters: true,
5453:     includeWidgets: true,
5454:     enabled: dashboardEnabled,
5455:   });
5456:
5457:   const analyticsFilters = useMemo(() => {
5458:     if (!analyticsTarget) return [];
5459:     const { tier, name } = analyticsTarget;
5460:     const fieldKey =
5461:       hierarchyMode === 'suppliers'
5462:         ? analyticsFilterFields?.suppliers?.[String(tier)] ??
5463:           analyticsFilterFields?.suppliers?.['1']
5464:         : analyticsFilterFields?.parts?.[String(tier)];
5465:     const attribute =
5466:       (fieldKey ? resolveAttributePath(dataModel as Record<string, any>, fieldKey) : null) ??
5467:       (fieldKey ? (dimension as Record<string, any>)[fieldKey] : null);
5468:     if (!attribute || !name) return [];
5469:     return [filterFactory.equals(attribute, name)];
5470:   }, [analyticsFilterFields, analyticsTarget, dimension, hierarchyMode]);
5471:
5472:   const analyticsDashboardProps = useMemo(() => {
5473:     if (!dashboard) return null;
5474:     const props = dashboardModelTranslator.toDashboardProps(dashboard);
5475:     const nextConfig = {
5476:       ...props.config,
5477:       filtersPanel: {
5478:         ...props.config?.filtersPanel,
5479:         collapsedInitially: true,
5480:         persistCollapsedStateToLocalStorage: false,
5481:       },
5482:     };
5483:     const nextProps = { ...props, config: nextConfig };
5484:     return analyticsFilters.length ? { ...nextProps, filters: analyticsFilters } : nextProps;
5485:   }, [dashboard, analyticsFilters]);
5486:   const resolvedDashboardProps = useMemo(() => {
5487:     if (!analyticsDashboardProps) return null;
5488:     const nextFilters = analyticsFilters.length
5489:       ? analyticsFilters
5490:       : analyticsDashboardProps.filters;
5491:     return { ...analyticsDashboardProps, filters: nextFilters };
5492:   }, [analyticsDashboardProps, analyticsFilters]);
5493:
5494:   const embeddedAnalyticsDashboardProps = useMemo(() => {
5495:     if (!resolvedDashboardProps) return null;
5496:     if (mode !== 'dark') return resolvedDashboardProps;
5497:     return {
5498:       ...resolvedDashboardProps,
5499:       widgets: mergeSisenseWidgetsForAnalyticsDark(resolvedDashboardProps.widgets),
5500:     };
```

## Lines 6665 to 6700

```text
6665:       if (!target || !target.isNode) {
6666:         clearPopover();
6667:         return;
6668:       }
6669:
6670:       const nodeId = String(target.getId());
6671:       if (clickTimeoutRef.current !== null) {
6672:         window.clearTimeout(clickTimeoutRef.current);
6673:       }
6674:       clickTimeoutRef.current = window.setTimeout(() => {
6675:         clickTimeoutRef.current = null;
6676:         if (expandOnClick) {
6677:           void expandNode(ogma, nodeId);
6678:         }
6679:         if (popoverNodeIdRef.current === nodeId) {
6680:           clearPopover();
6681:           return;
6682:         }
6683:         setAnalyticsOpen(false);
6684:         setAnalyticsHost(null);
6685:         const nextPartSupplierDrawerData = buildDellPartSupplierDrawerData(target);
6686:         if (nextPartSupplierDrawerData) {
6687:           setAnalyticsTarget(null);
6688:           setPartSupplierDrawerData(nextPartSupplierDrawerData);
6689:           setAnalyticsOpen(nextPartSupplierDrawerData.suppliers.length > 0);
6690:         } else {
6691:           setPartSupplierDrawerData(null);
6692:           const analyticsTier = Number(target.getData?.('tier'));
6693:           const analyticsName = target.getData?.('name');
6694:           if (Number.isFinite(analyticsTier) && analyticsName) {
6695:             setAnalyticsTarget({ tier: analyticsTier, name: String(analyticsName) });
6696:           } else {
6697:             setAnalyticsTarget(null);
6698:           }
6699:         }
6700:         const initialTabId = hasHierarchicalPopoverTabs
```
