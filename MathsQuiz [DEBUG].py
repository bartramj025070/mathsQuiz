## Maths Quiz -- Main
import pygame
import time
import random

## Pygame Setup
pygame.init()

ScreenW = 500
ScreenH = 500

Screen = pygame.display.set_mode( (ScreenW, ScreenH) )
Clock = pygame.time.Clock()

__shouldRun = True
while __shouldRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            __shouldRun = False

    pygame.display.flip() ## Effectively a blit
    Clock.tick(60)
    
pygame.quit()
    
