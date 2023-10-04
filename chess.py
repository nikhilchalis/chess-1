import chess

def display_board(board):
    board_str = board.__str__()  # Get the board's string representation
    print(board_str)

def main():
    board = chess.Board()  # Initialize a new chessboard



    # Game is over
    display_board(board)
    result = board.result()
    print(f"Game Over. Result: {result}")

if __name__ == "__main__":
    main()


import numpy as np

board = np.array([
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
])