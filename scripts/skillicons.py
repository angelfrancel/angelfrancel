"""16x16 pixel icons for the Skills board, one per skill in the README.

Shapes are authored on a 14x14 canvas; `build()` pads them to 16x16 and adds the dark
outline. Edit a shape here, then run `python3 scripts/build_assets.py`.
"""
import math

PAL = {
    "w": "#f2dfbc", "W": "#ffffff", "r": "#e0483a", "R": "#a3281f", "O": "#f08a3c", "y": "#f2c14e",
    "g": "#6db33f", "G": "#3f7a2a", "l": "#a9d86e", "b": "#3d8fd9", "B": "#24508a", "c": "#5cc8f0",
    "p": "#a678e0", "P": "#6a3fa0", "k": "#2a2430", "s": "#c9ced6", "S": "#8d93a0", "n": "#9a6a42",
    "N": "#5c3a24", "t": "#e0bb86", "e": "#ff7aa8", "m": "#8fe3b5", "x": "#4169e1", "X": "#2c4aa8",
}
N = 14


def blank():
    return [["."] * N for _ in range(N)]


def put(c, rows, ox, oy, mapto=None):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch != "." and 0 <= oy + j < N and 0 <= ox + i < N:
                c[oy + j][ox + i] = (mapto or {}).get(ch, ch)


def disc(c, ch, cx=6.5, cy=6.5, r=6.4):
    for y in range(N):
        for x in range(N):
            if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                c[y][x] = ch


def line(c, ch, x0, y0, x1, y1, t=1):
    steps = max(abs(x1 - x0), abs(y1 - y0)) * 2 + 1
    for s in range(steps + 1):
        x = x0 + (x1 - x0) * s / steps
        y = y0 + (y1 - y0) * s / steps
        for dx in range(t):
            for dy in range(t):
                xx, yy = int(round(x)) + dx, int(round(y)) + dy
                if 0 <= xx < N and 0 <= yy < N:
                    c[yy][xx] = ch


def rows_of(c):
    return ["".join(r) for r in c]


# ---------- individual icons ----------
def java():
    c = blank()
    put(c, [
        "....r.........",
        ".....r..r.....",
        "....r..r......",
        ".....r..r.....",
        "....r..r......",
        "..............",
        ".bbbbbbbbb....",
        ".bcbbbbbbbbbb.",
        ".bcbbbbbbb..b.",
        ".bbbbbbbbb..b.",
        ".bbbbbbbbbbbb.",
        "..bbbbbbbbb...",
        "...BBBBBBB....",
        ".SSSSSSSSSSS..",
    ], 0, 0)
    return rows_of(c)


def sql():
    c = blank()
    for k in range(3):
        y = 1 + k * 4
        put(c, ["..pppppppp..", ".pllllllllp.", ".pppppppppp.", ".PppppppppP."], 1, y)
    c[12] = list("..PPPPPPPP....")[:N]
    c[12] = list(".PPPPPPPPPP...")[:N]
    return rows_of(c)


def postgres():
    c = blank()
    put(c, [
        "....xxxxxx....",
        ".XX.xxxxxx.XX.",
        "XXXXxxxxxxXXXX",
        "XXXXxkxxkxXXXX",
        "XXXXxxxxxxXXXX",
        "XXXXxxxxxxXXXX",
        ".XXXxxxxxxXXX.",
        "..XX.xxxx.XX..",
        "....WxxxxW....",
        "....WxxxxW....",
        ".....xxxx.....",
        ".....xxxX.....",
        "......xxX.....",
        ".......XX.....",
    ], 0, 0)
    return rows_of(c)


def spring_badge(glyph, ox, oy, glyph_ch="W"):
    c = blank()
    disc(c, "g")
    for j in range(N):                       # simple shading at the bottom-right
        for i in range(N):
            if c[j][i] == "g" and (i + j) >= 19:
                c[j][i] = "G"
    put(c, glyph, ox, oy, {"#": glyph_ch})
    return rows_of(c)


