"""Rebuild the static graphics (no network needed):

    python3 scripts/build_assets.py

Writes assets/welcome.svg (header card), assets/skills.svg, assets/projects-heading.svg,
assets/project-*.svg (one quest card per project) and the sample previews used by PREVIEW.html.
Edit the constants below to change the header text, skills layout or featured projects.
"""
import base64
from pathlib import Path

import character
import generate_analytics
import generate_calendar
import pixelkit as pk
import skillicons
import sprites as sp

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

NAME = "ANGEL FRANCEL"
CLASS_TITLE = "CS STUDENT"
CLASS_SUB = "LEARNING FULL STACK DEVELOPMENT"
QUEST_TITLE = "BUILDING TAPONSUSI & CONTEXTGUARD"
QUEST_SUB = "JAVA, SPRING BOOT"

PORTRAIT_IMAGE = ASSETS / "portrait.png"
PORTRAIT_KEEP_SCENE = True

SKILL_PANELS = [
    ("BACKEND", [
        "Java", 
        "Spring Boot", 
        "Spring MVC", 
        "Spring Data JPA", 
        "Hibernate", 
        # "Spring AI"
    ]),
    ("DATA & APIS", [
        # "SQL", 
        "PostgreSQL", 
        "REST APIs", 
        # "Swagger UI", 
        # "Postman"
    ]),
    ("TESTING & TOOLS", [
        "JUnit 5", 
        # "Mockito", 
        "Git", 
        "Maven", 
        "IntelliJ IDEA", 
        "VS Code"
    ]),
]

# PROJECTS = [
#     {"name": "TaponSusi", "file": "project-taponsusi.svg", "url": "https://github.com/angelfrancel/taponsusi",
#      "desc": "An item availability and reservation system with buyer notifications when stock returns.",
#      "tags": ["RESERVATIONS", "STOCK ALERTS"]},
#     {"name": "ContextGuard", "file": "project-contextguard.svg", "url": "https://github.com/angelfrancel/contextguard",
#      "desc": "An MCP gateway for exploring privacy and policy checks before requests reach connected tools.",
#      "tags": ["MCP", "PRIVACY", "POLICY CHECKS"]},
#     {"name": "ContractRescue", "file": "project-contractrescue.svg", "url": "https://github.com/angelfrancel/contractrescue",
#      "desc": "An IBM Bob powered workflow for detecting, resolving, and verifying contradictory API contracts.",
#      "tags": ["IBM BOB", "API CONTRACTS"]},
# ]


def wrap(text, max_chars):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if len(trial) <= max_chars:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    return lines + [cur] if cur else lines


def portrait_background(x, y, w, h):
    """Stardew-style sky, clouds, hills and grass behind the character."""
    out = []
    bands = ["#5aa9ea", "#68b4ee", "#7bc0f1", "#8ecbf3", "#a3d6f5"]
    sky_h = int(h * 0.62)
    for i, c in enumerate(bands):
        y0 = y + i * sky_h // len(bands)
        out.append(f'<rect x="{x}" y="{y0}" width="{w}" height="{sky_h // len(bands) + 1}" fill="{c}"/>')
    cloud = ["..ww..", ".wwwww", "wwwwwww"]
    for cx, cy in ((x + 10, y + 34), (x + w - 52, y + 70)):
        out.append(pk.grid(cloud, {"w": "#f4f9ff"}, cx, cy, 6))
    out.append(f'<rect x="{x}" y="{y + sky_h - 22}" width="{w}" height="26" fill="#4f9a7c"/>')
    out.append(f'<rect x="{x}" y="{y + sky_h - 8}" width="{w}" height="14" fill="#3f8a63"/>')
    gy = y + sky_h
    out.append(f'<rect x="{x}" y="{gy}" width="{w}" height="{h - sky_h}" fill="#5eaa3e"/>')
    for i, gx in enumerate(range(x, x + w, 18)):
        out.append(f'<rect x="{gx}" y="{gy + 12 + (i % 4) * 24}" width="12" height="4" fill="#4d9632"/>')
        out.append(f'<rect x="{gx + 8}" y="{gy + 4 + (i % 3) * 28}" width="6" height="4" fill="#78c150"/>')
    return "".join(out)


