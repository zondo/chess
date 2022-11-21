"""Chess puzzles from The Fuddler, in FEN format.
"""

from fenwrite import write_popeye, write_svg


puzzles = {
    "2018-04": "8/8/3Nn1p1/6n1/R3p3/B2pk1K1/1R6/5B2",
    "2018-06": "6QB/7B/8/8/4pk1q/5p2/5P1p/7K",
    "2018-07": "3R4/8/KNkB4/8/2pp3n/4n3/6N1/7B",
    "2018-08": "8/3r4/3Qb3/4RN2/2k2n2/8/2P1NB2/2bK4",
    "2018-09": "4R3/nN1k2r1/3NpR2/1P6/8/3B4/K1Q5/8",
    "2018-10": "1Q6/8/2r5/P1k1N1R1/4P3/4b2r/K4N2/6B1",
    "2018-11": "2n5/n5Q1/4R3/1Pk2P2/8/P1N5/3N3b/5K2",
    "2018-12": "R2rk3/4p2n/6p1/2nB4/6QB/b7/8/3K4",
    "2019-01": "3Q2n1/8/p7/r2pkP2/6n1/b2Rp1K1/8/1B6",
    "2019-03": "8/1R4nr/2Nk4/3P2R1/K2P4/7b/B7/5r2",
    "2019-04": "8/2B2p2/8/1pk2P1p/4QN1R/8/n7/2n2K2",
    "2019-05": "8/4Q2p/4R1pk/2b4p/7P/4R3/8/2B3K1",
    "2019-06": "8/2b5/6p1/8/2KPkp1R/R2N3Q/4b3/6B1",
    "2019-07": "b3r3/8/5NB1/3Q2np/3R4/2B1k3/R5K1/8",
    "2019-08": "1n6/1N6/pR6/8/k2p4/6p1/1P3bQ1/3N3K",
    "2019-09": "R1N2K2/2k5/4PB2/P1N5/Br6/3b4/8/3Q4",
    "2019-10": "4k1n1/3pP3/n2Q2P1/3N4/8/1p6/1K6/8",
    "2019-11": "8/8/2p1pQ2/r3N3/b2k4/3P4/1P1R1K2/7B",
    "2019-12": "k3n3/qR2R3/4N3/2p5/2P5/2Q5/8/4K3",
    "2020-01": "8/1Q6/7p/4K1nk/7P/5P2/1p2n1N1/1B5N",
    "2020-02": "b7/3Q4/8/2P1p3/4k3/6PB/1N3B1n/2nK4",
    "2020-03": "8/8/4p2p/Q6K/3bNkB1/4R3/5B2/8",
    "2022-02": "8/4K3/3Q4/5bR1/4k1p1/Rn6/3n4/3B2B1",
    "2022-03": "8/5p2/2N1bP2/1Q6/N1n1k3/8/8/4KRB1",
    "2022-04": "3R4/8/8/1N6/1Pk1r1nQ/K1N5/8/6b1",
    "2022-06": "B7/1K6/2r2p2/3kp3/N1N3Q1/8/2R5/1n6",
    "2022-07": "1Q6/1P6/4N3/4Rp2/r3B2p/r3k3/8/2N1K3",
    "2022-08": "8/Q7/8/2p5/8/1n1R2pR/4PNKp/3Bk3",
    "2022-09": "3n2N1/5p2/3k1p2/2RP1B2/2K2p2/2BR4/8/8",
    "2022-10": "3R4/Q7/2k5/5n2/P3NK2/4p3/5P2/nq5B",
    "2022-11": "6K1/3PRnQB/2p5/3p4/5k2/7q/2N5/4N3",
}


def dump_puzzle(month, fen, dirname="fuddler"):
    prefix = f"{dirname}/{month}"
    write_svg(fen, prefix + ".svg")

    title = "The Fuddler, " + month
    write_popeye(fen, prefix + ".txt", title)

    print(f"Wrote {month}")


def dump(dirname="fuddler"):
    for month, fen in sorted(puzzles.items()):
        dump_puzzle(month, fen, dirname)
