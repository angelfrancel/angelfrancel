"""Render the ANALYTICS board (total contributions, current streak, longest streak).

Run in GitHub Actions with GITHUB_TOKEN and GITHUB_USERNAME set:
    python3 scripts/generate_analytics.py --output profile/analytics.svg
Use --sample for illustrative numbers (local preview only, never the live file).
"""
import argparse
import datetime as dt
import math
import os
from pathlib import Path

import ghdata
import pixelkit as pk
import sprites as sp


def streaks(days, today):
    """(current, longest). A streak still counts if today has no contributions yet."""
    longest = run = 0
    prev = None
    for d in sorted(days):
        if days[d] > 0:
            run = run + 1 if prev and (d - prev).days == 1 else 1
            longest = max(longest, run)
            prev = d
    cur, d = 0, today
    if days.get(d, 0) == 0:
        d -= dt.timedelta(days=1)
    while days.get(d, 0) > 0:
        cur += 1
        d -= dt.timedelta(days=1)
    return cur, longest


def fmt(n):
    return f"{n:,}"


W, H = 920, 330
COLS = [153, 460, 767]  # column centres


def ring(cx, cy, r):
    out = []
    for k in range(0, 360, 6):
        a = math.radians(k)
        x, y = round(cx + r * math.cos(a)) - 2, round(cy + r * math.sin(a)) - 2
        out.append(f'<rect x="{x}" y="{y}" width="4" height="4"/>')
    ring_svg = f'<g fill="{pk.GOLD}">' + "".join(out) + "</g>"
    leaves = []
    for side in (-1, 1):
        for k in range(-58, 59, 17):
            a = math.radians(k if side == 1 else 180 - k)
            x, y = cx + (r + 10) * math.cos(a), cy + (r + 10) * math.sin(a)
            leaves.append(pk.grid(sp.LEAF, sp.LEAF_PAL, round(x) - 6, round(y) - 6, 3))
    return ring_svg + "".join(leaves)


def render(total, current, longest):
    b = [pk.frame(W, H)]
    # banner
    b.append(f'<rect x="300" y="26" width="320" height="56" fill="{pk.WOOD}" stroke="{pk.GOLD}" stroke-width="3"/>')
    b.append(pk.grid(sp.BARS, sp.BARS_PAL, 333, 44, 3))
    b.append(pk.text("ANALYTICS", 373, 42, 3, pk.CREAM))
    for x in (258, 642):
        b.append(pk.grid(sp.LEAF, sp.LEAF_PAL, x, 40, 5))
        b.append(pk.grid(sp.LEAF, sp.LEAF_PAL, x + (-20 if x < 400 else 28), 56, 3))
    # dividers
    b.append(f'<path d="M307 104v206M613 104v206" stroke="{pk.EDGE2}" stroke-width="2"/>')
    b.append(ring(COLS[1], 195, 90))
    cols = [
        (sp.SPROUT, sp.SPROUT_PAL, total, ["TOTAL", "CONTRIBUTIONS"]),
        (sp.FLAME, sp.FLAME_PAL, current, ["CURRENT", "STREAK"]),
        (sp.CROWN, sp.CROWN_PAL, longest, ["LONGEST", "STREAK"]),
    ]
    for cx, (icon, pal, value, label) in zip(COLS, cols):
        b.append(pk.grid(icon, pal, cx - 32, 118, 4))
        s = 4 if len(fmt(value)) * 32 <= 240 else 3
        b.append(pk.text(fmt(value), cx, 194, s, pk.CREAM, "middle"))
        b.append(pk.text(label[0], cx, 238, 2, pk.TAN, "middle"))
        b.append(pk.text(label[1], cx, 260, 2, pk.TAN, "middle"))
    return pk.svg(W, H, f"GitHub analytics: {fmt(total)} total contributions, {current} day current streak, {longest} day longest streak", "".join(b))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--sample", action="store_true", help="illustrative numbers for the local preview")
    args = ap.parse_args()
    if args.sample:
        total, cur, longest = 1284, 12, 47
    else:
        days, total = ghdata.fetch_all(os.environ["GITHUB_USERNAME"], os.environ["GITHUB_TOKEN"])
        if not days:
            raise ValueError("No contribution days were returned")
        today = min(ghdata.today(), max(days))
        cur, longest = streaks(days, today)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(render(total, cur, longest), encoding="utf-8")


if __name__ == "__main__":
    main()
