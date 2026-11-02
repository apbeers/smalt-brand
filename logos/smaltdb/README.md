# smaltdb logos

The Grain mark: a ground-glass particle (`smalt-700`, `#003399`) and its chip (`smalt-300`, `#7B97D4`).

| File | Use |
| --- | --- |
| `lockup.svg`, `lockup-on-dark.svg` | Mark + wordmark, outlined. README headers, docs nav, slides. |
| `wordmark.svg`, `wordmark-on-dark.svg` | Wordmark alone; `alt` in `#003399` (light) or `#9DB4F5` (dark), the rest in `#151922` / `#E9EBF0`. |
| `grain-mark.svg`, `grain-mark-on-dark.svg` | The mark alone. Dark version: `#9DB4F5` body, `#D6E0F3` chip. |
| `app-icon.svg` | A smalt tile with the mark knocked out in `#F5F6F8`. App and PWA icons, avatars. |
| `favicon-32.svg`, `favicon-16.svg` | Browser tabs. The 16 px version drops the notch so it holds at that size. |

The `-on-dark` files are transparent with light ink, so they look blank in light-background previews. That's expected.

The wordmark files are Martian Mono 600 (width 112.5) converted to paths, so they need no font. Regenerate them with `scripts/wordmark.py`.

Don't recolour, rotate, outline or add effects, and keep the light files off dark backgrounds.
