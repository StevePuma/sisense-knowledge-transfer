# Registry

Source: `src/data/dataModelRegistry.ts`. Working-tree snapshot on 2026-11-04; original line numbers retained.

## Lines 1 to 43

```text
1: import * as SupplyChainTest from './supply-chain-test';
2: import * as RivianGraph from './rivian_graph';
3: import * as RivianHierarchical from './rivian-hierarchical';
4: import * as RivianSubtier from '../rivian_subtier';
5: import * as RivianAiV2 from '../rivian_ai_v2';
6: import * as SizewellData from './sizewell-data';
7: import * as NgSubtierDemo from '../ng-subtier_demo';
8: import * as ArmySkyfoundry from '../army_skyfoundry';
9: import * as DemoConfig from './demo_config';
10: import * as Dell from '../dell';
11: import * as Infineum from '../infineum';
12: import * as Diebold from '../diebold';
13: import * as Coherent from '../coherent';
14: import * as Medline from '../medline';
15: import * as Telenor from '../telenor';
16: import * as RollsRoyce from '../rolls_royce';
17:
18: const DATA_MODEL_REGISTRY: Record<string, any> = {
19:   'src/data/demo_config.ts': DemoConfig,
20:   'src/data/supply-chain-test.ts': SupplyChainTest,
21:   'src/data/rivian_graph.ts': RivianGraph,
22:   'src/data/rivian-hierarchical.ts': RivianHierarchical,
23:   'src/rivian_subtier.ts': RivianSubtier,
24:   'src/rivian_ai_v2.ts': RivianAiV2,
25:   'src/data/sizewell-data.ts': SizewellData,
26:   'src/ng-subtier_demo.ts': NgSubtierDemo,
27:   'src/army_skyfoundry.ts': ArmySkyfoundry,
28:   'src/dell.ts': Dell,
29:   'src/infineum.ts': Infineum,
30:   'src/diebold.ts': Diebold,
31:   'src/coherent.ts': Coherent,
32:   'src/medline.ts': Medline,
33:   'src/telenor.ts': Telenor,
34:   'src/rolls_royce.ts': RollsRoyce,
35: };
36:
37: export const DEFAULT_GRAPH_DATA_MODEL = SupplyChainTest;
38: export const DEFAULT_HIERARCHICAL_DATA_MODEL = RivianHierarchical;
39:
40: export const getDataModelByFile = (file?: string | null) => {
41:   if (!file) return null;
42:   return DATA_MODEL_REGISTRY[file] ?? null;
43: };
```
