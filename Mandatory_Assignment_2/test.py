import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((612,792))
pygame.display.set_caption("This works!")

red = (255,0,0)
black = (0, 0, 0)
screen.fill(red)

# point (0,0) is at upper left
pygame.draw.lines(screen,black,False,[(100,100),(150,200),(200,100)], 1)

pygame.display.update() #nothing is drawn

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
