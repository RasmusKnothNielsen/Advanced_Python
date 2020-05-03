import pygame
import sys
import math
import numpy as np

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 250, 0)
BLUE = (0, 0, 250)
RED = (250, 0, 0)
YELLOW = (255, 255, 0)
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

    start = (0, 0)
    end = (0, 0)

    while True:
        drawGrid(BLOCK_SIZE)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == 771 and end is not (0, 0):   # Space pressed and end point selected
                print("SPACE pressed")
                aStar(start, end)


            # Used to select blocks for start, stop and walls

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
                    start = (floored_y, floored_x)
                elif number_of_clicks == 1:
                    grid[floored_y][floored_x] = 2
                    number_of_clicks += 1
                    end = (floored_y, floored_x)
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
            if grid[y][x] == 1:     # Starting point
                pygame.draw.rect(SCREEN, GREEN, rect, 2)
            elif grid[y][x] == 2:   # Ending point
                pygame.draw.rect(SCREEN, RED, rect, 2)
            elif grid[y][x] == 3:   # Wall
                pygame.draw.rect(SCREEN, BLUE, rect, 2)
            elif grid[y][x] == 4:   # Checking path
                pygame.draw.rect(SCREEN, YELLOW, rect, 2)
            elif grid[y][x] == 6:   # Path found
                print("Okok")
            else:

                pygame.draw.rect(SCREEN, WHITE, rect, 2)


def aStar(start, end):

    open_list = []
    closed_list = []

    open_list.append(start)
    print(calculateDistance(start, end))

    #while True:


    x, y = start
    # Find all neighbours
    grid[x - 1][y - 1] = 4
    grid[x - 1][y + 1] = 4
    grid[x - 1][y] = 4
    grid[x][y - 1] = 4
    grid[x][y + 1] = 4
    grid[x + 1][y] = 4
    grid[x + 1][y + 1] = 4
    grid[x + 1][y - 1] = 4

    drawGrid(BLOCK_SIZE)


def calculateDistance(a, b):
    result = 0
    if a[0] > b[0]:
        result += a[0] - b[0]
    else:
        result += b[0] - a[0]

    if a[1] > b[1]:
        result += a[1] - b[1]
    else:
        result += b[1] - a[1]

    return result

main()