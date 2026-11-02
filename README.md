<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logos/smaltdb/lockup-on-dark.svg">
    <img alt="smaltdb" src="logos/smaltdb/lockup.svg" width="320">
  </picture>
</h1>

**Small. Alternative. Fast.**

Brand assets and design tokens for the smalt projects, starting with [smaltdb](https://github.com/stenhoor/smaltdb), a fast alternative database for the browser, written in TypeScript. Docs: [smaltdb.dev](https://smaltdb.dev).

## What's here

| Path | Contents |
| --- | --- |
| [`BRAND.md`](BRAND.md) | The brand book: name, voice, logo use, colour and readability rules, type. |
| [`DECISIONS.md`](DECISIONS.md) | How the brand was chosen: the options explored, what was picked and why. |
| [`tokens/tokens.json`](tokens/tokens.json) | Design tokens, the source of truth: colours (light and dark), type styles, spacing, radii. |
| [`tokens/tokens.css`](tokens/tokens.css) | The same tokens as CSS custom properties. Generated; don't edit by hand. |
| [`logos/smaltdb/`](logos/smaltdb/) | Grain mark, lockup and wordmark (light and dark), app icon, favicons. |
| [`components/`](components/) | Static HTML/CSS references: Button, StatusBadge, CodeBlock, Wordmark. |
| [`themes/vitepress/`](themes/vitepress/) | The VitePress theme and Shiki code colours used by smaltdb.dev. |
| [`scripts/`](scripts/) | `build_tokens.py` (JSON → CSS) and `wordmark.py` (outlines the wordmark). |

## At a glance

- **Palette (Kiln):** smalt `#003399` on neutral graphite, with kiln orange for commits and focus. Every text pairing meets WCAG AA or better in both themes; ratios are in `tokens.json`.
- **Type:** Geist (headings, body), Martian Mono (wordmark, labels), Geist Mono (code). All Google Fonts, OFL.
- **Voice:** describe what smaltdb is, never what it isn't; no comparisons with other databases.

## Working on it

```sh
python3 scripts/build_tokens.py                    # after editing tokens/tokens.json
python3 scripts/wordmark.py MartianMono.ttf logos/smaltdb   # after changing the wordmark
```

`wordmark.py` needs `fonttools` (`pip install fonttools`) and the Martian Mono variable font from [google/fonts](https://github.com/google/fonts/tree/main/ofl/martianmono).

## Fonts

Geist, Geist Mono and Martian Mono are licensed under the SIL Open Font License 1.1. The wordmark and lockup SVGs contain Martian Mono glyphs converted to paths.
