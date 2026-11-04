# Customer capture template

Use this as a writing checklist, not as evidence of an implementation.

## Identity and scope

Record client key, display name, capture date, source revision, dirty-tree status, and selected file hashes. Distinguish demo configuration from verified deployment.

## Data and lineage

Record source title/type, semantic model file, physical model evidence if available, field-role mappings, types, row grain, keys, metrics, and known business definitions. Mark configured, queried, and rendered fields separately.

## Data to UI

Trace configuration selection, model resolution, query dimensions/filters/limits, positional mapping, identity/deduplication, graph orientation, metric aggregation, layout, and interactions. Record inherited defaults and customer-specific branches.

## Analytics and security

Record dashboard routing and filter semantics. Keep UI/query filters separate from server-side access controls. Do not include credentials, signed URLs, licensed binaries, or real row exports merely to document architecture.

## Evidence and questions

Include focused excerpts with original paths/line numbers and hashes; provide worked questions and known unknowns. Add evaluation prompts that test likely confusions. Verify all field-role references and local links before publishing changes.