def slot_with(icon_name, x, y):
    rows, pal = sp.SLOT_ICONS[icon_name]
    return pk.slot(x, y) + pk.grid(pk.outlined(rows), dict(pal, o=pk.INK), x + 8, y + 8, 3)


def welcome():
    W, H = 920, 280
    b = [pk.frame(W, H)]
    ys = [38, 114, 190]
    for icon, y in zip(("ring", "bracelet", "sneakers"), ys):
        b.append(slot_with(icon, 34, y))
    for icon, y in zip(("earbuds", "top", "pants"), ys):
        b.append(slot_with(icon, 264, y))
    # portrait card with the standing Stardew-style farmer
    fx, fy, fw, fh = 98, 20, 154, 240
    b.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" fill="{pk.SLOT_OUT}"/>')
    b.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="4" fill="#b8794a"/><rect x="{fx}" y="{fy}" width="4" height="{fh}" fill="#b8794a"/>')
    ix, iy, iw, ih = fx + 6, fy + 6, fw - 12, fh - 12
    clip = f'<clipPath id="pf"><rect x="{ix}" y="{iy}" width="{iw}" height="{ih}"/></clipPath>'
    if PORTRAIT_IMAGE.exists():
        data = base64.b64encode(PORTRAIT_IMAGE.read_bytes()).decode()
        if len(data) > 600_000:
            print("Warning: portrait.png is large; keep it under ~400 KB so the header loads quickly.")
        fit = "xMidYMax meet" if PORTRAIT_KEEP_SCENE else "xMidYMid slice"
        scene = portrait_background(ix, iy, iw, ih) if PORTRAIT_KEEP_SCENE else ""
        pad = 8 if PORTRAIT_KEEP_SCENE else 0
        figure = (f'<image x="{ix}" y="{iy}" width="{iw}" height="{ih - pad}" preserveAspectRatio="{fit}" '
                  f'style="image-rendering:pixelated" href="data:image/png;base64,{data}"/>')
    else:
        sprite = character.farmer()
        s = 5
        sx = ix + (iw - len(sprite[0]) * s) // 2
        sy = iy + ih - 14 - len(sprite) * s
        scene = portrait_background(ix, iy, iw, ih)
        figure = (f'<rect x="{sx + 14}" y="{sy + len(sprite) * s - 6}" width="{(len(sprite[0]) - 6) * s - 10}" height="10" fill="#3f8a3a" opacity=".55"/>'
                  f'{pk.grid(sprite, character.PALETTE, sx, sy, s)}')
    b.append(clip)
    b.append(f'<g clip-path="url(#pf)">{scene}{figure}</g>')
    # text block
    # text block
    tx = 346

    b.append(pk.slot(tx, 34))
    b.append(pk.grid(sp.STAR, sp.STAR_PAL, tx + 5, 42, 3))
    b.append(pk.text(NAME, tx + 68, 46, 4, pk.CREAM))

    b.append(f'<rect x="{tx}" y="100" width="540" height="3" fill="{pk.EDGE2}"/>')

    b.append(pk.text("CLASS", tx, 114, 2, pk.GOLD))
    b.append(pk.text(CLASS_TITLE, tx, 134, 2, pk.CREAM))
    b.append(pk.text(CLASS_SUB, tx, 160, 2, pk.TAN))

    b.append(pk.text("CURRENT QUEST", tx, 198, 2, pk.GOLD))
    b.append(pk.text(QUEST_TITLE, tx, 218, 2, pk.CREAM))

    if QUEST_SUB:
        b.append(pk.text(QUEST_SUB, tx, 246, 2, pk.TAN))
    return pk.svg(W, H, f"{NAME.title()}. Class: {CLASS_TITLE.title()}, {CLASS_SUB.title()}. Current quest: {QUEST_TITLE.title()}.", "".join(b))


