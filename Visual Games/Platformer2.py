import pygame
 
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 0, 0)
LIME = (0, 255, 0)

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
        
        self.calc_grav()
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
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .20
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        #self.rect.y += 0
        #self.rect.y -= 0
 
        # If it is ok to jump, set our speed upwards
        #if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
        self.change_y = -4
 
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


 
 

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

wall = Wall(300, 950, 200, 10)
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
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
            
        all_sprite_list.update()
 
        screen.fill(LIME)
 
        all_sprite_list.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)
     
pygame.quit()
