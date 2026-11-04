# Hierarchy Builder

Source: `src/features/supply-chain/components/HierarchicalViz/HierarchicalViz.tsx`. Working-tree snapshot on 2026-11-04; original line numbers retained.

## Lines 1543 to 1560

```text
1543: const resolveAttributePath = (model: Record<string, any>, path?: string) => {
1544:   if (!path) return null;
1545:   const parts = path.split('.').filter(Boolean);
1546:   return parts.reduce<Record<string, any> | null>((acc, key) => {
1547:     if (!acc) return null;
1548:     return acc[key] ?? null;
1549:   }, model);
1550: };
1551:
1552: const buildRiskMaps = (rows: any[], metricIds: string[]) => {
1553:   const metricMaps = metricIds.reduce<Record<string, Map<string, number>>>(
1554:     (acc, metricId) => {
1555:       acc[metricId] = new Map();
1556:       return acc;
1557:     },
1558:     {}
1559:   );
1560:
```

## Lines 1575 to 1615

```text
1575:
1576: const buildGraphData = (
1577:   rows: any[],
1578:   rootName: string | null,
1579:   mode: HierarchyMode,
1580:   levels: Array<{ tier: number }>,
1581:   riskMetrics: Array<{ id: string; ogmaField: string }>,
1582:   riskMaps?: RiskMaps
1583: ): GraphData => {
1584:   const nodes = new Map<string, GraphNode>();
1585:   const edges = new Map<string, GraphEdge>();
1586:   const childrenByParent = new Map<string, Set<string>>();
1587:   const rootIds = new Set<string>();
1588:   let rootId: string | null = null;
1589:   const defaultPlatformImageUrl = riskMaps?.defaultPlatformImageUrl ?? null;
1590:   const partDisplayNamesByTier = riskMaps?.partsDisplayNamesByTier ?? {};
1591:   let riskSignature = '';
1592:   if (riskMaps?.metricsByTier && riskMetrics.length) {
1593:     let riskCount = 0;
1594:     let riskSum = 0;
1595:     Object.values(riskMaps.metricsByTier).forEach((metricMaps) => {
1596:       riskMetrics.forEach((metric) => {
1597:         const map = metricMaps?.[metric.id];
1598:         if (!map) return;
1599:         map.forEach((value) => {
1600:           if (Number.isFinite(value)) {
1601:             riskCount += 1;
1602:             riskSum += value;
1603:           }
1604:         });
1605:       });
1606:     });
1607:     riskSignature = `${riskCount}:${riskSum.toFixed(4)}`;
1608:   }
1609:
1610:   const addChild = (parentId: string, childId: string) => {
1611:     const existing = childrenByParent.get(parentId);
1612:     if (existing) {
1613:       existing.add(childId);
1614:       return;
1615:     }
```

## Lines 1620 to 1875

