"""ASCII pixel sprites. Each row is one line of pixels; letters map to palette colours."""

# --- 16x16 icons ---
SPROUT = [
    "................",
    "................",
    "................",
    "...gg......gg...",
    "..glllg..glllg..",
    ".glllllggllllllg",
    ".glllllggllllllg",
    "..gllllggllllg..",
    "...gggg.sgggg...",
    "........ss......",
    "........ss......",
    "........ss......",
    ".....dddssddd...",
    "....dddddddddd..",
    "................",
    "................",
]
SPROUT_PAL = {"g": "#4e6d44", "l": "#8fb35a", "s": "#a86b3a", "d": "#6b4630"}

FLAME = [
    "................",
    ".......r........",
    "......rr........",
    ".....rrr.r......",
    "....rrroor......",
    "....rroooor.....",
    "...rrooyyoor....",
    "..rrroyyyoorr...",
    "..rroyyyyyoor...",
    "..rroyyccyoor...",
    "..rroyccccyor...",
    "..rrooyccyoor...",
    "...rroyyyyorr...",
    "....rrooooorr...",
    ".....rrrrrrr....",
    "................",
]
FLAME_PAL = {"r": "#dc6735", "o": "#e88b3d", "y": "#f2ba58", "c": "#ffe2a0"}

CROWN = [
    "................",
    "................",
    "................",
    "..y.....y.....y.",
    "..yy...yyy...yy.",
    "..yyy..yyy..yyy.",
    "..yyyyyyyyyyyyy.",
    "..yYyyyyyyyyyYy.",
    "..yyyyyRyyyyyyy.",
    "..yyyyyyyyyyyyy.",
    "..ddddddddddddd.",
    "..bbbbbbbbbbbbb.",
    "................",
    "................",
    "................",
    "................",
]
CROWN_PAL = {"y": "#f3c371", "Y": "#ffe2a0", "R": "#dc6735", "d": "#d99a52", "b": "#b77b39"}

BOOK = [
    "................",
    "................",
    "................",
    "..bbbbbb.bbbbbb.",
    ".bcccccbbcccccb.",
    ".bcwwwwcbcwwwwb.",
    ".bcccccbbcccccb.",
    ".bcwwwwcbcwwwwb.",
    ".bcccccbbcccccb.",
    ".bcwwwwcbcwwwwb.",
    ".bcccccbbcccccb.",
    "..bbbbbbbbbbbbb.",
    "................",
    "................",
    "................",
    "................",
]
BOOK_PAL = {"b": "#d99a52", "c": "#f2dfbc", "w": "#c7a786"}

LEAF = [
    ".gg.",
    "gllg",
    "gllg",
    ".gg.",
]
LEAF_PAL = {"g": "#4e6d44", "l": "#8fb35a"}

BARS = [
    "......oo",
    "......oo",
    "..oo..oo",
    "..oo..oo",
    "oooo..oo",
    "oooooooo",
]
BARS_PAL = {"o": "#d99a52"}

STAR = [
    "......yy......",
    "......yy......",
    ".....yyyy.....",
    "yyyyyyyyyyyyyy",
    ".yyyyyyyyyyyy.",
    "..yyyyyyyyyy..",
    "...yyyyyyyy...",
    "...yyyyyyyy...",
    "..yyyyyyyyyy..",
    "..yyyy..yyyy..",
    ".yyy......yyy.",
    ".yy........yy.",
]
STAR_PAL = {"y": "#d99a52"}

