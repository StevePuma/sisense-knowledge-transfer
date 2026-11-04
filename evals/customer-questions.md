# Customer question evaluation

Ask an agent the question without providing the expected answer. Check the response against this rubric and require source citations. These are evaluation cases, not claims of an automated agent test run.

| Question | Required observations | Failure mode |
| --- | --- | --- |
| What data powers NG? | Live `NG_SUBTIER_DEMO`; BOM tiers, spine, confidence; role versus schema distinction | Invented warehouse lineage |
| Does NG use the geo view? | Only hierarchical enabled | Borrowing another client’s features |
| What is prefix mode? | Successively deeper supplier column prefixes | Describing name prefix search |
| Why is the parent’s risk higher? | Numeric averaging followed by descendant maximum; confidence semantics unverified | Declaring a validated risk algorithm |
| Is capacity rendered as a risk metric? | Mapped/projected but absent from registered risk metric list | Treating a role as a visible metric |
| Why no dashboard at part level zero? | Direct tier lookup; keys 1–3 and no default | Silently shifting tier indexes |
| Are supplier dashboards node-filtered? | No supplier analytics filter mapping in NG | Assuming part filter mapping applies |
| Are all 952 fields displayed? | Available schema versus configured/query/rendered layers | Equating model exports to UI |
| Does Ogma query Linkurious Enterprise? | Compose queries Sisense; Ogma renders; no Enterprise backend evidence | Confusing vendor with backend |
| What is the exact production row count? | Cannot determine from source; request actual authorized query evidence | Treating 100,000 query limit as count |
| Build a reusable NG-like plugin | Inspect versions, choose plugin contract, isolate mapping, use synthetic data | Copying customer source as a universal scaffold |
| Can the base commit reproduce the capture? | Dirty working tree; hashes/excerpts preserve inspected state | Claiming commit-only reproducibility |
