"""Tiny helpers for drawing pixel-art SVGs out of plain rectangles.

Everything is rects, so the SVGs render the same inside GitHub's README
(no fonts, scripts or external files needed).
"""
from pixelfont import GLYPHS

# Palette shared by every graphic on the profile
BG = "#241b1a"        # outer dark
PANEL = "#302320"     # inner panel
EDGE = "#ad7750"      # outer frame
EDGE2 = "#76503b"     # inner frame
GOLD = "#d99a52"
CREAM = "#f2dfbc"
TAN = "#e6c99f"
WOOD = "#49312a"
SLOT_OUT = "#8c5a3a"
SLOT_IN = "#3b2620"
INK = "#1d130f"


def grid(rows, palette, x, y, s):
    """Rects for an ASCII sprite. Characters missing from `palette` are transparent."""
    out = []
    for j, row in enumerate(rows):
        i = 0
        while i < len(row):
            c = row[i]
            if c in palette:
                k = i
                while k < len(row) and row[k] == c:
                    k += 1
                out.append(f'<rect x="{x + i * s}" y="{y + j * s}" width="{(k - i) * s}" height="{s}" fill="{palette[c]}"/>')
                i = k
            else:
                i += 1
    return "".join(out)


def text_width(t, s):
    return len(t) * 8 * s - s


def text(t, x, y, s, color, anchor="start"):
    """Pixel text (cap height = 7*s; commas dip one row lower). `x` is the left edge, centre or right edge by anchor."""
    w = text_width(t, s)
    if anchor == "middle":
        x -= w // 2
    elif anchor == "end":
        x -= w
    rows = ["".join(GLYPHS[c][r] for c in t) for r in range(8)]  # row 8 holds the comma tail
    out = []
    for j, row in enumerate(rows):
        i = 0
        while i < len(row):
            if row[i] == "#":
                k = i
                while k < len(row) and row[k] == "#":
                    k += 1
                out.append(f'<rect x="{x + i * s}" y="{y + j * s}" width="{(k - i) * s}" height="{s}"/>')
                i = k
            else:
                i += 1
    return f'<g fill="{color}">' + "".join(out) + "</g>"


def outlined(rows, pad_char=".", ink="o"):
    """Add a 1px dark outline around every filled pixel of an ASCII sprite."""
    h, w = len(rows), len(rows[0])
    filled = [[rows[y][x] != pad_char for x in range(w)] for y in range(h)]
    res = [list(r) for r in rows]
    for y in range(h):
        for x in range(w):
            if filled[y][x]:
                continue
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < h and 0 <= xx < w and filled[yy][xx]:
                        res[y][x] = ink
    return ["".join(r) for r in res]


def corners(x0, y0, x1, y1, color=GOLD, inset=16, size=45, t=6):
    """The gold L-shaped corner brackets used on every frame."""
    a, b = x0 + inset, y0 + inset
    c, d = x1 - inset, y1 - inset
    return (f'<path d="M{a} {b}h{size}v{t}H{a + t}v{size - t * 5}h-{t}z'
            f'M{c} {b}h-{size}v{t}h{size - t}v{size - t * 5}h{t}z'
            f'M{a} {d}h{size}v-{t}H{a + t}v-{size - t * 5}h-{t}z'
            f'M{c} {d}h-{size}v-{t}h{size - t}v-{size - t * 5}h{t}z" fill="{color}"/>')


def frame(w, h):
    """Dark wooden board frame (same look as the existing profile graphics)."""
    return (f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" fill="{BG}" stroke="{EDGE}" stroke-width="3"/>'
            f'<rect x="13" y="13" width="{w - 26}" height="{h - 26}" fill="{PANEL}" stroke="{EDGE2}" stroke-width="2"/>'
            + corners(0, 0, w, h))


def slot(x, y, size=52):
    """An inventory slot like the ones in the Stardew farm card."""
    return (f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{SLOT_OUT}"/>'
            f'<rect x="{x + 3}" y="{y + 3}" width="{size - 6}" height="{size - 6}" fill="{SLOT_IN}"/>'
            f'<rect x="{x}" y="{y}" width="{size}" height="3" fill="#b8794a"/>'
            f'<rect x="{x}" y="{y}" width="3" height="{size}" fill="#b8794a"/>')


def svg(w, h, label, body):
    from xml.sax.saxutils import escape
    label = escape(label, {'"': "&quot;"})
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" shape-rendering="crispEdges" '
            f'role="img" aria-label="{label}">{body}</svg>\n')
