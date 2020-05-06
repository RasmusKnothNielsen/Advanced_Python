import pygame
import sys
import math
import numpy as np

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 250, 0)
BLUE = (0, 0, 250)
RED = (250, 0, 0)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCK_SIZE = 20

grid_size = WINDOW_WIDTH / BLOCK_SIZE

grid = [[0 for x in range(math.floor(WINDOW_WIDTH/BLOCK_SIZE))] for y in range(math.floor(WINDOW_HEIGHT/BLOCK_SIZE))]

print(grid)


def main():
    global SCREEN, CLOCK
    number_of_clicks = 0
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid(BLOCK_SIZE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

                # Find out which square was pressed
                x, y = pygame.mouse.get_pos()
                floored_x = math.floor(x / 20)
                floored_y = math.floor(y / 20)
                print("X:", floored_x)
                print("Y:", floored_y)
                print("number of clicks",number_of_clicks)

                # Starting position
                if number_of_clicks == 0:
                    grid[floored_y][floored_x] = 1
                    number_of_clicks += 1
                elif number_of_clicks == 1:
                    grid[floored_y][floored_x] = 2
                    number_of_clicks += 1
                else:
                    grid[floored_y][floored_x] = 3
                    number_of_clicks += 1

                print(grid)

        pygame.display.update()


def drawGrid(BLOCK_SIZE):
    for x in range(math.floor(WINDOW_WIDTH/BLOCK_SIZE)):
        for y in range(math.floor(WINDOW_HEIGHT/BLOCK_SIZE)):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE,
                               BLOCK_SIZE, BLOCK_SIZE)
            if grid[y][x] == 1:
                pygame.draw.rect(SCREEN, GREEN , rect, 1)
            elif grid[y][x] == 2:
                pygame.draw.rect(SCREEN, RED, rect, 1)
            elif grid[y][x] == 3:
                pygame.draw.rect(SCREEN, BLUE, rect, 1)
            else:

                pygame.draw.rect(SCREEN, WHITE, rect, 1)

main()