```text
1620:     tier: number,
1621:     name: string,
1622:     data: HierarchyNodeData,
1623:     nodeId?: string
1624:   ) => {
1625:     const id = nodeId ?? `T${tier}:${name}`;
1626:     const existing = nodes.get(id);
1627:     if (existing) {
1628:       existing.data = {
1629:         ...existing.data,
1630:         supplierName: mergeTextValue(existing.data.supplierName, data.supplierName),
1631:         platformName: mergeTextValue(existing.data.platformName, data.platformName),
1632:         platformNames: mergePlatformNames(
1633:           existing.data.platformNames,
1634:           data.platformNames
1635:         ),
1636:         standardizedParts: mergeStringLists(
1637:           existing.data.standardizedParts ?? [],
1638:           data.standardizedParts ?? []
1639:         ),
1640:         platformImageUrl: mergeTextValue(
1641:           existing.data.platformImageUrl,
1642:           data.platformImageUrl
1643:         ),
1644:         riskReportLink: mergeTextValue(existing.data.riskReportLink, data.riskReportLink),
1645:       };
1646:       riskMetrics.forEach((metric) => {
1647:         const prev = existing.data[metric.ogmaField] ?? null;
1648:         const next = data[metric.ogmaField] ?? null;
1649:         existing.data[metric.ogmaField] = mergeRiskValue(prev, next);
1650:       });
1651:       return existing;
1652:     }
1653:
1654:     const node: GraphNode = {
1655:       id,
1656:       data,
1657:     };
1658:     nodes.set(id, node);
1659:     return node;
1660:   };
1661:
1662:   if (mode === 'suppliers') {
1663:     const trimmedRootName = rootName ? rootName.trim() : '';
1664:     const rootMeta = riskMaps?.supplierRootMeta ?? null;
1665:     const rootNodeName = rootMeta?.name?.trim() || trimmedRootName || rootMeta?.id || '';
1666:     const rootNodeId = rootNodeName
1667:       ? rootMeta?.id
1668:         ? `T0VID:${rootMeta.id}`
1669:         : `T0:${rootNodeName}`
1670:       : null;
1671:     if (rootNodeId) {
1672:       rootId = rootNodeId;
1673:       rootIds.add(rootNodeId);
1674:
1675:       nodes.set(rootNodeId, {
1676:         id: rootNodeId,
1677:         data: {
1678:           hierarchyMode: 'suppliers',
1679:           name: rootNodeName,
1680:           tier: 0,
1681:           supplierName: rootNodeName,
1682:           platformName: null,
1683:           platformNames: [],
1684:           platformImageUrl: defaultPlatformImageUrl,
1685:           childCount: 0,
1686:         },
1687:       });
1688:       riskMetrics.forEach((metric) => {
1689:         nodes.get(rootNodeId)!.data[metric.ogmaField] = null;
1690:       });
1691:     }
1692:
1693:     rows.forEach((row) => {
1694:       let parentId = rootNodeId;
1695:       for (let index = 0; index < levels.length; index += 1) {
1696:         const level = levels[index];
1697:         const levelCell = row?.[index];
1698:         const levelName = normalizeCellValue(levelCell?.data).trim();
1699:         if (!levelName) break;
1700:         const levelVid = normalizeCellValue(
1701:           (levelCell as Record<string, unknown> | undefined)?.__scVid
1702:         ).trim();
1703:         const supplierPlatforms = riskMaps?.supplierPlatformsByName?.get(levelName) ?? [];
1704:         const primaryPlatform =
1705:           supplierPlatforms.length > 0 ? supplierPlatforms[0] : null;
1706:         const metricsForTier = riskMaps?.metricsByTier?.[level.tier] ?? {};
1707:         const nodeData: HierarchyNodeData = {
1708:           hierarchyMode: 'suppliers',
1709:           name: levelName,
1710:           tier: level.tier,
1711:           supplierName: levelName,
1712:           riskReportLink: riskMaps?.supplierLinksByTier?.[level.tier]?.get(levelName) ?? null,
1713:           platformName: primaryPlatform,
1714:           platformNames: supplierPlatforms,
1715:           standardizedParts:
1716:             riskMaps?.supplierStandardizedPartsByTier?.[level.tier]?.get(levelName) ?? [],
1717:           platformImageUrl: defaultPlatformImageUrl,
1718:           childCount: 0,
1719:         };
1720:         riskMetrics.forEach((metric) => {
1721:           const metricMap = metricsForTier[metric.id];
1722:           nodeData[metric.ogmaField] = metricMap?.get(levelName) ?? null;
1723:         });
1724:         const node = ensureNode(
1725:           level.tier,
1726:           levelName,
1727:           nodeData,
1728:           levelVid ? `T${level.tier}VID:${levelVid}` : undefined
1729:         );
1730:         if (parentId) {
1731:           const edgeId = `${parentId}->${node.id}`;
1732:           if (!edges.has(edgeId)) {
1733:             edges.set(edgeId, { id: edgeId, source: parentId, target: node.id });
1734:             addChild(parentId, node.id);
1735:           }
1736:         } else {
1737:           rootIds.add(node.id);
1738:           if (!rootId) rootId = node.id;
1739:         }
1740:         parentId = node.id;
1741:       }
1742:     });
1743:   } else {
1744:     rows.forEach((row) => {
1745:       let parentId: string | null = null;
1746:       let platformName: string | null = null;
1747:       let platformImageUrl: string | null = null;
1748:       for (let index = 0; index < levels.length; index += 1) {
1749:         const level = levels[index];
1750:         const levelName = normalizeCellValue(row?.[index]?.data).trim();
1751:         if (!levelName) break;
1752:         const displayName =
1753:           partDisplayNamesByTier[level.tier]?.get(levelName) ?? levelName;
1754:         if (index === 0) {
1755:           platformName = displayName;
1756:           platformImageUrl =
1757:             levelName !== ''
1758:               ? riskMaps?.platformImageByName?.get(levelName) ?? null
1759:               : null;
1760:         }
1761:         const resolvedPlatformImageUrl = platformImageUrl ?? defaultPlatformImageUrl;
1762:         const metricsForTier = riskMaps?.metricsByTier?.[level.tier] ?? {};
1763:         const tierSupplierNames =
1764:           riskMaps?.partSuppliersByTier?.[level.tier]?.get(levelName) ?? [];
1765:         const nodeData: HierarchyNodeData = {
1766:           hierarchyMode: 'parts',
1767:           name: displayName,
1768:           tier: level.tier,
1769:           supplierName:
1770:             tierSupplierNames.length > 0 ? tierSupplierNames.join(', ') : null,
1771:           riskReportLink: null,
1772:           platformName: platformName ?? null,
1773:           platformNames: platformName ? [platformName] : [],
1774:           platformImageUrl: resolvedPlatformImageUrl,
1775:           childCount: 0,
1776:         };
1777:         riskMetrics.forEach((metric) => {
1778:           const metricMap = metricsForTier[metric.id];
1779:           nodeData[metric.ogmaField] = metricMap?.get(levelName) ?? null;
1780:         });
1781:         const nodeId = parentId ? `${parentId}|T${level.tier}:${levelName}` : undefined;
1782:         const node = ensureNode(level.tier, levelName, nodeData, nodeId);
1783:         if (!parentId) {
1784:           rootIds.add(node.id);
1785:         } else {
1786:           const edgeId = `${parentId}->${node.id}`;
1787:           if (!edges.has(edgeId)) {
1788:             edges.set(edgeId, { id: edgeId, source: parentId, target: node.id });
1789:             addChild(parentId, node.id);
1790:           }
1791:         }
1792:         parentId = node.id;
1793:       }
1794:     });
1795:
1796:     if (rootIds.size) {
1797:       rootId = Array.from(rootIds.values())[0];
1798:     }
1799:
1800:     const syntheticPartsRoot = (rootName ?? '').trim();
1801:     if (syntheticPartsRoot && rootIds.size > 0) {
1802:       const syntheticRootId = `T0:${syntheticPartsRoot}`;
1803:       if (!nodes.has(syntheticRootId)) {
1804:         const syntheticNode: GraphNode = {
1805:           id: syntheticRootId,
1806:           data: {
1807:             hierarchyMode: 'parts',
1808:             name: syntheticPartsRoot,
1809:             tier: 0,
1810:             supplierName: null,
1811:             riskReportLink: null,
1812:             platformName: syntheticPartsRoot,
1813:             platformNames: [syntheticPartsRoot],
1814:             platformImageUrl: defaultPlatformImageUrl,
1815:             childCount: 0,
1816:           },
1817:         };
1818:         riskMetrics.forEach((metric) => {
1819:           syntheticNode.data[metric.ogmaField] = null;
1820:         });
1821:         nodes.set(syntheticRootId, syntheticNode);
1822:       }
1823:       const priorRootIds = Array.from(rootIds.values());
1824:       priorRootIds.forEach((childRootId) => {
1825:         const edgeId = `${syntheticRootId}->${childRootId}`;
1826:         if (!edges.has(edgeId)) {
1827:           edges.set(edgeId, { id: edgeId, source: syntheticRootId, target: childRootId });
1828:           addChild(syntheticRootId, childRootId);
1829:         }
1830:       });
1831:       rootIds.clear();
1832:       rootIds.add(syntheticRootId);
1833:       rootId = syntheticRootId;
1834:     }
1835:   }
1836:
1837:   childrenByParent.forEach((children, parentId) => {
1838:     const node = nodes.get(parentId);
1839:     if (node) {
1840:       node.data.childCount = children.size;
1841:     }
1842:   });
1843:
1844:   if (mode === 'parts' && riskMetrics.length > 0) {
1845:     // Propagate worst descendant risk upward so top hierarchy levels reflect supplier risk exposure.
1846:     const sortedNodes = Array.from(nodes.values()).sort(
1847:       (a, b) => (b.data.tier ?? 0) - (a.data.tier ?? 0)
1848:     );
1849:     sortedNodes.forEach((node) => {
1850:       const children = childrenByParent.get(node.id);
1851:       if (!children || children.size === 0) return;
1852:       riskMetrics.forEach((metric) => {
1853:         const ownValue = parseNumericCell(node.data[metric.ogmaField]);
1854:         let inheritedMax = ownValue;
1855:         children.forEach((childId) => {
1856:           const childNode = nodes.get(childId);
1857:           if (!childNode) return;
1858:           const childValue = parseNumericCell(childNode.data[metric.ogmaField]);
1859:           if (childValue === null) return;
1860:           inheritedMax = inheritedMax === null ? childValue : Math.max(inheritedMax, childValue);
1861:         });
1862:         node.data[metric.ogmaField] = inheritedMax;
1863:       });
1864:     });
1865:   }
1866:
1867:   return {
1868:     nodes: Array.from(nodes.values()),
1869:     edges: Array.from(edges.values()),
1870:     rootId,
1871:     rootIds: Array.from(rootIds.values()),
1872:     childrenByParent,
1873:     riskSignature,
1874:   };
1875: };
```
