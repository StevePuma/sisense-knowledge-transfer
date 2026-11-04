# Maintain the knowledge

Capture another customer with [the template](templates/customer-capture.md). Record a source revision and whether the working tree is dirty; retain hashes for every source used. Curate narrow evidence instead of copying entire applications, build outputs, lockfiles, credentials, or licensed packages.

When refreshing NG, compare the current config and consuming code with the captured evidence. Update the case study, schema extraction, role mappings, original line ranges, hashes, and evaluated answers together. Hash changes are a prompt to inspect behavior, not permission to overwrite conclusions mechanically.

General guidance belongs under `knowledge/`; observed customer behavior belongs under `customers/`. Keep skill instructions short and route to the maintained reference. Add a new profile only when it changes how an agent approaches a task.

Run `python3 scripts/validate.py` before committing. It checks relative file links, skill frontmatter, configured fields, snapshot invariants, and recognizable credential patterns. It is not a proof that all secrets are absent or that a live Sisense integration works. Review the diff and intended audience as part of the capture.

Use [evaluation questions](evals/customer-questions.md) to assess an agent’s answers. The expected evidence is a rubric for a human reviewer; the repository validator does not pretend to evaluate natural-language reasoning.
