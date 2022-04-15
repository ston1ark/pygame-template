import pygame as pg
import sys
pg.init()


WIDTH, HEIGHT = 900, 500

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Some Game!')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 165


def draw_window():
    WIN.fill(WHITE)
    pg.display.update()


def main():
    clock = pg.time.Clock()
    draw_window()
    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print('Thanks for playing!')
                pg.quit()

        pg.display.update()

    sys.exit()


if __name__ == '__main__':
    main()