def skills():
    W, H = 920, 540
    b = [pk.frame(W, H)]
    b.append(pk.grid(sp.BOOK, sp.BOOK_PAL, 40, 28, 3))
    b.append(pk.text("SKILLS", 104, 38, 4, pk.CREAM))
    b.append(pk.text("TOOLS FOR THE NEXT QUEST.", 852, 46, 2, pk.TAN, "end"))
    b.append(pk.text(">", 886, 41, 3, pk.GOLD, "end"))
    pw, pitch = 276, 62
    for col, (title, names) in enumerate(SKILL_PANELS):
        px = 34 + col * (pw + 12)
        b.append(f'<rect x="{px}" y="100" width="{pw}" height="416" fill="#2a1f1c" stroke="{pk.EDGE2}" stroke-width="2"/>')
        b.append(f'<rect x="{px}" y="100" width="{pw}" height="30" fill="{pk.WOOD}" stroke="{pk.EDGE2}" stroke-width="2"/>')
        b.append(pk.text(title, px + pw // 2, 108, 2, pk.GOLD, "middle"))
        for row in range(6):
            y = 142 + row * pitch
            b.append(pk.slot(px + 10, y, 56))
            if row >= len(names):
                continue
            name = names[row]
            pal = dict(skillicons.PAL, o=pk.INK)
            b.append(f'<g><title>{name}</title>{pk.grid(skillicons.build(name), pal, px + 14, y + 4, 3)}</g>')
            lines = wrap(name.upper(), 12)
            ty = y + 21 if len(lines) == 1 else y + 12
            for k, line in enumerate(lines):
                b.append(pk.text(line, px + 78, ty + k * 18, 2, pk.CREAM))
    alt = "Skills: " + "; ".join(f"{t.title()}: {', '.join(n)}" for t, n in SKILL_PANELS)
    return pk.svg(W, H, alt, "".join(b))


def projects_heading():
    W, H = 920, 110
    b = [pk.frame(W, H)]
    b.append(f'<rect x="226" y="26" width="468" height="58" fill="{pk.WOOD}" stroke="{pk.GOLD}" stroke-width="3"/>')
    b.append(pk.text("FEATURED PROJECTS", 460, 45, 3, pk.CREAM, "middle"))
    for x in (186, 716):
        b.append(pk.grid(sp.STAR, sp.STAR_PAL, x, 42, 2))
    return pk.svg(W, H, "Featured Projects", "".join(b))


def project_card(i, p):
    W, H = 920, 214
    b = [pk.frame(W, H)]
    rows, pal = sp.PROJECT_ICONS[p["name"]]
    b.append(pk.slot(34, 40, 122))
    b.append(pk.grid(pk.outlined(rows), dict(pal, o=pk.INK), 34 + 13, 40 + 13, 6))
    x = 182
    b.append(pk.text(f"QUEST {i}", x, 32, 2, pk.GOLD))
    b.append(pk.text(p["name"].upper(), x, 54, 3, pk.CREAM))
    for k, line in enumerate(wrap(p["desc"].upper(), 43)[:3]):
        b.append(pk.text(line, x, 100 + k * 20, 2, pk.TAN))
    cx = x
    for tag in p["tags"]:
        tw = pk.text_width(tag, 2) + 16
        b.append(f'<rect x="{cx}" y="172" width="{tw}" height="24" fill="{pk.WOOD}" stroke="{pk.EDGE2}" stroke-width="2"/>')
        b.append(pk.text(tag, cx + 8, 178, 2, pk.CREAM))
        cx += tw + 10
    label = "VIEW REPO >"
    bw = pk.text_width(label, 2) + 28
    b.append(f'<rect x="{886 - bw}" y="170" width="{bw}" height="28" fill="{pk.WOOD}" stroke="{pk.GOLD}" stroke-width="3"/>')
    b.append(pk.text(label, 886 - bw + 14, 177, 2, pk.GOLD))
    return pk.svg(W, H, f"{p['name']}: {p['desc']}", "".join(b))


if __name__ == "__main__":
    out = {"welcome.svg": welcome(), "skills.svg": skills(), "projects-heading.svg": projects_heading()}
    # for i, p in enumerate(PROJECTS, 1):
    #     out[p["file"]] = project_card(i, p)
    for name, svg in out.items():
        (ASSETS / name).write_text(svg, encoding="utf-8")
    (ASSETS / "analytics-preview.svg").write_text(generate_analytics.render(1284, 12, 47), encoding="utf-8")
    today = generate_calendar.ghdata.today()
    import datetime as dt
    (ASSETS / "calendar-preview.svg").write_text(
        generate_calendar.render(generate_calendar.sample_days(today), today, dt.date(today.year - 2, 1, 1)), encoding="utf-8")
    print("Rebuilt:", ", ".join(list(out) + ["analytics-preview.svg", "calendar-preview.svg"]))
