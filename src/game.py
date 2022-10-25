import user
import move
import bmove
from display import *

def singleplayer():
    board = generate()

    while True:
        p1moved = 0

        show_emoji(board)
        while p1moved == 0:
            pos1row = int(input("Enter the rank for piece to move:"))
            pos1col = int(input("Enter the file for piece to move:"))
            pos2row = int(input("Enter the rank for square to move:"))
            pos2col = int(input("Enter the file for square to move:"))

            match board[pos1row][pos1col].colour:
                case "W":
                    match board[pos1row][pos1col].piece:
                        case "P":
                            if move.validateMoveWP(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][
                                    pos1col]  # replaces square moved to with this piece chosen
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                if pos2row == 0:
                                    board[pos2row][pos2col] = WQueen
                                continue
                            else:
                                print("invalid")
                        case "N":
                            if move.validateMoveKnight(pos1row, pos1col, pos2row, pos2col, board):
                                print("done")
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                        case "R":
                            if move.validateMoveRK(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                            else:
                                print("Invalid move")
                        case "Q":
                            if move.validate_queen(pos1row, pos1col, pos2row, pos2col,board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                            else:
                                print("Invalid move")
                        case "B":
                            if move.validate_bishop(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                        case "K":
                            if move.king_move(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                            else:
                                print("Invalid move")

        # bmove.blackmove(board)

        clear()
        # new_board = display.new_board(board)
        # display.show_debug(new_board)
        # display.show(board)
        show_emoji_black(board)

        p2moved = 0

        while p2moved == 0:
            pos1row = int(input("Enter the rank for piece to move:"))
            pos1col = int(input("Enter the file for piece to move:"))
            pos2row = int(input("Enter the rank for square to move:"))
            pos2col = int(input("Enter the file for square to move:"))

            match board[pos1row][pos1col].colour:
                case "B":
                    match board[pos1row][pos1col].piece:
                        case "P":
                            if move.validateMoveBP(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]  # replaces square moved to with this piece chosen
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                if pos2row == 0:
                                    board[pos2row][pos2col] = BQueen
                                continue
                            else:
                                print("invalid")
                        case "N":
                            if move.validateMoveKnight(pos1row, pos1col, pos2row, pos2col, board):
                                print("done")
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                continue
                        case "R":
                            if move.validateMoveRK(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                continue
                            else:
                                print("Invalid move")
                        case "Q":
                            if move.validate_queen(pos1row, pos1col, pos2row, pos2col,board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                continue
                            else:
                                print("Invalid move")
                        case "B":
                            if move.validate_bishop(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                continue
                        case "K":
                            if move.king_move(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                continue
                            else:
                                print("Invalid move")