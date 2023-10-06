import pygame as pg
from state import GameState, Move

# initialise variables
WIDTH = HEIGHT = 512
BOARD_DIMENSION = 8
SQUARE_SIZE = HEIGHT // BOARD_DIMENSION
MAX_FPS = 15
IMAGES = {}

# loads images into the IMAGES dictionary
def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("./images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


# main loop
def main():
    pg.init()
    sc = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    sc.fill(pg.Color("White"))

    gs = GameState()
    loadImages()

    running = True
    square_selected = () # no square selected - empty tuple of the form (row, col)
    player_clicks = [] # keep track of players clicks - list of two tuples [(6, 4), (4, 4)] means start click at (6,4) and end at (4,4)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:# This implementation does not allow click and drag - that could be a future addition
                location = pg.mouse.get_pos()# returns as (x, y) tuple
                # this works as is since there is no border and the board is the entire screen
                # if we add a border or have the board in a larger area, we need to take care of the offsets
                col = location[0] // SQUARE_SIZE
                row = location[1] // SQUARE_SIZE

                if square_selected == (row, col): #user clicked the same square twice - we deselect
                    square_selected = () # deselect
                    player_clicks = [] # clear player clicks
                else:
                    square_selected = (row, col)
                    player_clicks.append(square_selected)

                # was that the users second click?
                if len(player_clicks) == 2: # after second click
                    move = Move(player_clicks[0], player_clicks[1], gs.board)
                    print(f"move made: {move.get_chess_notation()}")
                    gs.make_move(move)
                    square_selected = ()
                    player_clicks = []

        
        draw_game_state(sc, gs)
        clock.tick(MAX_FPS)
        pg.display.flip()


def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    board_colors = [pg.Color("white"), pg.Color("gray")]
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            color = board_colors[((row + col) % 2)]#checks whether combination is even or odd
            pg.draw.rect(screen, color, pg.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(screen, board):
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], pg.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                

if __name__ == "__main__":
    main()
