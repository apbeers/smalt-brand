# How the brand was chosen

A record of the brand work for smaltdb, in order, so later changes can see what was already tried and why.

## Inputs

- **The pigment.** Smalt is cobalt-coloured potash glass ground into powder, `#003399` (sRGB 0, 51, 153). Finer grinds read paler, which became the tonal scale (`smalt-900` → `smalt-100`).
- **The name.** smaltdb also reads as **sm**all **alt**ernate **d**ata**b**ase.
- **The product.** An embedded SQL database for the browser: OPFS storage, Web Worker execution, WAL-durable commits. Speed is treated as a feature. The audience is coders.

## Round 1: three complete directions

| Direction | Idea | Outcome |
| --- | --- | --- |
| A · Ground Glass | Faceted shard mark, serif display, light-first | The pigment idea carried forward; the serif did not. |
| B · Fast Path | Slanted-bar motion mark, Geist, dark-first, cyan accent | Geist carried forward. |
| C · Pane | Page-grid mark, mono wordmark, orange accent | Mono wordmark and orange accent carried forward. |

Feedback: complete directions made it hard to see the options. Round 2 split them into separate categories to mix and match.

## Round 2: alternatives by category

Six marks (Alt key, ⌥ glyph, alternate route, grain, small cube, wordmark only), four palettes, four type pairings, three icon styles and six taglines.

Feedback that shaped round 3:

- Don't pick fights with other databases. Dropped "without the WASM" and anything defined against another engine.
- Liked Ground Glass, Alt key and Alternate route.
- Liked Geist 700 and Martian Mono; monospace suits the coder audience.
- Refine the colours, with a focus on readability.

## Round 3: refined, and the picks

| Category | Options | **Picked** |
| --- | --- | --- |
| Tagline | T1–T5 | **T3: "Small. Alternate. Fast."** |
| Mark | Ground Glass, Grain, Alt key, Alternate route | **Grain:** a ground-glass particle and the chip it shed |
| Type | S1 mono-forward, S2 Geist-forward | **S2:** Geist 700 headings, Martian Mono for wordmark and labels, Geist Mono for code |
| Palette | P1 Ground Glass, P2 Hot Path, P3 Kiln | **P3 Kiln:** smalt on neutral graphite, kiln orange for commits and focus |

### Readability rules applied to every palette

1. Body text ≥ 12:1, secondary ≥ 7:1 (AAA), tertiary ≥ 4.5:1, on both ground and surface.
2. Every syntax colour ≥ 5:1 on its code background, comments included.
3. Dark mode is off-white on graphite, never `#FFF` on `#000`.
4. Colours that fail text contrast (`kiln-500`, `smalt-300`) are fills only.
5. Status is never colour alone: icon plus word.
6. `danger` is crimson, kept apart from the orange accent. It was orange-red until the check caught that the two were too close.
7. A 2px focus ring, ≥ 3:1 against the ground.

All ratios were computed with the WCAG 2 relative-luminance formula and are recorded in each token's `usage` note.

## After the picks

- **Positioning line:** "A fast alternative database for the browser, written in TypeScript." It was first "pure JavaScript", but the source is TypeScript and "pure JavaScript" undersold the first-class types. "No WASM" was rejected as framing against other engines.
- **Voice rule added:** describe what smaltdb is, never what it isn't.
- **Outlined wordmark:** GitHub strips inline styles from Markdown, so the coloured `alt` can only appear in a README as an image. The wordmark and lockup are Martian Mono 600 converted to paths (`scripts/wordmark.py`), switched for light and dark with `<picture>`.
- **Cover simplified:** an early design-system cover scattered grain-sized squares to suggest powder. It read as noise and was replaced by the oversized mark alone.
- **Docs site:** smaltdb.dev uses the VitePress theme in `themes/vitepress/`, with the wordmark in the hero.

## Still open

- **Icon style.** Not chosen. Components use a 24px-grid outline style as a placeholder.
- **Social preview card** for links shared on GitHub and social sites.
- **Research pages on smaltdb.dev** include benchmark comparisons with other engines. The no-comparisons rule covers marketing copy; whether those pages stay on the public site is undecided.
