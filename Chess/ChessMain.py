# Driver file
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initialize a global dictionary images.This will be called exactly once in the main
'''


def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bK", "bQ"]
    for pieces in pieces:
        IMAGES[pieces] = p.transform.scale(p.image.load("chess images/" + pieces + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note we can access an image by 'IMAGES['wp']


'''
The main driver for code. THis will handle user input and updating the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)
    loadImages()  # only once, before thw while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for all the graphics within a current game state
'''


def drawGameState(screen, gs):
    drawBoard(screen)  # draw squares on the board
    drawPieces(screen, gs.board)  # draw pieces on top of those squares


'''
Draw the squares on the board
'''


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the pieces on the board on the current Gamestate.board
'''


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not empty squares
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
    main()
