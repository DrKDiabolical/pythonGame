import pygame

pygame.init()

# Initial values
WIDTH = 512 # Screen width
HEIGHT = 512 # Screen height
Surface = pygame.display.set_mode((WIDTH, HEIGHT)) # Create screen
pygame.display.set_caption("Gridrunner") # Set caption
clock = pygame.time.Clock() # Initialize clock
font = pygame.font.SysFont(None, 100) # Initialize font

# CUSTOMIZABLE GAME OPTIONS

gridSize = 8 # Choose grid size (Currently supports 8x8, 16x16 and 32x32)

# Use the following list below to define the level layout, the keys change between the different objects to draw on the screen

# OBJECT KEYS
# Empty = 0   Wall = 1   Player = 2   Enemy = 3
# Coin = 4   Button = 5   Door = 6

# This list is the layout for the level

# Template for 8x8 grid
level = [
 [1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 6, 1],
 [1, 0, 4, 0, 4, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1],
 [1, 0, 4, 5, 4, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 0, 1],
 [1, 2, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1]
]

# Template for 16x16 grid
""" level = [
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
] """

# Template for 32x32 grid
""" level = [
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
] """

# END OF CUSTOMIZABLE GAME OPTIONS

# Selects player speed and sprite size based on grid size
playerSpeed = 0
spriteSize = 0
if gridSize == 8:
    playerSpeed = 8
    spriteSize = 64
elif gridSize == 16:
    playerSpeed = 4
    spriteSize = 32
elif gridSize == 32:
    playerSpeed = 2
    spriteSize = 16

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
wall = spritesheet(ss, (12, 0, 4, 4), spriteSize)
playerSprite = spritesheet(ss, (8, 4, 4, 4), spriteSize)
enemy = spritesheet(ss, (12, 4, 4, 4), spriteSize)
coin = spritesheet(ss, (8, 0, 4, 4), spriteSize)
buttonUnclicked = spritesheet(ss, (0, 4, 4, 4), spriteSize)
buttonClicked = spritesheet(ss, (4, 4, 4, 4), spriteSize)
doorOpen = spritesheet(ss, (0, 0, 4, 4), spriteSize)
doorClosed = spritesheet(ss, (4, 0, 4, 4), spriteSize)

# Stores data on basic grid objects
class gridElement(object):
    def __init__(self, name, sprite, pos):
        grid.append(self)
        self.name = name
        self.sprite = sprite
        self.rect = pygame.Rect(pos[0], pos[1], spriteSize, spriteSize)

# Stores data on interactable grid objects
class interactElement(object):
    def __init__(self, name, state, sprites, pos):
            grid.append(self)
            self.name = name
            self.state = state
            self.sprites = sprites
            self.sprite = sprites[1]
            self.rect = pygame.Rect(pos[0], pos[1], spriteSize, spriteSize)
            if self.state == 0:
                self.sprite = sprites[0]
            else:
                self.sprite = sprites[1]

# Defines all player data
class Player():
    def __init__(self, spawn):
        self.spawn = spawn # Stores original spawn location
        self.rect = pygame.Rect(spawn[0], spawn[1], spriteSize, spriteSize) # Creates rect for player
        self.score = 0 # Initializes score
        self.win = False # Contains win status

    # Moves the player based on axis
    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    # Moves the player on a single axis
    def move_single_axis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

        # Collision detection
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
            if i.name == "Door":
                if i.state == 0:
                    if self.rect.colliderect(i.rect):
                        self.win = True
            if i.name == "Button":
                if i.state == 0:
                    i.state = 1



# Generates a level based on the level list
spawnPoint = (0, 0)
grid = []
gridX = 0
gridY = 0
for y in level:
    for x in y:
        if x == 1:
            gridElement("Wall", wall, (gridX, gridY))
        elif x == 2:
            spawnPoint = (gridX, gridY)
        elif x == 3:
            gridElement("Enemy", enemy, (gridX, gridY))
        elif x == 4:
            gridElement("Coin", coin, (gridX, gridY))
        elif x == 5:
            interactElement("Button", 0, [buttonUnclicked, buttonClicked], (gridX, gridY))
        elif x == 6:
            interactElement("Door", 0, [doorOpen, doorClosed], (gridX, gridY))
        gridX += spriteSize
    gridY += spriteSize
    gridX = 0

player = Player(spawnPoint) # Initializes player object
win = font.render("You Win!", True, (146, 244, 66)) # Initializes win text
buttonAmount = 0

isPlaying = True # Checks if the user is playing the game
while isPlaying: # Game loop begins
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False

    Surface.fill((255, 255, 255)) # Refreshes game display

    pressed = pygame.key.get_pressed() # Handles player input
    if pressed[pygame.K_LEFT]:
        player.move(-playerSpeed, 0)
    if pressed[pygame.K_RIGHT]:
        player.move(playerSpeed, 0)
    if pressed[pygame.K_UP]:
        player.move(0, -playerSpeed)
    if pressed[pygame.K_DOWN]:
        player.move(0, playerSpeed)
    
    # Renders the level grid
    for i in grid:
        if i.name == "Wall":
            Surface.blit(i.sprite, i.rect)
        elif i.name == "Enemy":
            Surface.blit(i.sprite, i.rect)
        elif i.name == "Coin":
            Surface.blit(i.sprite, i.rect)
        elif i.name == "Button":
            Surface.blit(i.sprite, i.rect)
        elif i.name == "Door":
            Surface.blit(i.sprite, i.rect)
            

    # Checks if the player has won
    if player.win == True:
        Surface.blit(win, (256 - win.get_width() // 2, 256 - win.get_height() // 2))
        
    scoreText = font.render(str(player.score), True, (146, 244, 66)) # Initializes (Or refreshes) score text
    Surface.blit(playerSprite, player.rect) # Renders player
    Surface.blit(scoreText, (0, 0)) # Renders score texxt

    pygame.display.update() # Updates display
    clock.tick(30) # Sets framerate

pygame.quit() # Quits pygame
quit() # Quits application