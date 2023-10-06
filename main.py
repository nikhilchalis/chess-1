import pygame as pg
from state import GameState

WIDTH = HEIGHT = 512
BOARD_DIMENSION = 8
SQUARE_SIZE = HEIGHT // BOARD_DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("./images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

def main():
    pg.init()
    sc = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    sc.fill(pg.Color("White"))

    gs = GameState()
    loadImages()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        drawGameState(sc, gs)
        clock.tick(MAX_FPS)
        pg.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    board_colors = [pg.Color("white"), pg.Color("gray")]
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            color = board_colors[((row + col) % 2)]#checks whether combination is even or odd
            pg.draw.rect(screen, color, pg.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawPieces(screen, board):
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], pg.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                

if __name__ == "__main__":
    main()
