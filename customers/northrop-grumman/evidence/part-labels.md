# Part Labels

Source: `src/features/supply-chain/components/HierarchicalViz/HierarchicalViz.tsx`. Working-tree snapshot on 2026-11-04; original line numbers retained.

## Lines 2180 to 2240

```text
2180:     const keys = Object.keys(supplierTraversalRoles) as Array<keyof typeof supplierTraversalRoles>;
2181:     const map = new Map<string, number>();
2182:     let index = 0;
2183:     keys.forEach((key) => {
2184:       if (supplierTraversalRoles[key]) {
2185:         map.set(key, index);
2186:         index += 1;
2187:       }
2188:     });
2189:     return map;
2190:   }, [supplierTraversalRoles]);
2191:   const partsLevelLabelRoles = useMemo(
2192:     () =>
2193:       partsLevels.map((level, index) => {
2194:         const configured = (level as any).labelRole as string | undefined;
2195:         if (configured) return configured;
2196:         if (index === 0) return 'rootProduct';
2197:         if (index === 1) return 'bomTextTier1';
2198:         if (index === 2) return 'bomTextTier2';
2199:         if (index === 3) return 'bomTextTier3';
2200:         if (index === 4) return 'bomTextTier4';
2201:         if (index === 5) return 'partSupplierDisplayName';
2202:         return undefined;
2203:       }),
2204:     [partsLevels]
2205:   );
2206:   const partsLabelLookupFields = useMemo(() => {
2207:     if (!partsEnabled) return [];
2208:     const fields: any[] = [];
2209:     const addRole = (role?: string) => {
2210:       const field = getOptionalField(role);
2211:       if (!field) return;
2212:       fields.push(field);
2213:     };
2214:     partsLevelLabelRoles.forEach((role) => addRole(role));
2215:     addRole('bomProduct');
2216:     addRole('standardizedProduct');
2217:     addRole('matchedCompanyProduct');
2218:     addRole('partSupplierDisplayName');
2219:     return fields;
2220:   }, [partsEnabled, partsLevelLabelRoles, fieldRoles, dataModel, dimensionKey]);
2221:   const partsLabelLookupIndexByRole = useMemo(() => {
2222:     const map = new Map<string, number>();
2223:     let nextIndex = 0;
2224:     const rolesToTrack = [
2225:       ...partsLevelLabelRoles,
2226:       'bomProduct',
2227:       'standardizedProduct',
2228:       'matchedCompanyProduct',
2229:       'partSupplierDisplayName',
2230:     ].filter(Boolean) as string[];
2231:     rolesToTrack.forEach((role) => {
2232:       const field = getOptionalField(role);
2233:       if (!field) return;
2234:       // Role order mirrors `partsLabelLookupFields`, so role-specific tier fields with the same
2235:       // attribute name (e.g. STANDARDISED_PRODUCT across T1..T5) do not collapse.
2236:       if (!map.has(role)) {
2237:         map.set(role, nextIndex);
2238:       }
2239:       nextIndex += 1;
2240:     });
```

## Lines 3585 to 3680