# --- 12x12 equipment-slot icons for the header card ---
SLOT_ICONS = {
    "ring": ([
        "............",
        ".....ww.....",
        "....wccw....",
        ".....ww.....",
        "...ssssss...",
        "..ss....ss..",
        "..s......s..",
        "..s......s..",
        "..ss....sS..",
        "...ssSSSS...",
        "............",
        "............",
    ], {"s": "#c9ced6", "S": "#8d93a0", "w": "#f5f5f5", "c": "#bcd4ff"}),
    "bracelet": ([
        "............",
        "....rryy....",
        "..yrrRRrry..",
        "..rR....Rr..",
        ".rr......rr.",
        ".yR......Ry.",
        ".rr......rr.",
        ".rR......Rr.",
        "..yr....ry..",
        "..rrRyyRrr..",
        "....rrrr....",
        "............",
    ], {"r": "#b3261e", "R": "#7d1a15", "y": "#f2ba58"}),
    "sneakers": ([
        "............",
        "............",
        "......cc....",
        ".....cccc...",
        "....ccccc...",
        "..ccccccccc.",
        ".ccccccccccc",
        ".cccccccccck",
        ".kkkkkkkkkkk",
        "............",
        "............",
        "............",
    ], {"c": "#ece3cf", "k": "#9a8c74"}),
    "earbuds": ([
        "............",
        "...ww.......",
        "..wwww......",
        "..wwWw......",
        "...ww.......",
        "....W.......",
        "....W.......",
        "....W.......",
        "....Ww......",
        ".....W......",
        ".....WW.....",
        "............",
    ], {"w": "#f5f5f5", "W": "#bfc4cc"}),
    "necklace": ([
        "............",
        ".ssssssssss.",
        ".s........s.",
        "..s......s..",
        "..s......s..",
        "...s....s...",
        "....s..s....",
        ".....ss.....",
        ".....ww.....",
        "....wccw....",
        ".....ww.....",
        "............",
    ], {"s": "#c9ced6", "w": "#f5f5f5", "c": "#bcd4ff"}),
    "pants": ([
        "............",
        "..pppppppp..",
        "..pPPPPPPp..",
        "..pppppppp..",
        "..ppppPppp..",
        "..pppp.ppp..",
        "..pppp.ppp..",
        "..pppp.ppp..",
        "..pppp.ppp..",
        "..ppp...pp..",
        "............",
        "............",
    ], {"p": "#4a4352", "P": "#2d2832"}),
    "top": ([
        "............",
        "..tt....tt..",
        "..ttt..ttt..",
        "..ttt..ttt..",
        "..tttttttt..",
        "...tttttt...",
        "...tTTTTt...",
        "...tttttt...",
        "...tttttt...",
        "...tttttt...",
        "............",
        "............",
    ], {"t": "#8a6551", "T": "#6b4a3a"}),
}


# --- Calendar crops (10x10): growth stage by contribution count ---
CROPS = [
    [   # 1: sprout
        "..........",
        "..........",
        "..........",
        "..........",
        "...l..l...",
        "....lgl...",
        ".....g....",
        ".....g....",
        "..dddddd..",
        ".dddddddd.",
    ],
    [   # 2-3: young plant
        "..........",
        "..........",
        ".ll....ll.",
        ".llll.lll.",
        "..llllll..",
        "...lgl....",
        "....g.....",
        "....g.....",
        "..dddddd..",
        ".dddddddd.",
    ],
    [   # 4-6: flowering
        "...eeee...",
        "..eeyyee..",
        "..eeyyee..",
        "...eeee...",
        ".l..gg..l.",
        ".lll.g.lll",
        "..lllgll..",
        "....gg....",
        "..dddddd..",
        ".dddddddd.",
    ],
    [   # 7+: ripe pumpkin
        ".....g....",
        "....gg....",
        "...OOOOO..",
        "..OOoOOOO.",
        ".OOoOOoOOO",
        ".OOoOOoOOO",
        ".OOoOOoOOO",
        "..OOoOOOO.",
        "...OOOOO..",
        "..........",
    ],
]
CROP_PAL = {"l": "#8fb35a", "g": "#4e6d44", "d": "#7a4f31", "e": "#f08cb0", "y": "#f2c14e", "O": "#e8892e", "o": "#b8601f"}


