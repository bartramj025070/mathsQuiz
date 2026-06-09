## XMLReader.py
## Parses basic XML syntax through custom ruling for "pages"
import os
import xml.etree.ElementTree as XML

directory = os.path.dirname(__file__)
root = os.path.dirname(directory)

pagesDir = os.path.join(root, "Pages")
pages = os.listdir(pagesDir)
        
def GetPages():
    return pages

def ReadPage(pageName):
    with open(os.path.join(pagesDir, pageName), 'r') as page:
        return page.read()
    return ""

class XMLTag:
    def __init__(self, tagName, attributes):
        self.tagName=tagName
        self.attributes=attributes
        self.tags=[]
        
    def addTag(self, tag):
        self.tags.append(tag)

class XMLFile:
    def __init__(self, pageName):
        self.pageName=pageName
    
    def get(self):
        tree = XML.parse(os.path.join(pagesDir, self.pageName) + ".xml")
        root = tree.getroot()
        return root