# StatusBadge

A compact state label that always pairs an icon with a word, coloured `success`, `warning` or `danger` on `surface`.

- Committed (check), Stale (exclamation mark: a bar and a chip), Failed (cross), drawn in the Chevron icon style (see `BRAND.md`, Iconography). Never rely on colour alone.
- Stale is for materialized views that need a refresh; Failed is for errors and rolled-back transactions.
- The consumer provides the state and, if needed, a tooltip with detail.
