# StatusBadge

A compact state label that always pairs an icon with a word, coloured `success`, `warning` or `danger` on `surface`.

- Committed (check), Stale (triangle), Failed (x). Never rely on colour alone.
- Stale is for materialized views that need a refresh; Failed is for errors and rolled-back transactions.
- The consumer provides the state and, if needed, a tooltip with detail.
