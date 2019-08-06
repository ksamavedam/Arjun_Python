import pygame
 
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

#knockout = input("Would you like to play knockout?")
#knockout_2 = int(knockout)
#knockout_2 = True

speed = input("How fast should your character go?(25+ causes glitch, 100+ causes lag)")
a = int(speed) 
 
 
class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def update(self):
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
  
 
 
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Test')
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 10, 1000)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 990, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(990, 0, 10, 1000)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 990, 990, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 200, 940, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
player = Player(50, 50)
player.walls = wall_list

wall = Wall(60, 300, 950, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
player = Player(50, 50)
player.walls = wall_list

wall = Wall(10, 400, 940, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
player = Player(50, 50)
player.walls = wall_list

wall = Wall(60, 500, 950, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
player = Player(50, 50)
player.walls = wall_list

wall = Wall(10, 600, 940, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
player = Player(50, 50)
player.walls = wall_list

wall = Wall(60, 700, 950, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
player = Player(50, 50)
player.walls = wall_list

wall = Wall(10, 800, 940, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
player = Player(50, 50)
player.walls = wall_list

wall = Wall(60, 900, 950, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
player = Player(50, 50)
player.walls = wall_list

all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-a, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(a, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -a)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, a)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(a, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-a, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, a)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -a)
 
            
    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()