## Maths Quiz -- Main
import pygame
import time
import random
from Helpers import XMLReader

WINDOW_NAME = "Maths Quiz"
WINDOW_CONSTRUCTORS = {}

## Functions
### https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def WindowConstructor(func):
    def Wrapper(constructorName, parameters):
        WINDOW_CONSTRUCTORS[constructorName] = {
            "func": func,
            
        }
    return Wrapper

## Pygame Setup
pygame.init()

ScreenW = 500
ScreenH = 500

Screen = pygame.display.set_mode( (ScreenW, ScreenH) )
Clock = pygame.time.Clock()

CurrentPage = 'LoginPage'

pygame.display.set_caption(WINDOW_NAME)

__shouldRun = True
while __shouldRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            __shouldRun = False

    xmlContent = XMLReader.XMLFile(CurrentPage).get()
    attributes = xmlContent.attrib
    for key in attributes:
        if key == "windowPostfix":
            postfix = attributes[key]
            pygame.display.set_caption(WINDOW_NAME + ": " + postfix)
        if key == "background":
            hexCol = attributes[key]
            Screen.fill(hex_to_rgb(hexCol))
            

    pygame.display.flip() ## Effectively a blit
    Clock.tick(60)
    
pygame.quit()
    
