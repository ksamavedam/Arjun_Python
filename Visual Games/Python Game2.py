import pygame, sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

White = (255, 255, 255)
Green = (0, 128, 0)
Blue = (0, 0, 128)
Aqua = (0, 255, 255)
Lime = (0, 255, 0)
Olive = (128, 128, 0)
fontObj = pygame.font.Font('freesansbold.ttf', 32)

textSurfaceObj = fontObj.render('Hello world!', True, Blue, Green)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True: # main game loop
    DISPLAYSURF.fill(Green)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()