def spring_boot():
    return spring_badge([
        "...#...",
        ".#.#.#.",
        "#..#..#",
        "#..#..#",
        "#.....#",
        ".#...#.",
        "..###..",
    ], 3, 3)


def spring_mvc():
    return spring_badge([
        "...###...",
        "...###...",
        "..#...#..",
        ".#.....#.",
        "###...###",
        "###...###",
    ], 2, 4)


def spring_jpa():
    return spring_badge([
        ".#####.",
        "#.....#",
        "#######",
        "#.....#",
        "#######",
        "#.....#",
        ".#####.",
    ], 3, 3)


def spring_ai():
    return spring_badge([
        "...#...",
        "...#...",
        "..###..",
        "#######",
        "..###..",
        "...#...",
        "...#...",
    ], 3, 3)


def hibernate():
    c = blank()
    disc(c, "n", 6.5, 7.6, 5.0)
    put(c, ["NN", "NN"], 1, 1)
    put(c, ["NN", "NN"], 11, 1)
    put(c, ["nn", "nn"], 1, 1)
    put(c, ["nn", "nn"], 11, 1)
    put(c, ["tttttt", "tttttt", "ttNNtt", "tttttt", ".tttt."], 4, 7)
    c[6][2:5] = list("NNN")
    c[6][9:12] = list("NNN")
    return rows_of(c)


def rest():
    c = blank()
    put(c, [
        "......c.....",
        "......cc....",
        "cccccccccc..",
        "ccccccccccc.",
        "cccccccccc..",
        "......cc....",
        "......c.....",
    ], 1, 1)
    put(c, [
        ".....O......",
        "....OO......",
        "..OOOOOOOOOO",
        ".OOOOOOOOOOO",
        "..OOOOOOOOOO",
        "....OO......",
        ".....O......",
    ], 1, 7 - 0)
    return rows_of(c)[:N]


def swagger():
    c = blank()
    disc(c, "l")
    for j in range(N):
        for i in range(N):
            if c[j][i] == "l" and (i + j) >= 19:
                c[j][i] = "g"
    put(c, ["..kk", ".k..", ".k..", "kk..", ".k..", ".k..", "..kk"], 1, 3)
    put(c, ["kk..", "..k.", "..k.", "..kk", "..k.", "..k.", "kk.."], 9, 3)
    return rows_of(c)


def postman():
    c = blank()
    disc(c, "O")
    for j in range(N):
        for i in range(N):
            if c[j][i] == "O" and (i + j) >= 19:
                c[j][i] = "r"
    line(c, "W", 4, 9, 9, 4, 2)
    put(c, ["WWWW", "...W", "...W", "...W"], 7, 3)
    c[3][7:11] = list("WWWW")
    return rows_of(c)


def junit():
    c = blank()
    put(c, ["nnnnnnnnnnnn"] + ["nwwwwwwwwwwn"] * 11 + ["nnnnnnnnnnnn"], 1, 1)
    put(c, ["..ssss..", ".sSSSSs."], 3, 0)
    for y in (4, 8):
        put(c, ["...g", "g.g.", ".g.."], 3, y)
        put(c, ["SSSS"], 8, y + 1)
    return rows_of(c)


def mockito():
    c = blank()
    # glass
    put(c, [
        "mmmmmmmmmm",
        ".mmmmmmmm.",
        "..mmmmmm..",
        "...mmmm...",
        "....mm....",
    ], 2, 4)
    put(c, ["WWWWWWWWWW"], 2, 3)
    put(c, ["..", "..", ".."], 6, 9)
    c[9][6:8] = list("ss"); c[10][6:8] = list("ss"); c[11][6:8] = list("ss")
    put(c, ["ssssss"], 4, 12)
    # mint leaves + straw
    put(c, ["..gg.", ".gggg", "gGgg.", ".gg.."], 0, 0)
    put(c, [".gg..", "gggg.", ".ggGg", "..gg."], 3, 0)
    line(c, "r", 9, 5, 12, 0, 1)
    return rows_of(c)


