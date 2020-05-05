import pygame

pygame.init()

display_width = 500
display_height = 500

win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 40
vel = 30     # Velocity of player

run = True
while run:
    pygame.time.delay(100)  # used as clock, to delay actions

    # Retrieving events from pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit was pressed")
            run = False

    # Save keypresses
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and (x - vel >= 0):
        x -= vel

    if keys[pygame.K_RIGHT] and (x + vel <= display_width - 50):
        x += vel

    if keys[pygame.K_UP] and (y - vel >= 0):
        y -= vel

    if keys[pygame.K_DOWN] and (y + vel <= display_height - 50):
        y += vel

    win.fill((0, 0, 0))
    # Draw a rectangle on the window, with color red and in the designated place
    print("Drawing rect")
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    print("Rect drawn")
    # Refresh display
    pygame.display.update()
    print("Display updated")


# If we get here, the program has to quit
print("Quiting")
pygame.quit()