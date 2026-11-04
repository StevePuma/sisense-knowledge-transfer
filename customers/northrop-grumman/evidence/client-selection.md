# Client Selection

Source: `src/config/clientConfig.ts`. Working-tree snapshot on 2026-11-04; original line numbers retained.

## Lines 626 to 649

```text
626:
627: const CLIENT_CONFIGS: Record<string, ClientConfig> = {
628:   demo: normalizePopoverConfig(demoConfig as ClientConfig),
629:   dell: normalizePopoverConfig(dellConfig as ClientConfig),
630:   army_skyfoundry: normalizePopoverConfig(armySkyfoundryConfig as ClientConfig),
631:   ng_subtier_demo: normalizePopoverConfig(ngSubtierDemoConfig as ClientConfig),
632:   rivian: normalizePopoverConfig(rivianConfig as ClientConfig),
633:   rivian_ai_mappingv2: normalizePopoverConfig(rivianAiMappingV2Config as ClientConfig),
634:   rivian_ai_v2: normalizePopoverConfig(rivianAiMappingV2Config as ClientConfig),
635:   sizewell: normalizePopoverConfig(sizewellConfig as ClientConfig),
636:   infineum: normalizePopoverConfig(infineumConfig as ClientConfig),
637:   diebold: normalizePopoverConfig(dieboldConfig as ClientConfig),
638:   coherent: normalizePopoverConfig(coherentConfig as ClientConfig),
639:   medline: normalizePopoverConfig(medlineConfig as ClientConfig),
640:   telenor: normalizePopoverConfig(telenorConfig as ClientConfig),
641:   rolls_royce: normalizePopoverConfig(rollsRoyceConfig as ClientConfig),
642: };
643:
644: export const getClientConfig = (clientId?: string) => {
645:   const resolved = clientId ?? process.env.REACT_APP_SUPPLY_CHAIN_CLIENT ?? 'rolls_royce';
646:   return CLIENT_CONFIGS[resolved] ?? CLIENT_CONFIGS.rolls_royce;
647: };
648:
649: export const getRiskMetric = (config: ClientConfig, id: string) =>
```
