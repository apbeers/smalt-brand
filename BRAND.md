# smaltdb

**Small. Alternate. Fast.**

smaltdb is a fast alternative database for the browser, written in TypeScript. This document is its brand: the Grain mark, the Kiln palette, and a Geist-forward type system with a monospaced voice for coders.

## The name

The name carries three meanings at once:

- **sm** — small
- **alt** — alternate
- **db** — database
- **smalt** — the cobalt-glass pigment, `#003399`, ground into powder. Finer grinds read paler; the brand scale (`smalt-900` → `smalt-100`) follows those grades.

In the wordmark, `alt` is set in `primary`. Write the name in lowercase, as one word: **smaltdb**. In prose, "smaltdb" is fine at the start of a sentence; never "SmaltDB" or "Smalt DB".

## Voice

- Plain and specific. Say what the engine does, such as "runs in a Web Worker", "stores data in OPFS", or "commits through a write-ahead log".
- Describe what smaltdb is, never what it isn't. No "no WASM", "unlike X" or "without Y" framing.
- No comparisons with other databases. Let readers draw their own; never name another engine in marketing copy.
- No unsourced performance claims. A number appears only with its benchmark and method linked beside it.
- Written for coders: show code early, keep sentences short.

Tagline: **Small. Alternate. Fast.** Use it under the wordmark, in social cards, and in the docs hero.

## Logo — the Grain mark

A ground-glass particle and the chip it shed: small, and a little apart.

| Asset | Use |
| --- | --- |
| `logos/smaltdb/grain-mark.svg` | On light grounds. Body `smalt-700`, chip `smalt-300`. |
| `logos/smaltdb/grain-mark-on-dark.svg` | On dark grounds. Body `smalt-200`, chip `smalt-100`. |
| `logos/smaltdb/app-icon.svg` | App and PWA icons, social avatars. |
| `logos/smaltdb/favicon-32.svg`, `favicon-16.svg` | Browser tabs. The 16 px version simplifies the notch away. |
| `logos/smaltdb/lockup.svg`, `lockup-on-dark.svg` | Mark + wordmark, outlined. README headers, docs nav, slides. |
| `logos/smaltdb/wordmark.svg`, `wordmark-on-dark.svg` | Wordmark alone, outlined, `alt` in `primary`. Where the mark already appears nearby. |

The wordmark and lockup SVGs are Martian Mono 600 (width 112.5, the Google Fonts default) converted to paths, so they render identically everywhere with no font loading.

**In a GitHub README** (GitHub strips inline colour styles, so use the image, switched by theme). Copy the two lockup files into the project, here as in smaltdb's `docs/brand/`:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/brand/lockup-on-dark.svg">
  <img alt="smaltdb" src="docs/brand/lockup.svg" width="320">
</picture>
```

Lockup: the mark to the left of the wordmark (style `wordmark`, Martian Mono 600), with the gap equal to half the mark's width and the mark at about 1.6× the wordmark's cap height. Clear space on every side: the chip's width. Don't recolour, rotate, outline or add effects, and don't put the light mark on dark grounds.

## Colour — Kiln

Smalt on neutral graphite, with kiln orange for commits and focus. Every pairing below was checked with the WCAG 2 contrast formula, in both themes.

**Readability rules**

1. `text` ≥ 12:1, `text-2` ≥ 7:1 (AAA), `text-3` ≥ 4.5:1, on both `bg` and `surface`.
2. Every `syn-*` token ≥ 5:1 on `code-bg`, comments included.
3. Dark theme is off-white on graphite (`#E9EBF0` on `#14171F`), never `#FFF` on `#000`.
4. `kiln-500` and `smalt-300` are fills only: they fail text contrast on light grounds.
5. Status is never colour alone: `success`, `warning` and `danger` always come with an icon and a word.
6. `danger` is crimson, not orange, so it is never confused with `accent`.
7. Focus is a 2px `focus` ring with a 2px offset (≥ 7:1 against `bg` in both themes).

Roles: `primary` for the one main action per view; `link` for links (underlined in body copy); `accent` for commit/write emphasis; `border` for hairlines only.

## Type

- **Geist** (`--font-sans`): headings and body. Headings are Geist 700 with tight negative tracking; body is 17px / 1.6, at most 70 characters a line.
- **Martian Mono** (`--font-brand`): the wordmark, eyebrows, breadcrumbs and labels. Short strings only; never paragraphs or code blocks.
- **Geist Mono** (`--font-mono`): all code, 15px / 1.6 in blocks.

All three are Google Fonts (OFL). Load them with:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700&family=Geist+Mono:wght@400;500&family=Martian+Mono:wght@400;600&display=swap" rel="stylesheet">
```

## Iconography

The icon style is not chosen yet. Components here use a 24px-grid outline style (1.75–2.5px round strokes) as a placeholder, and status icons are drawn in their status colour.

## Tokens

`tokens/tokens.json` is the source of truth. `tokens/tokens.css` is generated from it (`python3 scripts/build_tokens.py`) and exposes every token as a CSS custom property: light theme on `:root`, dark under `prefers-color-scheme: dark` or `data-theme="dark"`, plus a class per type style (`.h1`, `.body`, `.code` and so on).

## Components

`components/` holds `Button`, `StatusBadge`, `CodeBlock` and `Wordmark` as static HTML and CSS references built on `tokens.css`. Open any `preview.html` in a browser; it follows the system's light or dark setting. There is no JavaScript bundle yet.

## Docs theme

`themes/vitepress/` is the VitePress theme used by smaltdb.dev: the Kiln palette mapped onto VitePress's variables, the type rules, and Shiki code themes built from the `syn-*` tokens.
