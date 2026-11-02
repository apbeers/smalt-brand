# VitePress theme

The theme used by [smaltdb.dev](https://smaltdb.dev). The live copy is in the smaltdb repo at `docs/.vitepress/theme/`; this is the reference copy.

- `smaltdb.css`: the Kiln palette mapped onto VitePress's `--vp-*` variables for light and dark, plus the type rules (Geist, 17px/1.6 body, Martian Mono labels and hero wordmark).
- `shiki.ts`: light and dark Shiki code themes built from the `syn-*` tokens.

To use it, import `smaltdb.css` from `.vitepress/theme/index.ts`, pass `{ light: smaltLight, dark: smaltDark }` from `shiki.ts` as `markdown.theme` in the config, and load the fonts:

```html
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700&family=Geist+Mono:wght@400;500&family=Martian+Mono:wght@400;600&display=swap" rel="stylesheet">
```
