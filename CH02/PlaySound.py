import pygame, sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()
soundObj = pygame.mixer.Sound('..\makinggames\\badswap.wav')
soundObj.play()

import time
time.sleep(1)

pygame.mixer.music.load('..\makinggames\\match0.wav')
pygame.mixer.music.play(-1, 0.0)
time.sleep(1)
pygame.mixer.music.load('..\makinggames\\match1.wav')
pygame.mixer.music.play(-1, 0.0)
time.sleep(1)
pygame.mixer.music.load('..\makinggames\\match2.wav')
pygame.mixer.music.play(-1, 0.0)
time.sleep(1)
pygame.mixer.music.load('..\makinggames\\match3.wav')
pygame.mixer.music.play(-1, 0.0)
time.sleep(1)
pygame.mixer.music.load('..\makinggames\\match4.wav')
pygame.mixer.music.play(-1, 0.0)
time.sleep(1)
pygame.mixer.music.load('..\makinggames\\match5.wav')
pygame.mixer.music.play(-1, 0.0)
time.sleep(1)

pygame.mixer.music.stop()
