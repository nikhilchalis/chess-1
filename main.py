import pygame as pg

WIDTH = HEIGHT = 512
BOARD_DIMENSION = 8
SQUARE_SIZE = HEIGHT // BOARD_DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("./images" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

def main():
    pg.init()
    sc = pg.display.set_mode((WIDTH, HEIGHT))
    cock = pg.time.Clock()
    sc.fill(pg.Color("White"))
    




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