def _seasons():
    def blank(n=12):
        return [["."] * n for _ in range(n)]

    def to_rows(c):
        return ["".join(r) for r in c]

    spring = blank()
    for (x, y) in ((4, 1), (7, 4), (4, 6), (1, 4)):
        for dx in range(3):
            for dy in range(3):
                spring[y + dy - 0][x + dx - 0] = "e" if 0 <= y + dy < 12 and 0 <= x + dx < 12 else "."
    for (x, y) in ((5, 4), (6, 4), (5, 5), (6, 5)):
        spring[y][x] = "y"
    for y in range(8, 12):
        spring[y][5] = "g"
    spring[9][6] = "g"; spring[9][7] = "g"; spring[10][4] = "g"; spring[10][3] = "g"

    summer = blank()
    for y in range(12):
        for x in range(12):
            if (x - 5.5) ** 2 + (y - 5.5) ** 2 <= 9:
                summer[y][x] = "y"
    for (x, y) in ((5, 0), (6, 0), (5, 11), (6, 11), (0, 5), (0, 6), (11, 5), (11, 6), (1, 1), (10, 1), (1, 10), (10, 10)):
        summer[y][x] = "O"

    fall = [list(r) for r in [
        ".....r......",
        "....OOO.....",
        "...OOOOO....",
        "..OOOOOOO...",
        ".OOOOOOOOO..",
        "..OOOOOOO...",
        ".OOOOOOOOO..",
        "..OOOOOOO...",
        "...OOOOO....",
        "....OOO.....",
        ".....r......",
        ".....r......",
    ]]

    winter = blank()
    for i in range(12):
        winter[5][i] = "c"; winter[6][i] = "c"; winter[i][5] = "c"; winter[i][6] = "c"
    for i in range(1, 11):
        winter[i][i] = "w"; winter[i][11 - i] = "w"
    return {"SPRING": (to_rows(spring), {"e": "#f08cb0", "y": "#f2c14e", "g": "#6aa84f"}),
            "SUMMER": (to_rows(summer), {"y": "#f2c14e", "O": "#e8892e"}),
            "FALL": (to_rows(fall), {"O": "#e8892e", "r": "#a8421f"}),
            "WINTER": (to_rows(winter), {"c": "#8fd3f4", "w": "#ffffff"})}


SEASONS = _seasons()
SEASON_BY_MONTH = {12: "WINTER", 1: "WINTER", 2: "WINTER", 3: "SPRING", 4: "SPRING", 5: "SPRING",
                   6: "SUMMER", 7: "SUMMER", 8: "SUMMER", 9: "FALL", 10: "FALL", 11: "FALL"}


# --- Project quest icons (16x16, drawn before outlining) ---
def _project_icons():
    def blank():
        return [["."] * 16 for _ in range(16)]

    def rows(c):
        return ["".join(r) for r in c]

    chest = blank()
    for y in range(5, 15):
        for x in range(1, 15):
            chest[y][x] = "n"
    for x in range(1, 15):
        chest[5][x] = "N"; chest[8][x] = "N"; chest[14][x] = "N"
    for y in range(5, 15):
        chest[y][1] = "N"; chest[y][14] = "N"
    for y in range(8, 12):
        for x in range(7, 9):
            chest[y][x] = "y"
    chest[10][7] = "k"
    for (x, y) in ((12, 1), (13, 1), (11, 2), (12, 2), (13, 2), (14, 2), (11, 3), (12, 3), (13, 3), (14, 3), (12, 4), (13, 4)):
        chest[y][x] = "r"
    chest[2][12] = "W"; chest[3][12] = "W"

    shield = blank()
    for y in range(1, 15):
        half = 6 if y < 8 else max(0, 6 - (y - 7))
        for x in range(8 - half, 8 + half):
            shield[y][x] = "b"
    for y in range(1, 15):
        for x in range(16):
            if shield[y][x] == "b" and x >= 8:
                shield[y][x] = "B"
    for y in range(1, 15):
        xs = [x for x in range(16) if shield[y][x] != "."]
        if xs and (y in (1, 2) or True):
            shield[y][xs[0]] = "y"; shield[y][xs[-1]] = "y"
    for x in range(2, 14):
        if shield[1][x] != ".":
            shield[1][x] = "y"
    shield[5][7] = "k"; shield[5][8] = "k"; shield[6][7] = "k"; shield[6][8] = "k"
    for y in (7, 8, 9):
        shield[y][7] = "k"; shield[y][8] = "k"

    buoy = blank()
    for y in range(16):
        for x in range(16):
            d = (x - 7.5) ** 2 + (y - 7.5) ** 2
            if 9 <= d <= 49:
                quad = (x >= 8) ^ (y >= 8)
                buoy[y][x] = "r" if quad else "W"
    return {"TaponSusi": (rows(chest), {"n": "#9a6a42", "N": "#5c3a24", "y": "#f2c14e", "k": "#2a1a14", "r": "#e0483a", "W": "#ffffff"}),
            "ContextGuard": (rows(shield), {"b": "#5aa0e0", "B": "#3a6fb0", "y": "#f2c14e", "k": "#1d2c44"}),
            "ContractRescue": (rows(buoy), {"r": "#e0483a", "W": "#f4f0e8"})}


PROJECT_ICONS = _project_icons()
