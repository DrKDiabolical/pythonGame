import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()

Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncer")
clock = pygame.time.Clock()

done = False
is_green = True
x = 30
y = 30

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    Surface.fill((0, 0, 0))

    if is_green:
        color = (0, 255, 0)
    else:
        color = (255, 0, 0)
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        is_green = not is_green


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    pygame.draw.rect(Surface, color, pygame.Rect(x, y, 60, 60))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()