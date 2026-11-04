# Metrics

Source: `src/features/supply-chain/components/HierarchicalViz/HierarchicalViz.tsx`. Working-tree snapshot on 2026-11-04; original line numbers retained.

## Lines 4865 to 4985

```text
4865:   const buildMetricsByTier = useCallback(
4866:     (
4867:       rows: any[],
4868:       nameIndexByTier: Map<number, number>,
4869:       metricRolesByTier: Record<string, Record<string, string>>,
4870:       metricRoleIndexByRole: Map<string, number>,
4871:       nameFieldsCount: number
4872:     ) => {
4873:       const sums: Record<number, Record<string, Map<string, number>>> = {};
4874:       const counts: Record<number, Record<string, Map<string, number>>> = {};
4875:       const valueVotes: Record<number, Record<string, Map<string, Map<number, number>>>> = {};
4876:
4877:       Object.keys(metricRolesByTier).forEach((tierKey) => {
4878:         const tier = Number(tierKey);
4879:         if (!Number.isFinite(tier)) return;
4880:         sums[tier] = {};
4881:         counts[tier] = {};
4882:         valueVotes[tier] = {};
4883:         metricIds.forEach((metricId) => {
4884:           sums[tier][metricId] = new Map();
4885:           counts[tier][metricId] = new Map();
4886:           valueVotes[tier][metricId] = new Map();
4887:         });
4888:       });
4889:
4890:       rows.forEach((row) => {
4891:         nameIndexByTier.forEach((nameIndex, tier) => {
4892:           const name = normalizeCellValue(row?.[nameIndex]?.data).trim();
4893:           if (!name) return;
4894:           const metricRoles = metricRolesByTier[String(tier)] ?? {};
4895:           metricIds.forEach((metricId) => {
4896:             const role = metricRoles[metricId];
4897:             if (!role) return;
4898:             const roleIndex = metricRoleIndexByRole.get(role);
4899:             if (roleIndex === undefined) return;
4900:             const rawValue = row?.[nameFieldsCount + roleIndex]?.data;
4901:             let value = parseNumericCell(rawValue);
4902:             if (value === null) {
4903:               const metricConfig = riskMetricById.get(metricId);
4904:               const valueMap = metricConfig?.valueMap;
4905:               if (valueMap) {
4906:                 const mapped = valueMap[normalizeMetricValueKey(rawValue)];
4907:                 if (Number.isFinite(mapped)) {
4908:                   value = mapped;
4909:                 }
4910:               }
4911:             }
4912:             if (value === null) return;
4913:             const metricConfig = riskMetricById.get(metricId);
4914:             const useCategoricalMode = Boolean(
4915:               metricConfig?.comparison === 'eq' || metricConfig?.valueMap
4916:             );
4917:             if (useCategoricalMode) {
4918:               if (!valueVotes[tier][metricId].has(name)) {
4919:                 valueVotes[tier][metricId].set(name, new Map<number, number>());
4920:               }
4921:               const nodeVotes = valueVotes[tier][metricId].get(name)!;
4922:               nodeVotes.set(value, (nodeVotes.get(value) ?? 0) + 1);
4923:             }
4924:             const prevSum = sums[tier][metricId].get(name) ?? 0;
4925:             const prevCount = counts[tier][metricId].get(name) ?? 0;
4926:             sums[tier][metricId].set(name, prevSum + value);
4927:             counts[tier][metricId].set(name, prevCount + 1);
4928:           });
4929:         });
4930:       });
4931:
4932:       const result: Record<number, Record<string, Map<string, number>>> = {};
4933:       Object.keys(sums).forEach((tierKey) => {
4934:         const tier = Number(tierKey);
4935:         result[tier] = {};
4936:         metricIds.forEach((metricId) => {
4937:           const avgMap = new Map<string, number>();
4938:           const metricConfig = riskMetricById.get(metricId);
4939:           const useCategoricalMode = Boolean(
4940:             metricConfig?.comparison === 'eq' || metricConfig?.valueMap
4941:           );
4942:           sums[tier][metricId].forEach((sum, name) => {
4943:             const count = counts[tier][metricId].get(name) ?? 0;
4944:             if (count <= 0) return;
4945:             if (useCategoricalMode) {
4946:               const votes = valueVotes[tier][metricId].get(name);
4947:               if (!votes || votes.size === 0) return;
4948:               let selectedValue: number | null = null;
4949:               let selectedCount = -1;
4950:               votes.forEach((voteCount, numericValue) => {
4951:                 if (
4952:                   voteCount > selectedCount ||
4953:                   (voteCount === selectedCount &&
4954:                     (selectedValue === null || numericValue < selectedValue))
4955:                 ) {
4956:                   selectedValue = numericValue;
4957:                   selectedCount = voteCount;
4958:                 }
4959:               });
4960:               if (selectedValue !== null) {
4961:                 avgMap.set(name, selectedValue);
4962:               }
4963:               return;
4964:             }
4965:             avgMap.set(name, sum / count);
4966:           });
4967:           result[tier][metricId] = avgMap;
4968:         });
4969:       });
4970:       return result;
4971:     },
4972:     [metricIds, riskMetricById]
4973:   );
4974:
4975:   const supplierRiskMapsByTier = useMemo(
4976:     () =>
4977:       buildMetricsByTier(
4978:         supplierRiskData?.rows ?? [],
4979:         supplierNameIndexByTier,
4980:         supplierRiskRolesByTier,
4981:         supplierRiskFieldIndexByRole,
4982:         supplierNameFields.length
4983:       ),
4984:     [
4985:       buildMetricsByTier,
```

## Lines 5030 to 5060

```text
5030:   const partsRiskMapsByTier = useMemo(
5031:     () =>
5032:       buildMetricsByTier(
5033:         partsRiskData?.rows ?? [],
5034:         partsNameIndexByTier,
5035:         partsRiskRolesByTier,
5036:         partsRiskFieldIndexByRole,
5037:         partsNameFields.length
5038:       ),
5039:     [
5040:       buildMetricsByTier,
5041:       partsRiskData,
5042:       partsNameIndexByTier,
5043:       partsRiskRolesByTier,
5044:       partsRiskFieldIndexByRole,
5045:       partsNameFields.length,
5046:     ]
5047:   );
5048:
5049:   const graph = useMemo(
5050:     () => {
5051:       if (isDellPartsHierarchyClient) {
5052:         if (requiresPartSelectionBeforeLoad && !selectedDellRootProduct) {
5053:           return {
5054:             nodes: [],
5055:             edges: [],
5056:             rootId: null,
5057:             rootIds: [],
5058:             childrenByParent: new Map<string, Set<string>>(),
5059:           };
5060:         }
```
