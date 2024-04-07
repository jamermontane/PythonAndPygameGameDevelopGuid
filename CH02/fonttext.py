import pygame, sys
from pygame.locals import *
from myColors import *

pygame.init()
DISPLAY_SURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello world!')

fontObj = pygame.font.Font('..\makinggames\\freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAY_SURF.fill(WHITE)
    DISPLAY_SURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
