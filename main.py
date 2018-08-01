import pygame
import os

pygame.init()

# Initial values
WIDTH = 512 # Screen width
HEIGHT = 512 # Screen height
Surface = pygame.display.set_mode((WIDTH, HEIGHT)) # Create screen
pygame.display.set_caption("Gridrunner") # Set caption
clock = pygame.time.Clock() # Initialize clock

# Controls spritesheet importing
def spritesheet(sheet, rectangle, scaleTo):
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert()
    image.blit(sheet, (0, 0), rect)
    image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
    # Scales the image to designated size
    image = pygame.transform.scale(image, (scaleTo, scaleTo))
    return image

# Creates the sprites from the provided spritesheet and stores them in individual surfaces
ss = pygame.image.load("spritesheet.png").convert()
wall = spritesheet(ss, (12, 0, 4, 4), 64)
player = spritesheet(ss, (8, 4, 4, 4), 64)
enemy = spritesheet(ss, (12, 4, 4, 4), 64)
coin = spritesheet(ss, (8, 0, 4, 4), 64)
buttonUnclicked = spritesheet(ss, (0, 4, 4, 4), 64)
buttonClicked = spritesheet(ss, (4, 4, 4, 4), 64)
doorOpen = spritesheet(ss, (0, 0, 4, 4), 64)
doorClosed = spritesheet(ss, (4, 0, 4, 4), 64)

class gridElement(object):
    def __init__(self, name, pos):
        grid.append(self)
        self.name = name
        self.rect = pygame.Rect(pos[0], pos[1], 64, 64)

# Empty = 0   Wall = 1   Player = 2   Enemy = 3
# Coin = 4   Button = 5   Open Door = 6   Closed Door = 7

# This list is the layout for the level (8x8 grid)


level = [
 [ 1, 1, 1, 1, 1, 1, 1, 1 ],
 [ 1, 5, 0, 0, 0, 0, 6, 1 ],
 [ 1, 0, 0, 1, 1, 1, 1, 1 ],
 [ 1, 0, 3, 0, 3, 0, 0, 1 ],
 [ 1, 1, 1, 1, 1, 1, 0, 1 ],
 [ 1, 0, 4, 0, 4, 0, 0, 1 ],
 [ 1, 2, 0, 0, 0, 0, 0, 1 ],
 [ 1, 1, 1, 1, 1, 1, 1, 1 ]
]

# Generates a level based on the level list
grid = []
gridX = 0
gridY = 0
for row in level:
    for col in row:
        if col == 1:
            gridElement("Wall", (gridX, gridY))
        elif col == 2:
            x = gridX
            y = gridY
        elif col == 3:
            gridElement("Enemy", (gridX, gridY))
        elif col == 4:
            gridElement("Coin", (gridX, gridY))
        elif col == 5:
            gridElement("Button", (gridX, gridY))
        elif col == 6:
            gridElement("Open Door", (gridX, gridY))
        elif col == 7:
            gridElement("Closed Door", (gridX, gridY))
        gridX += 64
    gridY += 64
    gridX = 0

isPlaying = True
while isPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False

    Surface.fill((255, 255, 255))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    Surface.blit(player, (x, y))
    for i in grid:
        if i.name == "Wall":
            Surface.blit(wall, i.rect)
        elif i.name == "Enemy":
            Surface.blit(enemy, i.rect)
        elif i.name == "Coin":
            Surface.blit(coin, i.rect)
        elif i.name == "Button":
            Surface.blit(buttonUnclicked, i.rect)
        elif i.name == "Open Door":
            Surface.blit(doorOpen, i.rect)
        elif i.name == "Closed Door":
            Surface.blit(doorClosed, i.rect)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()