```text
3585:     () => {
3586:       if (!partsEnabled || partsLevels.length === 0) return {};
3587:       const result: Record<number, Map<string, string>> = {};
3588:       partsLevels.forEach((level) => {
3589:         result[level.tier] = new Map<string, string>();
3590:       });
3591:       const labelOffset = partsNameFields.length;
3592:       const rootProductById = new Map<string, string>();
3593:       const bomLabelByBomId = new Map<string, string>();
3594:       const rootProductIndex = partsLabelLookupIndexByRole.get('rootProduct');
3595:       const bomProductIndex = partsLabelLookupIndexByRole.get('bomProduct');
3596:       const standardizedProductIndex = partsLabelLookupIndexByRole.get('standardizedProduct');
3597:       const matchedCompanyProductIndex = partsLabelLookupIndexByRole.get('matchedCompanyProduct');
3598:
3599:       (partsLabelLookupData?.rows ?? []).forEach((row: any[]) => {
3600:         const rootId = normalizeCellValue(row?.[0]?.data).trim();
3601:         const rootName =
3602:           rootProductIndex === undefined
3603:             ? ''
3604:             : normalizeCellValue(row?.[labelOffset + rootProductIndex]?.data).trim();
3605:         if (rootId && rootName && !rootProductById.has(rootId)) {
3606:           rootProductById.set(rootId, rootName);
3607:         }
3608:
3609:         const bomIdIndex = Math.min(4, Math.max(partsLevels.length - 2, 0));
3610:         const bomId = normalizeCellValue(row?.[bomIdIndex]?.data).trim();
3611:         const bomLabel =
3612:           (bomProductIndex === undefined
3613:             ? ''
3614:             : normalizeCellValue(row?.[labelOffset + bomProductIndex]?.data).trim()) ||
3615:           (standardizedProductIndex === undefined
3616:             ? ''
3617:             : normalizeCellValue(row?.[labelOffset + standardizedProductIndex]?.data).trim()) ||
3618:           (matchedCompanyProductIndex === undefined
3619:             ? ''
3620:             : normalizeCellValue(row?.[labelOffset + matchedCompanyProductIndex]?.data).trim());
3621:         if (bomId && bomLabel) {
3622:           const existing = bomLabelByBomId.get(bomId);
3623:           if (!existing || existing === bomId) {
3624:             bomLabelByBomId.set(bomId, bomLabel);
3625:           }
3626:         }
3627:       });
3628:
3629:       (partsLabelLookupData?.rows ?? []).forEach((row: any[]) => {
3630:         partsLevels.forEach((level, index) => {
3631:           const key = normalizeCellValue(row?.[index]?.data).trim();
3632:           if (!key) return;
3633:           const explicitLabelRole = partsLevelLabelRoles[index];
3634:           const labelAt = (role?: string) => {
3635:             const roleIndex =
3636:               role === undefined ? undefined : partsLabelLookupIndexByRole.get(role);
3637:             if (roleIndex === undefined) return '';
3638:             return normalizeCellValue(row?.[labelOffset + roleIndex]?.data).trim();
3639:           };
3640:           const explicitLabel = labelAt(explicitLabelRole);
3641:           const fallbackLabel =
3642:             labelAt('bomProduct') ||
3643:             labelAt('standardizedProduct') ||
3644:             labelAt('matchedCompanyProduct') ||
3645:             labelAt('partSupplierDisplayName') ||
3646:             '';
3647:           const globalLabel =
3648:             index === 0
3649:               ? rootProductById.get(key) ?? ''
3650:               : index <= 4
3651:                 ? bomLabelByBomId.get(key) ?? ''
3652:                 : '';
3653:           const label = globalLabel || explicitLabel || fallbackLabel || key;
3654:           const existing = result[level.tier].get(key);
3655:           if (!existing || existing === key || (label && label !== key && existing === key)) {
3656:             result[level.tier].set(key, label);
3657:           }
3658:         });
3659:       });
3660:       return result as Record<number, Map<string, string>>;
3661:     },
3662:     [
3663:       partsEnabled,
3664:       partsLevels,
3665:       partsNameFields.length,
3666:       partsLabelLookupData?.rows,
3667:       partsLabelLookupFields,
3668:       partsLabelLookupIndexByRole,
3669:       partsLevelLabelRoles,
3670:       fieldRoles,
3671:       dataModel,
3672:       dimensionKey,
3673:     ]
3674:   );
3675:   const supplierRootMeta = useMemo(() => {
3676:     if (!isEdgeTraversalHierarchicalClient) return null;
3677:     const rootVidIndex = supplierTraversalIndex.get('rootNodeVid');
3678:     const rootNameIndex = supplierTraversalIndex.get('rootNodeName');
3679:     if (rootVidIndex === undefined || rootNameIndex === undefined) return null;
3680:     for (const row of supplierTraversalData?.rows ?? []) {
```
