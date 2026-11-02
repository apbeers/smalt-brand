"""Outline the smaltdb wordmark and lockup into SVG paths.

Usage: python3 scripts/wordmark.py <MartianMono[wdth,wght].ttf> <output-dir>

Writes wordmark.svg, wordmark-on-dark.svg, lockup.svg and lockup-on-dark.svg.
Martian Mono 600 at width 112.5, tracking -0.06em; "alt" in smalt.
Requires fonttools (pip install fonttools).
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

src, outdir = sys.argv[1], sys.argv[2]
f = instantiateVariableFont(TTFont(src), {"wght": 600, "wdth": 112.5})
gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
cap = f['OS/2'].sCapHeight; xh = f['OS/2'].sxHeight
SIZE = 100.0; s = SIZE/upm; track = -0.06*SIZE

def word(x0, base):
    parts = []  # (segment, path)
    x = x0; bp = BoundsPen(gs)
    for seg, text in (("ink","sm"),("alt","alt"),("ink","db")):
        sp = SVGPathPen(gs)
        for ch in text:
            g = cmap[ord(ch)]
            t = (s,0,0,-s,x,base)
            gs[g].draw(TransformPen(sp,t)); gs[g].draw(TransformPen(bp,t))
            x += gs[g].width*s + track
        parts.append((seg, sp.getCommands()))
    return parts, bp.bounds

MARK = ('<path d="M14 18h18v10h14v24a6 6 0 0 1-6 6H14a6 6 0 0 1-6-6V24a6 6 0 0 1 6-6z" fill="{body}"/>'
        '<rect x="38" y="8" width="16" height="16" rx="3" fill="{chip}"/>')
themes = {"light": dict(ink="#151922", alt="#003399", body="#003399", chip="#7B97D4"),
          "dark":  dict(ink="#E9EBF0", alt="#9DB4F5", body="#9DB4F5", chip="#D6E0F3")}
base = 200.0
capH = cap*s
for lockup in (False, True):
    markH = 1.6*capH if lockup else 0
    markW = markH  # mark viewBox is square
    gap = markW/2 if lockup else 0
    _, (bx,_,_,_) = word(0, base)
    artR = 54/64*markW; artW = 46/64*markW
    x0 = artR + (artW/2 if lockup else 0) - bx
    parts, (xmin,ymin,xmax,ymax) = word(x0, base)
    capTop = base - capH
    my = capTop + capH/2 - markH/2  # mark centred on cap height
    top = min(ymin, my) ; bot = max(ymax, my+markH)
    left = 8/64*markW if lockup else xmin
    pad = 0.12*SIZE
    vx, vy, vw, vh = left-pad, top-pad, (xmax-left)+2*pad, (bot-top)+2*pad
    for th, c in themes.items():
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx:.2f} {vy:.2f} {vw:.2f} {vh:.2f}" width="{vw*1.6:.0f}" height="{vh*1.6:.0f}" role="img" aria-label="smaltdb">']
        if lockup:
            sc = markH/64
            out.append(f'<g transform="translate(0 {my:.2f}) scale({sc:.4f})">' + MARK.format(**c) + '</g>')
        for seg, d in parts:
            out.append(f'<path fill="{c[seg]}" d="{d}"/>')
        out.append('</svg>')
        name = ("lockup" if lockup else "wordmark") + ("-on-dark" if th=="dark" else "") + ".svg"
        open(f"{outdir}/{name}","w").write("".join(out))
        print(name, round(vw), round(vh))
