"""Angel as a Stardew Valley style farmer: front-facing, standing, chibi proportions.

Edit ROWS to change the look (letters map to PALETTE). `farmer()` returns a 24-wide grid
with the iced coffee and earbuds added on top.
"""

PALETTE = {
    "K": "#2a1a14", "H": "#3d2418", "h": "#5e3a27", "S": "#e3a574", "s": "#c58558", "E": "#2a1a14",
    "W": "#ffffff", "B": "#e88b6b", "T": "#7d5b4b", "t": "#5f4336", "P": "#2d2832", "p": "#433b4a",
    "F": "#f1e9d8", "f": "#b9ad95", "N": "#d3d7de", "D": "#ffffff", "R": "#c0372b", "Y": "#f2c14e",
    "U": "#ffffff", "C": "#efe3cf", "L": "#b9783b", "G": "#2f9a52", "I": "#d8e7f0",
}

ROWS = [
    "....................",
    "......KKKKKKKK......",
    ".....KHHHHHHHHK.....",
    "....KHHhhHHhhHHK....",
    "...KHHHHHHHHHHHHK...",
    "...KHHhHHHHHHhHHK...",
    "..KHHHHHSSSSHHHHHK..",
    "..KHHHHSSSSSSHHHHK..",
    "..KHHHSSSSSSSSHHHK..",
    "..KHHHSEWSSEWSHHHK..",
    "..KHHHBSSSSSSBHHHK..",
    "..KHHHSSSssSSSHHHK..",
    "..KHHHKSSSSSSKHHHK..",
    "..KHHHHKSSSSKHHHHK..",
    "..KHHHHHKSSKHHHHHK..",
    "..KHHSsSNSSNSsSHHK..",
    "..KHHSsSSNNSSsSHHK..",
    "..KHHSsTSDDSTsSHHK..",
    "..KHHSsTTSSTTsSHHK..",
    "..KHHSsTTTTTTsSHHK..",
    "..KHHSsTTTTttsSHHK..",
    "..KHHSsTTTTttsSHHK..",
    "...KHSsTTTTttsSHK...",
    "....KSsTTTTttsSK....",
    "....KRsTTTTttsSK....",
    "....KSSPPPPPPSSK....",
    "....KSSPPPPPPSSK....",
    ".....KKPPPPPPKK.....",
    "....KPPPPPPPPPPK....",
    "....KPPPPpPPpPPK....",
    "...KPPPPPPPPPPPPK...",
    "...KPPPPPKKPPPPPK...",
    "...KPPPPPK.KPPPPPK..",
    "..KFFFFFFKKFFFFFFK..",
    "..KKKKKKKKKKKKKKKK..",
]


def farmer():
    g = [list(".." + r + "..") for r in ROWS]     # 24 columns

    def put(rows, ox, oy):
        for j, row in enumerate(rows):
            for i, ch in enumerate(row):
                if ch != ".":
                    g[oy + j][ox + i] = ch

    # iced coffee in the right hand (viewer's right): straw, lid, cup
    put(["G", "G", "G", "G"], 20, 16)
    put(["KCCCK", "KLLLK", "KLILK", "KLLLK", "KLLLK", ".KKK."], 18, 20)
    g[26][17], g[27][17] = "S", "K"
    # earbud + wire
    g[9][5] = "U"
    g[10][5] = "U"
    return ["".join(r) for r in g]
