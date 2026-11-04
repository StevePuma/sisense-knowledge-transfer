# Sisense customer knowledge

Steve Puma’s working knowledge base for building customer analytics with Sisense Compose SDK, React, and Linkurious Ogma. The first detailed case study is Northrop Grumman’s SCRM configuration, captured from the local SCRM working tree on November 4, 2026.

## Start here

- [Agent instructions](AGENTS.md): routing, evidence standards, and how to answer customer questions.
- [Northrop Grumman](customers/northrop-grumman/README.md): data, hierarchy, metrics, analytics, and known gaps.
- [Compose SDK and plugins](knowledge/compose-sdk.md): React integration and plugin development workflow.
- [Ogma and React](knowledge/ogma-react.md): graph contracts, lifecycle, identity, and debugging.
- [Data modeling](knowledge/data-modeling.md), [dashboards](knowledge/dashboards.md), and [CustomJS](knowledge/custom-js.md).
- [Customer pattern catalog](knowledge/customer-patterns.md) and [official references](knowledge/sources.md).
- [Agent profiles](agents/README.md) and [skills](.agents/skills/README.md).

## Use with an agent

Open this repository in Codex and ask a question. `AGENTS.md` routes work to the relevant knowledge and repository-local skills. Profiles in `agents/` are reusable specialist instructions; they are not running services or a separate chat application. Skills live under `.agents/skills/<name>/SKILL.md`; keep the repository intact because they link to shared references.

Example prompts:

- What data does NG’s SCRM use, and which fields become supplier and part nodes?
- Trace `t3FinalRisk` from the semantic model to the node color. Is it actually a risk score?
- Why does NG have no analytics for its tier-zero part node?
- Design a React Compose SDK plugin that renders an Ogma hierarchy, using NG as a reference and synthetic test data.
- Debug missing tier-one suppliers without assuming the full dataset was returned.
- Explain which parts of a Fusion dashboard’s CustomJS must be reimplemented in React.

## Search and verify

Requires Python 3. No Sisense account, Ogma license, or Node installation is needed to read or validate this knowledge repo.

```sh
python3 scripts/search.py 'confidence'
python3 scripts/search.py 'BOM_TIER_3.CAPACITY'
python3 scripts/validate.py
```

The NG snapshot includes schema and selected code evidence, not live data. Customer claims are grounded in this snapshot; deployment status, business validation, warehouse joins, and actual dashboard contents remain unverified. See [provenance](customers/northrop-grumman/provenance.json).

## Extend it

Use [the customer capture template](templates/customer-capture.md) for another implementation and follow [maintenance](CONTRIBUTING.md). Keep this repository private. It contains customer-specific architecture and identifiers. No public license is granted for customer excerpts or proprietary vendor software.
