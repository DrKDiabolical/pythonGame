import pygame
import os

WIDTH = 800
HEIGHT = 600

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()

Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncer")
clock = pygame.time.Clock()

pygame.mixer.music.load('music/song.wav')
pygame.mixer.music.play(0)

done = False
is_green = True
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

    Surface.blit(get_image('imgs/player.png'), (x, y))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()