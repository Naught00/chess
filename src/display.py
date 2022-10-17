import os
import pprint
import pandas as pd
from dataclasses import dataclass


@dataclass(eq=False,unsafe_hash=True)
class Piece:
    colour: str
    piece: str
    hasMoved: bool
## PIECE, 0 = PAWN,
## 0 = Black, 1 = white

BPawn = Piece("B", "P", False)
WPawn = Piece("W", "P", False)
Empty = Piece("empty", "empty", False)
hashWPawn = hash(WPawn)
hashBPawn = hash(BPawn)
hashEmpty = hash(Empty)

pieceicons = {hashWPawn: "♙",
              hashBPawn: "♟",
              hashEmpty: "🨀"}


def iconBoard(board, dict):
    newBoardtemp = (pd.Series(board).map(dict))

    return list(newBoardtemp)


def generate():
    board = [
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, ],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, ],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    ]
    return board


def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def show_debug(board):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(board)


def show(board):
    i = 0
    x = 0
    c = 0

    while True:

        print("|", end="")

        if board[i][x].piece == "empty":
            print("  ", end="")
        else:
            print(f"{board[i][x].colour}{board[i][x].piece}", end="")

        if x == 7:
            i += 1
            print("|")
            x = 0
        else:
            c += 1
            x += 1
        if i > 7:
            break


def new_board(board):
    i = 0
    x = 0
    c = 0

    new_board = [
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
    ]

    while True:
        if board[i][x].piece == "empty":
            new_board[i][x] = "  "
        else:
            print(f"{board[i][x].colour}{board[i][x].piece}", end="")
            new_board[i][x] = board[i][x].colour + board[i][x].piece
            print(new_board[i][x])

        if x >= 7:
            i += 1
            x = 0
        if i > 7:
            break

        c += 1
        x += 1

    return new_board
