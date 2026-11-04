# Sisense knowledge agent instructions

Answer with the narrowest evidence that supports the claim. Read the customer case before offering generic advice about a customer implementation. This repository is a knowledge and skill pack for React analytics; it is not the SCRM application.

## Route the task

| Request | Specialist | Skill | Primary reference |
| --- | --- | --- | --- |
| NG data or behavior | [Customer analyst](agents/customer-analyst.md) | `.agents/skills/ng-scrm/SKILL.md` | `customers/northrop-grumman/README.md` |
| Compose SDK component or plugin | [Compose engineer](agents/compose-engineer.md) | `.agents/skills/sisense-compose-plugins/SKILL.md` | `knowledge/compose-sdk.md` |
| Graph, layout, interactions | [Ogma engineer](agents/ogma-engineer.md) | `.agents/skills/ogma-react/SKILL.md` | `knowledge/ogma-react.md` |
| Model, grain, joins, metric | [Data modeler](agents/data-modeler.md) | `.agents/skills/sisense-data-modeling/SKILL.md` | `knowledge/data-modeling.md` |
| Dashboard, filters, drilldown | [Dashboard engineer](agents/dashboard-engineer.md) | `.agents/skills/sisense-dashboards/SKILL.md` | `knowledge/dashboards.md` |
| Fusion widget or dashboard JS | [CustomJS engineer](agents/custom-js-engineer.md) | `.agents/skills/sisense-custom-js/SKILL.md` | `knowledge/custom-js.md` |
| React state, effects, performance | [React engineer](agents/react-engineer.md) | `.agents/skills/react-analytics/SKILL.md` | `knowledge/react-analytics.md` |

Profiles describe roles and can be applied by one agent. They do not require parallel delegation or authorize external mutations.

## Evidence rules

1. For customer facts, cite a repository path and original source line range from the evidence files, or a JSON pointer in the config snapshot. Distinguish observed configuration, implementation behavior, inference, and unverified business meaning.
2. `schema.json` is the available semantic field surface. `field-roles.md` identifies configured roles. Neither proves a field is queried, rendered, populated, or business-validated; trace the consumer.
3. Read `provenance.json` before making version claims. Its source tree was dirty; the base commit alone cannot reproduce the snapshot. Hashes identify the inspected file bytes.
4. Do not equate confidence with risk, absence with zero, label equality with entity identity, or a query row cap with complete coverage.
5. NG’s hierarchy is not the separate relationship-network or geo implementation. Do not import other clients’ features into an NG answer.
6. For new code, inspect the target repository’s package versions/types and instructions. Consult official version-matched references; the latest plugin system may differ from the captured application.
7. Keep credentials, actual customer row exports, signed download URLs, and vendor binaries out of commits. Do not copy source manifests or lockfiles wholesale. Use synthetic fixtures for examples.

## Answer shape

State what happens; trace config → attribute → query → transformation → UI; give citations; identify only gaps relevant to the question. For fixes, identify the narrowest layer, provide an implementation plan or patch as requested, and verify the affected behavior. Never claim a live test from static source inspection.
