"""Render the Stardew Valley style CALENDAR for the current month.

Each day shows a crop that grows with that day's GitHub contributions
(none -> sprout -> young plant -> flower -> ripe pumpkin).

Run in GitHub Actions with GITHUB_TOKEN and GITHUB_USERNAME set:
    python3 scripts/generate_calendar.py --output profile/calendar.svg
Use --sample for illustrative numbers (local preview only, never the live file).
"""
import argparse
import calendar
import datetime as dt
import os
import random
from pathlib import Path

import ghdata
import pixelkit as pk
import sprites as sp

W, H = 920, 468
GX, GY = 34, 126              # top-left of the day grid
CW, CH = 86, 52               # cell size
PANEL_X, PANEL_W = 656, 230
MONTHS = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
          "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
ABBR = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
WEEKDAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
INK_DATE, INK_TODAY, INK_FUTURE = "#5c3a24", "#b3261e", "#a58a63"


def level(n):
    return 0 if n <= 0 else 1 if n == 1 else 2 if n <= 3 else 3 if n <= 6 else 4


def cell(x, y, d, count, state):
    """One day tile. state: past | today | future."""
    fill = {"past": "#efd9a8", "today": "#f8e9b0", "future": "#cdb185"}[state]
    out = [f'<rect x="{x}" y="{y}" width="{CW - 4}" height="{CH - 4}" fill="#8c5a3a"/>',
           f'<rect x="{x + 3}" y="{y + 3}" width="{CW - 10}" height="{CH - 10}" fill="{fill}"/>',
           f'<rect x="{x + 3}" y="{y + 3}" width="{CW - 10}" height="2" fill="#fff6d8" opacity=".55"/>']
    if state == "today":
        out.append(f'<rect x="{x - 1}" y="{y - 1}" width="{CW - 2}" height="{CH - 2}" fill="none" stroke="{pk.GOLD}" stroke-width="3"/>')
    color = {"past": INK_DATE, "today": INK_TODAY, "future": INK_FUTURE}[state]
    out.append(pk.text(str(d), x + 9, y + 9, 2, color))
    lv = level(count) if state != "future" else 0
    if lv:
        out.append(pk.grid(sp.CROPS[lv - 1], sp.CROP_PAL, x + CW - 4 - 3 - 33, y + 9, 3))
    return "".join(out)


def render(days, today, created):
    first = dt.date(today.year, today.month, 1)
    dim = calendar.monthrange(today.year, today.month)[1]
    start_col = first.weekday()
    season = sp.SEASON_BY_MONTH[today.month]
    year_no = max(1, today.year - created.year + 1)

    month_days = {d: n for d, n in days.items() if d.year == today.year and d.month == today.month and d <= today}
    total = sum(month_days.values())
    active = sum(1 for n in month_days.values() if n > 0)
    best_day, best = (max(month_days.items(), key=lambda kv: kv[1]) if month_days else (None, 0))

    b = [pk.frame(W, H)]
    # header banner: season icon, month, season + year
    b.append(f'<rect x="{GX}" y="28" width="{7 * CW - 4 + 2}" height="58" fill="{pk.WOOD}" stroke="{pk.GOLD}" stroke-width="3"/>')
    icon, pal = sp.SEASONS[season]
    b.append(pk.slot(GX + 10, 33, 48) + pk.grid(icon, pal, GX + 10 + 6, 33 + 6, 3))
    b.append(pk.text(MONTHS[today.month - 1], GX + 76, 43, 4, pk.CREAM))
    b.append(pk.text(f"{season}, YEAR {year_no}", GX + 7 * CW - 4 - 8, 50, 2, pk.GOLD, "end"))
    # weekday strip
    b.append(f'<rect x="{GX}" y="94" width="{7 * CW - 4 + 2}" height="24" fill="{pk.WOOD}"/>')
    for i, name in enumerate(WEEKDAYS):
        b.append(pk.text(name, GX + i * CW + (CW - 4) // 2, 100, 2, pk.TAN, "middle"))
    # day grid
    for r in range(6):
        for c in range(7):
            x, y = GX + c * CW, GY + r * CH
            n = r * 7 + c - start_col + 1
            if n < 1 or n > dim:
                b.append(f'<rect x="{x}" y="{y}" width="{CW - 4}" height="{CH - 4}" fill="#2b1f1b"/>')
                continue
            d = dt.date(today.year, today.month, n)
            state = "today" if d == today else "future" if d > today else "past"
            b.append(cell(x, y, n, days.get(d, 0), state))
    # side panel
    px = PANEL_X + 12
    b.append(f'<rect x="{PANEL_X}" y="94" width="{PANEL_W}" height="{GY + 6 * CH - 94 - 4}" fill="#3b2a23" stroke="{pk.EDGE2}" stroke-width="2"/>')
    b.append(pk.text("THIS MONTH", px, 106, 2, pk.GOLD))
    b.append(pk.text(f"{total:,}", px, 130, 4, pk.CREAM))
    b.append(pk.text("CONTRIBUTIONS", px, 168, 2, pk.TAN))
    for y in (192, 262, 352):
        b.append(f'<rect x="{px}" y="{y}" width="{PANEL_W - 24}" height="2" fill="{pk.EDGE2}"/>')
    b.append(pk.text("ACTIVE DAYS", px, 204, 2, pk.GOLD))
    b.append(pk.text(f"{active}/{today.day}", px, 226, 3, pk.CREAM))
    b.append(pk.text("BEST DAY", px, 274, 2, pk.GOLD))
    if best > 0:
        b.append(pk.text(f"{ABBR[best_day.month - 1]} {best_day.day}", px, 296, 3, pk.CREAM))
        b.append(pk.text(f"{best} IN A DAY", px, 326, 2, pk.TAN))
    else:
        b.append(pk.text("NONE YET", px, 296, 3, pk.CREAM))
    b.append(pk.text("CROP GROWTH", px, 362, 2, pk.GOLD))
    for i, label in enumerate(["1", "2+", "4+", "7+"]):
        cx = px + i * 52
        b.append(pk.grid(sp.CROPS[i], sp.CROP_PAL, cx + 5, 382, 3))
        b.append(pk.text(label, cx + 20, 416, 2, pk.TAN, "middle"))
    alt = (f"Stardew style calendar for {MONTHS[today.month - 1].title()}: {total} contributions on "
           f"{active} active days, where each day's crop grows with its contributions.")
    return pk.svg(W, H, alt, "".join(b))


def sample_days(today):
    rng = random.Random(11)
    days = {}
    for n in range(1, today.day + 1):
        days[dt.date(today.year, today.month, n)] = rng.choices([0, 1, 2, 3, 5, 8, 12], [3, 3, 3, 2, 2, 1, 1])[0]
    return days


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--sample", action="store_true", help="illustrative numbers for the local preview")
    args = ap.parse_args()
    today = ghdata.today()
    if args.sample:
        days, created = sample_days(today), dt.date(today.year - 2, 1, 1)
    else:
        login, token = os.environ["GITHUB_USERNAME"], os.environ["GITHUB_TOKEN"]
        _, created = ghdata.account_info(login, token)
        days, _ = ghdata.fetch_range(login, token, dt.date(today.year, today.month, 1), today)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(render(days, today, created), encoding="utf-8")


if __name__ == "__main__":
    main()
