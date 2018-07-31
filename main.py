import pygame
import os

pygame.init()

WIDTH = 512
HEIGHT = 512

# Controls spritesheet importing
class spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        # Scales the image to 64x64s
        image = pygame.transform.scale(image, (64, 64))
        return image

def createLevel(level):

Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncer")

clock = pygame.time.Clock()

ss = spritesheet('spritesheet.png')
air = ss.image_at((0, 0, 1, 1), colorkey=(0, 0, 0))
coin = ss.image_at((8, 0, 4, 4), colorkey=(0, 0, 0))
enemy = ss.image_at((12, 4, 4, 4), colorkey=(0, 0, 0))
wall = ss.image_at((12, 0, 4, 4))
doorOpen = ss.image_at((0, 0, 4, 4), colorkey=(0, 0, 0))
doorClosed = ss.image_at((4, 0, 4, 4), colorkey=(0, 0, 0))
buttonClicked = ss.image_at((4, 4, 4, 4), colorkey=(0, 0, 0))
buttonUnclicked = ss.image_at((0, 4, 4, 4), colorkey=(0, 0, 0))
player = ss.image_at((8, 4, 4, 4))

# Air = 0   Wall = 1   Player = 2   Exit = 3
# Enemy = 4   Coin = 5   Door = 6   Button = 7

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

createLevel(level)

done = False
x = WIDTH/2
y = HEIGHT/2

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    Surface.fill((255, 255, 255))
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    Surface.blit(coin, (x, y))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()