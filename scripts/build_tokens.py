#!/usr/bin/env python3
"""Generate tokens/tokens.css from tokens/tokens.json.

Usage: python3 scripts/build_tokens.py

Light theme on :root and [data-theme="light"]; dark theme on [data-theme="dark"]
and, unless a page opts into light, under prefers-color-scheme: dark.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tokens = json.loads((ROOT / "tokens" / "tokens.json").read_text())

themes = [t["id"] for t in tokens["color"]["themes"]]
first = themes[0]
ALIAS = re.compile(r"^\{([A-Za-z0-9_.-]+)\}$")


def css_value(v):
    m = ALIAS.match(v) if isinstance(v, str) else None
    return f"var(--{m.group(1)})" if m else v


def colour_block(theme):
    lines = []
    for t in tokens["color"]["tokens"]:
        v = t["value"]
        if isinstance(v, dict):
            v = v.get(theme, v.get(first))
        elif theme != first:
            continue  # theme-independent: declared once on the base theme
        lines.append(f"  --{t['name']}: {css_value(v)};")
    return "\n".join(lines)


def static_block():
    lines = []
    for family in ("spacing", "radius"):
        for t in tokens.get(family, {}).get("tokens", []):
            lines.append(f"  --{t['name']}: {t['value']};")
    for key, stack in tokens["type"]["families"].items():
        lines.append(f"  --font-{key}: {stack};")
    return "\n".join(lines)


def type_classes():
    out = []
    for group in tokens["type"]["groups"]:
        for s in group["styles"]:
            fam = s.get("family", group["family"])
            props = [f"font-family: var(--font-{fam})", f"font-size: {s['fontSize']}",
                     f"line-height: {s['lineHeight']}", f"font-weight: {s['fontWeight']}"]
            if "letterSpacing" in s:
                props.append(f"letter-spacing: {s['letterSpacing']}")
            out.append(f".{s['name']} {{ " + "; ".join(props) + "; }")
    return "\n".join(out)


dark = [t for t in themes if t != first]
parts = [
    f"/* {tokens['name']} — generated from tokens/tokens.json by scripts/build_tokens.py. Do not edit by hand. */",
    f':root, [data-theme="{first}"] {{\n{colour_block(first)}\n}}',
]
for t in dark:
    parts.append(f'[data-theme="{t}"] {{\n{colour_block(t)}\n}}')
    parts.append(f'@media (prefers-color-scheme: {t}) {{\n  :root:not([data-theme="{first}"]) {{\n'
                 + "\n".join("  " + l for l in colour_block(t).splitlines()) + "\n  }\n}")
parts.append(f":root {{\n{static_block()}\n}}")
parts.append(type_classes())
(ROOT / "tokens" / "tokens.css").write_text("\n\n".join(parts) + "\n")
print("wrote tokens/tokens.css")
