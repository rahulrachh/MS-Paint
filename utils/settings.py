import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 300


WIDTH, HEIGHT = 500, 600

# make sure that value of rows/cols is less than width or height otherwise the pixel_size will be reduced to 0 and it will crash the program
ROWS = COLS = 100

TOOLBAR_HEIGHT = abs(HEIGHT - WIDTH)

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)



