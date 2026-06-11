## Maths Quiz -- Main
import pygame
import time
import random
from Helpers import XMLReader
from PageVariables import mewo

WINDOW_NAME = "Maths Quiz"
WINDOW_CONSTRUCTORS = {}

## Functions
### https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

## Pygame Setup
pygame.init()

ScreenW = 500
ScreenH = 500

Screen = pygame.display.set_mode( (ScreenW, ScreenH) )
Clock = pygame.time.Clock()

CurrentPage = 'LoginPage'
WindowFont = pygame.font.SysFont('Comic Sans MS', 30)

pygame.display.set_caption(WINDOW_NAME)

## Constructors
class Constructor:
    def __init__(self, constructorName, parameters, func):
        self.name=constructorName
        self.params=parameters
        self.func=func

        WINDOW_CONSTRUCTORS[constructorName] = self

    def Run(self, elementInfo):
        self.func(elementInfo, self.params)

def LoadAttributes(attributes):
    def LoadValue(key, expectedType):
        value = str(attributes[key])
        if value.startswith("@"):
            return mewo.GetExposed(value)
    
        try:
            if expectedType == "float":
                return float(value)
            elif expectedType == "int":
                return int(value)
            elif expectedType == "colour":
                return hex_to_rgb(value)
        except Exception as e:
            print("Can't load Attribute value - something stopped me!")
    
    formattedAttributes = {}
    for key in attributes:
        if key == "x":
            formattedAttributes["posX"] = LoadValue(key, "float")
        elif key == "y":
            formattedAttributes["posY"] = LoadValue(key, "float")
        elif key == "width" or key == "height":
            formattedAttributes[key] = LoadValue(key, "float")
        elif key == "colour":
            formattedAttributes[key] = LoadValue(key, "colour")
    return formattedAttributes
    

def BuildText(elementInfo, parameters):
    attributes = LoadAttributes(elementInfo.attrib)

    attributes["posX"] *= ScreenW
    attributes["posY"] *= ScreenH

    rendered = WindowFont.render(elementInfo.text, False, attributes["colour"])
    Screen.blit(rendered, rendered.get_rect(center = (attributes["posX"], attributes["posY"])))
    
def BuildFrame(elementInfo, parameters):
    attributes = LoadAttributes(elementInfo.attrib)
    
    attributes["posX"] *= ScreenW
    attributes["width"] *= ScreenW
    
    attributes["posY"] *= ScreenH
    attributes["height"] *= ScreenH
    
    pygame.draw.rect(Screen, attributes["colour"], (attributes["posX"] - attributes["width"] / 2, attributes["posY"] - attributes["height"] / 2, attributes["width"], attributes["height"]))

## Class Variables
Constructor("Text", {}, BuildText)
Constructor("Frame", {}, BuildFrame)

## XML Stuff
def ParseNode(node):
    for ClassName in WINDOW_CONSTRUCTORS:
        if ClassName == node.tag:
            WINDOW_CONSTRUCTORS[ClassName].Run(node)
            break
    
    for child in node:
        ParseNode(child)

__shouldRun = True
while __shouldRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            __shouldRun = False

    mewo.Update(float(1 / 60))

    xmlContent = XMLReader.XMLFile(CurrentPage).get()
    attributes = xmlContent.attrib
    for key in attributes:
        if key == "windowPostfix":
            postfix = attributes[key]
            pygame.display.set_caption(WINDOW_NAME + ": " + postfix)
        if key == "background":
            hexCol = attributes[key]
            Screen.fill(hex_to_rgb(hexCol))

    ParseNode(xmlContent)

    pygame.display.flip() ## Effectively a blit
    Clock.tick(60)
    
pygame.quit()
    