def git():
    c = blank()
    for y in range(N):
        for x in range(N):
            if abs(x - 6.5) + abs(y - 6.5) <= 6.6:
                c[y][x] = "r"
    for y in range(N):
        for x in range(N):
            if c[y][x] == "r" and (x + y) >= 16 and x >= 7:
                c[y][x] = "R"
    for y in range(3, 11):
        c[y][6] = "W"
    line(c, "W", 6, 8, 9, 5, 1)
    put(c, ["WW", "WW"], 5, 2)
    put(c, ["WW", "WW"], 5, 10)
    put(c, ["WW", "WW"], 9, 3)
    return rows_of(c)


def maven():
    c = blank()
    # feather
    shape = [
        "..........rr..",
        "........rrrrr.",
        "......rrrrrrrr",
        "....rrrrrrrrr.",
        "...rrrrrrrrr..",
        "..rrrrrrrrr...",
        ".rrrrrrrrr....",
        ".rrrrrrrr.....",
        "rrrrrrr.......",
        "Rrrrr.........",
        "Rr............",
        "R.............",
    ]
    put(c, shape, 0, 1)
    line(c, "W", 1, 11, 11, 2, 1)
    return rows_of(c)


def intellij():
    c = blank()
    put(c, ["kkkkkkkkkkkk"] * 12, 1, 1)
    for j in range(7, 13):
        for i in range(1, 7):
            c[j][i] = "p" if (i + (12 - j)) <= 5 else "k"
    for j in range(8, 13):
        for i in range(1, 5):
            if c[j][i] == "p" and j >= 10:
                c[j][i] = "e"
    for i in range(1, 4):
        c[12][i] = "O"
    # I J
    put(c, ["WWW", ".W.", ".W.", ".W.", "WWW"], 2, 2)
    put(c, [".WW", "..W", "..W", "W.W", ".W."], 6, 2) 
    put(c, ["WWWW"], 6, 10)
    return rows_of(c)


def vscode():
    c = blank()
    put(c, [
        ".........bbb.",
        "........bbbb.",
        ".......bbbbb.",
        "..b...bbBbbb.",
        ".bbb.bbBBbbb.",
        "bbbbbbBBBbbb.",
        "bbbbbbBBBbbb.".replace("bbbbbbBBBbbb.", "bbbbbBBBBbbb."),
        ".bbb.bbBBbbb.",
        "..b...bbBbbb.",
        ".......bbbbb.",
        "........bbbb.",
        ".........bbb.",
    ], 0, 1)
    return rows_of(c)


ICONS = {
    "Java": java, "SQL": sql, "PostgreSQL": postgres, "Spring Boot": spring_boot, "Spring MVC": spring_mvc,
    "Spring Data JPA": spring_jpa, "Hibernate": hibernate, "Spring AI": spring_ai, "REST APIs": rest,
    "Swagger UI": swagger, "Postman": postman, "JUnit 5": junit, "Mockito": mockito, "Git": git,
    "Maven": maven, "IntelliJ IDEA": intellij, "VS Code": vscode,
}


def build(name):
    """16x16 outlined ASCII rows for a skill."""
    rows = ICONS[name]()
    pad = ["." * 16] + ["." + r.ljust(N, ".")[:N] + "." for r in rows] + ["." * 16]
    h, w = len(pad), 16
    filled = [[pad[y][x] != "." for x in range(w)] for y in range(h)]
    out = [list(r) for r in pad]
    for y in range(h):
        for x in range(w):
            if filled[y][x]:
                continue
            if any(0 <= y + dy < h and 0 <= x + dx < w and filled[y + dy][x + dx]
                   for dy in (-1, 0, 1) for dx in (-1, 0, 1)):
                out[y][x] = "o"
    return ["".join(r) for r in out]
