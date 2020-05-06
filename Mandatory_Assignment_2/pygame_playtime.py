import pygame

pygame.init()

display_width = 500
display_height = 500

win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("First Game")


def initial_setup(win, display_height, display_width):
    block_size = 50
    color = (255, 100, 50)
    for y2 in range(display_height):
        for x2 in range(display_width):
            rect = pygame.Rect(x2*(block_size+1), y2*(block_size+1), block_size, block_size)
            pygame.draw.rect(win, color, rect)

x = 50
y = 50
width = 40
height = 40
vel = 30     # Velocity of player

isJump = False
jumpCount = 10

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

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < display_width - width - vel:
        x += vel

    if not isJump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < display_height - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10


    win.fill((0, 0, 0))
    initial_setup(win, display_height, display_width)
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