import pygame
import os

pygame.init()

WIDTH = 800
HEIGHT = 600

# Controls spritesheet importing
class spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncer")

clock = pygame.time.Clock()

ss = spritesheet('spritesheet.png')
player = ss.image_at((8, 4, 4, 4))
player = pygame.transform.scale(player, (64, 64))

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

    Surface.blit(player, (x, y))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()