# Feature Routing

Source: `src/features/supply-chain/config/featureConfig.ts`. Working-tree snapshot on 2026-11-04; original line numbers retained.

## Lines 44 to 51

```text
44: export const getHierarchicalDataModel = (
45:   clientId: string | undefined = process.env.REACT_APP_SUPPLY_CHAIN_CLIENT
46: ) => {
47:   const clientConfig = getClientConfig(clientId);
48:   const model = getDataModelByFile(clientConfig.dataModels?.hierarchical?.file);
49:   return model ?? DEFAULT_HIERARCHICAL_DATA_MODEL;
50: };
51:
```

## Lines 65 to 80

```text
65:   SupplyChainClientId,
66:   { enabledViews: SupplyChainViewMode[] }
67: > = {
68:   default: {
69:     enabledViews: ['network', 'hierarchical', 'geo'],
70:   },
71:   demo: {
72:     enabledViews: ['network', 'hierarchical', 'geo'],
73:   },
74:   army_skyfoundry: {
75:     enabledViews: ['geo', 'aiInsight'],
76:   },
77:   ng_subtier_demo: {
78:     enabledViews: ['hierarchical'],
79:   },
80:   rivian: {
```

## Lines 114 to 130

```text
114:
115: export const getEnabledSupplyChainViews = (
116:   clientId: string | undefined = process.env.REACT_APP_SUPPLY_CHAIN_CLIENT
117: ) => {
118:   const clientConfig = getClientConfig(clientId);
119:   const configuredViews = clientConfig.features?.enabledViews;
120:   if (configuredViews?.length) {
121:     return configuredViews;
122:   }
123:   const resolvedClientId =
124:     clientId ?? (clientConfig?.clientId as SupplyChainClientId | undefined) ?? 'default';
125:   const resolved = (resolvedClientId as SupplyChainClientId) ?? 'default';
126:   return (
127:     SUPPLY_CHAIN_VIEW_FLAGS[resolved]?.enabledViews ??
128:     SUPPLY_CHAIN_VIEW_FLAGS.default.enabledViews
129:   );
130: };
```
