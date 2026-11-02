# CodeBlock

A code block set in Geist Mono at 15px / 1.6 on `code-bg`, with every syntax colour at least 5:1 against it in both themes.

- Map highlighter classes to `syn-keyword`, `syn-string`, `syn-number`, `syn-function`, `syn-comment` (italic) and `syn-punct`; plain identifiers use `text`.
- SQL inside strings stays `syn-string`; don't highlight it separately unless the block is pure SQL.
- The consumer provides the code and the highlighter; this defines the colours and metrics only.
