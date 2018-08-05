import pygame
import os

pygame.init()

# Initial values
WIDTH = 512 # Screen width
HEIGHT = 512 # Screen height
Surface = pygame.display.set_mode((WIDTH, HEIGHT)) # Create screen
pygame.display.set_caption("Gridrunner") # Set caption
clock = pygame.time.Clock() # Initialize clock
font = pygame.font.SysFont(None, 100)

x = 0
y = 0

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
wall = spritesheet(ss, (12, 0, 4, 4), 32)
playerSprite = spritesheet(ss, (8, 4, 4, 4), 32)
enemy = spritesheet(ss, (12, 4, 4, 4), 32)
coin = spritesheet(ss, (8, 0, 4, 4), 32)
buttonUnclicked = spritesheet(ss, (0, 4, 4, 4), 32)
buttonClicked = spritesheet(ss, (4, 4, 4, 4), 32)
doorOpen = spritesheet(ss, (0, 0, 4, 4), 32)
doorClosed = spritesheet(ss, (4, 0, 4, 4), 32)

class gridElement(object):
    def __init__(self, name, pos):
        grid.append(self)
        self.name = name
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    
    def delete(self):
        self.rect = None

# Empty = 0   Wall = 1   Player = 2   Enemy = 3
# Coin = 4   Button = 5   Open Door = 6   Closed Door = 7

# This list is the layout for the level (16x16 grid)


level = [
 [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
 [ 1, 0, 0, 4, 0, 4, 0, 0, 4, 1, 0, 0, 0, 0, 6, 1 ],
 [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
 [ 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 4, 0, 1 ],
 [ 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
 [ 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1 ],
 [ 1, 0, 0, 0, 1, 1, 4, 1, 0, 1, 1, 1, 4, 0, 0, 1 ],
 [ 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1 ],
 [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1 ],
 [ 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1 ],
 [ 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1 ],
 [ 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1 ],
 [ 1, 0, 0, 0, 0, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 1 ],
 [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
 [ 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 1 ],
 [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
]

class Player():
    def __init__(self, xd, yd):
        self.rect = pygame.Rect(xd, yd, 32, 32)
        self.score = 0
        self.win = False

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

        for i in grid:
            if i.name == "Wall":
                if self.rect.colliderect(i.rect):
                    if dx > 0:
                        self.rect.right = i.rect.left
                    if dx < 0:
                        self.rect.left = i.rect.right
                    if dy > 0:
                        self.rect.bottom = i.rect.top
                    if dy < 0:
                        self.rect.top = i.rect.bottom
            if i.name == "Coin":
                if self.rect.colliderect(i.rect):
                    self.score += 100
                    i.rect = pygame.Rect(10000, 10000, 0, 0)
            if i.name == "Open Door":
                if self.rect.colliderect(i.rect):
                    self.win = True



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
        gridX += 32
    gridY += 32
    gridX = 0

player = Player(x, y)
win = font.render("You Win!", True, (146, 244, 66))

isPlaying = True
while isPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False

    Surface.fill((255, 255, 255))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player.move(-4, 0)
    if pressed[pygame.K_RIGHT]:
        player.move(4, 0)
    if pressed[pygame.K_UP]:
        player.move(0, -4)
    if pressed[pygame.K_DOWN]:
        player.move(0, 4)
    
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

    if player.win == True:
        Surface.blit(win, (256 - win.get_width() // 2, 256 - win.get_height() // 2))
        
    scoreText = font.render(str(player.score), True, (146, 244, 66))
    Surface.blit(playerSprite, player.rect)
    Surface.blit(scoreText, (0, 0))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()