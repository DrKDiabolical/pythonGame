import pygame
import os

pygame.init()

# Initial values
WIDTH = 512 # Screen width
HEIGHT = 512 # Screen height
Surface = pygame.display.set_mode((WIDTH, HEIGHT)) # Create screen
pygame.display.set_caption("Gridrunner") # Set caption
clock = pygame.time.Clock() # Initialize clock

x = WIDTH/2
y = HEIGHT/2

# Empty = 0   Wall = 1   Player = 2   Enemy = 3
# Coin = 4   Button = 5   Open Door = 6   Closed Door = 7

# This list is the layout for the level (8x8 grid)
level = [
 [1, 1, 1, 1, 1, 1, 1, 1 ],
 [1, 0, 0, 0, 0, 0, 3, 1 ],
 [1, 0, 0, 1, 1, 1, 1, 1 ],
 [1, 0, 0, 0, 0, 0, 0, 1 ],
 [1, 1, 1, 1, 1, 1, 0, 1 ],
 [1, 0, 0, 0, 0, 0, 0, 1 ],
 [1, 2, 0, 0, 0, 0, 0, 1 ],
 [1, 1, 1, 1, 1, 1, 1, 1 ]
]

# Controls spritesheet importing
def spritesheet(sheet, rectangle, scaleTo):
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert()
    image.blit(sheet, (0, 0), rect)
    image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
    # Scales the image to designated size
    image = pygame.transform.scale(image, (scaleTo, scaleTo))
    return image

# Generates a level based on the level list
def createLevel(level):
    # Check size
    gridSize = len(level[0])
    gridPixel = 64
    levelGrid = []
    # Scan one gridspot | for sprite type
    for y in range(gridSize):
        for x in range(gridSize):
            levelGrid.append(level[y][x])
    # Place item and move to next one
    print(levelGrid)
    # Jump back once the gridmax has been reached

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

createLevel(level)

isPlaying = True
while isPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False

    Surface.fill((0, 0, 0))
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    Surface.blit(player, (x, y))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()